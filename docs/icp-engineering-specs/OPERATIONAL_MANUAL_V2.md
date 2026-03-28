# Operational Manual: ICP Framework v3.2

**Document Type**: Standard Operating Procedure (SOP)
**Target Audience**: Marketing Operations Team
**Prerequisite Knowledge**: Basic command line, CSV/JSON file formats

---

## 1. Pre-Execution Checklist

Before running ANY script, verify:

| Item | How to Check | Required? |
------|--------------|-----------|
| Python 3.8+ installed | `python --version` | ✅ Yes |
| Pandas library | `pip list \| findstr pandas` | ✅ Yes |
| Client folder exists | Navigate to `C:\...\ICP Research\Clients\{ClientName}` | ✅ Yes |
| Product Feed present | Look for `*.xml` or `*.txt` file | ✅ Yes |
| GA4 Export present | Look for `*Segments.csv` file | ⚠️ Optional |
| Harvest files present | Look for `harvest_*.json` files | ⚠️ Optional |

**WARNING**: If GA4 and Harvest files are missing, the system will still run but use fallback data (lower quality).

---

## 2. Phase 1: Client Configuration

### 2.1 Command

```powershell
cd C:\Users\Paweł\Documents\GitHub\skill-creator\skills\strategy\icp-research-lead\scripts
python setup_client.py {ClientName}
```

### 2.2 Interactive Prompts

The script will ask you for:

1. **URL Prefix** (e.g., `https://sklep.pl`)
   - Used to match GA4 URLs with Feed URLs
   - Leave blank if Feed already has full URLs

2. **Default Margin** (e.g., `0.30` = 30%)
   - Used to calculate Bid Caps
   - Higher margin = higher bids allowed

3. **VAT Rate** (e.g., `1.23` for Poland)
   - Converts gross prices to net for calculations

4. **Segments Definition**:
   - **Segment ID**: Internal name (e.g., `gaming`, `office`)
   - **Persona Label**: Marketing name (e.g., `"Gracz Pro"`, `"Biuro Premium"`)
   - **Keywords**: Comma-separated list for product matching
   - **Fallback Quotes**: PAIN and DREAM examples (if harvest files are missing)

### 2.3 Output

- File: `Clients/{ClientName}/client_config.json`
- Validation: Open the file and verify JSON is valid

### 2.4 Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'json'` | Python installation corrupted | Reinstall Python |
| `Permission denied` | Folder is read-only | Run as Administrator |
| Invalid JSON syntax | Manual edits broke the file | Regenerate with script |

---

## 3. Phase 2: Data Collection

### 3.1 Required Files

Upload these to `Clients/{ClientName}/`:

#### A. Product Feed (`*.xml` or `Feed.txt`)

**Source**: E-commerce platform export (WooCommerce, Shopify, etc.)
**Required fields**:

```xml
<item>
  <id>12345</id>
  <title>Product Name</title>
  <link>https://shop.com/product-url</link>
  <price>999.00 PLN</price>
</item>
```

**Validation**:

```powershell
# Check if XML is valid
[xml](Get-Content "path\to\feed.xml")
```

#### B. GA4 Export (`{Client}_Segments.csv`)

**Source**: Google Analytics 4 > Reports > Engagement > Landing Page
**Export Settings**:

- Date Range: Last 90 days
- Dimension: Landing Page
- Metrics: Revenue, Transactions
- Segment: (All Users)

**CRITICAL**: The file MUST have exactly 7 header rows before the data starts.

**Validation**:

```powershell
# Check first 10 lines
Get-Content "path\to\Segments.csv" | Select-Object -First 10
```

Expected format:

```
# Site name (line 1)
# Date range (line 2)
...
# Table headers (line 7)
/landing-page-url,... (line 8)
```

#### C. Psychology Data (`harvest_*.json`) [OPTIONAL]

**Source**: Manual customer research or review scraping
**Format**:

```json
{
  "deep_harvest_insights": {
    "google_reviews": [
      {
        "raw_quote": "Actual customer quote here",
        "basket": "PAIN"  // or "DREAM"
      }
    ]
  }
}
```

**Naming Convention**: `harvest_{segment_id}.json` (e.g., `harvest_gaming.json`)

---

## 4. Phase 3: Strategy Map Generation

### 4.1 Command

```powershell
cd C:\Users\Paweł\Documents\GitHub\skill-creator\skills\strategy\icp-research-lead\scripts
python tcp_analyzer.py {ClientName}
```

### 4.2 Expected Output

```
Analyzing Client Directory: C:\...\Clients\{ClientName}
Wygenerowano Mapę Strategii: {ClientName}_Mapa_Strategii.csv
```

### 4.3 Validation Checklist

After the script completes, verify:

| Check | Command | Expected Result |
|-------|---------|----------------|
| File exists | `Test-Path "{ClientName}_Mapa_Strategii.csv"` | True |
| File not empty | `(Get-Content "{ClientName}_Mapa_Strategii.csv").Count` | > 1 |
| Has GWIAZDA products | `Select-String "GWIAZDA" "{ClientName}_Mapa_Strategii.csv"` | At least 1 match |
| No blank personas | `Select-String ",," "{ClientName}_Mapa_Strategii.csv"` | 0 matches |

### 4.4 Common Errors

#### Error: "CRITICAL: No product feed found"

**Cause**: No `*.xml` or `*.txt` file in client directory
**Fix**:

1. Verify file exists in correct directory
2. Check file extension (must be exactly `.xml` or `.txt`)

#### Error: "WARNING: No GA4 CSV found"

**Impact**: Revenue and Transaction columns will be 0
**Decision**:

- If acceptable (new client, no historical data) → Continue
- If NOT acceptable → Export GA4 data and re-run

#### Error: "ParserWarning: Skipping line X"

**Cause**: GA4 CSV has inconsistent column count
**Impact**: Some landing pages may be excluded
**Fix**: Manually inspect GA4 CSV line X and remove/fix malformed rows

---

## 5. Phase 4: Manual Quality Assurance

### 5.1 Data Inspection

Open `{ClientName}_Mapa_Strategii.csv` in Excel and check:

1. **Persona Distribution**:
   - Are all major product categories covered?
   - Any "Klient Ogólny" (default) that should be segmented?

2. **Price Buckets**:
   - Do groupings make sense?
   - Example: If you have "GWIAZDA - 500-1000 PLN", are those actually similar products?

3. **Quotes Relevance**:
   - Read 5 random "Cytat (VoC)" entries
   - Do they match the product/persona?
   - If all quotes are identical → Harvest files are missing

4. **URL Validation**:
   - Copy 3 random "Link URL" entries
   - Paste into browser
   - All should return valid product pages (200 status)

### 5.2 Financial Sanity Checks

| Check | Formula | Red Flag |
|-------|---------|----------|
| Bid Cap < Price | `Bid Cap / Cena Produktu` should be < 1.0 | If > 1.0, margin config is wrong |
| Bid Cap consistency | All products with same margin should have same % ratio | Inconsistent ratios = bug |
| Negative values | Any column | Should never occur |

### 5.3 Reproducibility Test

```powershell
# Run twice and compare outputs
python tcp_analyzer.py {ClientName}
Copy-Item "{ClientName}_Mapa_Strategii.csv" "{ClientName}_Run1.csv"

python tcp_analyzer.py {ClientName}
Copy-Item "{ClientName}_Mapa_Strategii.csv" "{ClientName}_Run2.csv"

# Compare files
fc "{ClientName}_Run1.csv" "{ClientName}_Run2.csv"
```

**Expected**: Files should be IDENTICAL
**If different**: Random quote selection is active → P0 bug (see Technical Spec section 9)

---

## 6. Phase 5: Creative Briefing

### 6.1 Command

```powershell
cd C:\Users\Paweł\Documents\GitHub\skill-creator\skills\strategy\meta_ads_strategist\scripts
python brief_generator.py {ClientName}
```

### 6.2 Output

- File: `{ClientName}_Briefy_Produkcyjne.md`
- Contains: One brief per GWIAZDA product

### 6.3 Brief Quality Review

For each generated brief, verify:

1. **Hook Relevance**: Does the VoC quote make sense for the product?
2. **Persona Match**: Is the target persona logical?
3. **Bid Cap Awareness**: Is the technical note present?

### 6.4 Brief Customization

The generated briefs are TEMPLATES. Before sending to creative team:

1. **Add Specific Visual Directions**:
   - Replace "specific product detail" with actual feature (e.g., "USB-C charging port")
2. **Clarify Angle**:
   - If the quote is generic, add context about the product category
3. **Prioritize**:
   - Mark which briefs should be executed first (highest Bid Cap = highest priority)

---

## 7. Error Recovery Procedures

### 7.1 Scenario: Script Crashes Mid-Execution

**Symptoms**: Terminal shows error, no output file
**Diagnosis**:

```powershell
# Re-run with full error output
python tcp_analyzer.py {ClientName} 2>&1 | Out-File error_log.txt
notepad error_log.txt
```

**Common Causes**:

| Error Message | Root Cause | Fix |
|---------------|------------|-----|
| `KeyError: 'Landing page'` | GA4 CSV column structure changed | Check line 179-182 in tcp_analyzer.py |
| `xml.etree: ParseError` | Feed XML is malformed | Validate XML with online tool |
| `FileNotFoundError` | Client directory path is wrong | Verify in line 142-157 |

### 7.2 Scenario: Empty Output (0 Products)

**Diagnosis**:

1. Check if Feed file has products:

   ```powershell
   [xml]$feed = Get-Content "Feed.xml"
   $feed.rss.channel.item.Count
   ```

2. Check Revenue threshold:
   - If ALL products have Revenue = 0, the P80 calculation may exclude everything
   - **Temporary Fix**: Manually edit one product's revenue to > 0 and re-run

### 7.3 Scenario: All Products Assigned Same Persona

**Diagnosis**: Keyword matching not working
**Check**:

1. Open `client_config.json`
2. Verify `segments[].keywords` array is not empty
3. Verify keywords match actual product titles/URLs

**Test**:

```powershell
# Search for keyword in feed
Select-String -Path "Feed.xml" -Pattern "gaming" -CaseSensitive
```

If no matches → Keywords are wrong for this product catalog

---

## 8. Advanced: Integrating Meta Ads Historical Data

**Current Status**: ⚠️ NOT IMPLEMENTED (see Technical Spec section 4.1)

**Manual Workaround**:

1. Export Meta Ads data: Ads Manager > Reports > Download CSV
2. Save as `{Client}_Ads_Historical.csv` in client folder
3. Script will LOAD it but NOT USE it
4. **Action Required**: Modify `tcp_analyzer.py` lines 307-308 to merge `df_ads` with `strategy_rows`

**Expected Enhancement** (future):

```python
# Pseudo-code for integration
if not df_ads.empty:
    for row in strategy_rows:
        historical_match = df_ads[df_ads['Landing Page'] == row['Link URL']]
        if not historical_match.empty:
            row['Status Historyczny'] = f"CTR: {historical_match['CTR']}, ROAS: {historical_match['ROAS']}"
```

---

## 9. Troubleshooting Decision Tree

```
Is the script outputting a file?
├── NO → Check Section 7.1 (Script Crashes)
└── YES
    ├── Is the file empty (0 products)?
    │   ├── YES → Check Section 7.2 (Empty Output)
    │   └── NO
    │       ├── Are all personas "Klient Ogólny"?
    │       │   ├── YES → Check Section 7.3 (Keyword Matching)
    │       │   └── NO
    │       │       ├── Are quotes repetitive/generic?
    │       │       │   ├── YES → Missing harvest files → See Section 3.1.C
    │       │       │   └── NO
    │       │       │       └── ✅ Output is valid → Proceed to Phase 5
```

---

## 10. Appendix: File Location Reference

| File Type | Full Path | Created By |
|-----------|-----------|------------|
| Client Config | `C:\...\Clients\{Client}\client_config.json` | setup_client.py |
| Product Feed | `C:\...\Clients\{Client}\Feed.xml` | Manual upload |
| GA4 Export | `C:\...\Clients\{Client}\{Client}_Segments.csv` | Manual upload |
| Harvest Data | `C:\...\Clients\{Client}\harvest_*.json` | Manual upload |
| Strategy Map | `C:\...\Clients\{Client}\{Client}_Mapa_Strategii.csv` | tcp_analyzer.py |
| Production Briefs | `C:\...\Clients\{Client}\{Client}_Briefy_Produkcyjne.md` | brief_generator.py |
| Error Logs | `C:\...\scripts\error_log.txt` | Manual redirect (Section 7.1) |

---

## 11. Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.2 | 2026-02-04 | Added reproducibility test, error recovery procedures |
| 3.1 | 2026-02-04 | Interactive setup, persona keyword matching |
| 3.0 | 2026-01-XX | Generic framework (client-agnostic) |
