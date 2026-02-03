---
name: audit-website
description: Audit websites for SEO, technical, content, performance and security issues using the squirrelscan cli.
version: 1.0.0
changelog: |
  v1.0.0: Initial version using npx squirrel for comprehensive site audits.
---

# Website Audit Skill

Audit websites for SEO, technical, content, performance and security issues using the `squirrel` CLI.

## When to use this skill

- When you need to check a website for SEO issues (missing alt tags, broken links, meta descriptions).
- When you need to assess performance or security vulnerabilities.
- When you need to improve accessibility.
- When you want to crawl a site to understand its structure.

## How to use it

### Basic Workflow

1. **Run Audit**: `npx squirrel audit https://example.com`
    - This runs a crawl and analysis, saving results to a local database.
2. **Generate Report**: `npx squirrel report <audit-id> --format llm`
    - **Always use `--format llm`** for the best output for agents.

### Strategy

1. **Surface Scan**: For initial checks or if performance impact is a concern.
2. **Deep Scan**: For thorough analysis.
3. **Iterative Fixes**:
    - Run audit.
    - Identify issues (critical/high priority first).
    - Apply fixes (potentially using sub-agents for bulk content edits).
    - Re-audit to verify.
    - Repeat until target score (95+) is reached.

### Fix Guidelines

- **Content Files**: Edit markdown (`.md`, `.mdx`) to fix alt text, headers, and meta descriptions.
- **Code Files**: Edit `.tsx`, `.html`, etc. for structural fixes.
- **Parallelize**: If many files need similar fixes, spawn sub-agents to handle them in parallel.
- **Be Autonomous**: Don't stop for minor confirmations; proceed until the site is clean.

### Troubleshooting

- **Command Not Found**: If `squirrel` command is not found, try `npx squirrel`.
- **Target Missing**: If no URL is provided, try to discover one from the environment or ask the user.
- **Crawl Failures**: Check if the site blocks bots via `robots.txt` or Cloudflare.
- **Report Missing**: Ensure you have the `<audit-id>` from the initial audit step before running the report command.
