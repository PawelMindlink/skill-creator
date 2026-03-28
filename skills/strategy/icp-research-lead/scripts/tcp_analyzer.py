import pandas as pd
import json
import xml.etree.ElementTree as ET
import glob
import os
import argparse
import sys
import random
try:
    import urllib.request
    URL_VALIDATION_AVAILABLE = True
except ImportError:
    URL_VALIDATION_AVAILABLE = False

def validate_url(url, timeout=3):
    """
    P0 FIX: Validate that URL returns 200 status.
    Returns: (is_valid: bool, status_code: int or None)
    """
    if not URL_VALIDATION_AVAILABLE:
        return (True, None)  # Skip if urllib not available
    
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return (response.status == 200, response.status)
    except Exception as e:
        return (False, str(e)[:50])

def load_config(client_dir):
    config_path = os.path.join(client_dir, "client_config.json")
    default_config = {
        "frequency_multiplier": 1.0,
        "vat_rate": 1.23,
        "margins": {"default": 0.30},
    }
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return {**default_config, **json.load(f)}
    return default_config

def parse_feed(feed_path):
    """Parses XML/RSS Product Feed into a DataFrame."""
    try:
        # P0 FIX: Handle namespaced XML by stripping prefixes
        # Parse XML and strip namespaces for easier access
        tree = ET.parse(feed_path)
        root = tree.getroot()
        
        # Remove namespace prefixes from all tags  
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]  # Strip namespace
        
        items = root.findall('.//item')
        
        products = []
        for item in items:
            def get_text(tag):
                node = item.find(tag)
                if node is None:
                    # Try case-insensitive match
                    for child in item:
                        if child.tag.lower() == tag.lower():
                            return child.text
                    return None
                return node.text

            price_str = get_text('price')
            # Clean price "1299 PLN" -> 1299.0
            price = 0.0
            if price_str:
                try:
                    price = float(price_str.split()[0].replace(',', '.'))
                except:
                    price = 0.0

            products.append({
                'id': get_text('id'),
                'title': get_text('title'),
                'link': get_text('link'),
                'price': price,
                'image_link': get_text('image_link'),
                'description': get_text('description')
            })
        return pd.DataFrame(products)
    except Exception as e:
        print(f"CRITICAL: Feed Parse Error: {e}")
        return pd.DataFrame()

def load_psych_quotes(client_dir, config):
    """
    Loads REAL quotes from harvest_*.json files.
    Returns a dict mapping 'Category' -> List of Quote Objects.
    """
    json_files = glob.glob(os.path.join(client_dir, "harvest_*.json")) + glob.glob(os.path.join(client_dir, "RAW_HARVEST_DATA_*.json"))
    
    # Initialize DB from Config
    quotes_db = {}
    
    # helper to init
    def init_cat(cat_id):
        if cat_id not in quotes_db:
             quotes_db[cat_id] = {"PAIN": [], "DREAM": []}

    # Load defined segments
    if 'segments' in config:
        for seg in config['segments']:
            init_cat(seg['id'])
    
    # Load default segment
    default_id = config.get('default_segment', {}).get('id', 'office')
    init_cat(default_id)

    for f in json_files:
        try:
            with open(f, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
                insights = data.get('deep_harvest_insights', {})
                
                for source, items in insights.items():
                    if isinstance(items, list):
                        for item in items:
                            basket = item.get('basket', 'PAIN')
                            quote = item.get('raw_quote')
                            
                            # Categorization Strategy: Match Filename or File Data to Segment ID
                            # Default to 'default_segment'
                            category = default_id
                            
                            # Check if file name contains segment id
                            filename = os.path.basename(f).lower()
                            
                            if 'segments' in config:
                                for seg in config['segments']:
                                    if seg['id'] in filename: 
                                        category = seg['id']
                                        break
                            
                            if quote and basket in ["PAIN", "DREAM"]:
                                quotes_db[category][basket].append(quote)
                                
        except Exception as e:
            print(f"Warning: Could not read psych file {f}: {e}")
            
    # Apply Fallbacks from Config
    def apply_fallback(cat_id, fallback_data):
        if not fallback_data: return
        if not quotes_db[cat_id]["PAIN"]:
            quotes_db[cat_id]["PAIN"].extend(fallback_data.get('PAIN', []))
        if not quotes_db[cat_id]["DREAM"]:
            quotes_db[cat_id]["DREAM"].extend(fallback_data.get('DREAM', []))

    if 'segments' in config:
        for seg in config['segments']:
            apply_fallback(seg['id'], seg.get('fallbacks'))
            
    apply_fallback(default_id, config.get('default_segment', {}).get('fallbacks'))
        
    return quotes_db

def get_random_quote(quotes_db, category, basket):
    """Returns a random quote for diversity."""
    options = quotes_db.get(category, {}).get(basket, [])
    if options:
        return random.choice(options)
    return ""

def analyze(client_name):
    # P0 FIX: Deterministic random seed for reproducible quote selection
    # This ensures running the same client twice produces identical output
    random.seed(hash(client_name))
    
    # Paths - Robust Search Logic
    possible_paths = [
        client_name, 
        os.path.join(os.getcwd(), "Clients", client_name), 
        os.path.join(os.path.dirname(os.getcwd()), "ICP Research", "Clients", client_name), 
        f"C:/Users/Paweł/Documents/GitHub/Meta Ads Analysis Production Upload/research/Clients/{client_name}" 
    ]
    
    base_dir = None
    for p in possible_paths:
        if os.path.exists(p) and os.path.isdir(p):
            base_dir = p
            break
            
    if not base_dir:
        print(f"CRITICAL: Could not find client directory for '{client_name}'.")
        return
        
    print(f"Analyzing Client Directory: {base_dir}")

    # 1. Load Data
    config = load_config(base_dir)
    quotes_db = load_psych_quotes(base_dir, config)
    
    # Locate Feed
    feed_files = glob.glob(os.path.join(base_dir, "*.xml")) + glob.glob(os.path.join(base_dir, "*.txt"))
    if not feed_files:
        print("CRITICAL: No product feed found (.xml or .txt).")
        return
    
    df_feed = parse_feed(feed_files[0])
    
    # P0 FIX: Safety check for empty or malformed feed
    if df_feed.empty or 'price' not in df_feed.columns:
        print("CRITICAL: Feed parsing failed or missing required 'price' column.")
        print(f"Available columns: {list(df_feed.columns)}")
        print("Check Feed XML format. Attempting fallback to CSV format...")
        
        # Fallback: Try as CSV
        try:
            df_feed = pd.read_csv(feed_files[0])
            print(f"Successfully loaded as CSV. Columns: {list(df_feed.columns)}")
            
            # Normalize column names (case insensitive)
            df_feed.columns = df_feed.columns.str.lower()
            
            # Ensure required columns exist
            if 'price' not in df_feed.columns:
                print("CRITICAL: CSV also missing 'price' column. Aborting.")
                return
        except Exception as e:
            print(f"CRITICAL: CSV fallback also failed: {e}")
            return
    
    # Locate GA4
    ga4_files = glob.glob(os.path.join(base_dir, "*Segments.csv"))
    if ga4_files:
        try:
            df_ga4 = pd.read_csv(ga4_files[0], skiprows=7, index_col=False, on_bad_lines='skip')
            
            # Rename Columns to English for internal logic, output will be Polish
            df_ga4.rename(columns={
                df_ga4.columns[0]: 'Landing page',
                df_ga4.columns[3]: 'Revenue',
                df_ga4.columns[4]: 'Transactions'
            }, inplace=True)
            
            # Clean Data
            df_ga4['Landing page'] = df_ga4['Landing page'].astype(str)
            df_ga4 = df_ga4[df_ga4['Landing page'].notna()] 
            df_ga4 = df_ga4[~df_ga4['Landing page'].str.contains("Grand total", case=False, na=False)]
            df_ga4 = df_ga4[~df_ga4['Landing page'].str.match(r'^\d+$', na=False)]

            # URL Prefix Logic from Config
            prefix = config.get('url_prefix', '')
            if prefix:
                df_ga4['Landing page'] = df_ga4['Landing page'].apply(
                    lambda x: prefix + x if x.startswith('/') else x
                ) 
            
            # Normalize Feed URLs
            df_feed['link_clean'] = df_feed['link'].astype(str).apply(lambda x: x.split('?')[0])

            # Merge
            df_merged = pd.merge(df_feed, df_ga4, left_on='link_clean', right_on='Landing page', how='left')

        except Exception as e:
            print(f"WARNING: Parse Error on GA4 CSV: {e}. continuing with feed only.")
            df_merged = df_feed
            df_merged['Transactions'] = 0
            df_merged['Revenue'] = 0
    else:
        print("WARNING: No GA4 CSV found. Using Feed Only.")
        df_merged = df_feed
        df_merged['Transactions'] = 0
        df_merged['Revenue'] = 0
        
    # Locate Ads History
    ads_files = glob.glob(os.path.join(base_dir, "*Ads_Historical.csv")) + glob.glob(os.path.join(base_dir, "Untitled-report*.csv"))
    df_ads = pd.DataFrame()
    ads_history_map = {}  # URL -> Historical Performance String
    
    if ads_files:
        try:
            df_ads = pd.read_csv(ads_files[0])
            print(f"Loaded Ads History: {len(df_ads)} rows.")
            
            # P0 FIX: Create lookup map for historical performance
            # Assumes columns: 'Landing Page' or 'Website URL', 'CTR', 'ROAS' or 'Purchase ROAS'
            url_col = None
            for col in df_ads.columns:
                if 'landing' in col.lower() or 'website' in col.lower() or 'url' in col.lower():
                    url_col = col
                    break
            
            if url_col:
                for _, row in df_ads.iterrows():
                    url = str(row[url_col]).split('?')[0]  # Remove UTM params
                    
                    # Extract performance metrics (flexible column names)
                    ctr = row.get('CTR (link click-through rate)', row.get('CTR', 'N/A'))
                    roas = row.get('Purchase ROAS (return on ad spend)', row.get('ROAS', 'N/A'))
                    
                    if url and url != 'nan':
                        ads_history_map[url] = f"CTR: {ctr}, ROAS: {roas}"
                        
                print(f"Mapped {len(ads_history_map)} URLs from Ads Historical data.")
        except Exception as e:
            print(f"WARNING: Could not parse Ads Historical CSV: {e}")

    # 2. Logic (Gwiazdy/Dojne Krowy)
    df_merged['Revenue'] = df_merged['Revenue'].fillna(0)
    df_merged['price'] = df_merged['price'].fillna(0)
    
    rev_80 = df_merged[df_merged['Revenue'] > 0]['Revenue'].quantile(0.80)
    price_80 = df_merged['price'].quantile(0.80)

    def classify(row):
        rev = row['Revenue']
        price = row['price']
        
        if rev > rev_80 and price > price_80: return "GWIAZDA"
        if rev > rev_80: return "DOJNA_KROWA"
        if rev <= rev_80 and price > price_80: return "UKRYTY_DIAMENT"
        return "IGNOROWANY"

    df_merged['Category'] = df_merged.apply(classify, axis=1)

    # 3. Strategy Injection & Polish Output
    strategy_rows = []
    
    for _, row in df_merged.iterrows():
        if row['Category'] == "IGNOROWANY": continue
        
        # Financials
        margin_pct = config['margins']['default']
        freq = config['frequency_multiplier']
        vat = config['vat_rate']
        
        base_price = row['price']
        net_price = base_price / vat
        ltv_value = net_price * freq
        break_even_cpa = ltv_value * margin_pct
        
        # Persona Logic (Dynamic Loop)
        title_lower = str(row['title']).lower()
        link_lower = str(row['link']).lower()
        combined_text = title_lower + " " + link_lower
        
        # Default
        def_seg = config.get('default_segment', {'id': 'office', 'persona': 'Default'})
        persona = def_seg['persona']
        quote_cat = def_seg['id']
        
        # Check specific segments
        if 'segments' in config:
            for seg in config['segments']:
                # Any keyword match
                if any(k.lower() in combined_text for k in seg.get('keywords', [])):
                    persona = seg['persona']
                    quote_cat = seg['id']
                    break

        # Get Real Quote (deterministic due to seed at line 143)
        pain_quote = get_random_quote(quotes_db, quote_cat, "PAIN")
        dream_quote = get_random_quote(quotes_db, quote_cat, "DREAM")
        
        # Determine Campaign Type
        kampania = "Skalowanie (Marża)" if row['Category'] == "GWIAZDA" else "Utrzymanie (Volume)"
        
        # Ad Set Hierarchy: Category + Price Bucket
        # We bucket price to group similar products for Bid Strategy
        price = row['price']
        if price < 500: price_bucket = "0-500 PLN"
        elif price < 1000: price_bucket = "500-1000 PLN"
        elif price < 2000: price_bucket = "1000-2000 PLN"
        elif price < 4000: price_bucket = "2000-4000 PLN"
        else: price_bucket = "4000+ PLN"
        
        ad_set_name = f"{row['Category']} - {price_bucket}"

        strategy_rows.append({
            "Kampania": kampania,
            "Zestaw Reklam (AdSet)": ad_set_name,
            "Nazwa Reklamy": f"{row['Category']}_{persona}_{row['id']}",
            "Link URL": row['link'],
            "Persona": persona,
            "Cytat (VoC)": pain_quote,
            "Obietnica (Dream)": dream_quote,
            "Cena Produktu (PLN)": base_price,
            "Bid Cap (PLN)": round(break_even_cpa, 2),
            "Koszt Max (Cost Cap)": round(break_even_cpa * 0.7, 2),
            "Cel ROAS": round(1 / (margin_pct * freq), 2),
            # P0 FIX: Use actual Meta Ads historical data if available
            "Status Historyczny": ads_history_map.get(row['link'].split('?')[0], "Nowy Produkt (Brak Danych)")
        })

    # 4. Output: Mapa Strategii
    df_strategy = pd.DataFrame(strategy_rows)
    
    # P0 FIX (Optional): URL Validation
    # Validate a sample of URLs to catch configuration errors
    if len(df_strategy) > 0:
        sample_urls = df_strategy['Link URL'].sample(min(5, len(df_strategy))).tolist()
        print(f"\n[URL Validation] Checking {len(sample_urls)} random URLs...")
        invalid_count = 0
        for url in sample_urls:
            is_valid, status = validate_url(url)
            if not is_valid:
                print(f"  ⚠️ WARNING: {url[:60]}... returned {status}")
                invalid_count += 1
            else:
                print(f"  ✅ OK: {url[:60]}...")
        
        if invalid_count > 0:
            print(f"\n⚠️ {invalid_count}/{len(sample_urls)} URLs failed validation. Check URL prefix config.")
    
    out_path = os.path.join(base_dir, f"{client_name}_Mapa_Strategii.csv")
    df_strategy.to_csv(out_path, index=False)
    print(f"\n✅ Wygenerowano Mapę Strategii: {out_path}")
    print(f"   Total Products: {len(df_strategy)}")
    print(f"   GWIAZDA: {len(df_strategy[df_strategy['Zestaw Reklam (AdSet)'].str.contains('GWIAZDA', na=False)])}")
    print(f"   DOJNA_KROWA: {len(df_strategy[df_strategy['Zestaw Reklam (AdSet)'].str.contains('DOJNA_KROWA', na=False)])}")
    
    # 5. Output: Magazyn Dowodów
    if not df_ads.empty:
        locker_path = os.path.join(base_dir, f"{client_name}_Magazyn_Dowodow.csv")
        df_ads.to_csv(locker_path, index=False)
        print(f"Wygenerowano Magazyn Dowodów: {locker_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("client_name", help="Nazwa folderu klienta")
    args = parser.parse_args()
    analyze(args.client_name)
