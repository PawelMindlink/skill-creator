# Gemini API — Prompt Types & Generation Parameters

Source: [GenerateContentConfig](https://ai.google.dev/api/generate-content#generationconfig) | [System Instructions](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions) | [Thinking Docs](https://ai.google.dev/gemini-api/docs/thinking)

---

## 1. Prompt Role Types

The Gemini API uses a conversation structure built from **roles** and **turns**. Understanding which role to use where is the single most common source of agent misconfiguration.

### Role Reference Table

| Role | Where Set | Purpose | Notes |
|---|---|---|---|
| `system` / `system_instruction` | `GenerateContentConfig` (not in `contents`) | Sets the model's persistent persona, constraints, and output format | Applied once per request; not part of the visible conversation |
| `user` | `contents[].role = "user"` | Represents a human turn (input, query, instruction) | Default role for `contents` if role is omitted |
| `model` | `contents[].role = "model"` | Represents previous model responses; used to supply synthetic chat history | Inject pre-baked assistant responses for few-shot examples |

> **Note:** There is no `developer` role in the Gemini API (this term is used by OpenAI). The equivalent in Gemini is the `system_instruction` field.

### How the Roles Map to API Fields

```text
GenerateContentConfig
├── system_instruction  →  "system" role  (set once, outside contents[])
│
contents[]
├── { role: "user",  parts: [...] }   →  Human turn
├── { role: "model", parts: [...] }   →  Model/assistant turn (injected history)
└── { role: "user",  parts: [...] }   →  Current query (last turn)
```

### Code Example — Full Role Structure

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=types.GenerateContentConfig(
        # SYSTEM role: sets behavior for the whole session
        system_instruction=(
            "You are a JSON extraction engine. "
            "Output only valid JSON. No commentary. No markdown fences."
        )
    ),
    # USER + MODEL turns: few-shot examples + actual query
    contents=[
        types.Content(role="user",  parts=[types.Part(text='Extract names: "Alice and Bob met Carol."')]),
        types.Content(role="model", parts=[types.Part(text='{"names": ["Alice", "Bob", "Carol"]}')]),
        types.Content(role="user",  parts=[types.Part(text='Extract names: "David called Emma."')]),
    ]
)
print(response.text)
# → {"names": ["David", "Emma"]}
```

### What Goes Where — Decision Rule

```text
Behavior / persona / output format / constraints → system_instruction
Few-shot examples (Q/A pairs)                   → contents[] with alternating user/model roles
Actual query                                    → Last turn in contents[] with role="user"
```

---

## 2. Deterministic Results

The Gemini API is **not deterministic by default**. Even with `temperature=0`, minor non-determinism can occur across infrastructure versions. For reproducible outputs in testing and CI pipelines, use **both** `temperature=0` and `seed`.

### Parameters for Determinism

| Parameter | Value for Determinism | Notes |
|---|---|---|
| `temperature` | `0.0` | Greedy decoding — always picks the highest-probability token |
| `seed` | Any fixed integer (e.g., `42`) | Pins the random seed; same seed + temperature → same output |

> **Caveat:** Identical outputs are not guaranteed across model version updates or infrastructure changes. Do not rely on determinism for security-critical operations.

### Code Example — Deterministic Output

```python
from google import genai
from google.genai import types

client = genai.Client()

config = types.GenerateContentConfig(
    temperature=0.0,
    seed=42,
    system_instruction="Classify the sentiment: output exactly 'positive' or 'negative'."
)

# Calling this twice with the same inputs yields the same result
response1 = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=config,
    contents="This product is absolutely terrible."
)
response2 = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=config,
    contents="This product is absolutely terrible."
)

assert response1.text == response2.text  # True (within same model version)
print(response1.text)  # → "negative"
```

### When Determinism Matters

| Use Case | Recommended Setting |
|---|---|
| Classification/extraction at scale | `temperature=0, seed=42` |
| LLM-as-judge evaluation | `temperature=0, seed=42` |
| Creative content (ads, copy) | `temperature=0.9–1.4` (no seed) |
| Code generation | `temperature=0.2–0.4` |
| Brainstorming / ideation | `temperature=1.0–1.8` |

---

## 3. Generation Parameters

All parameters live inside `GenerateContentConfig`. **Not all parameters are supported by all models** — check `getModel()` for model-specific defaults.

### 3.1 `temperature` — Randomness Control

**Range:** `0.0 – 2.0`  **Default:** model-specific (typically 1.0 for chat models)

Controls the probability distribution over the vocabulary. Lower = more predictable, higher = more creative/random.

| Value | Effect | Output Character |
|---|---|---|
| `0.0` | Greedy — always picks the most probable token | Deterministic, repetitive for creative tasks |
| `0.2–0.4` | Focused, factual | Technical writing, code, structured extraction |
| `0.7–1.0` | Balanced | General-purpose generation, chat |
| `1.2–1.6` | Creative | Ad copy, brainstorming, storytelling |
| `1.8–2.0` | Very high randomness | Experimental; risk of incoherence |

```python
# Focused structured output
config = types.GenerateContentConfig(temperature=0.2)

# Creative ad copy
config = types.GenerateContentConfig(temperature=1.3)
```

> **Anti-pattern:** Using `temperature=0` for creative tasks → repetitive, robotic output.  
> **Anti-pattern:** Using `temperature>1.0` for classification → hallucinations and format breaks.

---

### 3.2 `top_p` — Nucleus Sampling

**Range:** `0.0 – 1.0`  **Default:** model-specific (typically 0.95)

Restricts the token selection pool to the smallest set of tokens whose cumulative probability exceeds `top_p`. A lower value makes output more conservative; higher allows rarer tokens.

| Value | Effect |
|---|---|
| `0.5` | Very conservative — only high-probability tokens |
| `0.9` | Standard creative quality |
| `0.95` | Default for most models |
| `1.0` | No nucleus filtering; all tokens eligible |

> **Combined with `top_k`:** Gemini uses both Top-k and Top-p simultaneously. The token must pass **both** filters to be eligible for sampling.

```python
config = types.GenerateContentConfig(
    temperature=1.0,
    top_p=0.9  # Restrict to high-probability tokens even at temp=1.0
)
```

---

### 3.3 `top_k` — Top-K Sampling

**Range:** integer ≥ 1  **Default:** model-specific

Hard-limits the candidate token pool to the K most probable tokens regardless of their probability values.

| Value | Effect |
|---|---|
| `1` | Equivalent to greedy; only top-1 token selected |
| `10–40` | Conservative, focused |
| `40` | Typical default |
| `100+` | Wide range; similar to no top-k filtering |

> **Note:** Some Gemini models do not expose `top_k` as a settable parameter (the `topK` attribute in the model spec will be empty). Use `top_p` instead for those models.

```python
config = types.GenerateContentConfig(
    temperature=0.8,
    top_k=40,
    top_p=0.95
)
```

---

### 3.4 `thinking_level` — Reasoning Control (Gemini 3.x)

Gemini 3 models use internal chain-of-thought before producing output. **Thinking tokens are billed as output tokens.** Control them explicitly — the default is `"high"`, which is expensive for simple tasks.

| Level | Reasoning Depth | Latency | Cost | Best For |
|---|---|---|---|---|
| `"minimal"` | Near zero (model may still think slightly) | Fastest | Lowest | Classification, extraction, creative generation |
| `"low"` | Light | Fast | Low | Summarization, simple Q&A, ad copy generation |
| `"medium"` | Moderate | Medium | Medium | General analysis, structured reports |
| `"high"` | Deep — **model default** | Slowest | Highest | Complex reasoning, code review, multi-step research |

> **Cannot disable thinking** on Gemini 3 Pro. `"minimal"` on Gemini 3 Flash is the closest to off.

```python
# Ad image prompt generation — minimal thinking needed
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="minimal")
)

# Multi-scene video script generation — medium is enough
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="medium")
)

# Complex campaign analysis — use high (or leave default)
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="high")
)
```

> **Cost warning:** At default `"high"` thinking, a batch of 1,000 calls can generate millions of hidden thinking tokens. Always profile with `thoughtsTokenCount` before scaling.

---

## 4. Parameter Decision Cheat-Sheet

| Task Type | temperature | top_p | top_k | thinking |
|---|---|---|---|---|
| Classification / sentiment | 0.0 | default | default | off or minimal |
| JSON / structured extraction | 0.1–0.2 | 0.9 | 40 | off or minimal |
| Summarization | 0.3–0.5 | 0.95 | 40 | low |
| Chat / Q&A | 0.7–1.0 | 0.95 | 40 | low–medium |
| Code generation | 0.2–0.4 | 0.9 | 40 | medium |
| Ad copy / creative writing | 1.0–1.4 | 0.95 | 100 | off |
| Complex reasoning / research | 0.3–0.6 | 0.95 | default | high or budget 8192+ |
| **Imagen 4** — product variation batch | 0.8–1.0 | 0.95 | default | N/A |
| **Imagen 4** — reproducible hero shot | 0.0–0.2 + seed | 0.9 | default | N/A |
| **Nano Banana 2** — iterative ad editing | 0.7–1.0 | 0.95 | default | N/A |
| **Veo 3.1** — scripted product video | 0.3–0.5 | 0.9 | default | N/A |
| **Veo 3.1** — creative/exploratory clip | 1.0–1.4 | 0.95 | default | N/A |

---

## 4b. Creative Modalities — Parameter Impact

The parameters above affect text generation. For image and video models they still apply, but the *perceptual* effect differs significantly. If you are working with a creative pipeline, read this section before tuning.

> For full prompting guides, see `imagen-prompting-guide.md`, `nano-banana-prompting-guide.md`, and `veo-prompting-guide.md`.

### Imagen 4

`temperature` controls **variation between image candidates** when `number_of_images > 1`.

| temperature | Perceptual Effect | When to Use |
|---|---|---|
| `0.0` | Near-identical images across runs; minimal color/texture variation | Reproducible hero shots, brand-locked assets |
| `0.5–0.8` | Moderate variation in composition, props, and color palette | A/B creative testing (3–5 variants) |
| `1.0–1.2` | Strong variation; same scene, very different executions | Exploratory ideation, mood boards |

**`seed` on Imagen:** Set `seed` alongside any `temperature` value to pin a specific variant for reproducibility. Same seed = same image, useful when iterating on a prompt while keeping the base composition locked.

```python
# Generate 4 creative variants of a product shot, then pin the best one
config_explore = types.GenerateImagesConfig(number_of_images=4, temperature=1.0)
config_locked  = types.GenerateImagesConfig(number_of_images=1, temperature=0.2, seed=7341)
```

**`top_p` on Imagen:** Lowering `top_p` (e.g., to 0.85) narrows stylistic choices — fewer unexpected elements appear in the scene. Useful for brand safety (keeps backgrounds clean, prevents model from adding unexpected objects).

---

### Nano Banana 2 (Gemini image generation via generate_content)

Nano Banana 2 uses the standard `GenerateContentConfig`, so all text-generation parameters apply.

| temperature | Perceptual Effect |
|---|---|
| `0.4–0.6` | Conservative edits — model stays close to the reference; safe for brand consistency |
| `0.8–1.0` | Balanced — natural variation in background, lighting, minor reComposition |
| `1.2–1.5` | Bold stylistic shifts — background, color grading, mood can change significantly |

**Key distinction from Imagen:** Nano Banana uses conversational context. A high temperature in turn 3 of a chat session doesn't just vary the image — it can cause the model to reinterpret earlier context. **For character/product consistency across turns, use `temperature=0.6–0.8`.**

```python
# Turn 1: establish product at moderate temp
# Turn 2: iterative edit — lower temp to stay close to Turn 1 result
chat_config = types.GenerateContentConfig(
    response_modalities=["TEXT", "IMAGE"],
    temperature=0.7   # balanced for editing without drifting
)
```

---

### Veo 3.1

Veo 3.1 generation parameters influence **narrative variation and shot diversity**, not just token output.

| temperature | Perceptual Effect |
|---|---|
| `0.2–0.4` | High fidelity to prompt; exact camera motion, precise scene composition; recommended for scripted ad videos |
| `0.6–0.9` | Natural motion variation; same camera directive but model interprets lighting/pace slightly differently each run |
| `1.0–1.4` | Model takes creative liberties — unexpected shot transitions, camera reinterpretation; good for exploratory briefs |

**`seed` on Veo:** Critical for iterative video pipelines. When editing a prompt (e.g., changing dialogue while keeping scene locked), fix `seed` to isolate the variable you are testing.

```python
# Scripted product video — deterministic
veo_config_scripted = types.GenerateContentConfig(temperature=0.3, seed=1042)

# Exploratory mood reel — creative variation
veo_config_explore  = types.GenerateContentConfig(temperature=1.1)
```

**`thinking_level` on Veo prompts (Gemini 3.x only):** Veo prompt generation via a text model (before calling the Veo API) benefits from `thinking_level="low"` — fast, sufficient for structured prompt formatting. Reserve `thinking_level="high"` for complex multi-scene script construction.

---

## 5. Full Config Example (All Parameters)

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash",  # Latest Gemini 3.x — preferred for production
    config=types.GenerateContentConfig(
        # Prompt structure
        system_instruction="You are a senior data analyst. Output JSON only.",

        # Sampling parameters
        temperature=0.1,       # Focused, deterministic-ish
        top_p=0.9,
        top_k=40,
        seed=42,               # For reproducibility in testing

        # Token limits
        max_output_tokens=512,
        stop_sequences=["```"],  # Stop if model tries to add a code fence

        # Thinking (Gemini 3.x) — use thinking_level, not thinking_budget
        thinking_config=types.ThinkingConfig(thinking_level="minimal"),  # Off for extraction

        # Structured output enforcement
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]},
                "confidence": {"type": "number"}
            },
            "required": ["sentiment", "confidence"]
        }
    ),
    contents="Analyze: 'The product exceeded my expectations in every way.'"
)
print(response.text)
# → {"sentiment": "positive", "confidence": 0.98}
```
