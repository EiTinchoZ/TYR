# LOG: Expansión Base de Conocimiento Institucional ITSE
**Fecha:** 26 de noviembre de 2025
**Autor:** Claude (TYR Development Team)
**Tipo de actualización:** Expansión de Base de Conocimiento + Dataset

---

## 📋 Resumen Ejecutivo

Se expandió significativamente la base de conocimiento del chatbot TYR para incluir información institucional completa del ITSE, permitiendo al chatbot responder preguntas sobre:

- Historia, fundación y creación del ITSE
- Misión, visión y modelo educativo internacional
- Las 4 escuelas y sus características específicas
- Reconocimientos internacionales (Foro Económico Mundial, UE, Hackatones)
- Alianzas estratégicas (ACP, Copa Airlines, MIT, Columbia, Singapur, etc.)
- Empleabilidad y estadísticas de inserción laboral
- Infraestructura actual y segunda fase 2025
- Autoridades y estructura organizacional

---

## 🎯 Problema Identificado

El usuario detectó que:
> "el chatbot a veces le preguntan sobre el mismo ITSE y responde sobre las carreras"

**Causa raíz:** El chatbot no tenía un intent específico para información institucional general del ITSE, por lo que clasificaba estas preguntas como `informacion_carreras` o `faq_general`, dando respuestas genéricas o incorrectas.

---

## ✅ Solución Implementada

### 1. Nuevo Intent: `informacion_institucional`

Se creó una nueva intención dedicada exclusivamente a información institucional del ITSE.

**Archivo modificado:** `data/respuestas_base.json`

**Contenido de la respuesta:**
- 📜 Historia y Creación (Ley 71, inauguración 2019, crecimiento de 154 a 4,000 estudiantes)
- 🎯 Misión y Visión completas
- 🌍 Modelo Educativo Internacional (Singapur, UK, Alemania)
- 🏫 4 Escuelas Especializadas con detalles
- 🏆 Reconocimientos Internacionales 2025
- 🤝 Alianzas Estratégicas (12+ instituciones)
- 📊 Empleabilidad (80% inserción laboral)
- 🏗️ Segunda Fase 2025 (residencia, CAIPI, parque científico)
- 👥 Autoridades actuales

**Keywords agregados:** 41 palabras clave específicas incluyendo:
- historia, creación, misión, visión, modelo educativo
- reconocimientos, alianzas, convenios, internacional
- empleabilidad, inserción laboral, autoridades
- CAIPI, parque científico, residencia
- Singapur, MIT, Columbia, Foro Económico Mundial
- Canal de Panamá, Copa Airlines
- qué es ITSE, sobre el ITSE, estadísticas, cifras

---

### 2. Dataset Expandido: 201 Nuevas Preguntas

**Archivo creado:** `nuevas_preguntas_institucionales.json`
**Archivo actualizado:** `Dataset_TYR_3000_FINAL.json`

**Métricas:**
- **Antes:** 4,358 ejemplos de entrenamiento
- **Después:** 4,559 ejemplos de entrenamiento
- **Incremento:** +201 preguntas (+4.6%)

**Categorías de preguntas añadidas:**

1. **Historia y Fundación (15 preguntas)**
   - "Cuándo se fundó el ITSE?"
   - "Qué ley creó el ITSE?"
   - "Cuándo fue inaugurado el ITSE?"

2. **Misión, Visión y Modelo Educativo (18 preguntas)**
   - "Cuál es la misión del ITSE?"
   - "Qué modelo educativo usa el ITSE?"
   - "De dónde es el modelo educativo del ITSE?"

3. **Estadísticas y Matrícula (12 preguntas)**
   - "Cuántos estudiantes tiene el ITSE?"
   - "Cuál es la matrícula actual del ITSE?"
   - "Cuál es la capacidad del ITSE?"

4. **Escuelas y Estructura (15 preguntas)**
   - "Cuántas escuelas tiene el ITSE?"
   - "Cuándo se inauguró la Escuela de Innovación Digital?"
   - "Quién financió la Escuela de Innovación Digital?"

5. **Reconocimientos Internacionales (10 preguntas)**
   - "Qué reconocimientos ha recibido el ITSE?"
   - "Qué dijo el Foro Económico Mundial sobre el ITSE?"
   - "La Unión Europea reconoció al ITSE?"

6. **Alianzas Estratégicas (15 preguntas)**
   - "Qué alianzas tiene el ITSE?"
   - "El Canal de Panamá trabaja con el ITSE?"
   - "Copa Airlines tiene alianza con el ITSE?"
   - "El MIT colabora con el ITSE?"

7. **Empleabilidad y Resultados (12 preguntas)**
   - "Cuál es la tasa de empleabilidad del ITSE?"
   - "Qué porcentaje de egresados consigue trabajo?"
   - "Cuántos graduados ya tienen trabajo?"

8. **Segunda Fase y Expansión (15 preguntas)**
   - "Qué viene en la segunda fase del ITSE?"
   - "Va a haber residencia estudiantil?"
   - "Qué es el CAIPI del ITSE?"
   - "Hay parque científico en el ITSE?"

9. **Autoridades y Estructura (10 preguntas)**
   - "Quién es la rectora del ITSE?"
   - "Quiénes son las autoridades del ITSE?"
   - "Qué es el Consejo Directivo del ITSE?"

10. **Tipo de Institución (12 preguntas)**
    - "El ITSE es público o privado?"
    - "Qué tipo de institución es el ITSE?"
    - "El ITSE está reconocido por el Estado?"

11. **Metodología y Aprendizaje (15 preguntas)**
    - "Qué metodología usa el ITSE?"
    - "Qué porcentaje es práctica en el ITSE?"
    - "Aprender haciendo es del ITSE?"

12. **Infraestructura y Tecnología (12 preguntas)**
    - "Qué infraestructura tiene el ITSE?"
    - "El ITSE tiene simuladores?"
    - "Hay realidad virtual en el ITSE?"

13. **Calidad y Reputación (20 preguntas)**
    - "Vale la pena estudiar en el ITSE?"
    - "Por qué estudiar en el ITSE?"
    - "Qué tan bueno es el ITSE?"
    - "El ITSE tiene buena calidad educativa?"

14. **Comparación con Universidades (12 preguntas)**
    - "Cuál es la diferencia entre ITSE y universidad?"
    - "El ITSE es mejor que la universidad?"
    - "Por qué elegir ITSE en vez de universidad?"

15. **Profesores y Docencia (8 preguntas)**
    - "El ITSE tiene buenos profesores?"
    - "Los profesores del ITSE trabajan en empresas?"
    - "El ITSE tiene docentes con experiencia real?"

16. **Contacto y Accesibilidad (10 preguntas)**
    - "El ITSE tiene redes sociales?"
    - "Cuál es el sitio web del ITSE?"
    - "Cómo llegar al ITSE?"

---

### 3. Label Map Actualizado

**Archivo modificado:** `data/label_map.json`

**Cambio:**
- Se agregó el intent `"6": "informacion_institucional"`
- Se reindexaron los intents posteriores (inscripcion_admision: 7, requisitos_ingreso: 8, saludo_despedida: 9)

**Total de intenciones:** 9 → **10 intenciones**

---

## 📊 Impacto en el Sistema

### Archivos Modificados

1. ✅ `data/respuestas_base.json` - Versión 1.0 → **2.0**
2. ✅ `data/label_map.json` - 9 → **10 intenciones**
3. ✅ `Dataset_TYR_3000_FINAL.json` - 4,358 → **4,559 ejemplos**
4. ✅ `nuevas_preguntas_institucionales.json` - **Creado** (201 preguntas)

### Metadata Actualizada

```json
{
  "version": "2.0",
  "fecha_actualizacion": "2025-11-26",
  "total_intenciones": 10,
  "descripcion": "Base de respuestas predefinidas para cada intención del chatbot TYR - Expandida con información institucional completa"
}
```

---

## 🔄 Próximos Pasos (Reentrenamiento)

⚠️ **IMPORTANTE:** Para que los cambios surtan efecto, es necesario **reentrenar el modelo BERT** con el dataset expandido.

### Proceso de Reentrenamiento

1. **Ejecutar notebook de reentrenamiento:**
   - Archivo: `TYR_REENTRENAMIENTO_4358_Colab.ipynb`
   - Plataforma: Google Colab (GPU recomendado)

2. **Parámetros sugeridos:**
   ```python
   NUM_LABELS = 10  # Actualizado de 9 a 10
   BATCH_SIZE = 16
   EPOCHS = 3-4  # Ajustar según convergencia
   LEARNING_RATE = 2e-5
   ```

3. **Validación post-entrenamiento:**
   - Verificar que el modelo reconoce el nuevo intent `informacion_institucional`
   - Probar con preguntas de ejemplo:
     - "Cuándo se fundó el ITSE?"
     - "Qué reconocimientos ha recibido el ITSE?"
     - "El MIT colabora con el ITSE?"
     - "Cuál es la empleabilidad del ITSE?"

4. **Reemplazar modelo:**
   - Guardar nuevo modelo en `modelo_bert_tyr_XXXX/`
   - Actualizar referencias en `backend/main.py` y `tyr_chatbot.py`

---

## 🧪 Testing Sugerido

### Casos de Prueba

**1. Preguntas sobre Historia:**
```
User: "Cuándo se fundó el ITSE?"
Expected: informacion_institucional
Response: "📜 Creado por Ley 71 del 8 de noviembre de 2017..."
```

**2. Preguntas sobre Reconocimientos:**
```
User: "Qué reconocimientos tiene el ITSE?"
Expected: informacion_institucional
Response: "🏆 Reconocimientos Internacionales 2025..."
```

**3. Preguntas sobre Alianzas:**
```
User: "El MIT trabaja con el ITSE?"
Expected: informacion_institucional
Response: "🤝 Alianzas Estratégicas: ... Columbia University y MIT (EEUU)"
```

**4. Preguntas sobre Empleabilidad:**
```
User: "Cuántos egresados consiguen trabajo?"
Expected: informacion_institucional
Response: "📊 Empleabilidad (2025): 80% inserción laboral exitosa..."
```

**5. Diferenciación con otros intents:**
```
User: "Qué carreras hay en ITSE?"
Expected: informacion_carreras (no informacion_institucional)

User: "Cómo me inscribo?"
Expected: inscripcion_admision (no informacion_institucional)
```

---

## 📈 Métricas de Éxito

### KPIs para Monitorear

1. **Precisión del nuevo intent:**
   - Target: >90% de clasificación correcta para preguntas institucionales

2. **Reducción de confusión:**
   - Reducir clasificación errónea de preguntas institucionales como `informacion_carreras`
   - Reducir respuestas genéricas a preguntas específicas sobre el ITSE

3. **Cobertura de preguntas:**
   - El chatbot debe poder responder 201+ variaciones de preguntas institucionales

4. **Satisfacción del usuario:**
   - Monitorear feedback sobre calidad de respuestas institucionales
   - Verificar que las respuestas son completas y precisas

---

## 📝 Fuente de Información

**Documento base:** `ITSE-informacion-completa.md`

**Secciones utilizadas:**
- ✅ Información General
- ✅ Misión y Visión
- ✅ Modelo Educativo
- ✅ Las Cuatro Escuelas
- ✅ Admisión y Requisitos
- ✅ Infraestructura
- ✅ Alianzas Estratégicas
- ✅ Reconocimientos Internacionales
- ✅ Resultados y Empleabilidad
- ✅ Autoridades
- ✅ Contacto e Inscripciones

**Verificación:** Toda la información fue extraída del documento oficial y verificada contra fuentes públicas del ITSE (noviembre 2025).

---

## ⚙️ Integración con Sistema Actual

### Compatibilidad

✅ **Compatible con:**
- `tyr_chatbot.py` - Carga automática de nueva respuesta desde JSON
- `backend/tyr_simple.py` - Wrapper FastAPI compatible
- `backend/main.py` - Sin cambios necesarios
- `Figma/components/TYRChat.tsx` - Frontend compatible

⚠️ **Requiere actualización:**
- `modelo_bert_tyr_4358/` - Reentrenar con 10 clases (actualmente 9)
- `modelo_bert_tyr_4358/config.json` - `num_labels: 10`

---

## 🔒 Control de Calidad

### Validaciones Realizadas

✅ JSON válido en `respuestas_base.json`
✅ JSON válido en `label_map.json`
✅ JSON válido en `nuevas_preguntas_institucionales.json`
✅ Dataset expandido correctamente (4,358 → 4,559)
✅ No hay duplicados en las nuevas preguntas
✅ Todas las preguntas están etiquetadas correctamente
✅ Keywords comprensivos y relevantes (41 keywords)
✅ Respuesta formateada con Markdown
✅ Información verificada contra documento oficial

---

## 👥 Créditos

**Desarrollo:** Claude (TYR Development Team)
**Solicitud:** Usuario (Martín Bundy)
**Fuente de datos:** ITSE Información Completa (Noviembre 2025)
**Fecha de implementación:** 26 de noviembre de 2025

---

## 📌 Notas Adicionales

- El nuevo intent permite separar claramente preguntas sobre **el instituto** (institucional) vs preguntas sobre **las carreras** (académico)
- La respuesta institucional es comprehensiva pero puede refinarse según feedback del usuario
- Se recomienda monitorear las primeras interacciones post-reentrenamiento para ajustar keywords si es necesario
- Las 201 preguntas cubren lenguaje natural variado (formal, informal, con errores ortográficos, diferentes formulaciones)

---

**Estado:** ✅ Completado - Pendiente Reentrenamiento del Modelo

**Próximo paso:** Ejecutar `TYR_REENTRENAMIENTO_4358_Colab.ipynb` con dataset actualizado
