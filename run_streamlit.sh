#!/bin/bash
# Script para ejecutar la aplicación Streamlit de TYR
# Compatible con: Linux, macOS, Git Bash (Windows)

echo "🎯 Iniciando App Streamlit TYR..."
echo "================================"

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

# Verificar si streamlit está instalado
if ! $PYTHON_CMD -c "import streamlit" &> /dev/null; then
    echo "⚠️  Streamlit no instalado. Instalando dependencias..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

echo "✅ Dependencias verificadas"
echo ""
echo "🌐 Streamlit estará disponible en: http://localhost:8501"
echo ""
echo "Presiona Ctrl+C para detener la aplicación"
echo "================================"
echo ""

# Ejecutar Streamlit
$PYTHON_CMD -m streamlit run tyr_chatbot.py
