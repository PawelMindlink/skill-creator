---
name: google_analytics
description: Official Google Analytics 4 (GA4) skill for auditing traffic, engagement, and conversion data. Acts as the "Auditor" to verify Meta Ads performance.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. Implemented attribution check and behavioral analysis protocols.
---

# Google Analytics 4 (GA4) Skill

## Purpose

You are the **Insight Generator**.
While Meta Ads is the "Source of Truth" for attribution, you provide the "Second Opinion" and deeper insights into user behavior.
Use GA4 to find new creative ideas, product opportunities, and validat landing page quality (not to audit Meta's attribution).

## Setup Requirements

To use the API features, the user must provide:

1. **Property ID**: `GOOGLE_ANALYTICS_PROPERTY_ID`
2. **Credentials**: `GOOGLE_APPLICATION_CREDENTIALS` (JSON key path)

*If these are missing, ask the user to provide them or fallback to analyzing exported CSV reports.*

## Capabilities

### 1. Audit Meta Performance

- **Traffic Verification**: Compare Meta `Link Clicks` vs GA4 `Sessions` (Source: facebook/instagram).
  - *Gap Analysis*: If `Sessions` < 70% of `Link Clicks`, flag as a "Landing Page Load/Bot" issue.
- **Conversion Verification**: Compare Meta `Purchases` vs GA4 `Key Events` (Purchases).
  - *Attribution Check*: Verify how many Meta conversions are reported in GA4 (Last Click vs. Data-Driven).

### 2. Behavioral Analysis

- **Engagement Rate**: Are Meta users staying > 10s?
- **Bounce Rate**: Are they leaving immediately?
- **Pages/Session**: Are they exploring the brand?

## Analysis Workflow

1. **Connect**: Check for credentials.
2. **Fetch**:
    - If API is ready: Use `google-analytics-data` Python client.
    - If API is missing: Ask user for "GA4 Acquisition Report (last 30 days) as CSV".
3. **Analyze**:
    - Filter for `Session source / medium` indicates `facebook` or `instagram`.
    - Compare metrics against the Meta Ads Report.
4. **Report**:
    - "Meta claims 1000 clicks, GA4 sees 800 sessions (80% match - Healthy)."
    - "Meta claims 50 purchases, GA4 attributes 30 to Last Click."

## Common Metrics Reference

- **Sessions**: Visits to the site.
- **Engaged Sessions**: Sessions > 10s, or with conversion, or > 2 pageviews.
- **Engagement Rate**: Engaged Sessions / Total Sessions.
- **Event Count**: Total interactions (clicks, scrolls, etc.).
- **Key Events**: Important actions (Purchases, Leads - formerly Conversions).

## Troubleshooting

- **Missing Credentials**: If `GOOGLE_APPLICATION_CREDENTIALS` is not set, you MUST ask the user for the JSON key path or fallback to CSV analysis.
- **Property ID Error**: Ensure the Property ID is purely numeric.
- **Data Not Found**: If "Realtime" shows no traffic but the site is live, check if the GTM tag is actually firing (use `audit-website`).
- **CSV Format**: If analyzing CSVs, ensure headers match expected GA4 export formats. Normalize headers using `data_science_core` if needed.
