---
name: agent-browser
description: Browser automation skill. Use to navigate, inspect, and interact with web pages via CLI commands.
version: 1.1.0
changelog: |
  v1.1.0 (2026-02-03): Added Windows PowerShell wrapper scripts for HOME variable fix
  - New: ensure-env.ps1 for environment normalization
  - New: browser.ps1 wrapper with npx validation
  - Enhanced: Platform-specific documentation
  - Fixed: Playwright installation on Windows
---

# Agent Browser Skill

This skill allows you to control a web browser to perform automated tasks, extract data, or test web applications.

# Troubleshooting & Environment (CRITICAL)

**Known Windows Issues:**

## Issue 1: "$HOME environment variable is not set"

**Symptoms:** Browser fails to initialize with error: `failed to install playwright: $HOME environment variable is not set`

**Root Cause:** Playwright requires `$HOME` to determine where to install browser binaries. Windows uses `%USERPROFILE%` instead and doesn't set `$HOME` by default.

**Fix Option A - Use Wrapper Script (Recommended):**

```powershell
# Navigate to the skill directory (adjust path to your installation)
cd <path-to-skill-creator>\skills\agent-browser

# Use the wrapper script instead of npx directly
.\scripts\browser.ps1 open https://example.com
```

**Fix Option B - Manual Environment Setup:**

```powershell
# Set HOME for current PowerShell session
$env:HOME = $env:USERPROFILE

# Optionally set browser path
$env:PLAYWRIGHT_BROWSERS_PATH = "$env:HOME\.playwright-browsers"

# Now run agent-browser as normal
npx agent-browser open https://example.com
```

**Fix Option C - Permanent Environment Variable:**

1. Open System Properties → Environment Variables
2. Add new User variable: `HOME` = `%USERPROFILE%`
3. Restart PowerShell and try again

**Diagnostic Steps:**

```powershell
# Check if HOME is set
Write-Host "HOME: $env:HOME"
Write-Host "USERPROFILE: $env:USERPROFILE"

# If HOME is empty, use one of the fixes above
```

## Issue 2: "Daemon failed to start"

**Symptoms:** Browser daemon fails to start with path-related errors.

**Root Cause:** Path escaping issues with `cmd /c` on Windows.

**Fix:** Use PowerShell (not CMD), and ensure Node.js is in PATH:

```powershell
node --version  # Should show version number
npx --version   # Should show version number
```

## When to Fall Back to read_url_content

Only use `read_url_content` as fallback when:

- All fixes above fail after multiple attempts
- The target site doesn't require JavaScript or interaction
- You only need static HTML content

Do NOT immediately fall back without trying the fixes above first.

## Issue 3: "Scripts cannot be loaded" (Execution Policy)

**Symptoms:** PowerShell blocks script execution with error:

```
.\browser.ps1 : File cannot be loaded because running scripts is disabled on this system.
```

**Root Cause:** Windows PowerShell execution policy (security feature) blocks unsigned scripts by default.

**Fix:**

```powershell
# Check current policy
Get-ExecutionPolicy

# Option 1: Allow for current session only (safest)
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Option 2: Allow for current user (persistent)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then run the script
.\scripts\browser.ps1 open https://example.com
```

# When to use this skill

- When you need to read content from a website that requires JavaScript or interaction.
- When you need to take screenshots or record videos of web pages.
- When you need to fill out forms, click buttons, or navigate complex user flows.
- When `read_url_content` is insufficient (e.g., behind login, dynamic content).

# How to use it

## Platform-Specific Commands

**Windows Users (PowerShell):**
Use the wrapper script to avoid environment issues:

```powershell
# Navigate to where you have skill-creator installed
cd <path-to-skill-creator>\skills\agent-browser

# Run wrapper script
.\scripts\browser.ps1 [commands]
```

**Unix/Mac/Linux:**
Use `npx` directly:

```bash
npx agent-browser [commands]
```

> **Note:** The examples below use `npx agent-browser` for brevity. Windows users should replace this with `.\scripts\browser.ps1` when running from the skill directory.

## Core Workflow

1. **Navigate**: `npx agent-browser open <url>`
2. **Snapshot**: `npx agent-browser snapshot -i` (Gets interactive elements with `@ref` IDs)
3. **Interact**: `npx agent-browser click @e1`, `npx agent-browser fill @e2 "text"`
4. **Verify**: Re-snapshot or check state.

## Common Commands

### Navigation

- `open <url>`: Navigate to a URL.
- `back`, `forward`: Navigate history.
- `reload`: Reload the page.
- `close`: Close the browser.

### Page Analysis

- `snapshot -i`: List interactive elements with references (`@e1`, `@e2`, etc). **Use this most often.**
- `snapshot`: Full accessibility tree.
- `get text @ref`: Get text content.
- `get html @ref`: Get inner HTML.

### Interaction

- `click @ref`: Click an element.
- `fill @ref "text"`: Clear and type text.
- `type @ref "text"`: Type without clearing.
- `press <key>`: Press a key (e.g., Enter).
- `wait --load networkidle`: Wait for network to settle.

### Debugging & Output

- `screenshot`: Save a screenshot.
- `console`: View browser console logs.
- `--json`: Add this flag to any command for machine-readable JSON output.

## Examples

**Search Google:**

Unix/Mac:

```bash
npx agent-browser open https://google.com
npx agent-browser snapshot -i
# (Identify search box @ref, e.g., @e1)
npx agent-browser fill @e1 "Antigravity skills"
npx agent-browser press Enter
npx agent-browser wait --load networkidle
npx agent-browser snapshot -i
```

Windows (from skill directory):

```powershell
.\scripts\browser.ps1 open https://google.com
.\scripts\browser.ps1 snapshot -i
# (Identify search box @ref, e.g., @e1)
.\scripts\browser.ps1 fill @e1 "Antigravity skills"
.\scripts\browser.ps1 press Enter
.\scripts\browser.ps1 wait --load networkidle
.\scripts\browser.ps1 snapshot -i
```
