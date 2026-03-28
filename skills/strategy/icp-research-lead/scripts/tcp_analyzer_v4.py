"""
ICP Framework V4.0 - Uniwersalny Analizator Produktów (Full Version)

CEL: Robić lepsze reklamy poprzez:
1. Klasyfikację produktów według BCG Matrix (Item-based metrics) + Meta Ads
2. Priorytetyzację P1-P8 (tylko P1-P7 dostają persony)
3. Wykrywanie Person (na podstawie słów kluczowych)
4. Export Master Strategy Map

DANE WEJŚCIOWE:
- Feed XML (produkt title, description, price, category)
- GA4 CSV (Item-based export: Item ID, Item name, Items viewed, Items purchased, Item revenue, Revenue per view)
- Meta Ads CSV (URL, spend, conversion, ROAS)
- Global Templates JSON (słowa kluczowe do detekcji)

DANE WYJŚCIOWE:
- Master_Strategy_Map.csv
- Briefs/ (placeholder)
"""

import pandas as pd
import json
import xml.etree.ElementTree as ET
import glob
import os
import sys
from urllib.parse import urlparse
import re
from datetime import datetime

# ============================================================================
# 1. KONFIGURACJA
# ============================================================================

def zaladuj_konfiguracje(katalog_klienta):
    """Ładuje client_config.json + global_persona_templates.json"""
    config_path = os.path.join(katalog_klienta, 'client_config.json')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_klienta = json.load(f)
    except Exception as e:
        print(f"⚠ Nie można załadować {config_path}: {e}")
        config_klienta = {}
    
    # Globalne szablony person
    # Ścieżka relatywna od skryptu: ../../Core/Configs/global_persona_templates.json
    global_templates_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        '..', '..', 'Core', 'Configs', 'global_persona_templates.json'
    )
    
    try:
        with open(global_templates_path, 'r', encoding='utf-8') as f:
            global_personas = json.load(f)
    except Exception as e:
        print(f"⚠ Nie można załadować global_persona_templates.json: {e}")
        global_personas = {"templates": {}, "detection_rules": {}}
    
    return config_klienta, global_personas

# ============================================================================
# 2. FEED XML
# ============================================================================

def wyczsc_url(url):
    """Usuwa parametry UTM i zwraca canonical URL"""
    if not url or not isinstance(url, str):
        return '/'
    parsed = urlparse(url)
    canonical = parsed.path
    if canonical.endswith('/') and len(canonical) > 1:
        canonical = canonical[:-1]
    return canonical

def parsuj_feed(sciezka_xml):
    """Pobiera ID, Title, Link, Price, Availability, Product Type."""
    print(f"Wczytywanie feedu: {sciezka_xml}")
    try:
        tree = ET.parse(sciezka_xml)
        root = tree.getroot()
        
        products = []
        # Namespace map
        ns = {'g': 'http://base.google.com/ns/1.0'}
        
        items = root.findall('.//item')
        if not items:
             # Try RSS channel item
             items = root.findall('.//channel/item')

        for item in items:
            p = {}
            
            def get_val(tag, tags_list=None):
                # Try finding with namespace first, then without
                if tags_list is None: tags_list = [tag]
                
                for t in tags_list:
                    # Try with 'g:' prefix (namespace)
                    res = item.find(f'g:{t}', ns)
                    if res is not None and res.text: return res.text
                    
                    # Try without prefix
                    res = item.find(t)
                    if res is not None and res.text: return res.text
                return ""

            p['product_id'] = get_val('id')
            p['title'] = get_val('title')
            p['description'] = get_val('description')
            p['link'] = get_val('link')
            
            # Price cleaning
            price_raw = get_val('price')
            try:
                p['price_float'] = float(re.sub(r'[^\d.]', '', price_raw))
            except:
                p['price_float'] = 0.0
                
            p['availability'] = get_val('availability') or "in stock"
            p['product_type'] = get_val('product_type')
            
            products.append(p)
            
        df = pd.DataFrame(products)
        print(f"✓ Załadowano {len(df)} produktów z feedu.")
        return df
    except Exception as e:
        print(f"✗ Błąd Feed XML: {e}")
        return pd.DataFrame()

# ============================================================================
# 3. GA4 (ITEM-BASED)
# ============================================================================

def zaladuj_ga4(katalog_klienta):
    """
    Ładuje dane z GA4. Obsługuje Item-based ORAZ Page-based (jako fallback).
    """
    ga4_files = glob.glob(os.path.join(katalog_klienta, '*GA*.csv'))
    if not ga4_files:
        print("✗ Brak plików GA4 CSV")
        return pd.DataFrame()

    try:
        # Próba wczytania z pominięciem metadata header
        # Często header jest w linii 7 (index 6)
        try:
             # Najpierw sprawdźmy separator i strukturę
             df = pd.read_csv(ga4_files[0], skiprows=6, on_bad_lines='skip')
        except:
             df = pd.read_csv(ga4_files[0], on_bad_lines='skip')

        if df.empty: return pd.DataFrame()

        df.columns = df.columns.str.strip()
        print(f"GA4 Columns: {df.columns.tolist()}")
        
        col_map = {}
        is_page_based = False
        
        # Mapping logic
        if 'Landing page' in df.columns:
            is_page_based = True
            col_map['Landing page'] = 'match_id'
            col_map['Sessions'] = 'items_viewed'
            col_map['Transactions'] = 'items_purchased'
            col_map['Gross purchase revenue'] = 'item_revenue'
            col_map['ARPU'] = 'revenue_per_view'
            # Check for Item revenue explicit
            if 'Item revenue' in df.columns: col_map['Item revenue'] = 'item_revenue'
        else:
            # Item based
            for c in df.columns:
                if 'Item ID' in c: col_map[c] = 'match_id'
                elif 'Item name' in c: col_map[c] = 'match_name'
                elif 'Items purchased' in c: col_map[c] = 'items_purchased'
                elif 'Items viewed' in c: col_map[c] = 'items_viewed'
                elif 'Item revenue' in c: col_map[c] = 'item_revenue'
                elif 'Revenue per view' in c: col_map[c] = 'revenue_per_view'

        df = df.rename(columns=col_map)
        
        # Fallback ID logic
        if 'match_id' not in df.columns and 'match_name' in df.columns:
            df['match_id'] = df['match_name']
            
        if 'match_id' not in df.columns:
            print("✗ GA4: Nie znaleziono kolumny ID/Landing Page")
            return pd.DataFrame()

        # Clean ID
        if is_page_based:
             df['match_id'] = df['match_id'].astype(str).apply(wyczsc_url)

        # Uzupełnij braki
        required_metrics = ['items_purchased', 'items_viewed', 'item_revenue', 'revenue_per_view']
        for m in required_metrics:
            if m not in df.columns: df[m] = 0
            else:
                 # Clean numeric
                 if df[m].dtype == object:
                     df[m] = df[m].astype(str).str.replace(',', '').str.replace(r'[^\d.]', '', regex=True)
                     df[m] = pd.to_numeric(df[m], errors='coerce').fillna(0)

        # Aggregacja
        df_agg = df.groupby('match_id').agg({
            'items_purchased': 'sum',
            'items_viewed': 'sum',
            'item_revenue': 'sum',
            'revenue_per_view': 'mean'
        }).reset_index()

        print(f"✓ GA4 ({'Page' if is_page_based else 'Item'}-based): {len(df_agg)} wierszy")
        return df_agg

    except Exception as e:
        print(f"✗ Błąd GA4: {e}")
        return pd.DataFrame()

# ============================================================================
# 4. META ADS (URL-BASED)
# ============================================================================

def zaladuj_meta_ads(katalog_klienta):
    """Ładuje Ads performance - ZACHOWUJE KAŻDĄ REKLAMĘ OSOBNO (nie agreguje)"""
    ads_files = glob.glob(os.path.join(katalog_klienta, '*report*.csv')) + glob.glob(os.path.join(katalog_klienta, '*ads*.csv'))
    if not ads_files:
        print("⚠ Brak plików Meta Ads")
        return pd.DataFrame()
        
    try:
        # Use python engine for robustness
        df = pd.read_csv(ads_files[0], engine='python', on_bad_lines='warn')
        print(f"✓ Załadowano Meta Ads: {len(df)} wierszy")
        
        # Auto-map kolumn
        rename = {}
        
        # Ad Name
        name_c = next((c for c in df.columns if 'ad name' in c.lower()), None)
        if name_c: rename[name_c] = 'ad_name'
        
        # URL (Landing Page)
        url_c = next((c for c in df.columns if ('link' in c.lower() and 'ad settings' in c.lower()) or 
                      ('url' in c.lower() and 'destination' not in c.lower())), None)
        if url_c: rename[url_c] = 'ad_url'
        
        # Metrics
        spend_c = next((c for c in df.columns if 'amount spent' in c.lower()), None)
        roas_c = next((c for c in df.columns if 'roas' in c.lower()), None)
        val_c = next((c for c in df.columns if 'purchases conversion value' in c.lower()), None)
        purch_c = next((c for c in df.columns if c.lower() == 'purchases'), None)
        
        if spend_c: rename[spend_c] = 'ad_spend'
        if roas_c: rename[roas_c] = 'ad_roas'
        if val_c: rename[val_c] = 'ad_conversion_value'
        if purch_c: rename[purch_c] = 'ad_purchases'
        
        df = df.rename(columns=rename)
        
        # Walidacja
        required_cols = ['ad_url', 'ad_spend']
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            print(f"✗ Brakujące kolumny w Meta Ads: {missing}")
            return pd.DataFrame()
        
        # Czyszczenie URL
        df['canonical_url'] = df['ad_url'].apply(wyczsc_url)
        
        # Filtruj tylko reklamy z wydatkami > 0
        df = df[df['ad_spend'] > 0].copy()
        
        # Wybierz tylko potrzebne kolumny
        cols_to_keep = ['ad_name', 'canonical_url', 'ad_spend', 'ad_roas', 'ad_conversion_value', 'ad_purchases']
        cols_to_keep = [c for c in cols_to_keep if c in df.columns]
        df = df[cols_to_keep]
        
        print(f"✓ Meta Ads: {len(df)} reklam z wydatkami > 0")
        print(f"✓ Unikalne landing pages: {df['canonical_url'].nunique()}")
        return df
        
    except Exception as e:
        print(f"✗ Błąd Meta Ads: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame()

# ============================================================================
# 5. MERGE
# ============================================================================

def polacz_dane(df_feed, df_ga4, df_ads):
    """Integracja danych z DUPLIKACJĄ WIERSZY per reklama"""
    
    # 0. Przygotowanie URLi
    df_feed['link_clean'] = df_feed['link'].apply(wyczsc_url)
    
    # 1. Feed + GA4 (Match by ID)
    if df_ga4.empty:
        merged = df_feed.copy()
        for c in ['items_viewed', 'items_purchased', 'item_revenue', 'revenue_per_view']:
            merged[c] = 0
    else:
        # Preferowany match: produkt_id == match_id
        merged = df_feed.merge(df_ga4, left_on='product_id', right_on='match_id', how='left')
        
        # Sprawdź jakość matchu
        matched_rows = merged['items_viewed'].notna().sum()
        if matched_rows < 0.1 * len(df_feed) and matched_rows < 10:
             print("⚠ Słaby match po ID, próbuję po Title...")
             merged_title = df_feed.merge(df_ga4, left_on='title', right_on='match_id', how='left')
             if merged_title['items_viewed'].notna().sum() > matched_rows:
                 merged = merged_title
                 print("✓ Użyto matchowania po Title")
    
    # Fill NaNs dla GA4
    for c in ['items_viewed', 'items_purchased', 'item_revenue', 'revenue_per_view']:
        if c in merged.columns:
            merged[c] = merged[c].fillna(0)
        else:
            merged[c] = 0
    
    # 2. NOWA LOGIKA: Duplikacja wierszy dla każdej reklamy
    if not df_ads.empty and 'ad_name' in df_ads.columns:
        print(f"\n🔄 DUPLIKACJA WIERSZY per reklama...")
        
        # Znaleźć produkty które pasują do landing pages z reklam
        result_rows = []
        
        for _, product_row in merged.iterrows():
            product_url = product_row['link_clean']
            
            # Znaleźć wszystkie reklamy dla tego landing page
            matching_ads = df_ads[df_ads['canonical_url'] == product_url]
            
            if not matching_ads.empty:
                # DUPLIKUJ wiersz produktu dla każdej reklamy
                for _, ad_row in matching_ads.iterrows():
                    row_copy = product_row.copy()
                    # Dodaj dane z reklamy
                    row_copy['ad_name'] = ad_row.get('ad_name', '')
                    row_copy['ad_spend'] = ad_row.get('ad_spend', 0)
                    row_copy['ad_roas'] = ad_row.get('ad_roas', 0)
                    row_copy['ad_conversion_value'] = ad_row.get('ad_conversion_value', 0)
                    row_copy['ad_purchases'] = ad_row.get('ad_purchases', 0)
                    result_rows.append(row_copy)
            else:
                # Produkt bez reklam - zachowaj 1 wiersz z zerami
                product_row['ad_name'] = ''
                product_row['ad_spend'] = 0
                product_row['ad_roas'] = 0
                product_row['ad_conversion_value'] = 0
                product_row['ad_purchases'] = 0
                result_rows.append(product_row)
        
        merged = pd.DataFrame(result_rows)
        
        # Stats
        total_products = df_feed.shape[0]
        total_rows = merged.shape[0]
        total_ads = df_ads.shape[0]
        print(f"✓ Produkty w feedzie: {total_products}")
        print(f"✓ Reklamy Meta Ads: {total_ads}")
        print(f"✓ Rezultat: {total_rows} wierszy (duplikacja per reklama)")
        
    else:
        # Brak Meta Ads - wszystkie kolumny = 0
        print("⚠ Brak danych Meta Ads")
        for c in ['ad_name', 'ad_spend', 'ad_conversion_value', 'ad_purchases', 'ad_roas']:
            merged[c] = 0 if c != 'ad_name' else ''
    
    return merged

# ============================================================================
# 6. LOGIKA BIZNESOWA (BCG & PRIORYTETY)
# ============================================================================

def klasyfikuj_i_priorytetyzuj(df, config):
    """
    BCG Matrix na podstawie metryk Item-based:
    - Traffic = items_viewed
    - Volume = items_purchased
    - Value = revenue_per_view (Proxy dla 'quality of traffic' / ARPU)
    """
    
    # PROGI
    # Używamy prostych percentyli jeśli brak configu
    class_config = config.get('classification', {})
    thresholds = class_config.get('thresholds', {})
    
    # Filtrujemy tylko produkty z jakimkolwiek ruchem do wyznaczania progów
    active_products = df[df['items_viewed'] > 10]
    if active_products.empty:
        active_products = df # Fallback
        
    p_tx_high = active_products['items_purchased'].quantile(0.75) if not active_products.empty else 10
    p_view_high = active_products['items_viewed'].quantile(0.50) if not active_products.empty else 100
    p_rpv_high = active_products['revenue_per_view'].quantile(0.60) if not active_products.empty else 5.0
    p_tx_low = active_products['items_purchased'].quantile(0.25) if not active_products.empty else 0
    
    print(f"\nProgi BCG (obliczone):")
    print(f"- High Purchases: > {p_tx_high:.0f}")
    print(f"- High Views: > {p_view_high:.0f}")
    print(f"- High Rev/View: > {p_rpv_high:.2f}")

    def get_bcg(row):
        tx = row['items_purchased']
        views = row['items_viewed']
        rpv = row['revenue_per_view']
        
        if tx >= p_tx_high and views >= p_view_high and rpv >= p_rpv_high: return 'Star'
        if tx >= p_tx_high: return 'Cash Cow'
        if views >= p_view_high and rpv >= p_rpv_high: return 'Hidden Gem'
        if tx <= p_tx_low and tx > 0: return 'Slacker'
        return 'Ignore'

    df['bcg_matrix'] = df.apply(get_bcg, axis=1)

    # --- CONTRIBUTION MARGIN & CATEGORY ---
    
    def determine_category_and_margin(row):
        title = str(row['title']).lower()
        ptype = str(row.get('product_type', '')).lower()
        
        # Mapping rules based on User Request
        
        # HOME (10%)
        # - Desktop Monitors
        # - Gaming Monitors
        # - Signage Displays
        
        # PRO (15%)
        # - Open Frame Touch Screens
        # - Unified Communication
        # - Accessories
        # - IFP - Interactive Displays
        # - Touch Screen Monitors
        # - Android Touch Displays
        
        # Helper check
        def is_match(keywords):
            return any(k in title or k in ptype for k in keywords)

        # 1. Check Pro Segments first (Specialists)
        pro_ifp = ['interactive', 'ifp', 'interaktywne', ' te', 'te02', 'te04', 'te6', 'te7', 'te8'] # IFP (TE series for Education)
        pro_android_touch = [' th', 'th0', 'th1', 'th2', 'th6', 'th8', 'self-service', 'kiosk'] # Android Touch (TH series for POS/Kiosks)
        pro_touch = ['touch', 'dotykowe', 'prolite t', 'tf'] # Touch Screen Monitors (Desktop/Open Frame touch)
        pro_open = ['open frame', 'zabudowy'] # Open Frame
        pro_uc = ['unified communication', 'uc', 'webcam', 'kamera'] # UC
        pro_android = ['android'] # Android specific (catch-all)
        pro_acc = ['akcesoria', 'uchwyt', 'kabel', 'stojak', 'mount', 'cable', 'stand', 'folia', 'filtr'] # Accessories
        
        if is_match(pro_ifp + pro_android_touch + pro_touch + pro_open + pro_uc + pro_android + pro_acc):
            return "Pro", 0.15
            
        # 2. Check Home Segments
        home_gaming = ['g-master', 'gaming', 'black hawk', 'red eagle', 'gold phoenix', 'silver crow']
        home_signage = ['signage', 'lfd', 'large format', 'wielkoformatowe', 'lh'] # Signage (Non-touch LFD)
        home_desktop = ['desktop', 'monitory biurowe', 'biurkowe', 'prolite x', 'prolite b', 'prolite e'] # Desktop
        
        if is_match(home_gaming + home_signage + home_desktop):
            return "Home", 0.10
            
        # 3. Fallback logic
        # If it has "ProLite" and wasn't caught by Touch/OpenFrame, it's likely Desktop (Home)
        if 'prolite' in title:
             return "Home", 0.10
             
        # Default fallback
        return "Home", 0.10
            
    # Apply
    df[['category_segment', 'margin_percent']] = df.apply(
        lambda r: pd.Series(determine_category_and_margin(r)), axis=1
    )
    
    # CM Calculation: (Purchase Conversion Value / 1.23 * Gross Profit * 1.1) - Amount Spent
    def calc_cm(row):
        pcv = row.get('purchases_conversion_value', 0)
        spend = row.get('ad_spend', 0) # mapped from amount_spent
        margin = row['margin_percent']
        
        # Formulas
        # Net Value = PCV / 1.23
        # Gross Profit Value = Net Value * Margin
        # Uplifted Profit = Gross Profit Value * 1.1 (Frequency)
        
        cm = (pcv / 1.23 * margin * 1.1) - spend
        return cm

    df['contribution_margin'] = df.apply(calc_cm, axis=1)

    # PRIORYTETY P1-P8
    def get_priority(row):
        bcg = row['bcg_matrix']
        cm = row['contribution_margin']
        spend = row['ad_spend']
        
        # 4. W kolumnie BV (Ads Status) mamy 3 możliwe scenariusze: 
        # a) nie było reklam -> New 
        # b) Reklama jest nierentowna -> Unprofitable 
        # c) Reklama jest rentowna -> Profitable.
        
        if pd.isna(spend) or spend == 0:
            ads_status = 'New'
        elif cm > 0:
            ads_status = 'Profitable'
        else:
            ads_status = 'Unprofitable'
            
        row['ads_status'] = ads_status # Store for export
        
        if bcg == 'Star' and ads_status == 'Profitable': return 'P1'
        if bcg == 'Cash Cow' and ads_status == 'Profitable': return 'P2'
        if bcg == 'Hidden Gem' and ads_status == 'Profitable': return 'P3'
        
        if bcg == 'Star': return 'P4'
        if bcg == 'Cash Cow': return 'P5'
        if bcg == 'Hidden Gem': return 'P6'
        
        if ads_status == 'Profitable': return 'P7' # Anomaly
        
        return 'P8' # Ignore/Slacker without ads profit

    df['priority'] = df.apply(get_priority, axis=1)
    
    print(f"\nRozkład priorytetów:")
    print(df['priority'].value_counts().sort_index())
    
    return df

# ============================================================================
# 7. PERSONA DETECTION (Basic Structure)
# ============================================================================

def wykryj_persony(df, global_personas, katalog_klienta):
    """
    Zaawansowana detekcja person oparta o:
    1. Ekstrakcję cech (Regex) z Title/Description (Feed)
    2. Scoring System (Punkty za cechy i słowa kluczowe)
    3. Przypisanie zwycięskiej persony
    """
    print("\nWykrywanie person (Regex Extraction & Scoring)...")
    
    extraction_rules = global_personas.get('feature_extraction_rules', {})
    scoring_rules = global_personas.get('scoring_rules', {})
    templates = global_personas.get('templates', {})

    # --- 1. FEATURE EXTRACTION ---
    def extract_features(row):
        # Łączymy Title + Description z Feedu (z CSV export feed columns)
        # Feed data is in 'title' and 'description' columns of the merged DF
        text = (str(row.get('title', '')) + " " + str(row.get('description', ''))).lower()
        
        extracted = {}
        features_list = []
        
        for feature_name, rule in extraction_rules.items():
            pattern = rule.get('pattern')
            f_type = rule.get('type')
            
            match = re.search(pattern, text)
            if match:
                val = match.group(1) # Pierwsza grupa (wartość)
                
                # Konwersja typów
                if f_type == 'int':
                    try: val = int(val)
                    except: val = 0
                elif f_type == 'float':
                    try: val = float(val)
                    except: val = 0.0
                elif f_type == 'bool':
                    val = True
                    
                extracted[feature_name] = val
                
                # Do wyświetlania w kolumnie (np. "165hz", "docking")
                if f_type == 'bool': features_list.append(feature_name)
                else: features_list.append(f"{feature_name}:{val}")
                
        return pd.Series([extracted, ", ".join(features_list)])

    # Apply extraction
    df[['extracted_specs', 'detected_features']] = df.apply(extract_features, axis=1)

    # --- 2. SCORING SYSTEM ---
    def score_row(row):
        specs = row['extracted_specs']
        title = str(row.get('title', '')).lower()
        
        scores = {}
        
        for persona, rule in scoring_rules.items():
            score = rule.get('base_score', 0)
            
            for cond in rule.get('conditions', []):
                # 1. Title Keywords
                if 'title_keyword' in cond:
                    if cond['title_keyword'] in title:
                        score += cond['points']
                        
                # 2. Feature conditions
                elif 'feature' in cond:
                    fname = cond['feature']
                    if fname in specs:
                        fval = specs[fname]
                        op = cond.get('operator')
                        target = cond.get('value')
                        points = cond.get('points', 0)
                        
                        passed = False
                        if op == 'exists': passed = True
                        elif op == '>=': passed = fval >= target
                        elif op == '<=': passed = fval <= target
                        elif op == '<': passed = fval < target
                        elif op == '>': passed = fval > target
                        elif op == 'contains': passed = target in str(fval)
                        elif op == '==': passed = fval == target
                        
                        if passed: score += points
                        
            scores[persona] = score
            
        # Wybierz zwycięzcę
        if not scores: return 'generic_buyer'
        
        best_persona = max(scores, key=scores.get)
        if scores[best_persona] > 0:
            return best_persona
        else:
            return 'generic_buyer' # Brak punktów = generic

    df['persona_id'] = df.apply(score_row, axis=1)

    # --- 3. WZBOGACANIE (Enrichment) ---
    def enrich_row(row):
        pid = row.get('persona_id', 'generic_buyer')
        template = templates.get(pid, templates.get('generic', {}))
        
        return pd.Series({
            'persona_name': template.get('name', ''),
            'macro_persona': template.get('macro_persona', ''),
            'transformation': template.get('transformation', ''),
            'persona_pain': template.get('pain', ''),
            'persona_dream': template.get('dream', ''),
            'persona_voc': "; ".join(template.get('voice_of_customer', [])),
            'recommended_frameworks': "; ".join(template.get('frameworks', [])),
            'recommended_styles': "; ".join(template.get('styles', []))
        })
        
    enriched = df.apply(enrich_row, axis=1)
    df = pd.concat([df, enriched], axis=1)
    
    print(f"✓ Wykryto persony (Regex Scoring): {df['persona_id'].value_counts().to_dict()}")
    return df

# ============================================================================
# 8. EXPORT (Final Structure)
# ============================================================================

def eksportuj_wyniki(df, katalog_klienta):
    """Zapisuje Master_Strategy_Map.csv z PREFIKSAMI i PO POLSKU"""
    import datetime
    output_path = os.path.join(katalog_klienta, 'Master_Strategy_Map.csv')
    
    # =========================
    # KROK 1: RENAME COLUMNS (Prefiksy + Polski)
    # =========================
    
    rename_map = {
        # A. Identifiers
        'product_id': 'feed_product_id',
        'title': 'feed_title',
        'link': 'feed_url',
        
        # B. Feed Data
        'price_float': 'feed_price',
        'availability': 'feed_availability',
        
        # C. GA4 Metrics
        'items_viewed': 'ga4_sessions',
        'items_purchased': 'ga4_transactions',
        'item_revenue': 'ga4_revenue',
        'revenue_per_view': 'ga4_arpu',
        
        # D. Meta Ads Metrics
        'ad_name': 'meta_ad_name',
        'ad_spend': 'meta_spend',
        'ad_roas': 'meta_roas',
        'ad_conversion_value': 'meta_revenue',
        'ad_purchases': 'meta_transactions',
        
        # E. Classification (Calculated)
        'bcg_matrix': 'calc_bcg_type',
        'priority': 'calc_priority',
        'category_segment': 'calc_segment',
        'margin_percent': 'calc_margin_pct',
        'contribution_margin': 'calc_contribution_margin',
        
        # F. Persona (POLSKI)
        'macro_persona': 'makro_persona',
        'persona_id': 'persona_id',  # ID pozostaje
        'persona_name': 'persona_nazwa',
        'transformation': 'transformacja',
        'persona_pain': 'persona_bol',
        'persona_dream': 'persona_marzenie',
        'persona_voc': 'persona_cytat',
        'detected_features': 'wykryte_cechy',
        'recommended_frameworks': 'rekomendowane_frameworki',
        'recommended_styles': 'rekomendowane_style'
    }
    
    # Rename existing columns
    df = df.rename(columns=rename_map)
    
    # =========================
    # KROK 2: DODATKOWE KOLUMNY
    # =========================
    
    # 1. feed_description
    if 'description' in df.columns:
        df['feed_description'] = df['description'].astype(str).str[:200]
    else:
        df['feed_description'] = df['feed_title'].astype(str).str[:200]
    
    # 2. meta_status
    def determine_meta_status(row):
        if row.get('meta_spend', 0) > 0:
            return 'Active'
        return 'Not Running'
    
    df['meta_status'] = df.apply(determine_meta_status, axis=1)
    
    # 3. calc_aov (Average Order Value)
    def calculate_aov(row):
        transactions = row.get('ga4_transactions', 0)
        revenue = row.get('ga4_revenue', 0)
        if transactions > 0:
            return round(revenue / transactions, 2)
        return 0
    
    df['calc_aov'] = df.apply(calculate_aov, axis=1)
    
    # 4. sciezka_briefu
    def get_brief_path(row):
        filename = f"BRIEF_{row['calc_priority']}_{row['feed_product_id']}_{row['persona_id']}.md"
        path = os.path.join(katalog_klienta, filename)
        if os.path.exists(path):
            return filename
        return ''
    
    df['sciezka_briefu'] = df.apply(get_brief_path, axis=1)
    
    # 5. auto_insight (poprawione - również dla produktów bez ad spend)
    def generate_insight(row):
        priority = row.get('calc_priority', 'P8')
        roas = row.get('meta_roas', 0)
        ad_spend = row.get('meta_spend', 0)
        sessions = row.get('ga4_sessions', 0)
        revenue = row.get('ga4_revenue', 0)
        
        # Insighty dla produktów BEZ reklam
        if ad_spend == 0:
            if priority in ['P1', 'P2'] and revenue > 1000:
                return 'Organic Winner - No Paid Traffic Yet'
            elif sessions > 100 and revenue > 500:
                return 'Hidden Gem - Consider Testing'
            elif priority == 'P1':
                return 'Quick Win - Launch Ad Campaign'
        
        # Insighty dla produktów Z reklamami
        if ad_spend > 0:
            if priority == 'P1' and roas > 3.0:
                return 'High ROAS - Scale Up'
            elif priority in ['P6', 'P7', 'P8'] and ad_spend > 100:
                return 'Review - High Spend, Low Performance'
            elif priority in ['P1', 'P2'] and roas > 2.0:
                return 'Strong Performer - Continue'
        
        return ''
    
    df['auto_insight'] = df.apply(generate_insight, axis=1)
    
    # =========================
    # KROK 3: FINALNA STRUKTURA (30 kolumn - USUNIĘTO date_generated + confidence_score)
    # =========================
    
    cols = [
        # A. Identifiers (3)
        'feed_product_id', 'feed_title', 'feed_url',
        
        # B. Feed Data (3)
        'feed_price', 'feed_description', 'feed_availability',
        
        # C. GA4 Metrics (4)
        'ga4_sessions', 'ga4_transactions', 'ga4_revenue', 'ga4_arpu',
        
        # D. Meta Ads Metrics (6)
        'meta_ad_name', 'meta_spend', 'meta_revenue', 'meta_roas', 'meta_transactions', 'meta_status',
        
       # E. Classification (5)
        'calc_bcg_type', 'calc_priority', 'calc_segment', 'calc_margin_pct', 'calc_contribution_margin', 'calc_aov',
        
        # F. Persona (PL) (10)
        'makro_persona', 'persona_id', 'persona_nazwa', 'transformacja', 
        'persona_bol', 'persona_marzenie', 'persona_cytat', 'wykryte_cechy',
        'rekomendowane_frameworki', 'rekomendowane_style',
        
        # G. Creative Guidance (2)
        'sciezka_briefu', 'auto_insight'
    ]
    
    # Filtruj tylko istniejące kolumny
    final_cols = [c for c in cols if c in df.columns]
    
    # =========================
    # KROK 4: SORTOWANIE I ZAPIS
    # =========================
    
    sort_cols = ['calc_priority', 'calc_contribution_margin']
    if 'calc_contribution_margin' not in df.columns:
        sort_cols = ['calc_priority']
    
    df_sorted = df.sort_values(by=sort_cols, ascending=[True, False])
    
    df_sorted.to_csv(output_path, index=False, encoding='utf-8', columns=final_cols)
    print(f"\n✓ Zapisano: {output_path}")
    print(f"✓ Kolumn: {len(final_cols)}")
    print(f"✓ Wierszy: {len(df_sorted)}")
    
    # =========================
    # KROK 5: GENEROWANIE BRIEFÓW (NOWA STRATEGIA: P1 + P2 + P3 top5)
    # =========================
    
    def generate_sample_brief(row, output_dir):
        try:
            filename = f"BRIEF_{row['calc_priority']}_{str(row['feed_product_id'])}_{str(row['persona_id'])}.md"
            path = os.path.join(output_dir, filename)
            
            content = f"""# Creative Brief: {row['feed_title']}

**Priorytet**: {row['calc_priority']} ({row['calc_bcg_type']})
**Persona**: {row['persona_nazwa']} ({row.get('makro_persona', '')})
**Cena**: {row['feed_price']} PLN

---

## 🎯 Target Audience
**Kim jest**: {row.get('persona_nazwa', '')}
**Transformacja**: 
> {row.get('transformacja', '')}

**Ból**:
> {row.get('persona_bol', '')}

**Marzenie**:
> {row.get('persona_marzenie', '')}

**Voice of Customer**:
> "{row.get('persona_cytat', '')}"

---

## 🔍 Wykryte Cechy (USP)
{row.get('wykryte_cechy', '')}

---

## 🎨 Wytyczne Kreatywne
**Style**: {row.get('rekomendowane_style', '')}
**Frameworki**: {row.get('rekomendowane_frameworki', '')}

---

## 📊 Performance Data
**Sessions (90d)**: {row.get('ga4_sessions', 0)}
**Total Revenue**: {row.get('ga4_revenue', 0)} PLN
**Ad Spend**: {row.get('meta_spend', 0)} PLN
**ROAS**: {row.get('meta_roas', 0)}
"""
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filename}")
        except Exception as e:
            print(f"  ✗ Błąd: {e}")
    
    # === STRATEGIA BRIEFÓW ===
    # P1: wszystkie
    # P2: wszystkie
    # P3: top 5 (najwyższy contribution_margin)
    
    print("\n--- GENEROWANIE BRIEFÓW ---")
    
    # Usuń duplikaty - tylko unique produkty (różne reklamy mogą duplikować)
    df_unique = df_sorted.drop_duplicates(subset=['feed_product_id', 'persona_id'], keep='first')
    
    p1_products = df_unique[df_unique['calc_priority'] == 'P1']
    p2_products = df_unique[df_unique['calc_priority'] == 'P2']
    p3_products = df_unique[df_unique['calc_priority'] == 'P3'].nlargest(5, 'calc_contribution_margin')
    
    to_brief = pd.concat([p1_products, p2_products, p3_products])
    
    print(f"P1: {len(p1_products)} | P2: {len(p2_products)} | P3: {len(p3_products)} (top 5)")
    print(f"Total briefów do generacji: {len(to_brief)}\n")
    
    for _, product in to_brief.iterrows():
        generate_sample_brief(product, katalog_klienta)
    
    print(f"\n✓ Wygenerowano {len(to_brief)} briefów")


def main():
    if len(sys.argv) < 2:
        print("Użycie: python tcp_analyzer_v4.py <sciezka_do_klienta>")
        sys.exit(1)
        
    katalog = sys.argv[1]
    print(f"--- ANALIZA TCP V4.0: {os.path.basename(katalog)} ---")
    
    # 1. Config
    cfg, templates = zaladuj_konfiguracje(katalog)
    
    # 2. Data Loading
    df_feed = parsuj_feed(os.path.join(katalog, 'feed.xml'))
    if df_feed.empty:
        print("Błąd: Feed jest wymagany.")
        sys.exit(1)
        
    df_ga4 = zaladuj_ga4(katalog)
    df_ads = zaladuj_meta_ads(katalog)
    
    # 3. Merge
    df_full = polacz_dane(df_feed, df_ga4, df_ads)
    
    # 4. Logic (BCG + Priority)
    df_scored = klasyfikuj_i_priorytetyzuj(df_full, cfg)
    
    # 5. Logic (Persona Structure)
    df_personas = wykryj_persony(df_scored, templates, katalog)
    
    # 6. Export
    eksportuj_wyniki(df_personas, katalog)
    
    print("\n--- ZAKOŃCZONO SUKCESEM ---")

if __name__ == "__main__":
    main()
