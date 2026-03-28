# Imagen 4 — Precise Prompting Guide

Source: [Imagen Docs](https://ai.google.dev/gemini-api/docs/imagen)

---

## Model IDs (March 2026)

| Model | API ID | Best For |
|---|---|---|
| Imagen 4 | `imagen-4.0-generate-001` | Best text rendering, highest overall quality |
| Imagen 4 Ultra | `imagen-4.0-ultra-generate-001` | Product hero shots, maximum fidelity |
| Imagen 4 Fast | `imagen-4.0-fast-generate-001` | High-volume batch generation |

*Note: Imagen models generate images in a single call. If you need conversational editing, multi-image fusion, or character consistency, use **Nano Banana 2** instead.*

---

## Prompt Anatomy

Imagen 4 requires **dense, fully-specified prompts** because each generation is an independent, one-shot call. You cannot iteratively refine it like a chat model.

Every element below adds precision to your output. Define them all in a single prompt.

```
[Subject] [Attributes] [Action] [Scene/Environment] [Composition] [Lighting] [Style] [Technical]
```

| Element | Description | Example |
|---|---|---|
| **Subject** | What or who is the focus | "A glass bottle of olive oil" |
| **Attributes** | Visual properties | "dark green glass, matte label, clean edges" |
| **Action** | What the subject is doing | "standing upright on a surface" |
| **Scene** | Background and environment | "on a rustic wooden table with scattered herbs" |
| **Composition** | Shot type and framing | "macro close-up, rule of thirds, empty space on left" |
| **Lighting** | Light quality and direction | "warm golden hour side light with soft shadows" |
| **Style** | Aesthetic reference | "editorial food photography, minimal" |
| **Technical** | Resolution/quality cues | "8K, photorealistic, sharp focus" |

### Example Prompts

**Product hero shot:**
> "A sleek white sneaker with a translucent blue sole, standing on a white marble surface. Studio three-point lighting, front-facing, slight low angle. Minimal background. Editorial fashion photography. 8K, photorealistic, sharp focus."

**Lifestyle image with text:**
> "A woman in her 30s reading a book in a sunlit café. Render the text 'READ MORE. WORRY LESS.' in a clean sans-serif font on a chalkboard behind her. Warm bokeh background. Natural light, candid style."

---

## Text Rendering — Explicit Quotes

Imagen 4 has industry-leading text accuracy, but it must be told *exactly* what to render using quotes.

**Bad:** "Generate a logo for a coffee shop called Origin."
**Good:** "Generate a minimalist logo for a coffee brand. Render the text 'ORIGIN' in bold, dark green, sans-serif typography below a simple leaf icon. Clean white background."

---

## Negative Prompts (What to Avoid)

Unlike conversational models, Imagen 4 uses a strict `negative_prompt` API parameter to exclude elements.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='A modern living room with a white sofa and glass coffee table.',
    config=types.GenerateImagesConfig(
        negative_prompt="people, pets, clutter, dark shadows",
        number_of_images=1,
        output_mime_type="image/jpeg",
        aspect_ratio="16:9"
    )
)

for generated_image in response.generated_images:
  with open("output.jpg", "wb") as f:
      f.write(generated_image.image.image_bytes)
```

---

## Aspect Ratios

Always specify an aspect ratio; default is usually `1:1`.

- `1:1` (Square)
- `3:4` or `4:5` (Social Feed Portrait)
- `4:3` (Landscape Standard)
- `16:9` (Widescreen / YouTube / Presentations)
- `9:16` (Stories / Reels / Shorts)

---

## Recommended Generation Parameters

> See [prompt-and-parameter-guide.md](prompt-and-parameter-guide.md) for full parameter reference.

| Use Case | temperature | seed | number_of_images | Notes |
|---|---|---|---|---|
| Brand-locked hero shot | `0.0–0.2` | Fixed (e.g. `42`) | 1 | Reproducible; pin seed after approval |
| A/B creative variants | `0.8–1.0` | Omit | 3–4 | High variation for creative testing |
| Batch product catalogue | `0.5` | Omit | 1 | Balanced quality + throughput |

```python
from google import genai
from google.genai import types

client = genai.Client()

# Reproducible hero shot — pin temperature + seed
response = client.models.generate_images(
    model="imagen-4.0-generate-001",
    prompt="A premium glass olive oil bottle on rustic wood, golden hour side light, editorial food photography, 8K.",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="4:5",        # Feed portrait
        output_mime_type="image/jpeg",
        # temperature=0.2,         # Low variation — brand-locked
        # seed=7341                 # Uncomment to pin exact variant
    )
)
```

> **`thinking_level` does not apply to Imagen 4.** Imagen is not a text-generation model — generation config is via `GenerateImagesConfig`, not `GenerateContentConfig`.
