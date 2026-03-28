# Claude API — Copywriting Playbook

---

## Why Claude for Copywriting

Claude's Constitutional AI training reduces "AI fluff" — generic superlatives, buzzword soup, and passive-aggressive filler sentences. It responds well to context and constraint, behaving more like a senior strategist than a junior writer.

**Claude is not a button.** It is a collaborator. The quality of output is proportional to the quality of your brief.

---

## The Minimum Viable Brief

Every copywriting prompt must include:

| Element | Example |
|---|---|
| **Who you're writing for** | "B2B SaaS CTOs at 50–500-person companies" |
| **What the product does** | "Reduces engineering sprint planning from 2 hours to 15 minutes" |
| **The core pain point** | "Engineers waste half their day in planning ceremonies" |
| **The CTA** | "Book a 20-minute demo" |
| **Format / length** | "150 words max. 3 paragraphs. Landing page hero." |
| **Negative constraints** | "No emojis. No words: 'powerful', 'seamless', 'leverage'. No passive voice." |

Without at least 4 of these 6 elements, expect generic output.

---

## Brand Voice Injection

The single highest-leverage prompt engineering technique for copywriting.

```xml
<brand-voice>
  Study these examples of our best-performing copy. Match the sentence length,
  rhythm, and vocabulary — not just the "tone".

  Example 1: "We don't do pitch decks. We do results decks."
  Example 2: "Your CRM is full of leads. Few of them are real."
  Example 3: "Stop spending on traffic. Start converting what you have."
</brand-voice>

<task>Write a 3-line hero headline for our new retargeting feature.</task>
```

Feed **3–5 real examples** from your best-performing content. Generic examples produce generic output.

---

## Workflow: Human → AI → Human

```
1. Human writes the brief (context, audience, CTA, constraints)
         ↓
2. Claude drafts (provide brand examples, use XML structure)
         ↓
3. Human edits (cuts jargon, adds nuance, adjusts rhythm)
         ↓
4. Claude iterates if needed ("Rewrite paragraph 2 only. Make it punchier.")
```

Do not use Claude output directly without a human review pass. AI copy reads fine; human-edited AI copy converts.

---

## Template: Full Copywriting System Prompt

```python
SYSTEM_PROMPT = """
You are a direct-response copywriter specializing in B2B SaaS.
Your copy is short, direct, and benefit-driven.
You never use the following words: powerful, seamless, robust, leverage,
cutting-edge, game-changing, revolutionize, unlock.
You write in active voice. Sentences are under 20 words.
"""

def generate_copy(brief: str, examples: list[str], task: str) -> str:
    brand_examples = "\n".join(f"- {e}" for e in examples)

    prompt = f"""
<brand-voice>
Match the rhythm and vocabulary of these examples:
{brand_examples}
</brand-voice>

<brief>
{brief}
</brief>

<task>
{task}
</task>

First, think step by step inside <thinking> tags about what message will resonate most.
Then write the copy inside <output> tags.
"""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```

---

## Content Type Patterns

### Landing Page Hero

- Lead with the outcome, not the feature.
- Headline: The transformation in one sentence.
- Subhead: How you get there, one sentence.
- CTA: Action verb + specific result. ("Calculate your ROI", not "Get started")

### Cold Email Hook (First 2 Sentences)

- Open with their world, not yours ("Your team spends 12 hours/week in planning calls.")
- Introduce your mechanism, not your product. ("We reduced that to under 2 hours for 40+ teams.")

### Ad Copy (Meta / Google)

- Primary text: Pain → Solution → Proof → CTA. Under 125 characters for primary.
- Headline: Specific number + benefit if possible. ("Cut planning time by 85%")
- One explicit CTA per ad. Never two.

### Email Subject Lines

- Under 50 characters.
- Avoid clickbait framing — it damages long-term sender reputation.
- Best performers: question, specific number, or pattern interrupt.

---

## What Claude Will Push Back On

Claude will resist copy that is misleading, exaggerated, or unsupported by evidence. If you get a softer output than expected:

- Add specificity: "Results are based on our median customer case study of 74 companies."
- Cite a source: "82% of users reduced onboarding time by 40% in 30 days (internal data, n=200)."
- Frame the constraint: "This copy is for an opt-in landing page where users understand what they're signing up for."

Claude responds to evidence and context, not to "just do it more aggressively."
