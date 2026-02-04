
import pandas as pd
import numpy as np
import json
import os
import argparse

# === CONFIGURATION ===
# Load from JSON
def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# === LOGIC ===
def clean_currency(value):
    """Clean currency string or float to valid float."""
    if pd.isna(value): return 0.0
    if isinstance(value, float): return value
    if isinstance(value, int): return float(value)
    
    clean = str(value).replace('zł', '').replace('EUR', '').replace('$', '').replace(' ', '').replace(',', '.')
    try:
        return float(clean)
    except ValueError:
        return 0.0

def get_margin(category, margins_config):
    """Get margin based on category name from config."""
    # Look for partial match in category name
    cat_lower = str(category).lower()
    for key, value in margins_config.get('categories', {}).items():
        if key in cat_lower:
            return value
    return margins_config.get('default', 0.50)

def calculate_efficiency_triangle(df, account_avgs):
    """
    Classifies products into Unicorn, Premium, Mismatch, Burn, Junk.
    Based on Ratios vs Account Average.
    """
    
    def classify(row):
        # Ratios (1.0 = Average)
        cpm_ratio = row['CPM'] / account_avgs['CPM'] if account_avgs['CPM'] > 0 else 1.0
        ctr_ratio = row['CTR'] / account_avgs['CTR'] if account_avgs['CTR'] > 0 else 1.0
        cr_ratio  = row['CR']  / account_avgs['CR']  if account_avgs['CR'] > 0 else 1.0
        
        # Thresholds
        HIGH_COST = 1.2
        LOW_COST = 0.8
        HIGH_VAL = 1.1
        LOW_VAL  = 0.9
        
        # 1. UNICORN (Cheap, High Interest, High Desire)
        if cpm_ratio < LOW_COST and ctr_ratio > HIGH_VAL and cr_ratio > HIGH_VAL:
             return "Unicorn"
             
        # 2. PREMIUM (Expensive, High Interest, High Desire)
        if cpm_ratio > HIGH_COST and ctr_ratio > HIGH_VAL and cr_ratio > HIGH_VAL:
            return "Premium"
            
        # 3. MISMATCH (High Interest, Low Desire)
        # Scent Match Problem
        if ctr_ratio > HIGH_VAL and cr_ratio < LOW_VAL:
            return "Mismatch"
            
        # 4. BURN (Expensive, Low Interest, Low Desire)
        if cpm_ratio > HIGH_COST and ctr_ratio < LOW_VAL:
            return "Burn"
            
        # 5. JUNK (Cheap, Low Quality)
        if cpm_ratio < LOW_COST and cr_ratio < LOW_VAL:
             return "Junk"
             
        return "Standard"

    df['Diagnostic_Label'] = df.apply(classify, axis=1)
    return df

def main():
    parser = argparse.ArgumentParser(description="Generate ICP Data Foundation (Phase 1)")
    parser.add_argument("--config", required=True, help="Path to client_config.json")
    parser.add_argument("--ga4", required=True, help="Path to GA4 CSV")
    parser.add_argument("--meta", required=True, help="Path to Meta Ads Raw Data CSV")
    parser.add_argument("--output", required=True, help="Output CSV path")
    args = parser.parse_args()
    
    config = load_config(args.config)
    
    # 1. Load Data
    print("Loading Data...")
    df_ga4 = pd.read_csv(args.ga4)
    df_meta = pd.read_csv(args.meta)
    
    # 2. Filter Meta (Objective = Sales) -- IMPORTANT V5 Logic
    if 'Objective' in df_meta.columns:
        print("Filtering for SALES objective...")
        df_meta = df_meta[df_meta['Objective'].str.upper().isin(['CONVERSIONS', 'SALES', 'PRODUCT_CATALOG_SALES'])]
    else:
        print("WARNING: 'Objective' column missing. Skipping Filter (Potentially Dangerous).")
        
    # 3. Stitching (Mock Logic for now - assuming 'Landing Page' or 'Ad Name' contains SKU/ID)
    # In production, we need a robust join. Here we simplify.
    
    # Calculate Meta Metrics per URL/Product
    # Group by Landing Page (or Product ID if available)
    # For this script, we assume Meta has 'URL' or 'Ad Name' that maps to GA4 'Landing Page'
    
    # ... (Stitching logic would go here. For template purposes, we create placeholders) ...
    
    # 4. Financials
    # Calculate Contribution Margin
    # net_rev = rev / vat
    # gross_profit = net_rev * margin
    # contribution = gross_profit - spend
    
    # 5. Efficiency Triangle
    # Calculate Account Averages
    avg_cpm = df_meta['CPM'].mean() if 'CPM' in df_meta.columns else 10.0
    avg_ctr = df_meta['CTR'].mean() if 'CTR' in df_meta.columns else 1.0
    # avg_cr = ...
    
    account_avgs = {
        'CPM': avg_cpm,
        'CTR': avg_ctr,
        'CR': 1.0 # Placeholder
    }
    
    # Apply Classification
    # df_final = calculate_efficiency_triangle(df_merged, account_avgs)
    
    print("Script Template Generated. Requires actual column mapping adjustment for specific client data.")
    
    # Output
    # df_final.to_csv(args.output, index=False)
    print(f"Would write to: {args.output}")

if __name__ == "__main__":
    main()
