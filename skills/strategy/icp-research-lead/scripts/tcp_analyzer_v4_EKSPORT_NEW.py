# NOWA WERSJA eksportuj_wyniki - do skopiowania do tcp_analyzer_v4.py

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
        if os.exists(path):
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
