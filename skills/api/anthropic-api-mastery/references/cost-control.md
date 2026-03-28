# Claude API — Cost Control Guide

Source: [Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing) | [Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | [Models & Pricing](https://docs.anthropic.com/en/docs/about-claude/models/overview)

---

## Strategy Overview

| Strategy | Discount | Effort | When to Use |
|---|---|---|---|
| **Model Routing** | Up to 80%+ | Low | Always — route by task complexity |
| **Message Batches API** | 50% off all tokens | Low | Any non-real-time pipeline |
| **Prompt Caching** | Up to 90% on cached input | Medium | Same large context repeated across calls |
| **Stack Caching + Batching** | >90% combined | Medium | Maximum savings for async pipelines |
| **Context Pruning** | Variable | Low | Long multi-turn conversations |

---

## 1. Model Routing (always do this first)

| Task | Model | Savings vs. Default |
|---|---|---|
| Classification, extraction, routing | `claude-haiku-4-5-20251001` | 5× cheaper than Sonnet |
| Coding, copy, analysis, agents | `claude-sonnet-4-6` | Baseline |
| Max accuracy, 128K output, long agentic sessions | `claude-opus-4-6` | ~1.7× more than Sonnet |

```python
def route_model(task_type: str) -> str:
    routing = {
        "classification": "claude-haiku-4-5-20251001",
        "extraction": "claude-haiku-4-5-20251001",
        "summarization": "claude-haiku-4-5-20251001",
        "copywriting": "claude-sonnet-4-6",
        "coding": "claude-sonnet-4-6",
        "deep_analysis": "claude-opus-4-6",
        "agentic": "claude-opus-4-6",
    }
    return routing.get(task_type, "claude-sonnet-4-6")
```

---

## 2. Message Batches API (50% discount — official)

All batch usage is charged at **50% of standard API prices**. Batches complete in under 1 hour typically.

**Use for:** content pipelines, bulk evaluation, nightly reports, dataset processing.
**Do NOT use for:** anything user-facing or requiring real-time response.

```python
import anthropic

client = anthropic.Anthropic()

# Create a batch
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": f"item-{i}",  # use meaningful IDs — results are not ordered
            "params": {
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 512,
                "messages": [{"role": "user", "content": item_text}]
            }
        }
        for i, item_text in enumerate(items)
    ]
)

# Poll for completion
import time
while True:
    result = client.messages.batches.retrieve(batch.id)
    if result.processing_status == "ended":
        break
    time.sleep(30)

# Retrieve results
for result in client.messages.batches.results(batch.id):
    if result.result.type == "succeeded":
        print(result.custom_id, result.result.message.content[0].text)
```

**Best practices:**

- Use meaningful `custom_id` values — results return out of order.
- Dry-run a single request with the Messages API first to catch validation errors.
- Break very large datasets into multiple batches of ≤10,000 requests.

---

## 3. Prompt Caching (up to 90% reduction on cached input)

Cache large static context (system prompts, brand guidelines, tool definitions, documents) so you only pay full price once. Cache reads cost ~10% of base input price.

| Cache Event | Cost |
|---|---|
| Cache write | Base input price + 25% |
| Cache read | 10% of base input price |
| Default TTL | 5 minutes |
| Break-even point | After first cache read |

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "[Your full brand guidelines — 10,000 tokens]",
            "cache_control": {"type": "ephemeral"}  # mark for caching
        },
        {
            "type": "text",
            "text": "You are a direct-response copywriter."   # not cached (small)
        }
    ],
    messages=[{"role": "user", "content": "Write a hero headline for Product X."}]
)

# Check cache performance in the response
usage = response.usage
print(f"Cache read tokens: {usage.cache_read_input_tokens}")
print(f"Cache write tokens: {usage.cache_creation_input_tokens}")
```

**Rules for effective caching:**

1. Put cacheable content at the **start** of the prompt — the prefix must be identical across calls.
2. Only the suffix (user query) should vary.
3. Large, stable context (>1,000 tokens) yields the best cost savings.
4. Monitor `cache_read_input_tokens` in responses to confirm the cache is hitting.

---

## 4. Stack Caching + Batching (Maximum Savings)

Prompt Caching and Batch API discounts **stack** — they are applied to different parts of the cost:

```
Without optimization:
  1,000 requests × 50K token system prompt = 50M input tokens billed

With Prompt Caching (batch):
  ~30–98% of requests hit cache → ~5–35M tokens at 10% price
  + uncached tokens at standard price

With Batch API on top:
  All token costs × 50%

Combined effective reduction: >90% for cache-heavy workloads
```

From the official docs, cache hit rates in batches range from **30%–98%** depending on traffic patterns.

To maximize cache hits in batches:

1. Include identical `cache_control` blocks in every request.
2. Maintain steady request volume so cache entries stay alive (5-min TTL).
3. Structure requests to share as much cached prefix as possible.

---

## 5. Context Pruning

Multi-turn conversations silently accumulate tokens. Prune aggressively:

- Only send the **last N turns** relevant to the current task.
- Summarize older history into a `<conversation-summary>` block rather than sending verbatim turns.
- For document Q&A, don't resend the full document every turn — use Prompt Caching instead.

```python
def build_messages(history: list, max_turns: int = 5) -> list:
    """Keep only the most recent N turns."""
    return history[-max_turns * 2:]  # each turn = 2 messages (user + assistant)
```
