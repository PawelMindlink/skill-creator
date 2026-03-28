---
description: End-to-end ad creation pipeline from data to creative execution (v2 — post Koszulkowy test)
---

# Ad Creation Pipeline v2

// turbo-all

Full pipeline for creating Meta Ads for a new client or new campaign.

> [!IMPORTANT]
> **Order matters:** Data first, then research. MSC-ALGO output informs which segments to research deeply. This was validated in the Koszulkowy pipeline test (Feb 2026).

---

## Stage 1 — Data Pipeline (MSC-ALGO)

Run the MSC-ALGO n8n workflow to classify products.

**How:** Trigger the n8n workflow at `https://money-printing-machine.onrender.com/process`  
Or run locally: `python tests/reproduce_n8n_priority.py` in `Money Printing Machine/`

**Input:** Product Feed (XML), GA4 export (CSV), Meta Ads export (CSV)  
**Output:** `{ClientName}_Mapa_Strategii.csv` with P1-P8 classifications + Persona Product Map

**Key columns to check:**

- `Zestaw Reklam (AdSet)` — contains GWIAZDA/SLACKER classification
- `Bid_Cap`, `Cost_Cap`, `Critical_ROAS` — financial guardrails
- `Persona` — segment assignment (verify against audience.md segments)

**Skip if:** MSC-ALGO output already exists and is less than 30 days old.

---

## Stage 2 — Client Research

Run `client-researcher` skill to generate research files.

**Input:** Client name, product category, target market + MSC-ALGO output (for data-driven segments)  
**Output:** `Meta Ads Analysis Production Upload/_archive/ad-creator/Clients/{ClientName}/`

**Required files:**

- `audience.md` — ⚠️ MUST include real verbatim customer quotes (web research required, not inference)
- `mindstates.md` — JSON with heuristics and content tactics
- `product analysis.md` — USP, trust signals, top products (use MSC-ALGO data for product rankings)

**Optional files (create if competitive):**

- `competitors.md` — required for tech/specs categories (Iiyama); optional for niche/gift categories (Koszulkowy)
- `market.md` — required if seasonal patterns or events are important

**Quality check:** Every Customer Language quote must have a source. If inferred, mark as `[NEEDS_VERIFICATION]`.

**Skip if:** Files already exist and are less than 90 days old.

---

## Stage 3 — Creative Angle Generation

Run `creative-angle-writer` skill to generate GAM angle files.

**Input:** Research files from Stage 2 + MSC-ALGO data from Stage 1  
**Output:** `{CLIENT}-A{NN}-{slug}.md` files in `Meta Ads Analysis Production Upload/_archive/ad-creator/Clients/{ClientName}/`

**Process:**

1. Read research files + Persona Product Map
2. Identify segments from `audience.md`
3. For each segment: generate 2-3 angle candidates
4. Apply 3-Rule Filter (Visualizable / Falsifiable / Believable)
5. Write GAM files for passing angles
6. Score with Masterson Framework — only GREEN LIGHT (≥80) proceed
7. For time-sensitive angles: add `**Expiry:** {date}` to header

**Minimum output:** 1 angle per audience segment. Aim for 2.

---

## Stage 4 — Strategy & Briefs

Run `meta_ads_strategist` skill to connect data with angles.

**Input:**

- `{ClientName}_Mapa_Strategii.csv` (from Stage 1)
- All GAM-A0X files (from Stage 3)

**Process:**

1. Filter CSV for P1 (PROVEN STAR) and P3 (LAUNCH) products
2. For "Unclassified" products at >5,000 PLN spend: manually assign segment before proceeding
3. For each product: match to segment → select GAM angle by segment + score
4. Run brief generator: `python scripts/brief_generator.py {client_name}`
5. Enrich each brief with GAM fields (Hook, Big Idea, Objections, Evidence)
6. Output: `{ClientName}_Briefy_Produkcyjne.md`

---

## Stage 5 — Copywriting

Run `meta_ads_copywriter` skill.

**Input:** `{ClientName}_Briefy_Produkcyjne.md` + referenced GAM-A0X files  
**Output:** Ad copy variants (3 hooks + body + CTA per brief)

**For each brief:**

1. Read the GAM file referenced in the brief
2. Identify Lead Type (EMOTIONAL / DIRECT CLAIM / HYBRID)
3. Use verbatim Customer Language as hook (do NOT paraphrase)
4. Write Greased Chute body using Big Idea + Key Benefits
5. Handle top 1-2 objections mid-copy
6. End with What + Without + When CTA

---

## Stage 6 — Creative Execution

Run `nano-banana-creative` skill.

**Input:** `{ClientName}_Briefy_Produkcyjne.md` + GAM-A0X files  
**Output:** Image generation prompts for Nano Banana

**For each brief:**

1. Read GAM Lead Type and Segment
2. Select aesthetic hypothesis based on segment (see SKILL.md mapping table)
3. Generate 3 variants per brief: hypothesis aesthetic + opposite + wildcard
4. Apply Andromeda Diversity — always test opposites
5. Format: 4:5 (Feed) + 9:16 (Reels) for each variant

---

## Checklist Before Launch

- [ ] All GAM angles scored ≥80 (GREEN LIGHT)
- [ ] All customer language quotes verified from real sources (no [NEEDS_VERIFICATION] tags remaining)
- [ ] All claims in Evidence Table verified from source files
- [ ] Time-sensitive angles have Expiry date set
- [ ] Bid Cap and Cost Cap set in Meta Ads Manager
- [ ] "Unclassified" high-spend products manually segmented
- [ ] At least 2 aesthetic variants per angle (Andromeda Diversity)
- [ ] Copy reviewed against GAM Constraints (Handoff Notes section)
- [ ] Scent Match: ad copy matches landing page promise
