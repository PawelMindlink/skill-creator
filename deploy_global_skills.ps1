
# Deploy Global Skills
# Syncs current repo skills to the Global Antigravity Directory

$Source = "$PSScriptRoot\skills"
$GlobalDir = "$env:USERPROFILE\.gemini\antigravity\global_skills"

Write-Host "🚀 Deploying Skills to Global Context..." -ForegroundColor Cyan
Write-Host "Source: $Source"
Write-Host "Target: $GlobalDir"

# 1. Ensure Target Exists
if (-not (Test-Path $GlobalDir)) {
    New-Item -ItemType Directory -Path $GlobalDir -Force | Out-Null
    Write-Host "Created Global Directory." -ForegroundColor Green
}

# 2. Copy Categories
$Categories = Get-ChildItem -Path $Source -Directory

foreach ($Cat in $Categories) {
    $DestCat = Join-Path $GlobalDir $Cat.Name
    Write-Host "Syncing Category: $($Cat.Name)..." -ForegroundColor Yellow
    
    # Create Specifc Category Folder
    if (-not (Test-Path $DestCat)) {
        New-Item -ItemType Directory -Path $DestCat -Force | Out-Null
    }
    
    # Copy Content (Force Overwrite)
    Copy-Item -Path "$($Cat.FullName)\*" -Destination $DestCat -Recurse -Force
}

Write-Host "✅ Deployment Complete!" -ForegroundColor Green
Write-Host "Skills are now available globally via:"
Write-Host "  > Use skill strategy/icp-research-lead"
Write-Host "  > Use skill creative/nano-banana-creative"
