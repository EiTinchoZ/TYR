# 🚀 INSTRUCCIONES: Re-entrenar BERT con Dataset Expandido (4358 ejemplos)

## ✅ LO QUE YA HICIMOS

1. **Expandimos el dataset de 1835 a 4358 ejemplos**
   - Archivo generado: `Dataset_TYR_3000_FINAL.json`
   - Incluye 2499 nuevas preguntas sobre carreras
   - Agregadas variaciones como "Cuéntame sobre...", "Qué es...", etc.
   - Información actualizada v3: CAIPI, CIIECYT, reconocimientos

2. **Preprocesamos el dataset**
   - Train: 3050 ejemplos (70%)
   - Val: 654 ejemplos (15%)
   - Test: 654 ejemplos (15%)

## 🎯 LO QUE DEBES HACER AHORA

### OPCIÓN A: Entrenar en Google Colab con GPU (RECOMENDADO - 15-20 minutos)

#### Paso 1: Abrir Google Colab
1. Ve a https://colab.research.google.com/
2. Inicia sesión con tu cuenta de Google
3. Click en **File → Upload notebook**
4. Sube el archivo: `TYR_REENTRENAMIENTO_4358_Colab.ipynb`

#### Paso 2: Activar GPU
1. En el notebook, click en **Runtime → Change runtime type**
2. En "Hardware accelerator" selecciona **T4 GPU**
3. Click **Save**

#### Paso 3: Subir Dataset
1. En el panel izquierdo, click en el icono de carpeta 📁
2. Click en el botón de subir archivo ⬆️
3. Sube el archivo: `Dataset_TYR_3000_FINAL.json`
4. Espera a que termine de subir (138 KB)

#### Paso 4: Ejecutar Notebook
1. Ve a **Runtime → Run all** (o presiona Ctrl+F9)
2. Espera 15-20 minutos mientras entrena
3. Verás el progreso en tiempo real

#### Paso 5: Descargar Modelo Entrenado
1. Cuando termine, verás el archivo `modelo_bert_tyr_4358.zip`
2. Click derecho → **Download**
3. Descarga el archivo a tu PC

#### Paso 6: Instalar Modelo en tu Proyecto
1. Descomprime `modelo_bert_tyr_4358.zip`
2. Copia la carpeta `modelo_bert_tyr_4358` a:
   ```
   C:\Users\mbund\Escritorio\mi-claude\GladOS Chatbot PLN\TYR\
   ```

---

### OPCIÓN B: Entrenar en tu PC con CPU (NO RECOMENDADO - 2-4 horas)

Si prefieres entrenar en tu PC (será MUY LENTO):

```bash
cd "C:\Users\mbund\Escritorio\mi-claude\GladOS Chatbot PLN\TYR"
python bert_training.py
```

⚠️ **ADVERTENCIA:** Sin GPU, el entrenamiento puede tomar **2-4 horas**. Se recomienda usar Google Colab.

---

## 📋 DESPUÉS DEL ENTRENAMIENTO

Una vez que tengas el modelo entrenado (`modelo_bert_tyr_4358`), debes actualizar el chatbot:

### 1. Actualizar tyr_chatbot.py para usar el nuevo modelo

Busca la línea que dice:
```python
self.model_path = "modelo_bert_tyr_1500"
```

Cámbiala por:
```python
self.model_path = "modelo_bert_tyr_4358"
```

### 2. Actualizar la base de conocimiento con información v3

Agregar información sobre:
- CAIPI (Centro de Atención Integral a la Primera Infancia)
- CIIECYT (Centro de Investigación e Innovación)
- Reconocimientos internacionales (Foro Económico Mundial, Unión Europea)
- Alianzas estratégicas (Canal de Panamá, Copa Airlines)
- Indicadores de éxito 2025 (80% inserción laboral)

### 3. Probar el chatbot

Ejecuta Streamlit y prueba con preguntas que antes fallaban:

```bash
cd "C:\Users\mbund\Escritorio\mi-claude\GladOS Chatbot PLN\TYR"
streamlit run tyr_app.py
```

Preguntas de prueba:
- "Cuéntame sobre Big Data"
- "Qué es CAIPI?"
- "Reconocimientos del ITSE"
- "Alianzas con empresas"
- "Qué es CIIECYT?"

---

## 📊 RESULTADOS ESPERADOS

Con el nuevo modelo deberías ver:

✅ **Antes:** "Cuéntame sobre Big Data" → fuera_dominio (99.7%)
✅ **Después:** "Cuéntame sobre Big Data" → informacion_carreras (alta confianza)

✅ Mejor comprensión de variaciones de preguntas
✅ Respuestas sobre CAIPI, CIIECYT, reconocimientos
✅ Mayor inteligencia general del chatbot

---

## 🆘 PROBLEMAS COMUNES

### "No tengo cuenta de Google"
- Crea una cuenta gratuita en https://accounts.google.com/signup

### "No sé cómo descomprimir el archivo"
- Click derecho en `modelo_bert_tyr_4358.zip` → **Extraer aquí**

### "El modelo no se carga en el chatbot"
- Verifica que la carpeta `modelo_bert_tyr_4358` esté en la ruta correcta
- Verifica que contenga los archivos: `config.json`, `pytorch_model.bin`, `label_map.json`

---

## 📞 SIGUIENTE PASO

Una vez que hayas entrenado el modelo en Colab y lo hayas descargado, **avísame** para que actualice el chatbot con:
1. El nuevo modelo
2. La base de conocimiento v3
3. Pruebas finales

---

**Autor:** Martín Bundy
**Carrera:** Técnico Superior en Inteligencia Artificial
**Instituto:** ITSE Panamá
**Fecha:** Noviembre 2025
