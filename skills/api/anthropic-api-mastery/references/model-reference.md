# Claude API — Model Reference (March 2026)

Source: [Official Models Overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)

---

## Current Models

| Model | API ID | Context | Max Output | Price (in/out MTok) | Best For |
|---|---|---|---|---|---|
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | 200K (1M beta) | 64K | $3 / $15 | Default workhorse: coding, agents, copy, analysis |
| **Claude Opus 4.6** | `claude-opus-4-6` | 200K (1M beta) | 128K | $5 / $25 | Max accuracy, long agentic sessions, enterprise |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251001` | 200K | 64K | $1 / $5 | High-volume, classification, extraction, routing |

---

## Decision Rule

```
Task                                    → Model
────────────────────────────────────────────────────────────
Classification, extraction, routing     → claude-haiku-4-5-20251001  (5× cheaper)
Coding, copy, reasoning, agents         → claude-sonnet-4-6           (default)
Max accuracy, 128K output, long tasks   → claude-opus-4-6
```

When in doubt, start with Sonnet 4.6. Only upgrade to Opus if quality is measurably insufficient. Only downgrade to Haiku after testing that it meets quality requirements.

---

## Thinking Modes (Sonnet & Opus 4.6)

Both Sonnet 4.6 and Opus 4.6 support two thinking modes:

| Mode | Description | When to Use |
|---|---|---|
| **Extended Thinking** | Developer controls the thinking budget | Complex tasks needing deep reasoning |
| **Adaptive Thinking** | Model decides when to think deeply | General-purpose; model self-selects |

Haiku 4.5 supports Extended Thinking only.

Enabling extended thinking:

```python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8000,
    thinking={"type": "enabled", "budget_tokens": 5000},
    messages=[{"role": "user", "content": "Analyze this legal contract for risk..."}]
)
```

---

## 1M Token Context Window (Beta)

Available for Sonnet 4.6 and Opus 4.6 via a beta header:

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    betas=["context-1m-2025-08-07"],  # enable 1M context
    messages=[{"role": "user", "content": "...very long document..."}]
)
```

---

## Training Data Cutoffs

| Model | Training Cutoff |
|---|---|
| Claude Opus 4.6 | August 2025 |
| Claude Sonnet 4.6 | January 2026 |
| Claude Haiku 4.5 | July 2025 |
