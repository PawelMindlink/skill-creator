# Meta Ads API — Error Handling Reference

> Rule: **Never trust the HTTP status code alone.** Always parse the full JSON payload.

## Error Response Structure

Every error from the Meta Marketing API has this shape:

```json
{
  "error": {
    "message": "...",
    "type": "OAuthException",
    "code": 190,
    "error_subcode": 463,
    "error_user_title": "...",
    "error_user_msg": "...",
    "fbtrace_id": "AaBbCcDdEe",
    "error_data": {
      "blame_field_specs": [["daily_budget"]]
    }
  }
}
```

**Always log `fbtrace_id`** — it is required when submitting bug reports to Meta. Without it, support cannot trace the request.

---

## Error Classification & Handling Rules

| Category | Codes | Action |
|---|---|---|
| **Rate Limit** | 4, 17, 613, 80000 | Exponential backoff (do NOT refresh token) |
| **Auth / Token Expired** | 190, subcode 463/467 | Refresh token — do NOT retry |
| **Invalid Parameter** | 100, subcode 33 | Check `blame_field_specs` — often a permission or ID type mismatch |
| **Object Not Found / Deleted** | 803 | Verify the resource exists before retrying |
| **Server Error** | 2, 1, 5xx | Exponential backoff with short initial delay |
| **Policy / Business Violation** | 1870034, 1815010, 1815694 | Requires human action — surface `error_user_msg` to the user |

---

## Rate Limiting Deep Dive (BUC System)

The Marketing API uses a **Score-Based Business Use Case (BUC)** rate limit, completely separate from the standard Graph API:

- **Read calls**: 1 point. **Write calls**: 3 points.
- **Development tier**: Max 60 pts → 300s block if exceeded.
- **Standard/Advanced tier**: Max ~9,000 pts → 60s block if exceeded.
- Monitor the **`X-Business-Use-Case-Usage`** response header to track quota consumption in real time.

**Mitigation strategies:**

1. Implement exponential backoff starting at 60s for codes 17/613, starting at 5s for code 4.
2. Batch multiple reads into a single `/` batch request (up to 50 calls per batch).
3. Use `POST` (async) on the `/insights` edge instead of `GET` for large data requests.
4. Apply for **Advanced Access** via App Dashboard → Products → Marketing API to raise limits.

---

## Silent & Misleading HTTP 400 Errors

Code `100` with `subcode 33` ("Unsupported post request") **does NOT always mean a syntax error.** True cause is usually one of:

- Passing a Facebook **Page ID** where an Instagram **Business Account ID** is required.
- Missing token scope (`ads_read`, `ads_management`, `business_management`).
- The targeted Campaign / Ad Set / Ad was **deleted** or belongs to a **different account**.

**Diagnosis protocol when user reports a 400:**

1. Ask for the full `error_data` JSON — not just the HTTP status.
2. Extract `blame_field_specs` (see code below).
3. Cross-reference with token permissions in the [Graph API Explorer](https://developers.facebook.com/tools/explorer).

---

## Reference Code — Resilient Meta API Request (Python)

```python
import requests
import time
import json

RATE_LIMIT_CODES = {4, 17, 613, 80000}
AUTH_ERROR_CODES = {190}
RETRY_ERROR_CODES = {1, 2}  # Transient server errors

def make_meta_api_request(url, params=None, payload=None, max_retries=3):
    """
    Makes a Meta Graph/Marketing API request with:
    - Exponential backoff for rate limits and server errors
    - Deep extraction of blame_field_specs for validation errors
    - Auth error detection without retry
    """
    for attempt in range(max_retries):
        response = requests.request(
            "POST" if payload else "GET",
            url,
            params=params,
            json=payload
        )

        if response.status_code == 200:
            return response.json()

        error_res = response.json().get('error', {})
        error_code = error_res.get('code')
        fbtrace_id = error_res.get('fbtrace_id', 'unknown')

        print(f"[Meta API] Error code={error_code} fbtrace_id={fbtrace_id}")

        # Rate limiting — backoff and retry
        if error_code in RATE_LIMIT_CODES:
            wait = 60 * (2 ** attempt)
            print(f"Rate limited (Code {error_code}). Waiting {wait}s...")
            time.sleep(wait)
            continue

        # Transient server errors — short backoff and retry
        if error_code in RETRY_ERROR_CODES or response.status_code >= 500:
            wait = 5 * (2 ** attempt)
            print(f"Server error. Retrying in {wait}s...")
            time.sleep(wait)
            continue

        # Auth errors — do NOT retry, surface immediately
        if error_code in AUTH_ERROR_CODES:
            raise PermissionError(
                f"Authentication Error (Code {error_code}): "
                "Access token is expired or invalid. "
                "Refresh via Graph API Explorer or your token refresh flow."
            )

        # Validation errors — extract blame_field_specs
        raw_data = error_res.get('error_data', '{}')
        error_data = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
        blame = error_data.get('blame_field_specs', [])
        user_msg = error_res.get('error_user_msg', '')

        if blame:
            raise ValueError(
                f"Validation failed on fields: {blame}\n"
                f"Actionable message: {user_msg}\n"
                f"fbtrace_id: {fbtrace_id}"
            )

        raise RuntimeError(f"Meta API Error: {error_res}")

    raise RuntimeError(f"Max retries ({max_retries}) exceeded.")
```

---

## Troubleshooting Quick Reference

| Symptom | Likely Cause | Fix |
|---|---|---|
| 400 + "Unsupported post request" | Wrong ID type (Page vs. IG Account) | Check which endpoint expects which ID type |
| 429 — no error code in body | Hit BUC limit before custom codes triggered | Add `X-Business-Use-Case-Usage` header monitoring |
| 190 subcode 463 | Token expired | Generate a new long-lived or system user token |
| 1870034 | Custom Audience TOS not accepted | User must accept terms in Business Manager |
| 1815010 | Billing not configured | Set up payment method in the Ad Account |
| Empty `blame_field_specs` | `error_data` returned as string, not dict | Apply `json.loads()` guard (see code above) |
