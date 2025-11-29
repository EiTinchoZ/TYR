#!/bin/bash
# Script para ejecutar el frontend de TYR (Landing Page)
# Compatible con: Linux, macOS, Git Bash (Windows)

echo "🎨 Iniciando Frontend TYR..."
echo "================================"

# Verificar si estamos en el directorio correcto
if [ ! -d "Figma" ]; then
    echo "❌ Error: No se encontró el directorio 'Figma'"
    echo "Por favor ejecuta este script desde la raíz del proyecto TYR"
    exit 1
fi

# Verificar si Node.js está instalado
if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js no está instalado"
    echo "Instala Node.js 16+ desde: https://nodejs.org/"
    exit 1
fi

echo "📦 Verificando dependencias..."
cd Figma

# Verificar si node_modules existe
if [ ! -d "node_modules" ]; then
    echo "⚠️  Dependencias no instaladas. Instalando..."
    npm install
fi

# Verificar si existe .env
if [ ! -f ".env" ]; then
    echo "⚠️  Archivo .env no encontrado"
    if [ -f ".env.example" ]; then
        echo "📝 Copiando .env.example a .env..."
        cp .env.example .env
        echo "✅ Archivo .env creado. Puedes editarlo si necesitas cambiar configuraciones."
    fi
fi

echo "✅ Dependencias verificadas"
echo ""
echo "🌐 Frontend estará disponible en: http://localhost:5173"
echo "🔗 Asegúrate de que el backend esté corriendo en: http://localhost:8000"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo "================================"
echo ""

# Ejecutar el servidor de desarrollo
npm run dev
