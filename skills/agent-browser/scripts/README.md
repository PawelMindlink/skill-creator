# Agent Browser Scripts - Windows Support

This directory contains PowerShell scripts to fix Windows environment issues with Playwright/agent-browser.

## Files

### `ensure-env.ps1`

Normalizes environment variables required by Playwright:

- Sets `$env:HOME` to `$env:USERPROFILE` if not already set
- Sets `$env:PLAYWRIGHT_BROWSERS_PATH` to a reliable location
- Can be sourced by other scripts or run standalone

### `browser.ps1`

Wrapper script that:

1. Sources `ensure-env.ps1` to fix environment
2. Forwards all arguments to `npx agent-browser`
3. Provides helpful error messages

## Usage

**Recommended (from skill directory):**

```powershell
.\scripts\browser.ps1 open https://example.com
.\scripts\browser.ps1 snapshot -i
.\scripts\browser.ps1 click @e1
```

**Standalone environment fix:**

```powershell
.\scripts\ensure-env.ps1
npx agent-browser open https://example.com
```

## Why This Exists

Windows doesn't set the `$HOME` environment variable by default (uses `%USERPROFILE%` instead). Playwright requires `$HOME` to determine where to install browser binaries. Without these scripts, you'll get:

```
failed to install playwright: $HOME environment variable is not set
```

These scripts automatically fix this issue.
