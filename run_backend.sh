#!/bin/bash
# Script para ejecutar el backend de TYR
# Compatible con: Linux, macOS, Git Bash (Windows)

echo "🚀 Iniciando Backend TYR..."
echo "================================"

# Verificar si estamos en el directorio correcto
if [ ! -d "backend" ]; then
    echo "❌ Error: No se encontró el directorio 'backend'"
    echo "Por favor ejecuta este script desde la raíz del proyecto TYR"
    exit 1
fi

# Verificar si Python está instalado
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python no está instalado"
    echo "Instala Python 3.8+ desde: https://www.python.org/downloads/"
    exit 1
fi

# Usar python3 si está disponible, sino python
PYTHON_CMD="python"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

echo "📦 Verificando dependencias..."
cd backend

# Verificar si las dependencias están instaladas
if ! $PYTHON_CMD -c "import fastapi" &> /dev/null; then
    echo "⚠️  Dependencias no instaladas. Instalando..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

echo "✅ Dependencias verificadas"
echo ""
echo "🌐 Backend estará disponible en: http://localhost:8000"
echo "📚 Documentación API: http://localhost:8000/docs"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo "================================"
echo ""

# Ejecutar el servidor
$PYTHON_CMD main.py
