# Meta Ads API — Data Fetching & Analysis Reference

> Reference: [Insights API Docs](https://developers.facebook.com/docs/marketing-api/insights)

---

## Available Levels of Insights

All insight queries are scoped to a specific object level. Swap the object ID in the URL:

| Level | Endpoint |
|---|---|
| Account | `GET /act_{ad_account_id}/insights` |
| Campaign | `GET /{campaign_id}/insights` |
| Ad Set | `GET /{adset_id}/insights` |
| Ad | `GET /{ad_id}/insights` |

---

## Key Parameters

| Parameter | Description | Example |
|---|---|---|
| `fields` | Comma-separated metrics to return | `impressions,clicks,spend,cpm,ctr` |
| `date_preset` | Named date range | `last_30d`, `last_7d`, `this_month` |
| `time_range` | Custom ISO date range | `{"since":"2025-01-01","until":"2025-01-31"}` |
| `time_increment` | Day-by-day vs. aggregate | `1` (daily), `all` (total) |
| `breakdowns` | Segmentation dimensions | `age`, `gender`, `placement`, `device_platform` |
| `level` | Override the default level | `campaign`, `adset`, `ad` |
| `limit` | Pagination size | `500` |

---

## Conversion Math — Parsing the `actions` Field

Conversion metrics (purchases, leads, add-to-carts) are **not returned as top-level fields**. They are nested inside the `actions` array:

```python
def get_purchases(insights_row: dict) -> int:
    """Extracts purchase count from a Meta Insights row."""
    actions = insights_row.get('actions', [])
    for action in actions:
        if action.get('action_type') == 'purchase':
            return int(action.get('value', 0))
    return 0

def get_purchase_value(insights_row: dict) -> float:
    """Extracts purchase value (revenue) from a Meta Insights row."""
    action_values = insights_row.get('action_values', [])
    for av in action_values:
        if av.get('action_type') == 'purchase':
            return float(av.get('value', 0.0))
    return 0.0
```

---

## Asynchronous Insights (for Large Requests)

For historical data (90+ days), multiple campaigns, or breakdown combinations, use **async requests** to avoid Gateway Timeouts:

```python
import requests
import time

def fetch_insights_async(ad_account_id, access_token, params):
    """
    Submits an async insights job, polls until complete, then retrieves results.
    """
    base = f"https://graph.facebook.com/v21.0/act_{ad_account_id}/insights"
    
    # Step 1: Submit asynchronous job (POST, not GET)
    submit_resp = requests.post(base, params={
        **params,
        "access_token": access_token
    })
    submit_resp.raise_for_status()
    report_run_id = submit_resp.json()['report_run_id']
    
    # Step 2: Poll for completion
    while True:
        status_resp = requests.get(
            f"https://graph.facebook.com/v21.0/{report_run_id}",
            params={"access_token": access_token}
        )
        status = status_resp.json()
        
        if status['async_status'] == 'Job Completed':
            break
        elif status['async_status'] == 'Job Failed':
            raise RuntimeError(f"Async insights job failed: {status}")
        
        time.sleep(5)  # Poll every 5 seconds

    # Step 3: Retrieve results
    results_resp = requests.get(
        f"https://graph.facebook.com/v21.0/{report_run_id}/insights",
        params={"access_token": access_token, "limit": 500}
    )
    return results_resp.json().get('data', [])
```

---

## System Users for Automated / Long-Running Pipelines

For automation pipelines (cron jobs, dashboards) that cannot rely on a user being logged in:

1. In **Business Manager → Settings → System Users**, create a System User.
2. Assign the relevant Ad Accounts to it with the appropriate role (`Analyst` for read, `Advertiser` for write).
3. Generate a **System User Access Token** — these do not expire like regular User Access Tokens.

---

## Common Data Analysis Patterns

| Goal | Approach |
|---|---|
| Daily spend trend | `time_increment=1`, `fields=spend,impressions` |
| ROAS by campaign | `level=campaign`, `fields=spend,purchase_roas` |
| Audience breakdown | `breakdowns=age,gender`, `fields=impressions,clicks,ctr` |
| Placement performance | `breakdowns=publisher_platform,placement`, `fields=spend,cpm,ctr` |
| Top 10 ads by spend | `level=ad`, `fields=ad_name,spend`, sort client-side |
