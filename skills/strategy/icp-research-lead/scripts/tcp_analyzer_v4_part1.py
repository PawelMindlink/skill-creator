"""
ICP Framework V4.0 - Uniwersalny Analizator Produktów

CEL: Robić lepsze reklamy poprzez:
1. Klasyfikację produktów według BCG Matrix + Meta Ads
2. Priorytetyzację P1-P8 (tylko P1-P7 dostają persony)
3. Generowanie briefów dla copywritera i designera

DANE WEJŚCIOWE:
- Feed XML (produkt title, description, price, category)
- GA4 CSV (landing page, sessions, transactions, revenue, page title)
- Meta Ads CSV (URL, spend, conversion value, ROAS)
- Harvest JSON (cytaty VoC per kategoria)

DANE WYJŚCIOWE:
- Master_Strategy_Map.csv (wszystkie produkty P1-P7 z personami)
- Briefs/ (folder z briefami copywriterskimi per produkt)
- Personas_Summary.md (podsumowanie dla człowieka)
"""

import pandas as pd
import json
import xml.etree.ElementTree as ET
import glob
import os
import sys
from urllib.parse import urlparse, parse_qs
import re
from datetime import datetime

# ============================================================================
# ŁADOWANIE KONFIGURACJI
# ============================================================================

def zaladuj_konfiguracje(katalog_klienta):
    """Ładuje client_config.json + global_persona_templates.json"""
    config_path = os.path.join(katalog_klienta, 'client_config.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        config_klienta = json.load(f)
    
    # Globalne szablony person
    global_templates_path = os.path.join(
        os.path.dirname(__file__), 
        '..', '..', 'Core', 'Configs', 'global_persona_templates.json'
    )
    with open(global_templates_path, 'r', encoding='utf-8') as f:
        global_personas = json.load(f)
    
    return config_klienta, global_personas

# ============================================================================
# PARSOWANIE FEED XML
# ============================================================================

def wyczsc_url(url):
    """Usuwa parametry UTM i zwraca canonical URL"""
    if not url or url == '/':
        return '/'
    
    parsed = urlparse(url)
    # Tylko path, bez query i fragment
    canonical = parsed.path
    
    # Usuń trailing slash dla spójności
    if canonical.endswith('/') and len(canonical) > 1:
        canonical = canonical[:-1]
    
    return canonical

def parsuj_feed(sciezka_feed):
    """
    Parsuje XML feed produktowy do DataFrame
    Obsługuje namespace'd XML (Google Shopping format)
    """
    try:
        tree = ET.parse(sciezka_feed)
        root = tree.getroot()
        
        # Usuń namespace prefixes dla łatwiejszego dostępu
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
        
        products = []
        items = root.findall('.//item')
        
        def get_text(tag):
            elem = item.find(tag)
            return elem.text.strip() if elem is not None and elem.text else ''
        
        for item in items:
            product = {
                'product_id': get_text('id'),
                'title': get_text('title'),
                'description': get_text('description'),
                'link': wyczsc_url(get_text('link')),
                'price': get_text('price'),
                'product_type': get_text('product_type'),
                'availability': get_text('availability')
            }
            
            # Wyczyść cenę do float
            if product['price']:
                price_clean = re.sub(r'[^\d.]', '', product['price'])
                try:
                    product['price_float'] = float(price_clean)
                except:
                    product['price_float'] = 0.0
            else:
                product['price_float'] = 0.0
            
            products.append(product)
        
        df = pd.DataFrame(products)
        print(f"✓ Załadowano {len(df)} produktów z feed XML")
        return df
    
    except Exception as e:
        print(f"✗ Błąd parsowania feed: {e}")
        return pd.DataFrame()

# ============================================================================
# ŁADOWANIE GA4 I META ADS
# ============================================================================

def zaladuj_ga4(katalog_klienta):
    """
    Ładuje dane z GA4 CSV (Eksport Item-based)
    Oczekiwane kolumny: 'Item ID', 'Item name', 'Items viewed', 'Items purchased', 'Item revenue'
    """
    ga4_files = glob.glob(os.path.join(katalog_klienta, '*GA*.csv'))
    
    if not ga4_files:
        print("✗ Brak plików GA4 CSV")
        return pd.DataFrame()
    
    try:
        # Próba wczytania z pominięciem nagłówka (częste w GA4 export)
        try:
            df_ga4 = pd.read_csv(ga4_files[0], skiprows=6)
            if df_ga4.empty or 'Item' not in str(df_ga4.columns):
                 raise ValueError("Empty or wrong header")
        except:
            df_ga4 = pd.read_csv(ga4_files[0])

        # Wyczyść nazwy kolumn
        df_ga4.columns = df_ga4.columns.str.strip()
        
        # Znajdź kolumny
        id_col = next((c for c in df_ga4.columns if 'Item ID' in c), None)
        name_col = next((c for c in df_ga4.columns if 'Item name' in c), None)
        
        views_col = next((c for c in df_ga4.columns if 'Items viewed' in c or 'Item views' in c), None)
        purchases_col = next((c for c in df_ga4.columns if 'Items purchased' in c), None)
        revenue_col = next((c for c in df_ga4.columns if 'Item revenue' in c), None)
        
        if not id_col and not name_col:
            print(f"✗ Nie znaleziono kolumn 'Item ID' ani 'Item name'. Kolumny: {df_ga4.columns.tolist()}")
            return pd.DataFrame()

        # Rename
        rename_map = {}
        if id_col: rename_map[id_col] = 'match_id'
        elif name_col: rename_map[name_col] = 'match_id'
        
        if views_col: rename_map[views_col] = 'item_views'
        if purchases_col: rename_map[purchases_col] = 'items_purchased'
        if revenue_col: rename_map[revenue_col] = 'item_revenue'
        
        df_ga4 = df_ga4.rename(columns=rename_map)
        
        # Upewnij się że mamy kluczowe metryki
        for metric in ['item_views', 'items_purchased', 'item_revenue']:
            if metric not in df_ga4.columns:
                df_ga4[metric] = 0
        
        # Clean numeric columns
        for col in ['item_views', 'items_purchased', 'item_revenue']:
            if df_ga4[col].dtype == object:
                 df_ga4[col] = df_ga4[col].astype(str).str.replace(',', '').str.replace(r'[^\d.]', '', regex=True)
                 df_ga4[col] = pd.to_numeric(df_ga4[col], errors='coerce').fillna(0)
        
        # Aggregacja per Item
        df_aggregated = df_ga4.groupby('match_id').agg({
            'item_views': 'sum',
            'items_purchased': 'sum',
            'item_revenue': 'sum'
        }).reset_index()
        
        # Oblicz ARPU (Avg Revenue Per Item Purchased? Or View?)
        # Standard metrics: Revenue / Views (Revenue per View) or Revenue / Purchases (AOV)
        # Using Revenue / Views as proxy for "Value per visitor interest" in BCG context logic
        df_aggregated['arpu'] = df_aggregated['item_revenue'] / df_aggregated['item_views'].replace(0, 1)
        
        print(f"✓ Załadowano GA4 (Item-based): {len(df_aggregated)} unikalnych produktów")
        return df_aggregated
    
    except Exception as e:
        print(f"✗ Błąd ładowania GA4: {e}")
        return pd.DataFrame()

def zaladuj_meta_ads(katalog_klienta):
    """Ładuje historyczne dane z Meta Ads"""
    ads_files = glob.glob(os.path.join(katalog_klienta, '*report*.csv')) + \
                glob.glob(os.path.join(katalog_klienta, '*ads*.csv'))
    
    if not ads_files:
        print("⚠ Brak plików Meta Ads - kontynuuję bez danych reklamowych")
        return pd.DataFrame()
    
    try:
        df_ads = pd.read_csv(ads_files[0])
        
        # Znajdź kolumny (nazwy mogą się różnić)
        url_col = next((c for c in df_ads.columns if 'link' in c.lower() or 'url' in c.lower()), None)
        spend_col = next((c for c in df_ads.columns if 'spent' in c.lower() or 'spend' in c.lower()), None)
        value_col = next((c for c in df_ads.columns if 'conversion value' in c.lower()), None)
        purchases_col = next((c for c in df_ads.columns if 'purchase' in c.lower() and 'value' not in c.lower()), None)
        roas_col = next((c for c in df_ads.columns if 'roas' in c.lower()), None)
        
        # Rename
        rename_map = {}
        if url_col: rename_map[url_col] = 'url'
        if spend_col: rename_map[spend_col] = 'spend'
        if value_col: rename_map[value_col] = 'conversion_value'
        if purchases_col: rename_map[purchases_col] = 'purchases'
        if roas_col: rename_map[roas_col] = 'roas'
        
        df_ads = df_ads.rename(columns=rename_map)
        
        # Wyczyść URL
        if 'url' in df_ads.columns:
            df_ads['canonical_url'] = df_ads['url'].apply(wyczsc_url)
        else:
            print("✗ Brak kolumny URL w Meta Ads - pomijam")
            return pd.DataFrame()
        
        # Aggregacja per URL
        df_ads_agg = df_ads.groupby('canonical_url').agg({
            'spend': 'sum',
            'conversion_value': 'sum',
            'purchases': 'sum',
            'roas': 'mean'  # Średni ROAS
        }).reset_index()
        
        # Oblicz Contribution Profit
        df_ads_agg['contribution_profit'] = df_ads_agg['conversion_value'] - df_ads_agg['spend']
        
        # Oblicz AOV
        df_ads_agg['aov'] = df_ads_agg['conversion_value'] / df_ads_agg['purchases'].replace(0, 1)
        
        print(f"✓ Załadowano Meta Ads: {len(df_ads)} kampanii → {len(df_ads_agg)} unique URLs")
        return df_ads_agg
    
    except Exception as e:
        print(f"✗ Błąd ładowania Meta Ads: {e}")
        return pd.DataFrame()

# ============================================================================
# POŁĄCZENIE DANYCH
# ============================================================================

def polacz_dane(df_feed, df_ga4, df_ads):
    """
    Łączy Feed + GA4 (Item-based) + Meta Ads w jeden DataFrame
    """
    
    # 1. Match Feed & GA4 (ID or Title)
    if df_ga4.empty:
         df_merged = df_feed.copy()
         df_merged['item_views'] = 0
         df_merged['items_purchased'] = 0
         df_merged['item_revenue'] = 0
         df_merged['arpu'] = 0
    else:
        # Próba ID (best)
        merged_id = df_feed.merge(
            df_ga4,
            left_on='product_id',
            right_on='match_id',
            how='left'
        )
        matched_count = merged_id['item_views'].notna().sum()
        
        # Próba Title (fallback) jeśli słaby match po ID
        if matched_count < len(df_ga4) * 0.1 and matched_count < 20:
             merged_title = df_feed.merge(
                df_ga4,
                left_on='title',
                right_on='match_id',
                how='left'
            )
             if merged_title['item_views'].notna().sum() > matched_count:
                 df_merged = merged_title
             else:
                 df_merged = merged_id
        else:
            df_merged = merged_id

    # 2. Match Meta Ads (najczęściej URL-based)
    # Feed ma 'link', Meta Ads ma 'canonical_url'
    if not df_ads.empty:
        df_merged = df_merged.merge(
            df_ads,
            left_on='link',
            right_on='canonical_url',
            how='left',
            suffixes=('', '_ads')
        )
    else:
        for col in ['spend', 'conversion_value', 'contribution_profit', 'purchases', 'roas', 'aov']:
            df_merged[col] = 0
    
    # Fill NaN
    fill_cols = ['item_views', 'items_purchased', 'item_revenue', 'arpu',
                 'spend', 'conversion_value', 'contribution_profit', 'purchases', 'roas', 'aov']
    
    for col in fill_cols:
        if col in df_merged.columns:
            df_merged[col] = df_merged[col].fillna(0)
        else:
            df_merged[col] = 0

    print(f"✓ Połączono dane: {len(df_merged)} produktów")
    return df_merged

# ============================================================================
# KLASYFIKACJA BCG
# ============================================================================

def klasyfikuj_bcg(df, config):
    """
    Klasyfikuje produkty według BCG Matrix (Item-based)
    Metrics: item_views (Traffic), items_purchased (Volume), item_revenue (Value)
    """
    class_config = config.get('classification', {})
    mode = class_config.get('mode', 'percentile')
    
    print(f"\nKlasyfikacja BCG (tryb: {mode})...")
    
    # Threshold variable mapping
    # 1. Traffic Consideration Threshold (Minimum Viable Product to analyze)
    min_views = class_config.get('absolute_overrides', {}).get('min_sessions_for_consideration', 50)
    df_filtered = df[df['item_views'] >= min_views].copy()
    print(f"  Produkty z ≥{min_views} views: {len(df_filtered)}/{len(df)}")
    
    if df_filtered.empty:
        print("⚠ Brak produktów spełniających kryteria minimalne. Używam domyślnych.")
        tx_threshold = 10
        views_threshold = 100
        arpu_threshold = 50
        slacker_threshold = 5
    elif mode == 'percentile':
        thresholds = class_config.get('thresholds', {})
        
        tx_p = thresholds.get('cash_cow_transactions_percentile', 0.75)
        views_p = thresholds.get('hidden_gem_sessions_percentile', 0.50)
        arpu_p = thresholds.get('hidden_gem_arpu_percentile', 0.60)
        slacker_p = thresholds.get('slacker_transactions_percentile', 0.25)
        
        tx_threshold = df_filtered['items_purchased'].quantile(tx_p)
        views_threshold = df_filtered['item_views'].quantile(views_p)
        arpu_threshold = df_filtered['arpu'].quantile(arpu_p)
        slacker_threshold = df_filtered['items_purchased'].quantile(slacker_p)
        
        print(f"  Progi (percentyle):")
        print(f"    Cash Cow: ≥{tx_threshold:.0f} purchases")
        print(f"    Hidden Gem: ≥{views_threshold:.0f} views + ≥{arpu_threshold:.1f} ARPU")
    else:
        overrides = class_config.get('absolute_overrides', {})
        tx_threshold = overrides.get('min_transactions_for_star', 50)
        views_threshold = overrides.get('hidden_gem_min_sessions', 1000)
        arpu_threshold = overrides.get('hidden_gem_min_arpu', 50)
        slacker_threshold = overrides.get('slacker_transactions_absolute', 10)

    def classify_row(row):
        tx = row['items_purchased']
        views = row['item_views']
        arpu = row['arpu']
        
        if tx >= tx_threshold and views >= views_threshold and arpu >= arpu_threshold:
            return 'Star'
        elif tx >= tx_threshold:
            return 'Cash Cow'
        elif views >= views_threshold and arpu >= arpu_threshold:
            return 'Hidden Gem'
        elif tx <= slacker_threshold and tx > 0:
            return 'Slacker'
        else:
            return 'Ignore'
    
    df_filtered['bcg_type'] = df_filtered.apply(classify_row, axis=1)
    
    df = df.merge(
        df_filtered[['product_id', 'bcg_type']],
        on='product_id',
        how='left'
    )
    df['bcg_type'] = df['bcg_type'].fillna('Ignore')
    
    bcg_summary = df['bcg_type'].value_counts()
    print(f"\n  Wyniki klasyfikacji:")
    for bcg, count in bcg_summary.items():
        print(f"    {bcg}: {count}")
        
    return df

# ============================================================================
# MATRYCA PRIORYTETÓW (BCG × META ADS)
# ============================================================================

def oblicz_priorytety(df):
    """
    Przypisuje priorytety P1-P8 według matrycy:
    
    P1: Star + Profitable ads
    P2: Cash Cow + Profitable ads
    P3: Hidden Gem + Profitable ads
    P4: Star + New/No ads
    P5: Cash Cow + New/No ads
    P6: Hidden Gem + New/No ads
    P7: (Ignore/Slacker) + Profitable ads (anomalie)
    P8: Slacker + (Unprofitable/No ads) → POMIJAMY
    """
    
    print("\nObliczanie priorytetów (BCG × Meta Ads)...")
    
    # Określ status Meta Ads
    def meta_ads_status(row):
        if row['spend'] == 0:
            return 'New'  # Brak historii reklam
        elif row['contribution_profit'] > 0:
            return 'Profitable'
        else:
            return 'Unprofitable'
    
    df['ads_status'] = df.apply(meta_ads_status, axis=1)
    
    # Przypisz priorytety
    def assign_priority(row):
        bcg = row['bcg_type']
        ads = row['ads_status']
        
        if bcg == 'Star' and ads == 'Profitable':
            return 'P1'
        elif bcg == 'Cash Cow' and ads == 'Profitable':
            return 'P2'
        elif bcg == 'Hidden Gem' and ads == 'Profitable':
            return 'P3'
        elif bcg == 'Star' and ads in ['New', 'Unprofitable']:
            return 'P4'
        elif bcg == 'Cash Cow' and ads in ['New', 'Unprofitable']:
            return 'P5'
        elif bcg == 'Hidden Gem' and ads == 'New':
            return 'P6'
        elif bcg in ['Ignore', 'Slacker'] and ads == 'Profitable':
            return 'P7'  # Anomalie - profitable mimo ignore
        else:
            return 'P8'  # Slacker/Ignore + Unprofitable/New → SKIP
    
    df['priority'] = df.apply(assign_priority, axis=1)
    
    # Podsumowanie
    priority_summary = df['priority'].value_counts().sort_index()
    print(f"\n  Rozkład priorytetów:")
    for p, count in priority_summary.items():
        print(f"    {p}: {count} produktów")
    
    # Filtruj tylko P1-P7 (pomijamy P8)
    df_to_advertise = df[df['priority'] != 'P8'].copy()
    print(f"\n✓ Produkty do reklamy (P1-P7): {len(df_to_advertise)}/{len(df)}")
    
    return df, df_to_advertise

# TO BE CONTINUED... (kolejna część w następnym write_to_file)
