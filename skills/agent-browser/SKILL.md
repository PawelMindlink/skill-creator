---
name: agent-browser
description: Browser automation skill. Use to navigate, inspect, and interact with web pages via CLI commands.
---

# Agent Browser Skill

This skill allows you to control a web browser to perform automated tasks, extract data, or test web applications.

# Troubleshooting & Environment (CRITICAL)

**Known Windows Issues:**

1. **"failed to install playwright: $HOME environment variable is not set"**:
    * This occurs in environments where the user profile is not fully loaded.
    * *Fix*: Try setting the HOME variable explicitly if possible, or fall back to `read_url_content` (Python tool) if headless browsing is not strictly required.
2. **"Daemon failed to start"**:
    * This is a path escaping issue with `cmd /c` on Windows.
    * *Fix*: Ensure you are running in a shell that handles paths correctly (Powershell is preferred), or check if Node.js is correctly in the PATH.

# When to use this skill

* When you need to read content from a website that requires JavaScript or interaction.
* When you need to take screenshots or record videos of web pages.
* When you need to fill out forms, click buttons, or navigate complex user flows.
* When `read_url_content` is insufficient (e.g., behind login, dynamic content).

# How to use it

You will use the `npx agent-browser` command (or just `agent-browser` if installed globally, but prefer `npx` for portability).

## Core Workflow

1. **Navigate**: `npx agent-browser open <url>`
2. **Snapshot**: `npx agent-browser snapshot -i` (Gets interactive elements with `@ref` IDs)
3. **Interact**: `npx agent-browser click @e1`, `npx agent-browser fill @e2 "text"`
4. **Verify**: Re-snapshot or check state.

## Common Commands

### Navigation

* `open <url>`: Navigate to a URL.
* `back`, `forward`: Navigate history.
* `reload`: Reload the page.
* `close`: Close the browser.

### Page Analysis

* `snapshot -i`: List interactive elements with references (`@e1`, `@e2`, etc). **Use this most often.**
* `snapshot`: Full accessibility tree.
* `get text @ref`: Get text content.
* `get html @ref`: Get inner HTML.

### Interaction

* `click @ref`: Click an element.
* `fill @ref "text"`: Clear and type text.
* `type @ref "text"`: Type without clearing.
* `press <key>`: Press a key (e.g., Enter).
* `wait --load networkidle`: Wait for network to settle.

### Debugging & Output

* `screenshot`: Save a screenshot.
* `console`: View browser console logs.
* `--json`: Add this flag to any command for machine-readable JSON output.

## Examples

**Search Google:**

```bash
npx agent-browser open https://google.com
npx agent-browser snapshot -i
# (Identify search box @ref, e.g., @e1)
npx agent-browser fill @e1 "Antigravity skills"
npx agent-browser press Enter
npx agent-browser wait --load networkidle
npx agent-browser snapshot -i
```
