---
name: deep-research
description: A rigorous 8-phase verification protocol for complex questions.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. 8-phase protocol for zero-hallucination verification.
---

# Deep Research Protocol

## Purpose

To move beyond "Search" and achieve "Verification".
Use this skill when the user asks for "Research", "Deep Dive", or when verifying critical strategic assumptions (e.g., Auction Mechanics).

## Core Engineering Protocols

1. **Zero-Hallucination Mandate**:
    - Never invent libraries, benchmarks, or correlations.
    - If data is missing, state: "Data Missing". Do not extrapolate without warning.
2. **Anti-Simplification**:
    - Complexity is necessary. Do not "dumb down" the finding if it compromises validity.
    - *Example*: Instead of "High CPM is bad", say "High CPM is value-destructive only when $eCVR < 1.5\%$".
3. **Objective Neutrality (Critique First)**:
    - Use the **Scientific Method**.
    - If the User's premise is flawed (e.g., "Why is my perfect ad failing?"), aggressively correct it: "The ad is NOT perfect because it has a 0.5% CTR."
    - No fluff. No "Great question!". Just the raw diagnostic.

## Core Workflow (The 8 Phases)

1. **Clarify**: (Implicit) Do I understand the *nuance* of the question?
2. **Plan**: Break the question into sub-hypotheses ($H_1, H_2, H_n$).
3. **Retrieve**: Search explicitly for *opposing viewpoints* (Falsification).
    - *Query 1*: "Why X is true"
    - *Query 2*: "Why X is FALSE"
    - *Query 3*: "X vs Y correlation data 2025"
4. **Triangulate**: Cross-reference at least 3 distinct sources (e.g., Meta Official Docs, Third-Party Audit, Academic Paper).
5. **Synthesize**: Combine findings into a coherent narrative.
6. **Critique**: "What is missing? What is weak?"
7. **Refine**: Do one last search to plug gaps.
8. **Report**: Present findings with "Confidence Score" and "Limitations".

## The "Anti-Parrot" Rule

Do not just summarize the first search result.
If Source A says "Sky is Blue", explicitly look for Source B that might say "Sky is actually Violet but appears Blue".

## Example Usage

**User**: "Does Hook Rate correlate with CTR?"
**Deep Research**:

1. *Plan*: metrics definitions, correlation studies, industry benchmarks.
2. *Retrieve*: Search "Hook Rate CTR correlation case studies".
3. *Triangulate*: Find a MotionApp report, a Varos benchmark, and a Reddit media buyer thread.
4. *Report*: "Industry data suggests a weak positive correlation (0.2), confirming that Hooks capture attention but don't guarantee clicks (Bridge required)."

## Troubleshooting

- **Contradictory Results**: If sources conflict, report the conflict as a finding rather than choosing one. Use the "Triangulate" phase to find a third "tie-breaker" source.
- **Paywall/Access Issues**: If a key source is blocked, use `agent-browser` (Windows-ready) to attempt to read content or look for non-paywalled archives/summaries.
- **Vague Findings**: If search results are too broad, refine your sub-hypotheses with more specific technical terms.
