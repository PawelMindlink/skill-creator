---
name: anthropic-api-mastery
description: Expert skill for working with the Anthropic Claude API. Covers model selection (Sonnet/Opus/Haiku 4.x), API setup, copywriting, XML prompt engineering, Prompt Caching, and Message Batches API. Use when integrating Claude, writing marketing copy, or optimizing Anthropic API costs.
version: 3.0.0
changelog: |
  v3.0.0: Refactored into slim SKILL.md + references/ per skill-creator best practices.
  v2.0.0: Full rewrite with verified March 2026 model IDs from official Anthropic docs.
---

# Anthropic API Mastery

## When to use this skill

- Integrating the Anthropic Claude API into a codebase.
- Generating copywriting, marketing content, or structured outputs with Claude.
- Optimizing costs via Prompt Caching, Batch API, or model routing.
- Selecting the right Claude model for a task (Haiku / Sonnet / Opus).

## When NOT to use this skill

- User needs Claude.ai product features (not API) — refer them to claude.ai.
- User is working with AWS Bedrock or GCP Vertex integrations specifically — check platform-specific docs for credential setup.

---

## Agent Triage

| Task | Reference |
|---|---|
| Select a model or check pricing / API IDs | [references/model-reference.md](references/model-reference.md) |
| Structure prompts (XML, system, thinking) | [references/prompt-engineering.md](references/prompt-engineering.md) |
| Write marketing copy or brand voice content | [references/copywriting-playbook.md](references/copywriting-playbook.md) |
| Reduce costs (Caching, Batch, routing) | [references/cost-control.md](references/cost-control.md) |

---

## Quick Setup

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY env var

response = client.messages.create(
    model="claude-sonnet-4-6",   # default workhorse
    max_tokens=1024,
    system="You are a direct-response copywriter. Active voice. No fluff.",
    messages=[{"role": "user", "content": "Write a 3-sentence hook for a B2B SaaS landing page."}]
)
print(response.content[0].text)
```

**Default model:** `claude-sonnet-4-6`. Use `claude-haiku-4-5-20251001` for high-volume/cheap tasks.

---

## Common Mistakes

1. **Sonnet for everything.** Haiku 4.5 is 5× cheaper and handles classification, extraction, routing.
2. **No `cache_control` on large system prompts.** You're paying full price for static context on every call.
3. **Skipping the Batch API.** Any async pipeline of 20+ items gets 50% off automatically.
4. **Vague copy briefs.** Specify: word count, persona, pain point, CTA, negative constraints.
5. **Hardcoding `temperature`** without a specific reason — especially bad for deterministic extraction tasks.

---

## Official References

- [Models Overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)
- [Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)
- [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
