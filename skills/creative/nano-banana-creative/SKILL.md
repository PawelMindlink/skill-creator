---
name: nano-banana-creative
description: Expert skill for generating high-converting Meta Ad images using Nano Banana. Focus on "Pattern Interrupts" while maintaining "Andromeda Diversity". Reads GAM angle files to select the correct aesthetic.
version: 1.2.0
changelog: |
  v1.2.0: Added GAM angle type → aesthetic mapping. Added ad_formats_catalog.md reference.
  v1.1.0: Fixed hard-coded absolute paths. Added "Andromeda Diversity" aesthetic selectors.
  v1.0.0: Initial version.
---

# Goal

Teach the agent how to construct professional "production briefs" for Nano Banana to create high-performing Meta Ad assets.

# Core Philosophy: Andromeda Diversity (Testing is King)

* **Diversity Rule**: We do not know what will work. Therefore, we must **test opposites**.
* **The Mix**: For every product, you must generate briefs across the spectrum:
  * **Aesthetic A (Polished)**: High-end, studio, aspirational (Trust).
  * **Aesthetic B (Raw/Native)**: iPhone style, messy, UGC (Relatability).
  * **Aesthetic C (Weird/Shock)**: High contrast, odd objects, red circles (Curiosity).

# Learning Loop (Data-Driven)

Before generating new briefs, check the performance data if available in the project's data exports (e.g., `*.csv` files in the working directory).

## North Star Metrics

When analyzing what to iterate on, prioritize:

1. **Contribution Profit (Primary)**: The ultimate business truth. Did this creative make money?
2. **Hook Rate (Secondary)**: Did it stop the scroll? (Use this to optimize the *visual aesthetics*).
3. **Hold Rate (Tertiary)**: Did it keep attention? (Use this to optimize the *content/subject*).

## Iteration Logic

1. **Read**: Load the CSV.
2. **Identify**: Find the Top 3 Creatives by **Contribution Profit**.
3. **Refine**:
    * If "Raw" is winning -> Double down on "Ugly/Native" variants.
    * If "Studio" is winning -> Double down on "High Fidelity".
    * **Always** keep 20% of budget/briefs for the losing style (to catch trend shifts).

# Instructions

When creating briefs, follow the **Nano Banana Anatomy**:

1. **Format & Aspect Ratio**:
    * **4:5** (Feed) or **9:16** (Stories/Reels).

2. **Aesthetic Selectors (Pick diverse options)**:
    * **Style 1: Raw Native (UGC)**: "Shot on iPhone", "Flash photography", "Messy background". *Goal: Relatability/Stopping Power.*
    * **Style 2: Studio Polish**: "Softbox lighting", "Clean marble background", "bokeh". *Goal: Trust/Authority.*
    * **Style 3: The "Weird" Macro**: Extreme close-up of texture/detail. *Goal: Curiosity.*
    * **Style 4: Native Overlay**: Adding "native" UI elements (Red circle in Paint, iOS bubbles).

3. **Composition & Action**:
    * **Subject**: Clear focus.
    * **Lighting**: Match the aesthetic (Harsh for Raw, Soft for Studio).
    * **Text Integration**: "Rule of Thirds" to avoid UI overlap.

# Visual Hooks (The "Clickbait" Visuals)

Use these triggers in your prompts (apply primarily to Raw/Weird styles):

* **"The Red Circle"**: Explicitly ask to "Draw a rough red circle around [Feature] looking like it was done in Paint."
* **"The Arrow"**: "A big red arrow pointing at the product."
* **"The Contrast"**: "Split screen. Left side: Dim/Sad. Right side: Bright/Happy."
* **"The Oddity"**: "Product next to an unrelated, contrast-high object."

# GAM Angle → Aesthetic Starting Hypothesis

> [!IMPORTANT]
> **Andromeda Diversity overrides everything.** The table below is a *starting hypothesis* for your first test. You must always run at least one opposite aesthetic to discover what actually works.

When `meta_ads_strategist` provides a GAM-A0X file, use this as your **first test hypothesis**:

| GAM Lead Type | First Hypothesis | Always Also Test |
|--------------|-----------------|-----------------|
| EMOTIONAL | Raw Native (UGC) | Studio Polish (you may be wrong) |
| DIRECT CLAIM | Studio Void or Spec Card | Raw Native (specs in UGC style can outperform) |
| HYBRID | Both simultaneously | — |
| IDENTITY | The Context (product in scene) | Raw Native |
| SOCIAL PROOF | Native Overlay (forum/Discord style) | Studio Polish |

**Segment is a stronger signal than angle type:**

| Segment | Lean Toward | Why |
|---------|------------|-----|
| Competitive Shooter (18-26) | Raw Native | Peer-to-peer authenticity; distrust of polished ads |
| Immersive Gamer (25-35) | Studio Polish or Spec Card | Higher income; responds to quality signals |
| WFH Power User (28-42) | Studio Polish | Professional context; aspirational |
| Budget First Timer (16-22) | Raw Native | Relatability over aspiration |

**Placement is also a signal:**
* Reels / Stories → Raw Native (native to format)
* Feed → can be either; test both

Also read the **Handoff Notes** section of the GAM file — it contains visual constraints specific to that angle.

> **Ad Formats Reference**: See `references/ad_formats_catalog.md` for format specs (4:5, 9:16, carousel) and composition rules.

# Examples

## Example 1: The "Raw Native" Brief

**Input**: "Meta Ad for a coffee brand (Test A)."
**Output**:
Prompt: "4:5 aspect ratio. POV shot looking down at a messy kitchen counter. A hand holding a bag of [Coffee Brand], slightly tilted. Morning sunlight hitting the bag hard. Background: spilled beans. Style: iPhone photography, unpolished."

## Example 2: The "Studio Polish" Brief

**Input**: "Meta Ad for a coffee brand (Test B)."
**Output**:
Prompt: "4:5 aspect ratio. Eye-level macro shot of the [Coffee Brand] bag sitting on a pristine white marble surface. Soft, volumetric morning light. Steam rising gently from a cup in the background. Style: Cinematic, 8k, photorealistic, advertising standard."

## Troubleshooting

* **Aesthetic Mismatch**: If the Raw style looks too "AI-clean," add specific degradation prompts like "noisy image," "glare," or "bad lighting."
* **Prompt Ignored**: If Nano Banana ignores an element (like the Red Circle), try putting it at the very beginning of the prompt or using the "Native Overlay" style.
* **Low Engagement**: Test a completely opposite aesthetic. If Studio Polish is failing, go "iPhone-ugly" (Aesthetic B).
