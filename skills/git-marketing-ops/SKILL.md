---
name: git-marketing-ops
description: Comprehensive Git & GitHub workflow for marketing projects. Supports bootstrapping new campaigns, auditing existing ones, and maintaining context-rich history. Use for: (1) Setting up new marketing projects, (2) Auditing/fixing existing repos, (3) Making context-aware commits, (4) Tagging releases.
---

# Git Marketing Ops

This skill standardizes "Marketing Engineering" - applying robust engineering practices to marketing workflows to preserve history, context, and asset organization.

## When to use this skill

- **New Projects**: When the user wants to start a new campaign or project (`init_project`).
- **Existing Projects**: When opening an existing repo that feels "messy" or undocumented (`audit_repo`).
- **Daily Work**: When saving changes (`smart_commit`). Do NOT use standard `git commit` if you can use this.
- **Milestones**: When wrapping up a phase or campaign (`tag_version`).

## Workflows

### 1. Bootstrap New Project

Use this when creating a new marketing repository or folder.

1. **Initialize**: Run the initialization script.

    ```bash
    python <skill_path>/scripts/init_project.py --target "."
    ```

2. **Customize**:
    - The script creates `README.md` from a template.
    - **CRITICAL**: You MUST read the generated `README.md` and fill in the placeholders (Goal, Audience, Hypotheses) based on the user's request.

### 2. Audit Existing Project

Use this for "Inwentaryzacja" of a project you just opened.

1. **Analyze**: Run the audit tool.

    ```bash
    python <skill_path>/scripts/audit_repo_context.py
    ```

2. **Act on Feedback**:
    - If `README.md` is missing or incomplete, the script will flag it.
    - **Agent Action**: You MUST analyze the codebase (file structure, recent changes) and generate the missing `Definition` (Business Goal), `Structure`, and `Operation` sections in `README.md`. Use the "Ariadne Style" (Definition/Operation/Structure).
3. **Fix Structure**: If `assets/` or other standard folders are missing, suggest creating them.

### 3. Smart Commit

Use this for ALL commits to ensure history tells a story.

1. **Assist**: Run the commit helper.

    ```bash
    python <skill_path>/scripts/smart_commit.py
    ```

2. **Convention**:
    - The script facilitates Conventional Commits tailored for marketing:
        - `feat`: New campaign asset or code feature.
        - `content`: Copy update, image swap (Creative changes).
        - `design`: Visual structure, CSS, Layout.
        - `analytics`: Pixel, GTM, Tracking updates.
        - `fix`: Bug fix or typo fix.
3. **Context**: The script will ask for a Scope. Use the campaign name or component name (e.g., `(black-friday)` or `(hero-banner)`).

### 4. Release Tagging

Use this when a campaign launches, ends, or hits a major milestone.

1. **Tag**:

    ```bash
    python <skill_path>/scripts/tag_version.py
    ```

2. **SemVer for Marketing**:
    - `Major` (1.0.0): Campaign Launch / Rebranding.
    - `Minor` (1.1.0): New Wave of Creatives / New Landing Page Variant.
    - `Patch` (1.1.1): Typos, minor CSS fixes.

## Reference

- **Structure**: See `references/marketing-readme.md` for the gold standard documentation structure.
- **Commits**: See `references/commit-convention.md` for detailed commit types.
