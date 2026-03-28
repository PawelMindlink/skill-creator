---
name: meta-ads-api
description: Expert skill for building integrations with the Meta Ads Marketing API — covering data fetching, ad creatives, image/video uploads, error handling, and AI agent connections.
version: 2.0.0
changelog: |
  v2.0.0: Full refactor. Slim SKILL.md + references/ directory for progressive disclosure.
  v1.0.2: Added comprehensive use cases (data fetching, insights, creative uploads, and SDK references).
  v1.0.1: Added step-by-step instructions and code snippets for blame_field_specs.
  v1.0.0: Initial release covering Meta Ads API error handling principles.
---

# Meta Ads API Integration

## When to use this skill

- User asks to "build a Meta Ads integration", "automate Facebook Ads", or "work with the Meta Marketing API".
- User asks to fetch, analyze, or report on campaign performance data.
- User asks to upload images, videos, or manage ad creatives programmatically.
- User encounters HTTP 400 or HTTP 429 errors from the Meta Graph API.
- User asks to connect an AI agent or LLM to Meta Ads.

## When NOT to use this skill

- User is asking generic Python/JavaScript questions that happen to mention Meta.
- User is working with the Facebook Social Graph (personal profiles, pages, events) — not Ads.
- User needs the Instagram Creator API (different permission set, different SDK).

## How to Use (Agent Triage)

Before writing any code, determine which task the user needs:

| Task | Reference |
|---|---|
| Debug an API error (400, 429, auth) | [references/error_handling.md](references/error_handling.md) |
| Fetch campaign/ad data & analyze | [references/data_fetching.md](references/data_fetching.md) |
| Upload images/videos or manage creatives | [references/creative_management.md](references/creative_management.md) |
| Connect an AI agent or MCP to Meta Ads | See **Ecosystem** section below |

## Ecosystem Awareness (Read First)

Before writing custom code, check if an existing tool covers the need:

- **MCP Servers (For LLM Agents)**: [`hashcott/meta-ads-mcp-server`](https://github.com/hashcott/meta-ads-mcp-server), [`pipeboard-co/meta-ads-mcp`](https://github.com/pipeboard-co/meta-ads-mcp), [`lobehub/mcp-meta-ads`](https://github.com/lobehub/mcp-meta-ads). These provide 20–40 pre-built tools covering campaigns, insights, creatives, and accounts.
- **Official Python SDK**: [`facebook/facebook-python-business-sdk`](https://github.com/facebook/facebook-python-business-sdk). Install: `pip install facebook_business`.

## Official Reference Links

| Resource | URL |
|---|---|
| Marketing API Overview | <https://developers.facebook.com/docs/marketing-apis> |
| Error Codes Reference | <https://developers.facebook.com/docs/marketing-api/error-reference> |
| Rate Limiting Guide | <https://developers.facebook.com/docs/marketing-api/overview/rate-limiting> |
| Ad Creative Reference | <https://developers.facebook.com/docs/marketing-api/reference/ad-creative> |
| Insights API Reference | <https://developers.facebook.com/docs/marketing-api/insights> |
| Graph API Explorer | <https://developers.facebook.com/tools/explorer> |
