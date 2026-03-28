# Veo 3.1 — Video Generation Guide

Source: [Veo 3.1 Docs](https://ai.google.dev/gemini-api/docs/video)

---

## Model IDs

| Model | API ID | Use |
|---|---|---|
| Veo 3.1 | `veo-3.1-generate-preview` | Best quality, native audio, lip sync |
| Veo 3.1 Fast | `veo-3.1-fast-generate-preview` | Rapid iteration, lower latency |

> Both require the **Paid tier**. Preview models have stricter rate limits.

---

## What Veo 3.1 Can Do (vs. Veo 2)

| Feature | Veo 2 | Veo 3 | Veo 3.1 |
|---|---|---|---|
| Resolution | 720p | Up to 4K | Up to 4K |
| Native audio (dialogue, SFX, music) | ❌ | ✅ | ✅ |
| Lip sync | ❌ | ✅ | ✅ |
| Clip length | 8 sec | 8 sec | Up to ~1 min |
| Image-to-video (i2v) | ✅ | ✅ | ✅ |
| Video extension | ❌ | ✅ | ✅ |
| SynthID watermark | ✅ | ✅ | ✅ |

---

## Prompt Anatomy

Well-structured Veo prompts follow this order. Every element improves output quality.

```
[Subject] [Action] [Composition] [Scene/Location] [Camera Motion] [Ambiance] [Style]
```

| Element | Description | Example |
|---|---|---|
| **Subject** | Who or what is the focus | "A middle-aged female scientist" |
| **Action** | What the subject is doing | "writing on a whiteboard" |
| **Composition** | Framing and shot type | "Medium shot, rule of thirds" |
| **Scene** | Location and environment | "in a modern research lab, daytime" |
| **Camera Motion** | How the camera moves *(biggest quality lever)* | "slow dolly-in", "orbital pan", "static wide" |
| **Ambiance** | Light and color | "warm afternoon light through floor-to-ceiling windows" |
| **Style** | Aesthetic or cinematic reference | "cinematic, shallow depth of field, ARRI Alexa look" |

### Camera Motion Vocabulary

- **Static**: Tripod, locked off
- **Dolly**: Physical push toward/away from subject
- **Pan/Tilt**: Rotate left-right / up-down
- **Tracking shot**: Camera follows subject laterally
- **Orbital**: Rotates around subject
- **Aerial / Drone**: Top-down or elevated travel
- **Handheld**: Slight natural shake, documentary feel

### Example Prompts

**E-commerce product video:**
> "A white sneaker, rotating slowly, close-up macro shot, on a minimalist white surface with soft studio lighting. Orbital camera, 360°. Photorealistic, 4K."

**Dialogue scene:**
> "Two professionals in business attire having a conversation across a glass desk in a modern office. Medium two-shot. Natural window light on the left. Slight dolly-in. Cinematic. Veo 3.1 native dialogue: [Woman]: 'Let's look at the Q4 numbers.' [Man]: 'Already pulled them up.'"

---

## Files API — When to Use

Use the Files API for all video inputs:

- File is **>20MB** (hard limit for inline)
- You need to **reuse** the same file across multiple prompts
- Processing **YouTube URLs** as input is also supported

```python
# Upload a reference video
file = client.files.upload(path="reference.mp4")

# Use in generation
response = client.models.generate_content(
    model="veo-3.1-generate-preview",
    contents=["Extend this clip with a slow pull-back reveal:", file]
)
```

---

## Common Veo Mistakes

1. **No camera motion specified** → Veo defaults to a static locked shot. Always specify.
2. **Vague style** → "Cinematic" alone is not enough. Reference a look: "A24 film aesthetic", "BBC nature documentary", "fast-cut social media style".
3. **Attempting audio in Veo 2** → Only Veo 3+ supports native audio. Veo 2 delivers silent video.
4. **Using preview in production** → `veo-3.1-generate-preview` can change. Use `veo-3.0-generate-001` for stable production pipelines.

---

## Recommended Generation Parameters

> See [prompt-and-parameter-guide.md](prompt-and-parameter-guide.md) for full parameter reference.

| Use Case | temperature | seed | Notes |
|---|---|---|---|
| Scripted product ad (precise) | `0.3–0.4` | Fixed | Camera motion follows prompt exactly |
| Lifestyle / mood reel (exploratory) | `1.0–1.3` | Omit | Shot interpretation varies per run |
| Iterative prompt refinement | `0.5` | Fixed | Isolate prompt changes from random variation |

```python
from google import genai
from google.genai import types

client = genai.Client()

# Scripted ad — deterministic, high prompt fidelity
response = client.models.generate_content(
    model="veo-3.1-generate-preview",
    contents=(
        "A white sneaker rotating slowly on a white marble surface. "
        "Orbital camera, 360°. Studio three-point lighting. Photorealistic, 4K."
    ),
    config=types.GenerateContentConfig(
        temperature=0.3,
        seed=1042   # Fix seed to isolate prompt iterations
    )
)

# Exploratory mood reel — let model interpret creatively
response_explore = client.models.generate_content(
    model="veo-3.1-generate-preview",
    contents="A product launch moment in a sleek modern showroom. Cinematic feel.",
    config=types.GenerateContentConfig(temperature=1.2)
)
```

> **Always specify camera motion explicitly.** Temperature does not compensate for a missing camera directive — a prompt without camera motion produces a static shot at any temperature.
