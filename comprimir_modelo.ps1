# Script para comprimir el modelo BERT para subirlo a Google Drive
# Ejecutar con: .\comprimir_modelo.ps1

Write-Host "Comprimiendo modelo BERT para Google Drive..." -ForegroundColor Green

$sourcePath = "modelo_bert_tyr_10_clases_COMPLETO"
$zipFile = "modelo_bert_tyr_10_clases_COMPLETO.zip"

# Verificar que existe la carpeta del modelo
if (-Not (Test-Path $sourcePath)) {
    Write-Host "ERROR: No se encontró la carpeta del modelo en: $sourcePath" -ForegroundColor Red
    exit 1
}

# Eliminar ZIP anterior si existe
if (Test-Path $zipFile) {
    Write-Host "Eliminando archivo ZIP anterior..." -ForegroundColor Yellow
    Remove-Item $zipFile -Force
}

# Comprimir
Write-Host "Comprimiendo... (esto puede tomar 1-2 minutos)" -ForegroundColor Cyan
Compress-Archive -Path $sourcePath -DestinationPath $zipFile -CompressionLevel Optimal

# Verificar tamaño
$size = (Get-Item $zipFile).Length / 1MB
Write-Host "`nCompresión completada!" -ForegroundColor Green
Write-Host "Archivo: $zipFile" -ForegroundColor White
Write-Host "Tamaño: $([math]::Round($size, 2)) MB" -ForegroundColor White
Write-Host "`nAhora puedes subir este archivo a Google Drive." -ForegroundColor Cyan
Write-Host "Después, actualiza el README.md con el link de descarga." -ForegroundColor Cyan
