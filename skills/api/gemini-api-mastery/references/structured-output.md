# Gemini API — Structured Output (JSON Mode)

Source: [JSON Mode Docs](https://ai.google.dev/gemini-api/docs/json-mode) | [GenerationConfig](https://ai.google.dev/api/generate-content#generationconfig)

---

## Why Use Structured Output?

Asking a model to "respond in JSON" in a system prompt is **unreliable** — it breaks under high temperature, long context, and model updates. The `response_mime_type` + `response_schema` parameters enforce JSON at the API level: the model is **constrained** to produce valid JSON matching your schema. No parsing guard-rails needed.

---

## Method 1 — JSON Mode (no schema)

Guarantees valid JSON. Does **not** enforce field names or types.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=types.GenerateContentConfig(
        system_instruction="Extract all product names mentioned.",
        response_mime_type="application/json"
    ),
    contents="I bought a Kindle, an AirPods Pro, and a Dyson V15."
)
print(response.text)
# → {"products": ["Kindle", "AirPods Pro", "Dyson V15"]}
```

---

## Method 2 — Schema-Enforced JSON (recommended)

Guarantees valid JSON **and** enforces field names, types, enums, and required fields.

```python
from google import genai
from google.genai import types

client = genai.Client()

# Define schema inline (subset of OpenAPI / JSON Schema)
sentiment_schema = {
    "type": "object",
    "properties": {
        "sentiment":  {"type": "string", "enum": ["positive", "negative", "neutral"]},
        "confidence": {"type": "number"},
        "reason":     {"type": "string"}
    },
    "required": ["sentiment", "confidence"]
}

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a sentiment analysis engine.",
        response_mime_type="application/json",
        response_schema=sentiment_schema
    ),
    contents="The delivery was late but the product itself is great."
)

import json
result = json.loads(response.text)
print(result["sentiment"])    # → "positive"
print(result["confidence"])   # → 0.72
```

---

## Method 3 — Pydantic Schema (Python SDK)

Pass a Pydantic model directly. The SDK converts it to the JSON Schema automatically.

```python
from pydantic import BaseModel
from typing import Literal
from google import genai
from google.genai import types

class AdAnalysis(BaseModel):
    hook_rating:    int              # 1–10
    cta_present:    bool
    tone:           Literal["formal", "casual", "urgent"]
    key_message:    str

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-preview",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=AdAnalysis
    ),
    contents="LIMITED TIME OFFER! Buy now and save 50%. Don't miss this deal."
)

analysis = AdAnalysis.model_validate_json(response.text)
print(analysis.cta_present)  # → True
print(analysis.tone)         # → "urgent"
```

---

## Schema Capability Reference

| Feature | Supported |
|---|---|
| `type`: object, array, string, number, boolean | ✅ |
| `enum` (string or number values) | ✅ |
| `required` fields | ✅ |
| `$ref` and `$defs` (schema references) | ✅ |
| Nested objects and arrays | ✅ |
| `anyOf` / `oneOf` | ✅ (treated identically) |
| `minimum` / `maximum` | ✅ |
| `minItems` / `maxItems` | ✅ |
| `allOf` | ❌ Not supported |
| Cyclic references | ⚠️ Unrolled to limited depth |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using `response_schema` without `response_mime_type` | Always set both together |
| Asking for JSON in `system_instruction` only | Unreliable; use `response_mime_type` instead |
| Using `allOf` in schema | Not supported; restructure using `properties` |
| Setting `temperature>0.5` for strict extraction | Use `temperature=0.0–0.2` for extraction tasks |
| Not setting `response_schema` for high-stakes pipelines | Without schema, field names are not enforced |

---

## Batch Extraction Pattern (Pipeline)

```python
# Extract structured data from 1,000 ad copies
results = []
for ad_copy in ad_copies:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        config=types.GenerateContentConfig(
            temperature=0.0,
            seed=42,
            response_mime_type="application/json",
            response_schema=AdAnalysis,
            thinking_config=types.ThinkingConfig(thinking_level="minimal")
        ),
        contents=ad_copy
    )
    results.append(AdAnalysis.model_validate_json(response.text))
```
