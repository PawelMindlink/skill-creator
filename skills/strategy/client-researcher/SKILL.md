---
name: client-researcher
description: Generates the 5 qualitative research files for a new client (audience.md, mindstates.md, competitors.md, market.md, product analysis.md). Output feeds into creative-angle-writer.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. Based on reverse-engineering of Iiyama research files (Feb 2026).
---

# Client Researcher

## Purpose

Generate the 5 qualitative research documents that form the foundation of all creative work for a client. These documents are used by `creative-angle-writer` to generate ad angles, and by `meta_ads_copywriter` to write copy.

**Output location:** `Meta Ads Analysis Production Upload/_archive/ad-creator/Clients/{ClientName}/`

---

## ⚠️ This Skill vs icp-research-lead

| This Skill | icp-research-lead |
|-----------|-------------------|
| Qualitative research (who the customer is, what they say) | Quantitative pipeline (which products, what bid cap) |
| Input: web research, reviews, forums, product pages | Input: XML feed, GA4 CSV, Meta Ads CSV |
| Output: 5 markdown research files | Output: Mapa_Strategii.csv |
| Run first (or in parallel) | Run after data is available |

---

## The 5 Research Files

### File 1: `audience.md`

**What it contains:**

- 3–6 audience segments (name, age, income, gaming context, budget)
- For each segment: Goals, Pain Points, Failed Solutions, Buying Journey stages
- Customer Language section: verbatim quotes from real reviews/forums (Polish)
- Research sources used

**How to research:**

1. Search Polish review sites: Benchmark.pl, morele.net, Ceneo.pl, Elektroda.pl, dobreprogramy.pl
2. Search Polish gaming forums and Discord communities
3. Use Perplexity for: `"[product category] opinie forum polska" site:elektroda.pl OR site:dobreprogramy.pl`
4. Collect verbatim quotes — do NOT paraphrase. Real language is the asset.

**Schema:** See `references/research_file_schemas.md#audience`

---

### File 2: `mindstates.md`

**What it contains (JSON format):**

- `mindstate_primary` — the dominant psychological state at purchase
- `mindstate_backup` — secondary state
- `goals.functional` — what they want the product to do
- `goals.higher_order` — the identity/status goal behind the purchase
- `heuristics` — cognitive shortcuts that drive decisions (Price-Quality Cue, Social Proof, Guarantee/Commitment, Loss Aversion)
- `content_tactics` — what type of creative works for this mindstate
- `test_plan` — which angles to test first

**Key mindstates for Polish e-commerce buyers:**

- `Cautious Competence` — wants to make the objectively best decision; fears being wrong
- `Cautious Security` — fears risk (dead pixels, wrong purchase, no returns)
- `Prevention` — motivated by removing disadvantage, not gaining advantage
- `Promotion` — motivated by aspiration and identity upgrade

**Schema:** See `references/research_file_schemas.md#mindstates`

---

### File 3: `competitors.md`

**What it contains:**

- Summary of competitive landscape (who are the main players, what do they own)
- Competitor table: Name | Key Models | Price Range | Strengths | Weaknesses | Positioning
- Positioning gaps: what no competitor owns that the client could claim
- Specific competitor weaknesses to exploit (e.g., OLED burn-in, no dead pixel guarantee)

**How to research:**

1. Check x-kom.pl, morele.net, mediaexpert.pl for category rankings
2. Check Ceneo.pl for price comparison and review counts
3. Read competitor product pages for their claimed differentiators
4. Search for competitor complaints on forums: `"[competitor] problem opinia"`

**Schema:** See `references/research_file_schemas.md#competitors`

---

### File 4: `market.md`

**What it contains:**

- Market size and growth context (Poland-specific)
- Key trends (technology shifts, price movements, consumer behavior changes)
- Seasonal patterns (when do people buy? IEM, Black Friday, back-to-school?)
- Purchase channel behavior (where do Polish buyers research? where do they buy?)
- Key events and cultural moments relevant to the category

**Schema:** See `references/research_file_schemas.md#market`

---

### File 5: `product analysis.md`

**What it contains:**

- Product lines overview (name, specs, price, positioning)
- USP (Unique Selling Propositions) — what the client has that no competitor has
- Trust signals (years in business, order count, certifications, press quotes)
- Pricing table with competitor comparison
- Review quotes from Polish press (attributed with source)
- Constraints (what NOT to claim in ads — legal, accuracy)

**How to research:**

1. Read the client's official product pages
2. Search Polish tech press for reviews: `"[product name] recenzja" site:benchmark.pl OR site:instalki.pl`
3. Check the client's Ceneo profile for customer review language
4. Verify all specs from official product pages — do not rely on third-party spec listings

**Schema:** See `references/research_file_schemas.md#product`

---

## Workflow

```
1. Get client brief (product category, brand name, target market)
2. Run web research for each of the 5 files
3. Create files in Meta Ads Analysis Production Upload/_archive/ad-creator/Clients/{ClientName}/
4. Cross-reference: quotes in audience.md must be traceable to real sources
5. Verify: all claims in product analysis.md must have a source
6. Hand off to creative-angle-writer
```

---

## Quality Checklist

Before handing off to `creative-angle-writer`, verify:

- [ ] All customer quotes are verbatim (not paraphrased)
- [ ] Each quote has a source (forum thread, review site, survey)
- [ ] mindstates.md is valid JSON
- [ ] All product specs are verified from official sources
- [ ] Competitor prices are current (check date)
- [ ] At least 3 positioning gaps identified in competitors.md

---

## Reference: Iiyama Case Study

See `Meta Ads Analysis Production Upload/_archive/ad-creator/Clients/Iiyama/` for a complete example of all 5 files.  
The Iiyama research was conducted in February 2026 and represents the quality standard for this skill.
