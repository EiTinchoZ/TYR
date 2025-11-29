# Script para verificar que todos los screenshots estén presentes

$screenshotsPath = "documentacion\screenshots"

$requiredScreenshots = @(
    "01_landing_page.png",
    "02_chat_interface.png",
    "03_chat_conversation.png",
    "04_chat_features.png",
    "05_mobile_responsive.png"
)

Write-Host "`n=== Verificación de Screenshots ===" -ForegroundColor Cyan
Write-Host "Ubicación: $screenshotsPath`n" -ForegroundColor White

$missing = @()
$found = @()

foreach ($screenshot in $requiredScreenshots) {
    $fullPath = Join-Path $screenshotsPath $screenshot
    if (Test-Path $fullPath) {
        $size = (Get-Item $fullPath).Length / 1KB
        Write-Host "[✓] $screenshot ($([math]::Round($size, 2)) KB)" -ForegroundColor Green
        $found += $screenshot
    } else {
        Write-Host "[✗] $screenshot - FALTANTE" -ForegroundColor Red
        $missing += $screenshot
    }
}

Write-Host "`n=== Resumen ===" -ForegroundColor Cyan
Write-Host "Encontrados: $($found.Count) / $($requiredScreenshots.Count)" -ForegroundColor $(if ($found.Count -eq $requiredScreenshots.Count) { "Green" } else { "Yellow" })

if ($missing.Count -gt 0) {
    Write-Host "`nScreenshots faltantes:" -ForegroundColor Yellow
    foreach ($m in $missing) {
        Write-Host "  - $m" -ForegroundColor Red
    }
    Write-Host "`nPor favor, toma estos screenshots siguiendo GUIA_SCREENSHOTS.txt" -ForegroundColor Cyan
} else {
    Write-Host "`n¡Todos los screenshots están presentes! ✓" -ForegroundColor Green
    Write-Host "Ahora puedes hacer commit y push a GitHub." -ForegroundColor Cyan
}
