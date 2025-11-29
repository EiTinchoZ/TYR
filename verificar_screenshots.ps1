# Script para verificar que todos los screenshots estén presentes

$screenshotsPath = "documentacion\screenshots"

$requiredScreenshots = @(
    "landing\01_landing_hero.png",
    "chat\02_chat_modal_open.png",
    "chat\03_consulta_carreras.png",
    "chat\04_consulta_bigdata.png",
    "chat\05_modo_demo.png",
    "chat\06_chat_features.png",
    "chat\07_dark_mode.png",
    "landing\08_mobile_view.png",
    "features\09_pwa_install.png",
    "features\10_export_pdf.png"
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
    Write-Host "`nPor favor, toma estos screenshots siguiendo la guía." -ForegroundColor Cyan
} else {
    Write-Host "`n¡Todos los screenshots están presentes! ✓" -ForegroundColor Green
}
