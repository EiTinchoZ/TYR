@echo off
echo ====================================
echo   Iniciando Backend TYR (FastAPI)
echo ====================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no encontrado. Por favor instala Python 3.8+
    echo.
    pause
    exit /b 1
)

REM Cambiar al directorio backend
cd backend

REM Verificar que main.py existe
if not exist "main.py" (
    echo [ERROR] No se encuentra main.py en la carpeta backend
    echo.
    pause
    exit /b 1
)

echo [INFO] Iniciando servidor FastAPI en http://localhost:8000
echo [INFO] Presiona Ctrl+C para detener el servidor
echo.

REM Ejecutar el servidor
python main.py

REM Si el servidor termina inesperadamente, mantener ventana abierta
if errorlevel 1 (
    echo.
    echo [ERROR] El servidor terminó con errores
    pause
)
