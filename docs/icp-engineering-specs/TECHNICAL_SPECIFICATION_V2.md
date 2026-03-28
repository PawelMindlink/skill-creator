# Technical Specification: ICP Research Framework v3.2

**Document Type**: Engineering Specification
**Author**: AI Research Team
**Last Updated**: 2026-02-04
**Status**: DRAFT FOR REVIEW

---

## 1. System Overview

### 1.1 Purpose

Automate the creation of Meta Ads campaign structures by combining three data sources:

1. **Product Feed** (XML/CSV) - Inventory and pricing
2. **GA4 Analytics** (CSV) - Landing page performance
3. **Customer Psychology** (JSON) - Voice of Customer quotes

### 1.2 Core Output

`{Client}_Mapa_Strategii.csv` - A structured campaign blueprint containing:

- Campaign hierarchy (Campaign → Ad Set → Ad)
- Persona assignments
- Bid caps calculated from margins
- VoC-based creative angles

---

## 2. Data Sources & Schema

### 2.1 Input File Requirements

| File Type | Pattern | Required Fields | Purpose |
|-----------|---------|----------------|---------|
| Product Feed | `*.xml` or `*.txt` | `id`, `title`, `link`, `price` | Product catalog |
| GA4 Export | `*Segments.csv` | Column[0]=URL, Column[3]=Revenue, Column[4]=Transactions | Landing page performance |
| Psychology Data | `harvest_*.json` | `deep_harvest_insights.{source}[].raw_quote`, `.basket` | Customer quotes |
| Client Config | `client_config.json` | `url_prefix`, `margins`, `segments` | Business rules |
| **[MISSING]** Meta Ads Historical | `*Ads_Historical.csv` | **NOT CURRENTLY INTEGRATED** | Past campaign performance |

### 2.2 Data Processing Pipeline

```
┌─────────────────┐
│  Product Feed   │──┐
│   (XML/TXT)     │  │
└─────────────────┘  │
                     │
┌─────────────────┐  │    ┌──────────────────┐
│   GA4 Export    │──┼───▶│  tcp_analyzer.py │
│     (CSV)       │  │    └──────────────────┘
└─────────────────┘  │            │
                     │            │
┌─────────────────┐  │            ▼
│ Harvest Quotes  │──┘    ┌──────────────────┐
│     (JSON)      │       │ Mapa_Strategii   │
└─────────────────┘       │     (CSV)        │
                          └──────────────────┘
┌─────────────────┐                │
│ client_config   │────────────────┘
│     (JSON)      │
└─────────────────┘
```

---

## 3. Core Logic: tcp_analyzer.py

### 3.1 Phase 1: Data Ingestion

#### 3.1.1 Product Feed Parsing (Lines 22-60)

- **Input**: First `*.xml` or `*.txt` file found in client directory
- **Parser**: XML ElementTree with fallback for namespaced tags
- **Output**: DataFrame with columns: `id`, `title`, `link`, `price`, `image_link`, `description`
- **Error Handling**: Returns empty DataFrame on parse failure (line 59)
- **Known Issue**: Price parsing assumes format "XXXX PLN" - will fail on other formats

#### 3.1.2 GA4 Integration (Lines 172-213)

- **Input**: First `*Segments.csv` file
- **Processing**:
  1. Skip first 7 rows (GA4 metadata headers)
  2. Rename columns by index (not name) to avoid Polish/English mismatches
  3. Filter out noise: "Grand total" rows, pure numeric rows
  4. Apply URL prefix from config if URL starts with `/`
  5. Join with Feed on `feed.link_clean` == `ga4.Landing page`
- **Merge Type**: LEFT join (keeps all products even without GA4 data)
- **Fallback**: If GA4 missing, sets Revenue/Transactions to 0

#### 3.1.3 Psychographic Data Loading (Lines 62-131)

- **Input**: All `harvest_*.json` and `RAW_HARVEST_DATA_*.json` files
- **Processing**:
  1. Extract `deep_harvest_insights.{source}[].raw_quote` and `.basket`
  2. Categorize by segment ID (via filename matching)
  3. Store in structure: `{segment_id: {PAIN: [...], DREAM: [...]}}`
- **Assignment Logic**:
  - Check filename for segment ID (e.g., `harvest_gaming.json` → `gaming` segment)
  - Default to `config.default_segment.id` if no match
- **Fallback System**: If no real quotes found, uses `segments[].fallbacks` from config

### 3.2 Phase 2: Product Classification (Lines 224-240)

#### 3.2.1 BCG Matrix Logic

Products are classified using Revenue and Price percentiles:

| Category | Condition | Marketing Strategy |
|----------|-----------|-------------------|
| **GWIAZDA** (Star) | Revenue > P80 AND Price > P80 | Scale aggressively (Skalowanie) |
| **DOJNA_KROWA** (Cash Cow) | Revenue > P80 AND Price ≤ P80 | Maintain volume (Utrzymanie) |
| **UKRYTY_DIAMENT** (Hidden Gem) | Revenue ≤ P80 AND Price > P80 | Test creative angles |
| **IGNOROWANY** | Revenue ≤ P80 AND Price ≤ P80 | **Excluded from output** |

**Critical Note**: P80 is calculated ONLY from products with Revenue > 0 (line 228)

### 3.3 Phase 3: Hierarchy Generation (Lines 242-308)

#### 3.3.1 Campaign Level

```
Campaign Name = "Skalowanie (Marża)" if Category == GWIAZDA else "Utrzymanie (Volume)"
```

#### 3.3.2 Ad Set Level (Lines 284-293  

**Naming Formula**: `{Category} - {Price Bucket}`

Price Bucketing Logic:

```python
if price < 500:  → "0-500 PLN"
elif price < 1000: → "500-1000 PLN"
elif price < 2000: → "1000-2000 PLN"
elif price < 4000: → "2000-4000 PLN"
else: → "4000+ PLN"
```

**Purpose**: Group similar-priced products for bid optimization

#### 3.3.3 Ad Level Format (Line 298)

```
Ad Name = "{Category}_{Persona}_{ProductID}"
```

#### 3.3.4 Persona Assignment (Lines 258-275)

**Algorithm**:

1. Combine `product.title + product.link` into searchable text
2. Loop through `config.segments[]`
3. If ANY keyword in `segment.keywords[]` matches → assign `segment.persona`
4. If no match → use `config.default_segment.persona`

**Critical Gap**: No validation that the Landing Page content actually matches the assigned persona

#### 3.3.5 Quote Injection (Lines 277-279)

- Random selection from the assigned segment's quote pool
- **Separate** quotes for PAIN and DREAM
- **No uniqueness check** - same quote can appear multiple times

#### 3.3.6 Financial Calculations (Lines 248-256)

```python
net_price = gross_price / vat_rate
ltv = net_price * frequency_multiplier
break_even_cpa = ltv * margin_percentage
cost_cap = break_even_cpa * 0.7
target_roas = 1 / (margin * frequency)
```

---

## 4. CRITICAL GAPS IDENTIFIED

### 4.1 Meta Ads Historical Data (UNUSED)

**Code Location**: Lines 215-222
**Status**: ⚠️ **LOADED BUT NOT INTEGRATED**

```python
df_ads = pd.DataFrame()
if ads_files:
    df_ads = pd.read_csv(ads_files[0])
    # ... but df_ads is NEVER USED in strategy_rows generation
```

**Impact**: Cannot validate if a product has historical performance data

### 4.2 Landing Page Validation (MISSING)

**Problem**: Persona is assigned by product title keywords, but:

- No check if the Landing Page URL actually exists
- No validation that LP content matches the assigned persona
- No "Scent Match" audit (Ad promise vs LP content)

### 4.3 Error Handling (INCOMPLETE)

Currently fails silently when:

- Product Feed is invalid XML
- GA4 CSV has unexpected column count (ParserWarning partially fixed)
- No quotes found for a segment (returns empty string)

### 4.4 Reproducibility (UNPREDICTABLE)

**Quote Selection**: Uses `random.choice()` (line 137) without seed

- **Impact**: Running the same client twice produces different quotes

---

## 5. brief_generator.py Analysis

### 5.1 Input Processing

- **Source**: `{Client}_Mapa_Strategii.csv`
- **Filter**: Only rows where `Zestaw Reklam (AdSet)` contains "GWIAZDA"
- **Output**: Markdown file with creative briefs

### 5.2 Brief Structure

For each GWIAZDA product:

1. **Core Angle**: VoC Quote (Pain) + Promise (Dream) + Persona
2. **Copywriter Instructions**: Generic framework reference ("Hyperdopamine")
3. **Designer Instructions**: Generic style reference ("Raw Native")

### 5.3 CRITICAL GAP: No Creative Angle Differentiation

**Problem**: All briefs use the same generic instructions

- No specific visual suggestions based on product category
- No angle variation (all use "First Principles Discovery")
- Missing: Connection between VoC quote and actual product features

---

## 6. Quality Assurance Procedures

### 6.1 Pre-Flight Validation Checklist

| Check ID | Validation | Failure Mode | Fix |
|----------|------------|--------------|-----|
| `QA-001` | Product Feed XML validity | Script crashes | Add XML validation before parse |
| `QA-002` | GA4 CSV column count == expected | ParserWarning | ✅ Fixed with `on_bad_lines='skip'` |
| `QA-003` | At least 1 product with Revenue > 0 | P80 calculation fails | Add error message + use Feed-only mode |
| `QA-004` | All segments have ≥ 1 quote | Empty VoC fields | ✅ Has fallback system |
| `QA-005` | Persona keywords exist in Feed | No personas assigned | Add warning for unmatched products |
| `QA-006` | URL prefix matches Feed domain | GA4 merge fails | Add domain validator |
| `QA-007` | Mapa_Strategii has > 0 rows | No output generated | Add row count assertion |

### 6.2 Post-Execution Validation

**Required Tests** (Currently Missing):

1. Open 3 random Landing Page URLs → verify 200 status
2. Check Mapa_Strategii for duplicate Ad Names
3. Validate Bid Cap < Product Price (should never bid more than item value)
4. Confirm GWIAZDA products exist (if 0, process failed)

---

## 7. Process Flow (Actual vs Documented)

### 7.1 ACTUAL Implementation

```
1. setup_client.py → client_config.json
2. USER manually uploads: Feed.xml, GA4_Segments.csv, harvest_*.json
3. tcp_analyzer.py → {Client}_Mapa_Strategii.csv
4. brief_generator.py → {Client}_Briefy_Produkcyjne.md
5. USER manually creates ads in Meta Ads Manager
```

### 7.2 MISSING Steps (Should Exist)

- Automated Feed download from client's store
- GA4 API integration (currently manual CSV export)
- Meta Ads API integration for historical data
- Landing Page scraper for Scent Match validation
- Automated creative generation (currently manual from briefs)

---

## 8. Data Lineage: Where Does Each Field Come From?

| Output Field | Source | Transformation |
|--------------|--------|----------------|
| Kampania | Derived | If Category == GWIAZDA → "Skalowanie" |
| Zestaw Reklam (AdSet) | Derived | f"{Category} - {Price_Bucket}" |
| Nazwa Reklamy | Derived | f"{Category}_{Persona}_{ProductID}" |
| Link URL | **Product Feed** | `feed.link` (no transformation) |
| Persona | **client_config.json** | Keyword matching algorithm |
| Cytat (VoC) | **harvest_*.json** | Random from matching segment's PAIN pool |
| Obietnica (Dream) | **harvest_*.json** | Random from matching segment's DREAM pool |
| Cena Produktu | **Product Feed** | `feed.price` |
| Bid Cap | **Calculated** | `(price / VAT) * freq * margin` |
| Koszt Max | **Calculated** | `Bid Cap * 0.7` |
| Cel ROAS | **Calculated** | `1 / (margin * freq)` |
| Status Historyczny | **HARDCODED** | Always "Brak Danych" ⚠️ |

**Key Finding**: The "Status Historyczny" field is a placeholder - Meta Ads Historical data is never actually used.

---

## 9. Recommended Fixes (Priority Order)

### P0 - Critical (Breaks Process)

1. **Integrate Meta Ads Historical Data**: Currently loaded but not used (Line 215-322)
2. **Add URL Validation**: Check if Landing Pages return 200 status
3. **Reproducible Quote Selection**: Add seed parameter to random.choice()

### P1 - High (Data Quality)

4. **Scent Match Validator**: Crawl LP and check for persona keywords
2. **Duplicate Ad Name Detection**: Prevent conflicts in Ads Manager
3. **Bid Cap Sanity Check**: Alert if Bid > Product Price

### P2 - Medium (UX)

7. **Progress Logging**: Show which file is being processed
2. **Dry-Run Mode**: Preview output without writing files
3. **Config Validator**: Check client_config.json schema before running

---

## 10. Test Case: Iiyama Client

### 10.1 Expected Files

```
Clients/iiyama/
├── Feed.xml ✅
├── iiyama_Segments.csv ✅  
├── harvest_b2b.json ❓ (not found)
├── harvest_gaming.json ❓ (not found)
├── client_config.json ✅
└── iiyama_Mapa_Strategii.csv ✅ (output)
```

### 10.2 Validation Results

- **Total Products in Feed**: ?
- **Products with GA4 Data**: ?
- **GWIAZDA Products**: 8 (from Briefy_Produkcyjne.md)
- **Unique Personas**: "B2B / Edukacja" (only 1 observed)
- **Quote Diversity**: All quotes are "Utrudniona współpraca zespołu" or "Problemy z podłączeniem laptopa"

**Concern**: Low persona diversity suggests keyword matching may not be working correctly.

---

## 11. Summary

This system is **functional but incomplete**:

- ✅ Core data merge (Feed + GA4) works
- ✅ Price bucketing logic is sound
- ✅ Financial calculations are correct
- ❌ Meta Ads historical data is loaded but ignored
- ❌ No landing page validation
- ❌ No creative angle differentiation in briefs
- ❌ Missing automated QA checks

**Engineering Grade**: C+ (Works, but needs significant hardening for production use)
