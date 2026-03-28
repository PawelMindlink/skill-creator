---
name: gemini-api-mastery
description: Expert skill for working with the Google Gemini API. Covers text (Gemini 3.1), image (Imagen 4 / Nano Banana 2), and video (Veo 3.1) generation, API setup, prompt optimization, and cost control. Use when integrating Gemini API, generating multimodal content, or reducing Gemini API costs.
version: 3.1.0
changelog: |
  v3.1.0: Added prompt-and-parameter-guide.md covering role types, determinism, temperature/top_k/top_p/seed, and thinking controls.
  v3.0.0: Refactored into slim SKILL.md + references/ per skill-creator best practices.
  v2.0.0: Full rewrite with verified March 2026 model IDs from official Google AI docs.
---

# Gemini API Mastery

## When to use this skill

- Integrating the Gemini API (text, image, video) into an application.
- Choosing the right model for a given task or budget.
- Optimizing prompts or reducing API costs.
- Debugging connection issues or rate limit errors.

## When NOT to use this skill

- User is working with Vertex AI enterprise features (use GCP docs instead).
- User needs ad asset creation workflows → use `nano-banana-creative` skill directly.

---

## Agent Triage

Before writing any code, identify the task:

| Task | Reference |
|---|---|
| Select the right model or check API IDs | [references/model-reference.md](references/model-reference.md) |
| Configure system instructions, prompt roles, or control temperature / top_k / top_p / seed / thinking | [references/prompt-and-parameter-guide.md](references/prompt-and-parameter-guide.md) |
| Generate images with strict, one-shot precision (Imagen 4) | [references/imagen-prompting-guide.md](references/imagen-prompting-guide.md) |
| Generate/edit images conversationally (Nano Banana 2) | [references/nano-banana-prompting-guide.md](references/nano-banana-prompting-guide.md) |
| Generate video with Veo 3.1 | [references/veo-prompting-guide.md](references/veo-prompting-guide.md) |
| Reduce API costs (Batch, Caching, routing) | [references/cost-control.md](references/cost-control.md) |
| Generate **ad** images (Meta format, archetypes) | `nano-banana-creative` skill |

---

## Quick Setup

```python
# pip install -q -U google-genai
from google import genai

client = genai.Client()  # reads GEMINI_API_KEY env var

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",  # cheapest capable model
    contents="Your prompt here"
)
print(response.text)
```

**Default model:** `gemini-3.1-flash-lite-preview` for volume tasks. `gemini-3.1-pro-preview` only for complex reasoning.

---

## Common Mistakes

1. **Defaulting to Pro.** Flash-Lite handles 80% of tasks at ~10% of the cost.
2. **No System Instruction.** Set role, tone, and format there — not in user turns.
3. **Missing camera motion in Veo prompts.** Without it, Veo generates static shots.
4. **Files passed inline when >20MB.** Use the Files API for large video uploads.
5. **Skipping the Batch API.** Async pipelines get an automatic 50% discount.

---

## Official References

- [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Model Overview](https://ai.google.dev/gemini-api/docs/models)
- [Veo 3.1 Docs](https://ai.google.dev/gemini-api/docs/video)
- [Context Caching](https://ai.google.dev/gemini-api/docs/caching)
