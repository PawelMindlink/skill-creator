# Nano Banana 2 — Conversational Image Guide

Source: [Nano Banana](https://nano-banana.ai) | Gemini Documentation

---

## Model IDs (March 2026)

| Model | API ID | Best For |
|---|---|---|
| **Nano Banana 2** 🍌 | `gemini-3.1-flash-image-preview` | Fast iterative editing, chat-based generation |
| Nano Banana Pro 🍌 | `gemini-3-pro-image-preview` | Highest fidelity editing + generation combo |

*Note: If you need strict one-shot generation with discrete negative prompts and the absolute best text rendering, use **Imagen 4** instead.*
*If you are creating Meta Ad assets specifically, refer to the **nano-banana-creative** skill.*

---

## Conversational Generation Workflow

Unlike traditional image models (like Imagen), Nano Banana 2 operates natively via the standard Gemini `generate_content()` or `chats` interface.

You don't need a single massive prompt. You can provide a rough concept and iterate naturally:
*"Make it warmer"* → *"Add steam rising from the cup"* → *"Change the background to a café"*

### 1. Basic Turn / Initiation

You **must** specify `response_modalities=["TEXT", "IMAGE"]` or the model will only respond with text describing the image.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents="Generate an image of a minimalist logo for a coffee brand called 'Origin'. Dark green on white.",
    generation_config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"]
    )
)

# Extract and save the generated image
for part in response.candidates[0].content.parts:
    if part.inline_data:
        with open("output.png", "wb") as f:
            f.write(part.inline_data.data)
```

### 2. Multi-Turn Editing (Chat Loop)

To iteratively refine an image, use the `chats` module to maintain conversational state.

```python
chat = client.chats.create(
    model="gemini-3.1-flash-image-preview",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"]
    )
)

# Turn 1: Generate base image
response = chat.send_message("Generate a photo of a red ceramic coffee mug on a white table.")

# Turn 2: Edit the previous image
response = chat.send_message("Now add steam rising from the mug and a wooden spoon beside it.")

# Turn 3: Refine the aesthetic
response = chat.send_message("Make the background a slightly blurred café environment instead of white. Keep the mug identical.")
```

### 3. Injecting Reference Images

Nano Banana 2 excels at fusing or maintaining reference subjects.

```python
import base64

with open("product_photo.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode()

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=[
        types.Part(
            inline_data=types.Blob(mime_type="image/jpeg", data=image_data)
        ),
        types.Part(text="Place this exact product on a beach sunset background. Maintain the product's label and shape precisely.")
    ],
    generation_config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"]
    )
)
```

---

## Negative Prompts and Resolution

**Negative Prompts:** Handled via natural language.

- *Instead of:* `negative_prompt="people, clutter"`
- *Use:* `"Generate this office scene but ensure there are no people and the desks are completely clear of clutter."`

**Resolution:** Nano Banana 2 supports tiered outputs. Specify in prompt:

- `0.5K` (Thumbnails, speed previews)
- `2K` (Social, Standard web)
- `4K` (High-fidelity print/production)

*Example: "Generate a 4K portrait orientation image of..."*

---

## Recommended Generation Parameters

> See [prompt-and-parameter-guide.md](prompt-and-parameter-guide.md) for full parameter reference.

Nano Banana 2 uses `GenerateContentConfig` (standard text-gen config) — all parameters apply.

| Use Case | temperature | thinking_level | Notes |
|---|---|---|---|
| Brand-consistent iterative editing | `0.6–0.7` | `"minimal"` | Stays close to reference across turns |
| Ad creative exploration | `0.9–1.1` | `"minimal"` | More visual variation per edit |
| One-shot generation (no prior context) | `0.8` | `"minimal"` | Balanced quality |

```python
from google import genai
from google.genai import types

client = genai.Client()

# Iterative ad editing — brand-safe temperature, minimal thinking overhead
chat = client.chats.create(
    model="gemini-3.1-flash-image-preview",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        temperature=0.7,
        thinking_config=types.ThinkingConfig(thinking_level="minimal")
    )
)

response = chat.send_message("Generate a photo of our red ceramic coffee mug on a white marble surface.")
response = chat.send_message("Add a wooden spoon beside it, keep the mug identical.")
```

> **Keep `temperature` consistent across chat turns** to avoid the model reinterpreting product details established in earlier turns.
