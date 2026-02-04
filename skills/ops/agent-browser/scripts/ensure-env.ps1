# ensure-env.ps1
# PowerShell script to normalize environment variables for Playwright on Windows
# This script ensures that $HOME is set, which is required for Playwright installation

# Check if HOME is already set
if (-not $env:HOME) {
    # On Windows, use USERPROFILE as HOME
    if ($env:USERPROFILE) {
        Write-Host "[ensure-env] Setting HOME to USERPROFILE: $env:USERPROFILE" -ForegroundColor Green
        $env:HOME = $env:USERPROFILE
    } else {
        Write-Host "[ensure-env] ERROR: Neither HOME nor USERPROFILE are set!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "[ensure-env] HOME already set: $env:HOME" -ForegroundColor Cyan
}

# Optionally set PLAYWRIGHT_BROWSERS_PATH to a reliable location
# This ensures browser binaries are stored in a consistent, accessible location
if (-not $env:PLAYWRIGHT_BROWSERS_PATH) {
    $browsersPath = Join-Path $env:HOME ".playwright-browsers"
    Write-Host "[ensure-env] Setting PLAYWRIGHT_BROWSERS_PATH: $browsersPath" -ForegroundColor Green
    $env:PLAYWRIGHT_BROWSERS_PATH = $browsersPath
}

Write-Host "[ensure-env] Environment normalized successfully." -ForegroundColor Green
exit 0
