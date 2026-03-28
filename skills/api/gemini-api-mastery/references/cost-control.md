# Gemini API — Cost Control Guide

Source: [Official Pricing](https://ai.google.dev/gemini-api/docs/pricing) | [Context Caching Docs](https://ai.google.dev/gemini-api/docs/caching)

---

## Strategy Overview

| Strategy | Discount | When to Use |
|---|---|---|
| **Model Routing** | Up to 90%+ | Always — choose cheapest capable model |
| **Batch API** | 50% off all tokens | Async workloads (no real-time requirement) |
| **Context Caching** | Up to 90% on input | Same large context reused across many prompts |
| **Dynamic Thinking Budget** | Varies | When using reasoning models (Gemini 2.5+) |
| **Token Counting** | Preventive | Before expensive calls to catch prompt bloat |

---

## 1. Model Routing (highest leverage)

Most teams pay 5–10× too much by defaulting to Pro models.

```
Task Type                         → Recommended Model
─────────────────────────────────────────────────────
Classification / extraction       → gemini-3.1-flash-lite-preview
General reasoning / summarization → gemini-3.1-flash-preview
Complex reasoning / multimodal    → gemini-3.1-pro-preview
Production (no preview risk)      → gemini-2.5-flash (stable)
```

**Rule:** Only upgrade a model when you have measured the quality gap. Don't guess.

---

## 2. Batch API (50% Official Discount)

Use the Batch API for any non-real-time task. All batch requests are charged at **50% of standard pricing**. Most batches complete within 1 hour.

**Good batch use cases:**

- Bulk content generation (product descriptions, keywords)
- Dataset evaluation or LLM-as-judge scoring
- Nightly report generation
- Batch document summarization

```python
# Batch requests run async — do NOT use for user-facing real-time features
response = client.models.batch_generate_content(
    model="gemini-3.1-flash-lite-preview",
    requests=[
        {"contents": f"Summarize this: {doc}"}
        for doc in documents
    ]
)
# Poll for results — batches are asynchronous
```

---

## 3. Context Caching (up to 90% reduction on input)

When the same large prefix (system prompt, document, tool definitions) is sent in many requests, cache it once and pay only for new tokens.

| Cache Event | Cost |
|---|---|
| Cache write | Standard input price |
| Cache read | ~10% of standard input price |
| Minimum size for efficiency | >32K tokens |
| Availability | Paid tier only |

```python
# Create a cached context (e.g., a 200-page product manual)
cache = client.caches.create(
    model="gemini-3.1-pro-preview",
    contents=["<entire product manual content>"],
    ttl="600s"   # 10-minute TTL
)

# Use cached context in subsequent queries
response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="What is the battery replacement procedure?",
    cached_content=cache.name
)
```

**Best practice:** Cache stable, large prefixes. The cache must be an exact prefix match — vary only the suffix (the user query).

---

## 4. Dynamic Thinking Budget

Reasoning models (Gemini 2.5 Pro, Gemini 3.1 Pro) charge for "thinking tokens." Without a budget cap, a complex prompt can generate thousands of hidden thinking tokens.

```python
response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Classify this review as positive or negative: 'Great product!'",
    generation_config={
        "thinking_config": {
            "thinking_budget": 512  # low budget for simple tasks
        }
    }
)
```

**Rule of thumb:**

- Simple tasks (classification, extraction): thinking_budget 256–512
- Medium tasks (analysis, draft): thinking_budget 1024–4096
- Hard tasks (research synthesis, code review): uncapped or 8192+

---

## 5. Token Counting Before Calls

Use before expensive batch jobs or large-context calls to prevent runaway costs.

```python
token_count = client.models.count_tokens(
    model="gemini-3.1-pro-preview",
    contents=my_large_prompt
)
print(f"Estimated tokens: {token_count.total_tokens}")

# Abort or truncate if above threshold
if token_count.total_tokens > 50_000:
    raise ValueError("Prompt too large — truncate before sending.")
```

---

## Cost Stacking: Maximum Savings

Combine strategies for compounding effect:

```
Model Routing → Batch API → Context Caching
  ~90% cheaper    50% off      90% off cached tokens
```

For example, a batch of 1,000 requests all sharing the same 100K-token system prompt:

- Without optimization: 1,000 × 100K = 100M tokens billed
- With caching (batch-compatible): ~10M tokens billed (10% cache reads)
- With batch discount: ~5M tokens billed (50% off)
