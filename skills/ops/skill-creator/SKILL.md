---
name: skill-creator
description: Expert skill for designing and creating new agent skills. Follows best practices for modularity and clarity.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. Established directory structure and SKILL.md standardization rules.
---

# Skill Creator

This skill guides the creation of new skills for the agent ecosystem.

## When to use this skill

- When the user asks to "create a skill" or "add a capability".
- When you identify a repeatable workflow that should be standardized.

## Core Principles

- **Concise is Key**: Instructions should be brief and actionable.
- **Progressive Disclosure**: The `name` and `description` in frontmatter are for **discovery**. The body is for **execution**.
- **MECE**: Avoid creating skills that overlap significantly with existing ones.

## Creation Process

1. **Understand**: Define the goal. What problem does this skill solve?
2. **Plan**:
    - **SKILL.md**: The instruction set.
    - **Resources**: Cheat sheets, templates (put in `resources/` or `assets/`).
    - **Scripts**: Executables for deterministic tasks (put in `scripts/`).
    - **References**: Heavy documentation (put in `references/`).
3. **Initialize**: Create the directory structure.

    ```
    skill-name/
    ├── SKILL.md (required)
    ├── scripts/ (optional)
    ├── references/ (optional)
    └── assets/ (optional)
    ```

4. **Edit**: Write the `SKILL.md` with:
    - YAML Frontmatter (`name`, `description`).
    - "When to use" section.
    - "How to use" section (step-by-step).
5. **Iterate**: Refine based on usage.

## Folder Structure Rules

- **Do NOT** include `README.md`, `INSTALL.md`, etc. within the skill folder.
- **SKILL.md** is the single source of truth for the agent.
- Large docs go to `references/` to save context window.

## Example `SKILL.md`

```markdown
---
name: example-skill
description: Does X to achieve Y.
---
# Example Skill
## When to use
- Use when X happens.
## How to use
1. Step one
2. Step two
```

## Troubleshooting

- **Bloated SKILL.md**: If the file is getting too long, move detailed explanations or large templates to the `references/` directory.
- **Discovery Issues**: Ensure the `name` and `description` in the frontmatter accurately reflect the primary use case.
- **Agent Confusion**: If the agent ignores the skill, check for overlapping instructions with other skills in the ecosystem (ensure MECE).
