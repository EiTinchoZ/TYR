# 📚 Guía Rápida: Reentrenamiento TYR en Google Colab

**Archivo notebook:** `TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb`

---

## 🎯 Objetivo

Reentrenar el modelo BERT de TYR con la nueva intención `informacion_institucional` que incluye 201 nuevas preguntas sobre el ITSE.

---

## 📋 ANTES DE EMPEZAR

### 1️⃣ Archivos que necesitas

Este archivo se subirá directamente a Colab (no necesitas Google Drive):

```
📄 Dataset_TYR_3000_FINAL.json  (desde TYR/)
```

**Ubicación en tu PC:**
- `Dataset_TYR_3000_FINAL.json` → `TYR/Dataset_TYR_3000_FINAL.json`

Lo subirás en el PASO 3 del notebook.

---

## 🚀 PASOS PARA REENTRENAR

### 1️⃣ Abrir Google Colab

1. Ve a: https://colab.research.google.com/
2. Sube el notebook: `TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb`
   - Click en "File" → "Upload notebook"
   - Selecciona el archivo `.ipynb`

### 2️⃣ Activar GPU (MUY IMPORTANTE)

1. Click en: **Runtime** → **Change runtime type**
2. Selecciona: **T4 GPU**
3. Click en: **Save**

⚠️ **Sin GPU el entrenamiento tomará horas en vez de minutos**

### 3️⃣ Subir archivos a Colab

En el **PASO 3** del notebook:
1. Click en el ícono de carpeta 📁 (panel izquierdo)
2. Click en el ícono de subir archivo ⬆️
3. Selecciona el archivo:
   - `Dataset_TYR_3000_FINAL.json`
4. Espera a que suba

### 4️⃣ Ejecutar el notebook

**IMPORTANTE: Ejecutar paso a paso (NO usar "Run all")**
- Presiona `Shift + Enter` en cada celda
- Lee las instrucciones en cada paso
- **PASO 12** te mostrará si el modelo funciona ANTES de guardarlo
- **PASO 14** verificará que los pesos guardados funcionen correctamente
- Solo descarga si ambos pasos muestran 5/6 o 6/6 correctas

### 5️⃣ Monitorear el progreso

Verás barras de progreso que indican:
- **Epoch 1/4** - Primera pasada por los datos
- **Loss** - Debe bajar (ej: 0.5 → 0.2 → 0.1)
- **Accuracy** - Debe subir (ej: 0.85 → 0.92 → 0.96)

**Tiempo estimado con GPU T4:** 15-25 minutos

---

## 📊 MÉTRICAS ESPERADAS

Al final del entrenamiento deberías ver:

```
✅ ACCURACY:   >0.95   (95%+)
✅ F1-SCORE:   >0.94   (94%+)
✅ PRECISION:  >0.93   (93%+)
✅ RECALL:     >0.93   (93%+)
```

Si las métricas son más bajas:
- ❌ Verifica que subiste los archivos correctos
- ❌ Verifica que el dataset tenga 4,559 ejemplos
- 🔄 Intenta entrenar por 5 épocas en vez de 4

---

## 💾 DESPUÉS DEL ENTRENAMIENTO

### 1️⃣ Descargar los pesos del modelo

El modelo se guardó como archivo de pesos: `modelo_tyr_10_clases_PESOS_CORRECTOS.pth`

**Archivos generados:**
- ✅ `modelo_tyr_10_clases_PESOS_CORRECTOS.pth` (~420 MB - pesos del modelo)
- ✅ `label_map.json` (mapa de etiquetas)

**Cómo descargar:**
1. Click en el ícono de carpeta 📁 (panel izquierdo)
2. Busca: `modelo_tyr_10_clases_PESOS_CORRECTOS.pth`
3. Click derecho → **Download**
4. También descarga: `label_map.json`
5. Espera a que descargue (~420 MB)

---

### 2️⃣ Cargar los pesos en tu PC

Copia el archivo descargado a la carpeta TYR:

```bash
# En la carpeta TYR/

1. Copia el archivo descargado:
   modelo_tyr_10_clases_PESOS_CORRECTOS.pth  →  TYR/

2. Ejecuta el script de carga de pesos:
   python cargar_pesos_nuevo_modelo.py

3. El script cargará los pesos en: modelo_bert_tyr_4358/
```

---

### 3️⃣ Verificar que funcione

#### **Método 1: Solo backend**

```bash
# En la carpeta TYR/
cd backend
python main.py
```

Deberías ver:
```
✅ Modelo BERT cargado: dccuchile/bert-base-spanish-wwm-cased
✅ Precisión del modelo: 98.93%
✅ Device: cpu
✅ Modelo TYR inicializado correctamente
```

Si ves errores de "size mismatch", el modelo viejo sigue ahí.

#### **Método 2: Frontend + Backend**

**Opción A: Usando los .bat**
```
1. Doble click en: run_backend.bat
2. Doble click en: run_frontend.bat
3. Abre: http://localhost:5173
```

**Opción B: Manual**
```bash
# Terminal 1:
cd backend
python main.py

# Terminal 2:
cd Figma
npm run dev
```

---

### 4️⃣ Probar preguntas institucionales

En el chatbot, prueba estas preguntas:

**Preguntas sobre historia:**
- ❓ "Cuándo se fundó el ITSE?"
- ❓ "En qué año se creó el ITSE?"
- ❓ "Qué ley creó el ITSE?"

**Preguntas sobre reconocimientos:**
- ❓ "Qué reconocimientos tiene el ITSE?"
- ❓ "El Foro Económico Mundial habló del ITSE?"
- ❓ "Qué dijo la Unión Europea sobre el ITSE?"

**Preguntas sobre alianzas:**
- ❓ "El MIT colabora con el ITSE?"
- ❓ "Copa Airlines tiene alianza con el ITSE?"
- ❓ "El Canal de Panamá trabaja con el ITSE?"

**Preguntas sobre empleabilidad:**
- ❓ "Cuántos egresados consiguen trabajo?"
- ❓ "Qué porcentaje de estudiantes se emplean?"
- ❓ "Los graduados del ITSE trabajan?"

**Preguntas sobre expansión:**
- ❓ "Qué es el CAIPI?"
- ❓ "Va a haber residencia estudiantil?"
- ❓ "Qué viene en la segunda fase?"

**✅ Respuesta esperada:**

Todas estas preguntas deben responder con la respuesta institucional completa que incluye:
- 📜 Historia y Creación
- 🎯 Misión y Visión
- 🌍 Modelo Educativo Internacional
- 🏫 4 Escuelas Especializadas
- 🏆 Reconocimientos Internacionales
- 🤝 Alianzas Estratégicas
- 📊 Empleabilidad
- 🏗️ Segunda Fase 2025
- 👥 Autoridades

---

## ❌ SOLUCIÓN DE PROBLEMAS

### Error: "RuntimeError: size mismatch"

**Causa:** El modelo viejo (9 clases) todavía está en la carpeta

**Solución:**
1. Elimina completamente la carpeta `modelo_bert_tyr_4358`
2. Copia el nuevo modelo
3. Reinicia el backend

---

### Error: "FileNotFoundError: label_map.json"

**Causa:** El modelo no se descargó completo

**Solución:**
1. Verifica que la carpeta del modelo tenga todos los archivos
2. Especialmente `label_map.json`
3. Si falta, cópialo desde `TYR/data/label_map.json`

---

### El modelo clasifica mal las preguntas institucionales

**Causa:** El modelo no se entrenó correctamente

**Solución:**
1. Verifica las métricas finales (deben ser >95%)
2. Si son bajas, reentrena con 5 épocas
3. Verifica que el dataset tenga 4,559 ejemplos

---

### El entrenamiento es muy lento

**Causa:** No activaste GPU en Colab

**Solución:**
1. Ve a: Runtime → Change runtime type
2. Selecciona: T4 GPU
3. Reinicia y corre de nuevo

---

### El backend dice "98.93%" pero las respuestas son malas

**Causa:** Ese 98.93% es del entrenamiento anterior, no del nuevo modelo

**Solución:**
1. Verifica que la carpeta `modelo_bert_tyr_4358` sea la nueva
2. Debe tener 10 clases, no 9
3. Abre `modelo_bert_tyr_4358/config.json` y busca `"num_labels": 10`

---

## 📞 AYUDA ADICIONAL

Si algo falla:

1. **Revisa el log de entrenamiento en Colab**
   - Busca mensajes de error en rojo
   - Copia el error completo

2. **Verifica las rutas en el notebook**
   - En la celda 3, verifica:
     ```python
     DATASET_PATH = '/content/drive/MyDrive/TYR_Reentrenamiento/Dataset_TYR_3000_FINAL.json'
     LABEL_MAP_PATH = '/content/drive/MyDrive/TYR_Reentrenamiento/label_map.json'
     ```

3. **Verifica que los archivos se subieron correctamente**
   - Dataset debe tener 4,559 ejemplos
   - Label map debe tener 10 intenciones

---

## ✅ CHECKLIST FINAL

Antes de terminar, verifica:

- [ ] Modelo entrenado con accuracy >95%
- [ ] Modelo descargado desde Google Drive
- [ ] Modelo reemplazado en carpeta `modelo_bert_tyr_4358`
- [ ] Backend inicia sin errores
- [ ] Frontend muestra el chat correctamente
- [ ] Preguntas institucionales responden correctamente
- [ ] El intent detectado es `informacion_institucional`

---

## 🎉 ¡LISTO!

Tu chatbot TYR ahora puede responder preguntas sobre:
- ✅ Historia y fundación del ITSE
- ✅ Misión, visión y modelo educativo
- ✅ Reconocimientos internacionales
- ✅ Alianzas con MIT, Columbia, Canal de Panamá, Copa Airlines
- ✅ Empleabilidad y estadísticas
- ✅ Segunda fase y expansión
- ✅ Autoridades y estructura

---

**Fecha de actualización:** 26 de noviembre de 2025

**Dataset:** 4,559 ejemplos (4,358 + 201 nuevos)

**Intenciones:** 10 (9 + informacion_institucional)

**Modelo base:** dccuchile/bert-base-spanish-wwm-cased
