---
name: icp-research-lead
description: Data pipeline skill. Merges Product Feed + GA4 + Meta Ads into Strategy Map CSV with BCG classification, persona assignment, and margin-protected bid calculations.
version: 3.4.0
changelog: |
  v3.4.0: Scope clarified — data pipeline only. Qualitative research moved to client-researcher skill.
  v3.3.0: QA Hardening - Added deterministic quotes, Meta Ads integration placeholder, URL validation
  v3.2.0: Fixed GA4 parsing warnings, added robust error handling
  v3.1.0: Added interactive setup (setup_client.py) and ecosystem links
  v3.0.0: Generic framework with client_config.json dependency
---

# ICP Research Lead (The Architect)

## ⚠️ Scope: Data Pipeline Only

This skill handles **quantitative data processing** — it does NOT conduct qualitative brand research.

| Task | Skill |
|------|-------|
| Product Feed + GA4 + Meta Ads → CSV | ✅ **This skill** |
| Audience segments, customer language, mindstates | → @[strategy/client-researcher] |
| Creative angles (GAM files) | → @[strategy/creative-angle-writer] |

The `{Client}_Mapa_Strategii.csv` output feeds directly into @[strategy/meta_ads_strategist].

---

## 1. Purpose

Transform raw business data into an executable Meta Ads campaign structure by:

1. Merging Product Feed (inventory) with GA4 Analytics (performance)
2. Classifying products using BCG Matrix (Stars, Cash Cows, Hidden Gems)
3. Assigning personas via keyword matching
4. Calculating margin-protected bid caps
5. Injecting Voice of Customer quotes for creative direction

**Output**: `{Client}_Mapa_Strategii.csv` - Campaign blueprint ready for @[strategy/meta_ads_strategist]

---

## 2. Required Data Sources

### 2.1 Input Files (Client Directory)

| File | Pattern | Required | Purpose |
|------|---------|----------|---------|
| **Product Feed** | `*.xml` or `*.txt` | ✅ Yes | Product catalog with prices and URLs |
| **GA4 Export** | `*Segments.csv` | ⚠️ Optional | Landing page performance (Revenue, Transactions) |
| **Client Config** | `client_config.json` | ✅ Yes | Margins, personas, keywords (created via setup_client.py) |
| **Psychology Data** | `harvest_*.json` | ⚠️ Legacy | Customer quotes (PAIN/DREAM) — use @[strategy/client-researcher] to generate these properly |
| **Meta Ads Historical** | `*Ads_Historical.csv` | ⚠️ Optional | Past campaign performance (currently loaded but not fully integrated) |

### 2.2 Product Feed Schema

**Required XML fields**:

```xml
<item>
  <id>12345</id>  <!-- Product SKU -->
  <title>Product Name</title>  <!-- Used for persona matching -->
  <link>https://shop.com/product</link>  <!-- Landing page URL -->
  <price>999.00 PLN</price>  <!-- Gross price -->
</item>
```

### 2.3 GA4 Export Format

**Critical Requirements**:

- Must skip first 7 rows (GA4 metadata)
- Column[0] = Landing Page URL
- Column[3] = Revenue
- Column[4] = Transactions

**Export from**: GA4 > Reports > Engagement > Landing Page (Last 90 days)

### 2.4 Client Config Schema

```json
{
  "url_prefix": "https://shop.com",  // Used to complete relative GA4 URLs
  "margins": {"default": 0.30},  // Default 30% margin
  "vat_rate": 1.23,  // Poland standard
  "frequency_multiplier": 1.0,  // LTV multiplier
  "segments": [
    {
      "id": "gaming",  // Internal ID (used in harvest_gaming.json filename)
      "persona": "Pro Gamer",  // Marketing label
      "keywords": ["gaming", "rgb", "144hz"],  // Product title/URL matching
      "fallbacks": {  // Used if harvest_gaming.json is missing
        "PAIN": ["Generic pain quote"],
        "DREAM": ["Generic benefit quote"]
      }
    }
  ],
  "default_segment": {  // Catch-all for unmatched products
    "id": "general",
    "persona": "General Customer"
  }
}
```

---

## 3. Data Processing Logic

### 3.1 Phase 1: Data Ingestion

**Code Reference**: tcp_analyzer.py lines 140-213

1. **Load Config**: Read `client_config.json`
2. **Parse Feed**: Extract products from XML (lines 22-60)
3. **Load GA4** (if present):
   - Skip 7 header rows
   - Rename columns by index (not name)
   - Filter out "Grand total" and numeric-only rows
   - Apply URL prefix to relative paths
4. **Merge**: LEFT join Feed + GA4 on `feed.link` == `ga4.Landing page`
5. **Load Quotes**: From `harvest_*.json` files, categorize by segment ID

**Error Handling**:

- Missing Feed → CRITICAL ERROR (abort)
- Missing GA4 → WARNING (continue with Revenue=0)
- Missing Harvest → INFO (use fallbacks from config)

### 3.2 Phase 2: Product Classification

**Code Reference**: tcp_analyzer.py lines 224-240

**BCG Matrix Logic**:

```
P80_Revenue = 80th percentile of products with Revenue > 0
P80_Price = 80th percentile of all prices

IF Revenue > P80 AND Price > P80 → GWIAZDA (Star)
ELIF Revenue > P80 AND Price ≤ P80 → DOJNA_KROWA (Cash Cow)
ELIF Revenue ≤ P80 AND Price > P80 → UKRYTY_DIAMENT (Hidden Gem)
ELSE → IGNOROWANY (excluded from output)
```

**Campaign Assignment**:

- GWIAZDA → "Skalowanie (Marża)" campaign
- Others → "Utrzymanie (Volume)" campaign

### 3.3 Phase 3: Hierarchy Generation

**Code Reference**: tcp_analyzer.py lines 242-308

#### 3.3.1 Ad Set Naming

Format: `{Category} - {Price Bucket}`

**Price Buckets**:

```
< 500 PLN → "0-500 PLN"
500-1000 → "500-1000 PLN"
1000-2000 → "1000-2000 PLN"
2000-4000 → "2000-4000 PLN"
4000+ → "4000+ PLN"
```

**Purpose**: Group similar-priced products for bid strategy optimization

#### 3.3.2 Ad Naming

Format: `{Category}_{Persona}_{ProductID}`

Example: `GWIAZDA_ProGamer_SKU12345`

#### 3.3.3 Persona Assignment (lines 258-275)

**Algorithm**:

1. Combine `product.title + product.link` (lowercase)
2. Loop through `config.segments[]`
3. If ANY keyword matches → assign that segment's persona
4. If no match → use `default_segment.persona`

**Example**:

```
Product: "Monitor Gaming iiyama G-Master 144Hz"
Keywords: ["gaming", "144hz"]
Match: TRUE → Persona = "Pro Gamer"
```

#### 3.3.4 Quote Injection (lines 277-279)

**Current Implementation**:

- Selects **random** quote from matching segment's PAIN/DREAM pool
- **Known Issue**: Non-deterministic (each run produces different quotes)
- **Fix Status**: P0 bug, seed parameter needed

#### 3.3.5 Financial Calculations (lines 248-256)

```python
net_price = gross_price / vat_rate  # Remove VAT
ltv = net_price * frequency_multiplier  # Lifetime Value
break_even_cpa = ltv * margin_percentage  # Maximum profitable CPA
cost_cap = break_even_cpa * 0.7  # Conservative bidding (30% safety margin)
target_roas = 1 / (margin * frequency)  # Required ROAS to break even
```

---

## 4. Output Schema

### 4.1 Mapa_Strategii.csv Columns

| Column | Source | Transformation |
|--------|--------|----------------|
| Kampania | Derived | "Skalowanie (Marża)" if GWIAZDA else "Utrzymanie (Volume)" |
| Zestaw Reklam (AdSet) | Derived | f"{Category} - {Price_Bucket}" |
| Nazwa Reklamy | Derived | f"{Category}_{Persona}_{ProductID}" |
| Link URL | Product Feed | Direct copy from `feed.link` |
| Persona | Config + Matching | Keyword-based assignment |
| Cytat (VoC) | Harvest JSON | Random from segment's PAIN pool |
| Obietnica (Dream) | Harvest JSON | Random from segment's DREAM pool |
| Cena Produktu (PLN) | Product Feed | Direct copy from `feed.price` |
| Bid Cap (PLN) | Calculated | `(price / VAT) * freq * margin` |
| Koszt Max (Cost Cap) | Calculated | `Bid Cap * 0.7` |
| Cel ROAS | Calculated | `1 / (margin * freq)` |
| Status Historyczny | Meta Ads CSV | **Currently**: Always "Brak Danych" (P0 fix needed) |

---

## 5. Quality Assurance Procedures

### 5.1 Pre-Flight Validation

Before running `tcp_analyzer.py`, verify:

```powershell
# 1. Client directory exists
Test-Path "C:\...\Clients\{ClientName}"

# 2. Required files present
Get-ChildItem "C:\...\Clients\{ClientName}" | Where-Object {$_.Name -like "*.xml" -or $_.Name -like "client_config.json"}

# 3. Config JSON is valid
Get-Content "client_config.json" | ConvertFrom-Json
```

### 5.2 Post-Execution Validation

After script completes:

| Check ID | Test | Expected | Action if Failed |
|----------|------|----------|------------------|
| QA-001 | File exists | TRUE | Check for script errors |
| QA-002 | Row count > 0 | TRUE | Check BCG classification (all products may be IGNOROWANY) |
| QA-003 | GWIAZDA products exist | At least 1 | Adjust P80 threshold or add Revenue data |
| QA-004 | No empty personas | 0 blank cells | Check keyword matching config |
| QA-005 | Bid Cap < Product Price | All rows | Check margin config (should be < 1.0) |
| QA-006 | URLs return 200 | Sample 5 random | Check URL prefix config |

### 5.3 Reproducibility Test

**Critical**: Run twice and verify identical output

```powershell
python tcp_analyzer.py {Client}
Copy-Item "{Client}_Mapa_Strategii.csv" "Run1.csv"

python tcp_analyzer.py {Client}
fc Run1.csv "{Client}_Mapa_Strategii.csv"
```

**Expected**: Files should be IDENTICAL
**If different**: Quote randomization bug (P0 fix required)

---

## 6. Known Issues & Roadmap

### 6.1 P0 - Critical (Breaks Reliability)

**Issue #1**: Non-Deterministic Quote Selection

- **Impact**: Each run produces different creative briefs
- **Fix**: Add `random.seed(hash(client_name))` at line 140
- **Status**: TODO

**Issue #2**: Meta Ads Historical Data Not Integrated

- **Impact**: Cannot identify proven performers vs new products
- **Code**: Lines 215-222 load but don't use `df_ads`
- **Fix**: Merge with strategy_rows by URL matching
- **Status**: TODO

**Issue #3**: No URL Validation

- **Impact**: May generate campaigns for 404 pages
- **Fix**: Add HTTP HEAD request validation
- **Status**: TODO

### 6.2 P1 - High (Data Quality)

- Landing Page content validation (Scent Match check)
- Duplicate Ad Name detection
- Quote uniqueness enforcement

### 6.3 P2 - Medium (UX)

- Progress logging for large feeds
- Dry-run mode (preview without writing)
- Config schema validator

---

## 7. Usage Instructions

### 7.1 Interactive Setup (First Time)

```powershell
cd skills/strategy/icp-research-lead/scripts
python setup_client.py {ClientName}
```

Follow prompts to define:

- URL prefix
- Margin percentages
- Personas and keywords
- Fallback quotes

### 7.2 Analysis Execution

```powershell
python tcp_analyzer.py {ClientName}
```

**Expected Output**:

```
Analyzing Client Directory: C:\...\Clients\{ClientName}
Wygenerowano Mapę Strategii: {ClientName}_Mapa_Strategii.csv
```

### 7.3 Handover to Next Stage

```powershell
# Option A: Generate creative briefs
cd ../../meta_ads_strategist/scripts
python brief_generator.py {ClientName}

# Option B: Manual upload to Meta Ads Manager
# Open {ClientName}_Mapa_Strategii.csv in Excel
# Review GWIAZDA products
# Create campaigns manually
```

---

## 8. Integration Points

### 8.1 Upstream Dependencies

**Before this skill**:

1. Client must provide Product Feed export
2. GA4 data must be manually exported (no API yet)
3. Customer quotes must be harvested manually

### 8.2 Downstream Consumers

**After this skill**:

- **Primary**: @[strategy/meta_ads_strategist] ingests Mapa_Strategii.csv
- **Secondary**: Manual review by marketing team

---

## 9. Troubleshooting

### Common Error: "CRITICAL: No product feed found"

**Diagnosis**:

```powershell
Get-ChildItem "C:\...\Clients\{ClientName}" | Where-Object {$_.Extension -eq ".xml" -or $_.Extension -eq ".txt"}
```

**Fix**: Ensure file has correct extension (not .xml.txt)

### Common Error: "ParserWarning: Skipping line X"

**Cause**: GA4 CSV has inconsistent column count
**Impact**: Some landing pages excluded
**Fix**: Manually inspect line X and remove malformed row

### Common Issue: All Products Assigned "Klient Ogólny"

**Cause**: Keywords don't match product titles
**Diagnosis**:

```powershell
Select-String -Path "Feed.xml" -Pattern "gaming"
```

**Fix**: Update `client_config.json` keywords to match actual product catalog

---

## 10. Roadmap / Feature Requests

### 🔜 `inferred_segment` column (Priority: HIGH)

**Problem:** `meta_ads_strategist` cannot automatically match GAM angle files to products without knowing which creative segment each product belongs to.

**Proposed solution:** Add URL pattern matching to output an `inferred_segment` column in Mapa_Strategii.csv.

Example rules (configured per client in `client_config.json`):

```json
"segment_url_patterns": [
  {"pattern": "/gaming/", "segment": "Competitive Shooter"},
  {"pattern": "/office/", "segment": "WFH Power User"},
  {"pattern": "/32-inch/", "segment": "Immersive Gamer"},
  {"pattern": "/ultrawide/", "segment": "WFH Power User"}
]
```

This would allow `meta_ads_strategist` to automatically select the correct GAM angle file for each P1/P3 product without manual matching.

---

## 11. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| 3.4.0 | 2026-02-18 | Scope clarified — data pipeline only. Psychology Data marked legacy. |
| 3.3.0 | 2026-02-04 | QA hardening based on code audit |
| 3.2.0 | 2026-02-04 | Fixed GA4 parser warnings |
| 3.1.0 | 2026-02-04 | Interactive setup + ecosystem links |
| 3.0.0 | 2026-01-XX | Generic client-agnostic framework |
