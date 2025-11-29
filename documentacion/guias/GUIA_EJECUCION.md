# 🚀 Guía de Ejecución - TYR Chatbot

**Proyecto:** TYR - Asistente Virtual ITSE
**Versión:** modelo_bert_tyr_4358 (Final)
**Fecha:** Noviembre 2025

---

## ⚡ Inicio Rápido

### Windows (Recomendado)

**Opción 1: Doble clic**
```
1. Ir a la carpeta TYR/
2. Hacer doble clic en: ejecutar_streamlit.bat
3. Esperar que se abra el navegador automáticamente
```

**Opción 2: Terminal**
```bash
cd "C:\Users\[tu-usuario]\...\TYR"
python -m streamlit run tyr_app.py
```

### Linux / Mac

```bash
cd /ruta/a/TYR
streamlit run tyr_app.py
```

---

## 📋 Requisitos Previos

### 1. Python Instalado

**Versión mínima:** Python 3.8+

Verificar instalación:
```bash
python --version
```

### 2. Dependencias Instaladas

**Primera vez solamente:**
```bash
pip install -r requirements.txt
```

**Dependencias principales:**
- `transformers` (HuggingFace)
- `torch` (PyTorch)
- `streamlit`
- `vaderSentiment-es`

### 3. Modelo Descargado

El modelo debe estar en:
```
TYR/modelo_bert_tyr_4358/
```

**Tamaño:** ~440 MB
**Archivos requeridos:**
- model.safetensors
- config.json
- tokenizer.json
- vocab.txt
- label_map.json

---

## 🎯 Ejecutar la Aplicación

### Método 1: Script Automatizado (Windows)

```bash
ejecutar_streamlit.bat
```

Este script:
1. ✅ Configura Streamlit automáticamente
2. ✅ Inicia el servidor en puerto 8501
3. ✅ Abre el navegador automáticamente

### Método 2: Comando Manual

```bash
streamlit run tyr_app.py
```

### Método 3: Python directamente

```bash
python -m streamlit run tyr_app.py
```

---

## 🌐 Acceder a la Aplicación

Una vez ejecutado, la aplicación estará disponible en:

```
http://localhost:8501
```

**También puedes acceder desde:**
- `http://127.0.0.1:8501`
- `http://[tu-ip-local]:8501` (desde otros dispositivos en tu red)

---

## 💬 Usar el Chatbot

### 1. Escribir Preguntas

En el área de input en la parte inferior, escribe tu pregunta:

**Ejemplos:**
```
✅ "Cuéntame sobre Big Data"
✅ "¿Qué es CAIPI?"
✅ "Alianzas estratégicas"
✅ "Cómo me inscribo?"
✅ "Requisitos para estudiar"
```

### 2. Enviar Mensaje

- **Presiona Enter** ✅ (funciona perfectamente)
- O haz clic en el ícono de enviar

### 3. Ver Respuesta

El chatbot responderá instantáneamente con:
- 💬 Respuesta contextual
- 📊 Nivel de confianza
- 😊 Análisis de sentimiento

---

## 🛠️ Solución de Problemas

### Error: "Module not found"

**Problema:** Falta instalar dependencias

**Solución:**
```bash
pip install -r requirements.txt
```

### Error: "Port 8501 is already in use"

**Problema:** Streamlit ya está ejecutándose

**Soluciones:**

**Opción A:** Cerrar la aplicación anterior
```bash
# Windows
taskkill /F /IM streamlit.exe

# Linux/Mac
pkill -f streamlit
```

**Opción B:** Usar otro puerto
```bash
streamlit run tyr_app.py --server.port 8502
```

### Error: "Model not found"

**Problema:** El modelo no está en la ubicación correcta

**Solución:**
1. Verificar que existe la carpeta: `TYR/modelo_bert_tyr_4358/`
2. Verificar que contiene los 5 archivos necesarios
3. Si falta, descargar desde Google Colab o re-entrenar

### Aplicación muy lenta

**Problema:** Modelo cargando en CPU

**Soluciones:**
- Normal en primera carga (5-8 segundos)
- Respuestas subsecuentes son rápidas (<0.5s)
- Para GPU: Modificar `tyr_chatbot.py` línea 37

### Error de encoding (emojis)

**Problema:** Windows y UTF-8

**Solución:**
- La aplicación Streamlit maneja esto automáticamente
- Si usas scripts de prueba, ignorar warnings de encoding

---

## ⚙️ Configuración Avanzada

### Cambiar Puerto

```bash
streamlit run tyr_app.py --server.port 8080
```

### Modo Debug

```bash
streamlit run tyr_app.py --logger.level=debug
```

### Desactivar Auto-abrir Navegador

```bash
streamlit run tyr_app.py --server.headless=true
```

### Configuración Persistente

Editar `.streamlit/config.toml`:
```toml
[server]
port = 8501
headless = false

[browser]
gatherUsageStats = false
```

---

## 📊 Métricas y Monitoreo

### Ver Logs en Tiempo Real

La aplicación muestra logs en la terminal:
```
2025-11-21 10:30:15 - tyr_chatbot - INFO - Procesando consulta: 'Cuéntame sobre Big Data'
2025-11-21 10:30:15 - tyr_chatbot - INFO - Intención: informacion_carreras (99.89%)
2025-11-21 10:30:15 - tyr_chatbot - INFO - Carrera encontrada: T.S. en Big Data
```

### Historial de Conversaciones

Las conversaciones se guardan automáticamente en:
```
TYR/historial_conversaciones/
```

### Métricas Visibles

Cada respuesta muestra:
- **Intención detectada**
- **Confianza** (0-100%)
- **Sentimiento** (positivo/neutro/negativo)
- **Score de sentimiento** (-1 a +1)

---

## 🔄 Reiniciar la Aplicación

### Opción 1: Desde el Navegador

Presiona `R` en la página web para recargar

### Opción 2: Desde la Terminal

1. Presiona `Ctrl + C` para detener
2. Ejecuta nuevamente: `streamlit run tyr_app.py`

### Opción 3: Limpiar Caché

```bash
streamlit cache clear
streamlit run tyr_app.py
```

---

## 📱 Acceso desde Otros Dispositivos

### En la Misma Red Local

1. Obtener tu IP local:
   ```bash
   # Windows
   ipconfig

   # Linux/Mac
   ifconfig
   ```

2. Desde otro dispositivo, abrir:
   ```
   http://[tu-ip]:8501
   ```

   Ejemplo: `http://192.168.1.100:8501`

### Túnel Público (Opcional)

Usar `ngrok` para acceso externo:
```bash
ngrok http 8501
```

---

## 🎓 Preguntas de Ejemplo

### Sobre Carreras
```
- "Cuéntame sobre Big Data"
- "Información sobre Ciberseguridad"
- "Qué hace un técnico en Inteligencia Artificial?"
- "Cuánto dura la carrera de Desarrollo de Software?"
```

### Sobre ITSE
```
- "¿Qué es CAIPI?"
- "Reconocimientos del ITSE"
- "Alianzas estratégicas"
- "Inserción laboral de egresados"
```

### Sobre Inscripción
```
- "Cómo me inscribo?"
- "Requisitos para estudiar"
- "Becas disponibles"
- "Cuándo son las inscripciones?"
```

### Sobre Contacto
```
- "Dónde está el ITSE?"
- "Teléfono de contacto"
- "Correo electrónico"
```

---

## 🛑 Detener la Aplicación

### Método 1: Terminal

Presiona `Ctrl + C` en la terminal donde está ejecutándose

### Método 2: Cerrar Ventana

Simplemente cierra la ventana del navegador y la terminal

### Método 3: Task Manager (Windows)

1. Abrir Task Manager
2. Buscar proceso `python.exe` o `streamlit`
3. Finalizar proceso

---

## 📞 Soporte

### Problemas Técnicos

1. Revisar logs en la terminal
2. Verificar que todas las dependencias están instaladas
3. Verificar que el modelo existe en la ubicación correcta

### Documentación Adicional

- **README.md**: Guía general del proyecto
- **LOG.txt**: Historial de desarrollo
- **INSTRUCCIONES_REENTRENAMIENTO.md**: Cómo re-entrenar el modelo

---

**Última actualización:** Noviembre 2025
**Versión del modelo:** modelo_bert_tyr_4358
