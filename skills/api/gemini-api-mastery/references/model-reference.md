# Gemini API — Model Reference (March 2026)

Source: [Official Pricing Page](https://ai.google.dev/gemini-api/docs/pricing) | [Models Overview](https://ai.google.dev/gemini-api/docs/models)

---

## Text Models

| Model | API ID | Tier | Use Case |
|---|---|---|---|
| Gemini 3.1 Pro Preview | `gemini-3.1-pro-preview` | Preview/Paid | Complex reasoning, multimodal, agentic workflows |
| Gemini 3.1 Flash Preview | `gemini-3.1-flash-preview` | Preview/Paid | Balanced intelligence and speed |
| Gemini 3.1 Flash-Lite Preview | `gemini-3.1-flash-lite-preview` | Preview/Free+Paid | High-volume, cost-priority, classification |
| Gemini 2.5 Pro | `gemini-2.5-pro` | Stable/Paid | Production: complex reasoning |
| Gemini 2.5 Flash | `gemini-2.5-flash` | Stable/Free+Paid | Production: general purpose workhorse |
| Gemini 2.5 Flash-Lite | `gemini-2.5-flash-lite` | Stable/Free+Paid | Production: cost-optimized volume |

> **Preview models** change before becoming stable and have more restrictive rate limits. Do NOT use in production without fallback.

### Decision Rule

```
Volume / classification / extraction → gemini-3.1-flash-lite-preview
Reasoning / multimodal / agents     → gemini-3.1-pro-preview
Production stability needed          → gemini-2.5-flash (stable)
```

---

## Image Models

| Model | API ID | Notes |
|---|---|---|
| **Imagen 4** | `imagen-4.0-generate-001` | Best text rendering, highest photorealism |
| Imagen 4 Ultra | `imagen-4.0-ultra-generate-001` | Maximum quality, slowest, highest cost |
| Imagen 4 Fast | `imagen-4.0-fast-generate-001` | Speed-optimized |
| **Nano Banana 2** 🍌 | `gemini-3.1-flash-image-preview` | Conversational editing + generation (Flash speed) |
| Nano Banana Pro 🍌 | `gemini-3-pro-image-preview` | Highest quality generation + editing |

### Imagen 4 vs. Nano Banana — When to Use Which

| Need | Use |
|---|---|
| One-shot text-to-image, max quality/text rendering | Imagen 4 |
| Iterative editing, reference images, multi-image fusion | Nano Banana 2 |
| Highest fidelity generation + editing combo | Nano Banana Pro |
| High-throughput image pipeline | Imagen 4 Fast |

> Nano Banana 2 is the default engine in Gemini App, Google Search AI Mode, Google Lens, and Google Ads (as of Feb 26, 2026).

---

## Video Models

| Model | API ID | Tier | Notes |
|---|---|---|---|
| **Veo 3.1** | `veo-3.1-generate-preview` | Preview/Paid | Latest: audio, lip sync, up to ~1 min |
| **Veo 3.1 Fast** | `veo-3.1-fast-generate-preview` | Preview/Paid | Speed-optimized, for iteration |
| Veo 3 (stable) | `veo-3.0-generate-001` | Stable/Paid | Production-grade, native audio |
| Veo 3 Fast | `veo-3.0-fast-generate-001` | Stable/Paid | Stable fast variant |

All video models require the **Paid tier**.

---

## Embedding & Specialized Models

| Model | API ID |
|---|---|
| Gemini Embedding | `gemini-embedding-001` |

---

## Pricing Tiers

- **Free**: Limited model access, content used to improve products. Good for dev/testing.
- **Paid**: Higher rate limits, Context Caching, Batch API (50% discount), data not used for training.
- **Enterprise (Vertex AI)**: Dedicated support, compliance, provisioned throughput, volume discounts.
