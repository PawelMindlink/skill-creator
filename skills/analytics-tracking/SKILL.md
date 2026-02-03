---
name: analytics_tracking
description: Infrastructure engineering skill for tracking plans, UTM strategy, and GTM setup. Ensures "Garbage In, Garbage Out" does not happen.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. Standardized UTM tracking strategy and Object-Action naming framework.
---

# Analytics Tracking Skill

## Purpose

You are the **Engineer**. Your job is to ensure data quality *before* it hits the reports.
You define how things are named, tracked, and organized.

## Core Principles

1. **Track for Decisions**: Only track events that inform a decision (e.g., "Add to Cart" signals intent; "Scroll 10%" might be vanity).
2. **Consistent Naming**: `snake_case` for everything (events, parameters, UTMs).
3. **Validation**: Always verify implementation before launching campaigns.

## UTM Strategy (The Law)

All Meta Ads **MUST** use this UTM structure to ensure GA4 captures the data correctly:

| Parameter | Value Template | Example |
| :--- | :--- | :--- |
| `utm_source` | `{{site_source_name}}` | `fb`, `ig` |
| `utm_medium` | `paid_social` | `paid_social` |
| `utm_campaign` | `{{campaign.name}}` | `mindlink_prospecting_cbo` |
| `utm_content` | `{{ad.name}}` | `video_hook_01_pawel` |
| `utm_term` | `{{adset.name}}` | `broad_females_25_45` |

**Verification Rule**:

- Check `Untitled-report...csv` or `analysis_report.md`.
- If URLs lack UTMs, flag as **CRITICAL ERROR**.

## Event Naming (GTM/GA4)

Use the **Object-Action** framework:

- `product_viewed`
- `cart_added`
- `checkout_started`
- `purchase_completed`
- `newsletter_subscribed`

## Debugging & Troubleshooting

1. **Check the Link**: Copy the ad link. Does it have `?utm_source=...`?
2. **Check the Source**: In GA4, go to "Realtime". Click the link. Do you appear as `paid_social`?
3. **Check the Redirects**: does the landing page strip parameters? (Common issue).
4. **Data Discrepancy**: If Meta Link Clicks > GA4 Sessions, check for slow LCP or missing tracking pixel.
