# browser.ps1
# Wrapper script for agent-browser that ensures proper environment setup on Windows
# Usage: .\browser.ps1 [agent-browser commands and arguments]

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Source the environment normalization script
& "$ScriptDir\ensure-env.ps1"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[browser] Failed to normalize environment. Exiting." -ForegroundColor Red
    exit 1
}

# Check if npx is available
$npxCheck = Get-Command npx -ErrorAction SilentlyContinue
if (-not $npxCheck) {
    Write-Host "[browser] ERROR: npx is not found in PATH" -ForegroundColor Red
    Write-Host "" -ForegroundColor Yellow
    Write-Host "Please install Node.js (which includes npx):" -ForegroundColor Yellow
    Write-Host "  https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

# Forward all arguments to npx agent-browser
Write-Host "[browser] Executing: npx agent-browser $args" -ForegroundColor Cyan

try {
    npx agent-browser @args
    exit $LASTEXITCODE
} catch {
    Write-Host "[browser] Error executing agent-browser: $_" -ForegroundColor Red
    Write-Host "" -ForegroundColor Yellow
    Write-Host "Troubleshooting tips:" -ForegroundColor Yellow
    Write-Host "  1. Ensure Node.js is installed and in PATH" -ForegroundColor Yellow
    Write-Host "  2. Try running 'npx agent-browser --help' directly" -ForegroundColor Yellow
    Write-Host "  3. Check if firewall/antivirus is blocking npx" -ForegroundColor Yellow
    exit 1
}
