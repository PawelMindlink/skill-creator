#!/usr/bin/env python3
"""
Landing Page Final Generator - Iiyama (Refactored v2.0)
- Source: GA4 Landing Pages (Base)
- Joins: Product Feed, Meta Ads (Aggregated), VoC
- Logic: Aggregated Metrics, Financial Calcs (Margins, Caps), Price Groups
"""
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
from pathlib import Path
import json
import re
import random

# ============================================================================
# CONFIGURATION
# ============================================================================
CLIENT_DIR = Path(r"c:\Users\Paweł\Documents\GitHub\Meta Ads Analysis Production Upload\research\Clients\iiyama")
GA4_LANDING_PAGES = CLIENT_DIR / "GA4_Landing_Pages_Segments.csv"
GA4_ITEMS = CLIENT_DIR / "GA4_Items_Breakdown.csv"
FEED_XML = CLIENT_DIR / "feed.xml"

# NEW Aggregated Report
META_ADS = CLIENT_DIR / "Untitled-report-Feb-4-2025-URL breakdownto-Feb-4-2026.csv" 

CLIENT_CONFIG = CLIENT_DIR / "client_config.json"
VOC_INPUT = CLIENT_DIR / "voc_input.json"

OUTPUT_CSV = CLIENT_DIR / "landing_page_final.csv"

# Financial Constants
VAT_RATE = 0.23
MARGIN_PRO = 0.15
MARGIN_HOME = 0.10

# Price Groups (PLN Net or Gross? Usually based on Gross Price in Feed)
PRICE_THRESHOLDS = {
    "Budget": (0, 700),
    "Mainstream": (700, 1500),
    "High-End": (1500, 3000),
    "Premium": (3000, 999999)
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_feed_xml(feed_path):
    """Load product feed XML and return DataFrame"""
    try:
        tree = ET.parse(feed_path)
        root = tree.getroot()
        
        products = []
        for item in root.findall('.//item'):
            product = {
                'feed_id': item.find('g:id', {'g': 'http://base.google.com/ns/1.0'}).text if item.find('g:id', {'g': 'http://base.google.com/ns/1.0'}) is not None else None,
                'feed_title': item.find('title').text if item.find('title') is not None else None,
                'feed_link': item.find('link').text if item.find('link') is not None else None,
                'feed_price': item.find('g:price', {'g': 'http://base.google.com/ns/1.0'}).text if item.find('g:price', {'g': 'http://base.google.com/ns/1.0'}) is not None else None,
                'feed_description': item.find('description').text if item.find('description') is not None else None,
                'feed_category': item.find('g:product_type', {'g': 'http://base.google.com/ns/1.0'}).text if item.find('g:product_type', {'g': 'http://base.google.com/ns/1.0'}) is not None else None,
            }
            products.append(product)
        
        df = pd.DataFrame(products)
        
        # Extract price as float
        if 'feed_price' in df.columns:
            df['feed_price_clean'] = df['feed_price'].str.replace(' PLN', '').str.replace(',', '').astype(float)
        
        return df
    except Exception as e:
        print(f"Error loading feed: {e}")
        return pd.DataFrame()

def normalize_url(url):
    """Remove domain and query parameters, keep path"""
    if pd.isna(url): return ""
    url = str(url).strip()
    url = url.replace('https://iiyama-sklep.pl', '')
    url = url.split('?')[0]
    return url.strip('/')

def assign_price_group(price):
    """Assign Price Group based on Gross Price"""
    if pd.isna(price) or price == 0:
        return "Unknown"
    
    for group, (low, high) in PRICE_THRESHOLDS.items():
        if low <= price < high:
            return group
    return "Custom"

def assign_macro_persona(row):
    """Assign macro persona based on keywords"""
    url = str(row.get('landing_page', '')).lower()
    title = str(row.get('feed_title', '') or '').lower()
    
    # Pro/Business
    if any(kw in url or kw in title for kw in ['pro', 'professional', 'business', 'biurowe', 'office', 'signage']):
        return 'Specialist'
    # Gaming
    if any(kw in url or kw in title for kw in ['gaming', 'game', 'g-master', 'red eagle', 'black hawk']):
        return 'Enthusiast'
    # Default
    return 'Pragmatist'

def get_psychographics(persona, voc_data):
    """Get random Fear and Dream for persona from VoC"""
    # Map macro persona to VoC keys
    key_map = {
        "Enthusiast": "Enthusiast",
        "Specialist": "Specialist",
        "Pragmatist": "Specialist" # Default fallback
    }
    
    key = key_map.get(persona, "Specialist")
    
    data = voc_data.get(key, {})
    pains = data.get("PAIN", ["Standard market frustration"])
    dreams = data.get("DREAM", ["Reliable quality solution"])
    
    # Pick first item for stability
    fear = pains[0] if pains else ""
    dream = dreams[0] if dreams else ""
    
    return fear, dream

def calculate_financials(row):
    """Calculate Margins, Caps, Frequency"""
    
    # 1. Gross Margin %
    persona = row.get('makro_persona', 'Pragmatist')
    if persona == 'Specialist':
        margin_pct = MARGIN_PRO
    else:
        margin_pct = MARGIN_HOME
        
    # 2. Bid Cap
    # Formula: Product Price / 1.23 * Margin
    # If not a product (category page), use Avg Purchase Revenue?
    # Let's use avg purchase revenue from GA4 if product price missing.
    price = row.get('feed_price_clean', 0)
    if not price or price == 0:
        price = row.get('home_avg_purchase_revenue', 0) # Fallback
        
    bid_cap = (price / (1 + VAT_RATE)) * margin_pct
    
    # 3. Cost Cap
    cost_cap = bid_cap * 0.70
    
    # 4. Contribution Margin
    # Formula: (Meta Revenue / 1.23 * Margin * 1.1) - Ad Spend
    
    meta_rev = row.get('meta_revenue', 0)
    meta_spend = row.get('meta_ad_spend', 0)
    
    contribution_margin = (meta_rev / (1 + VAT_RATE) * margin_pct * 1.1) - meta_spend
    
    # 5. Frequency
    # Formula: Transactions / First Purchasers
    home_trans = row.get('home_transactions', 0)
    pro_trans = row.get('pro_transactions', 0)
    home_first = row.get('home_first_purchasers', 0)
    pro_first = row.get('pro_first_purchasers', 0)
    
    total_trans = home_trans + pro_trans
    total_first = home_first + pro_first
    
    if total_first > 0:
        freq = total_trans / total_first
    else:
        freq = 0
        
    return pd.Series([margin_pct, bid_cap, cost_cap, contribution_margin, freq])

# ============================================================================
# MAIN PIPELINE
# ============================================================================

def main():
    print("=" * 80)
    print("LANDING PAGE FINAL GENERATOR - REFACTOR v2.0")
    print("=" * 80)
    
    # Load VoC
    try:
        with open(VOC_INPUT, 'r', encoding='utf-8') as f:
            voc_data = json.load(f)
    except:
        voc_data = {}

    # ========================================================================
    # STEP 1: Load GA4 Landing Pages (BASE)
    # ========================================================================
    print("\n[1/6] Loading GA4 Landing Pages (BASE)...")
    col_names = [
        'landing_page', 
        'home_sessions', 'home_arpu', 'home_revenue', 'home_transactions', 'home_first_purchasers', 'home_avg_purchase_revenue',
        'pro_sessions', 'pro_arpu', 'pro_revenue', 'pro_transactions', 'pro_first_purchasers', 'pro_avg_purchase_revenue'
    ]
    try:
        df_base = pd.read_csv(GA4_LANDING_PAGES, skiprows=9, header=None, names=col_names, on_bad_lines='skip')
    except Exception as e:
        print(f"Error reading GA4 CSV: {e}")
        return

    df_base = df_base[df_base['landing_page'].notna()]
    df_base['landing_page_normalized'] = df_base['landing_page'].apply(normalize_url)
    
    # Numeric conversion
    numeric_cols = df_base.columns[1:-1] # exclude landing_page and normalized
    for col in numeric_cols:
        df_base[col] = pd.to_numeric(df_base[col], errors='coerce').fillna(0)
        
    print(f"   ✓ Loaded {len(df_base)} rows")

    # ========================================================================
    # STEP 2: Load Product Feed
    # ========================================================================
    print("\n[2/6] Loading Product Feed...")
    df_feed = load_feed_xml(FEED_XML)
    if not df_feed.empty:
        df_feed['feed_link_normalized'] = df_feed['feed_link'].apply(normalize_url)
    
    # ========================================================================
    # STEP 3: Load Meta Ads (Aggregated)
    # ========================================================================
    print("\n[3/6] Loading Meta Ads (Aggregated)...")
    try:
        # Load the new "Untitled..." report
        # It has "Website URL" etc.
        df_ads = pd.read_csv(META_ADS)
        
        df_ads.rename(columns={
            'Website URL': 'ad_url',
            'Amount spent (PLN)': 'meta_ad_spend',
            'Purchases conversion value': 'meta_revenue',
            'Purchases': 'meta_purchases'
        }, inplace=True)
        
        # Normalize URL
        df_ads['ad_link_normalized'] = df_ads['ad_url'].apply(normalize_url)
        
        # Aggregate just in case (though file seems aggregated)
        df_ads_agg = df_ads.groupby('ad_link_normalized').agg({
            'meta_ad_spend': 'sum',
            'meta_revenue': 'sum',
            'meta_purchases': 'sum'
        }).reset_index()
        
        print(f"   ✓ Loaded {len(df_ads_agg)} aggregated ad rows")
        
    except Exception as e:
        print(f"Error loading Meta Ads: {e}")
        df_ads_agg = pd.DataFrame(columns=['ad_link_normalized', 'meta_ad_spend', 'meta_revenue', 'meta_purchases'])

    # ========================================================================
    # STEP 4: JOIN DATA
    # ========================================================================
    print("\n[4/6] Joining Data Sources...")
    
    # Join Feed
    df_merged = pd.merge(df_base, df_feed, left_on='landing_page_normalized', right_on='feed_link_normalized', how='left')
    
    # Join Ads
    df_merged = pd.merge(df_merged, df_ads_agg, left_on='landing_page_normalized', right_on='ad_link_normalized', how='left')
    
    # Fill NAs
    df_merged['meta_ad_spend'] = df_merged['meta_ad_spend'].fillna(0)
    df_merged['meta_revenue'] = df_merged['meta_revenue'].fillna(0)
    df_merged['meta_purchases'] = df_merged['meta_purchases'].fillna(0)
    df_merged['is_product'] = df_merged['feed_id'].notna()

    # ========================================================================
    # STEP 5: CALCULATIONS & ENRICHMENT
    # ========================================================================
    print("\n[5/6] Calculating Metrics & Persona...")
    
    # Personas
    df_merged['makro_persona'] = df_merged.apply(assign_macro_persona, axis=1)
    
    # Psychographics (VoC)
    df_merged[['fears', 'dreams']] = df_merged.apply(
        lambda row: pd.Series(get_psychographics(row['makro_persona'], voc_data)), axis=1
    )
    
    # Price Groups
    df_merged['price_group'] = df_merged['feed_price_clean'].apply(assign_price_group)
    
    # Financials (Margins, Caps, Freq, Contribution)
    df_merged[['gross_margin_percent', 'bid_cap', 'cost_cap', 'contribution_margin', 'frequency']] = df_merged.apply(calculate_financials, axis=1)
    
    # Priority (P1-P8 Based on Contribution Margin)
    # Only prioritize products
    
    ranks = df_merged['contribution_margin'].rank(pct=True)
    df_merged['calc_priority'] = 'P8' # Default
    df_merged.loc[ranks >= 0.90, 'calc_priority'] = 'P1'
    df_merged.loc[(ranks >= 0.75) & (ranks < 0.90), 'calc_priority'] = 'P2'
    df_merged.loc[(ranks >= 0.60) & (ranks < 0.75), 'calc_priority'] = 'P3'
    df_merged.loc[(ranks >= 0.40) & (ranks < 0.60), 'calc_priority'] = 'P4'
    df_merged.loc[(ranks >= 0.25) & (ranks < 0.40), 'calc_priority'] = 'P5'
    df_merged.loc[(ranks >= 0.10) & (ranks < 0.25), 'calc_priority'] = 'P6'
    df_merged.loc[(ranks >= 0.02) & (ranks < 0.10), 'calc_priority'] = 'P7'
    
    # ========================================================================
    # STEP 6: EXPORT
    # ========================================================================
    print("\n[6/6] Exporting Final CSV...")
    
    final_cols = [
        'landing_page', 'is_product', 'product_name', 'feed_price_clean', 'price_group',
        'makro_persona', 'fears', 'dreams',
        'home_sessions', 'home_revenue', 'home_transactions',
        'pro_sessions', 'pro_revenue', 'pro_transactions',
        'meta_ad_spend', 'meta_revenue', 'meta_purchases',
        'gross_margin_percent', 'vat_rate', 'bid_cap', 'cost_cap', 'frequency',
        'contribution_margin', 'calc_priority'
    ]
    
    # Rename feed title and fill product_name
    df_merged['product_name'] = df_merged['feed_title']
    df_merged['vat_rate'] = VAT_RATE
    
    # Filter only available
    df_export = df_merged[[c for c in final_cols if c in df_merged.columns]].copy()
    
    # Sorting
    df_export.sort_values('contribution_margin', ascending=False, inplace=True)
    
    df_export.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    print(f"✅ Exported to {OUTPUT_CSV}")
    print(f"   ✓ Total Rows: {len(df_export)}")

if __name__ == "__main__":
    main()
