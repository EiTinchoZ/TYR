#!/bin/bash
# Script para preparar el modelo BERT para distribución
# Crea un archivo ZIP del modelo para subir a Google Drive

echo "📦 Preparando Modelo BERT TYR para Distribución"
echo "================================================"
echo ""

# Verificar que el modelo existe
if [ ! -d "modelo_bert_tyr_10_clases_COMPLETO" ]; then
    echo "❌ Error: No se encontró el directorio del modelo"
    echo ""
    echo "Asegúrate de que 'modelo_bert_tyr_10_clases_COMPLETO/' existe en este directorio"
    exit 1
fi

# Mostrar tamaño del modelo
echo "📊 Tamaño del modelo:"
du -sh modelo_bert_tyr_10_clases_COMPLETO/
echo ""

# Nombre del archivo ZIP
ZIP_NAME="modelo_bert_tyr_v3_4358ejemplos.zip"

# Verificar si zip está instalado
if ! command -v zip &> /dev/null; then
    echo "⚠️  El comando 'zip' no está disponible"
    echo ""
    echo "Alternativa en Windows: Usa el Explorador de Archivos"
    echo "1. Click derecho en 'modelo_bert_tyr_10_clases_COMPLETO'"
    echo "2. Selecciona 'Comprimir en archivo ZIP'"
    echo "3. Renombra a: $ZIP_NAME"
    echo ""
    exit 1
fi

echo "🗜️  Comprimiendo modelo..."
echo "Esto puede tomar 1-2 minutos..."
echo ""

# Comprimir el modelo
zip -r "$ZIP_NAME" modelo_bert_tyr_10_clases_COMPLETO/

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Modelo comprimido exitosamente"
    echo ""
    echo "📁 Archivo creado: $ZIP_NAME"
    ls -lh "$ZIP_NAME"
    echo ""
    echo "📤 Próximos Pasos:"
    echo "1. Sube $ZIP_NAME a Google Drive"
    echo "2. Haz el archivo público (Obtener enlace → Cualquier persona con el enlace)"
    echo "3. Copia el link de descarga directa"
    echo "4. Actualiza el link en MODELO_DESCARGA.md"
    echo ""
    echo "💡 Tip: El link debe terminar en '?usp=sharing'"
    echo "   Para descarga directa, cámbialo a '?usp=download'"
    echo ""
else
    echo ""
    echo "❌ Error al comprimir el modelo"
    exit 1
fi
