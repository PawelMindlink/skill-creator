---
name: creative-angle-writer
description: Generates creative angle files (GAM-A0X) from client research documents. Each angle is a structured brief with Big Idea, UMP/UMS, customer language, evidence table, and Masterson self-score.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. Based on reverse-engineering of Iiyama GAM angle files (Feb 2026).
---

# Creative Angle Writer

## Purpose

Transform client research files into structured creative angle briefs (GAM-A0X files). Each file is a complete brief that `meta_ads_strategist` and `meta_ads_copywriter` can execute without additional research.

**Input:** 5 research files from `client-researcher`  
**Output:** `{CLIENT}-A{NN}-{slug}.md` files in `Ad Creator/Clients/{ClientName}/`

---

## The GAM Angle File Format

Every angle file must follow this exact structure:

```markdown
# {CLIENT}-A{NN}: {Title} ({Angle Type Name})

**Type:** {Angle Type} → **{Lead Type}**
**Segment:** {Primary Segment} — Primary; {Secondary} (secondary)
**Date:** {YYYY-MM-DD}
**Status:** [NEW]

---

## 3-Rule Filter

- **Visualizable:** YES/NO — [explanation]
- **Falsifiable:** YES/NO — [explanation]
- **Believable & Specific:** YES/NO — [explanation]

**3-Rule Verdict: PASS / FAIL**

---

## Big Idea
[One sentence. The core claim. What makes this angle unique.]

## UMP (Unique Mechanism of Problem)
[Why does the problem exist? What is the mechanism that causes it?]

## UMS (Unique Mechanism of Solution)
[How does this specific product solve it? What is the mechanism?]

## Mechanism
[One sentence combining UMP + UMS into a single causal chain.]

## Lead Type
**Primary:** [Angle type]
**Secondary:** [Supporting element]

## Target Segment(s)
- [Primary segment] — [age, context, why this angle works for them]
- [Secondary segment] — [why it also works here]

## Psychology Reference
[Reference to mindstates.md — which mindstate, which heuristic, which audience signal]

## Headline Approach: {EMOTIONAL / DIRECT CLAIM / HYBRID}
**Guidance for Creative Strategist:** [How to write the headline]

**Example headlines:**
- "[Option A]"
- "[Option B]"
- "[Option C]"

**Why this works:** [Psychological mechanism in plain language]

## Customer Language to Use (from audience.md)
- "[verbatim quote 1]"
- "[verbatim quote 2]"
- "[verbatim quote 3]"

## Key Benefits
- [Benefit 1 — specific number or fact] (functional/emotional/financial)
- [Benefit 2]
- [Benefit 3]

## Objection Handling
- **Objection:** "[exact objection]" → **Overcome:** "[specific response]"
- **Objection:** "[exact objection]" → **Overcome:** "[specific response]"

## Evidence

| Claim | Tier | Source |
|-------|------|--------|
| [claim] | Verified | File: [filename] — "[exact quote or spec]" |

## Handoff Notes (For Creative Strategist)
- **Evidence available:** [what the strategist has to work with]
- **Constraints:** [what NOT to claim — legal, accuracy, competitor naming]
- **Psychological mechanism:** [which heuristic fires and why]

## Self-Score (5-Dimension Masterson Framework)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Big Idea Strength | /20 | |
| Mechanism Clarity | /20 | |
| Benefit Specificity | /20 | |
| Objection Handling | /20 | |
| Evidence Quality | /20 | |
| **TOTAL** | **/100** | GREEN LIGHT (≥80) / YELLOW (60-79) / RED (<60) |

## Why This Works for This Segment
[2-3 sentences connecting the angle to the segment's documented psychology]
```

---

## Angle Types

See `references/angle_types.md` for full definitions. Summary:

| Type | Lead | When to Use |
|------|------|-------------|
| Problem-Solution | EMOTIONAL | Customer has documented pain; product removes it |
| Mechanism Reveal | DIRECT CLAIM | Spec-price ratio is the hook; buyer is spec-literate |
| Risk Reversal | EMOTIONAL | Purchase anxiety is the barrier; guarantee is the solution |
| Comparison | DIRECT CLAIM | Buyer is at decision stage comparing options |
| Loss Aversion | EMOTIONAL/HYBRID | Buyer risks losing something by NOT buying |
| Identity-Based | EMOTIONAL | Cultural moment or community belonging is the hook |
| Social Proof | EMOTIONAL | Brand awareness is low; peer recommendation is the trust bridge |

---

## 3-Rule Filter (Apply to Every Angle Before Writing)

Every angle must pass all 3 rules:

1. **Visualizable** — Can a designer create the visual in under 0.5 seconds of viewing? If you can't describe the image in one sentence, the angle is too abstract.
2. **Falsifiable** — Is the claim specific and verifiable? Vague claims ("great quality") fail. Specific claims ("280Hz at 859 PLN") pass.
3. **Believable & Specific** — Does the claim have a source? Is it specific enough that a skeptic could verify it?

If any rule fails → **do not write the angle**. Find a different approach.

---

## Masterson 5-Dimension Scoring

| Dimension | What It Measures | Max |
|-----------|-----------------|-----|
| Big Idea Strength | Is the core claim memorable and unique? | 20 |
| Mechanism Clarity | Is the UMP/UMS specific and understandable? | 20 |
| Benefit Specificity | Are benefits expressed as numbers, not adjectives? | 20 |
| Objection Handling | Does it address the real objections for this segment? | 20 |
| Evidence Quality | Are all claims sourced and verifiable? | 20 |

**Thresholds:**

- ≥80: GREEN LIGHT — proceed to creative execution
- 60–79: YELLOW — revise before proceeding
- <60: RED — do not run; find a better angle

---

## Workflow

```
1. Read audience.md → identify segments and customer language
2. Read mindstates.md → load heuristics and content tactics
3. Read competitors.md → identify positioning gaps
4. Read product analysis.md → load verified claims, prices, specs
5. Read market.md → identify timing opportunities (seasonal, events)
6. For each segment: brainstorm 2-3 potential angles
7. Apply 3-Rule Filter → eliminate failing angles
8. Write GAM files for passing angles
9. Score each with Masterson Framework
10. Flag GREEN LIGHT angles for meta_ads_strategist
```

---

## Naming Convention

```
{CLIENT}-A{NN}-{slug}.md
```

- `{CLIENT}` — 3-letter client code (e.g., GAM for iiyama Gaming)
- `{NN}` — two-digit sequential number (01, 02, 03...)
- `{slug}` — kebab-case description of the angle

Examples: `GAM-A01-sprzet-mnie-wydal.md`, `GAM-A02-zero-martwych-pikseli.md`

---

## Reference: Iiyama Case Study

See `Ad Creator/Clients/Iiyama/GAM-A0X-*.md` for 10 complete examples.

**Highest scoring angles for reference:**

- GAM-A02 (91/100) — Risk Reversal, Zero Dead Pixel Guarantee
- GAM-A03 (89/100) — Mechanism Reveal, 280Hz at 859 PLN
- GAM-A04 (87/100) — Mechanism Reveal, 32" WQHD at 1199 PLN
