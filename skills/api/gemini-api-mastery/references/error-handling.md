# Gemini API — Error Handling & Rate Limits

Source: [Error Codes](https://ai.google.dev/gemini-api/docs/troubleshooting) | [Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits)

---

## Error Code Reference

| HTTP Code | gRPC Code | Error | Cause | Fix |
|---|---|---|---|---|
| 400 | INVALID_ARGUMENT | Bad request | Malformed payload, unsupported parameter, schema error | Check request body and schema |
| 400 | FAILED_PRECONDITION | Free tier blocking | Billing not enabled, feature not available on free tier | Enable billing or upgrade to paid |
| 403 | PERMISSION_DENIED | API key invalid or restricted | Wrong key, key missing required APIs | Verify key in Google AI Studio |
| 404 | NOT_FOUND | Model not found | Wrong model ID or model not available in region | Check `model-reference.md` for correct IDs |
| 429 | RESOURCE_EXHAUSTED | Rate limit hit | Too many requests per minute or per day | Implement exponential backoff (see below) |
| 500 | INTERNAL | Server error | Transient infrastructure issue | Retry with backoff; report if persistent |
| 503 | UNAVAILABLE | Service overloaded | High demand | Retry with backoff |

---

## Rate Limit Tiers (March 2026)

Rate limits vary by **model** and **tier**. Preview models have lower limits than stable models.

| Tier | RPM (Requests/Min) | TPM (Tokens/Min) | RPD (Requests/Day) |
|---|---|---|---|
| Free | 15 | 1M | 1,500 |
| Paid — Flash-Lite | 4,000 | 4M | Unlimited |
| Paid — Flash | 2,000 | 4M | Unlimited |
| Paid — Pro | 1,000 | 4M | Unlimited |
| Preview models | Lower (model-specific) | Lower | Lower |

> Always check the [official rate limits page](https://ai.google.dev/gemini-api/docs/rate-limits) — these change as models graduate from preview.

---

## Exponential Backoff Pattern (Production)

Never hard-retry immediately on 429. Use exponential backoff with jitter.

```python
import time
import random
from google import genai
from google.api_core.exceptions import ResourceExhausted, ServiceUnavailable, InternalServerError

client = genai.Client()

def generate_with_retry(model: str, contents, config=None, max_retries: int = 5):
    """Generate content with exponential backoff on transient errors."""
    retryable = (ResourceExhausted, ServiceUnavailable, InternalServerError)

    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=config
            )
        except retryable as e:
            if attempt == max_retries - 1:
                raise  # exhausted retries
            wait = (2 ** attempt) + random.uniform(0, 1)  # jitter
            print(f"Attempt {attempt + 1} failed ({type(e).__name__}). Retrying in {wait:.1f}s...")
            time.sleep(wait)
        except Exception:
            raise  # non-retryable errors bubble immediately

# Usage
response = generate_with_retry(
    model="gemini-3.1-flash-lite-preview",
    contents="Classify: Great product!"
)
```

---

## Error Handling for Schema Violations

When using `response_schema`, the API can still return a `RECITATION` or `SAFETY` finish reason instead of JSON on some inputs. Always check `finish_reason` before `json.loads()`.

```python
import json
from google.genai.types import FinishReason

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=my_schema
    ),
    contents=user_input
)

candidate = response.candidates[0]

if candidate.finish_reason != FinishReason.STOP:
    # SAFETY, RECITATION, MAX_TOKENS, etc.
    print(f"Generation stopped: {candidate.finish_reason}")
    result = None
else:
    result = json.loads(response.text)
```

---

## Quota Management Checklist

- [ ] Set `max_output_tokens` on every request to cap token spend
- [ ] Use `client.models.count_tokens()` before expensive batch calls
- [ ] Route classification/extraction to `gemini-3.1-flash-lite-preview` (highest RPM)
- [ ] Use Batch API for non-real-time work (no rate limit impact, 50% discount)
- [ ] Monitor `usage_metadata.total_token_count` per response
- [ ] Set up billing alerts in Google Cloud Console
- [ ] Never share API keys in code — use environment variables or Secret Manager

---

## Common Error Mistakes

| Mistake | Fix |
|---|---|
| Hard-retry immediately on 429 | Use exponential backoff with jitter |
| Using `model="gemini-3.1-pro-preview"` for all tasks | Route cheap tasks to Flash-Lite (higher RPM) |
| Not checking `finish_reason` before parsing JSON | Safety/recitation blocks return non-JSON text |
| Passing API key in URL params | Always use `x-goog-api-key` header or env var |
| Silent failure on 500 errors | Log and alert; 500s are transient but indicate infra issues |
