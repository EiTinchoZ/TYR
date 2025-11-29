# 📚 Base de Conocimiento TYR - Archivos JSON

**Proyecto:** TYR - Asistente Virtual ITSE
**Autor:** Martín Bundy
**Fecha de Externalización:** 23 de Noviembre 2025
**Versión:** 1.0

---

## 📋 Descripción

Este directorio contiene la base de conocimiento del chatbot TYR externalizada en archivos JSON para facilitar su mantenimiento y actualización sin necesidad de modificar el código fuente.

---

## 📁 Archivos

### 1. [`carreras_itse.json`](carreras_itse.json) (83 KB)

Contiene información completa de las **16 carreras** ofrecidas por ITSE.

**Estructura:**
```json
{
  "_metadata": {
    "version": "1.0",
    "fecha_actualizacion": "2025-11-23",
    "total_carreras": 16,
    "escuelas": ["Innovación Digital", "Tecnología Industrial", "Negocios", "Hospitalidad y Turismo"]
  },
  "nombre_carrera": {
    "nombre": "T.S. en Nombre Completo",
    "escuela": "Nombre de la Escuela",
    "creditos": 112,
    "duracion": {
      "diurna": "2 años 4 meses",
      "nocturna": "3 años"
    },
    "jornadas": ["diurna", "nocturna"],
    "aprendizaje": "Descripción de lo que aprenderás...",
    "campo_ocupacional": ["Cargo 1", "Cargo 2", ...],
    "enlace": "https://www.itse.ac.pa/..."
  }
}
```

**Carreras incluidas:**
- **Escuela de Innovación Digital** (4): Desarrollo de Software, Big Data, Ciberseguridad, Inteligencia Artificial
- **Escuela de Tecnología Industrial** (7): Electricidad Industrial, Mantenimiento de Aeronaves, Mantenimiento Industrial, Metalmecánicas, Automotriz Liviano, Automotriz Pesado, Construcción
- **Escuela de Negocios** (3): Gestión Ejecutiva Bilingüe, Operaciones Logísticas, Servicios Empresariales
- **Escuela de Hospitalidad y Turismo** (2): Artes Culinarias, Operaciones Hoteleras

**Claves de búsqueda:**
- `desarrollo de software`
- `big data`
- `ciberseguridad`
- `inteligencia artificial`
- `electricidad industrial`
- `mantenimiento de aeronaves`
- `mantenimiento industrial`
- `metalmecánicas`
- `automotriz liviano`
- `automotriz pesado`
- `construcción`
- `gestión ejecutiva`
- `operaciones logísticas`
- `servicios empresariales`
- `artes culinarias`
- `operaciones hoteleras`

---

### 2. [`respuestas_base.json`](respuestas_base.json) (8 KB)

Contiene las respuestas predefinidas para las **9 intenciones** del sistema BERT.

**Estructura:**
```json
{
  "_metadata": {
    "version": "1.0",
    "fecha_actualizacion": "2025-11-23",
    "total_intenciones": 9
  },
  "nombre_intencion": {
    "respuesta": "Texto de la respuesta con formato markdown...",
    "keywords": ["palabra1", "palabra2", ...]
  }
}
```

**Intenciones incluidas:**

| Intención | Descripción | Keywords principales |
|-----------|-------------|---------------------|
| `saludo_despedida` | Saludos y despedidas | hola, saludos, buenos días, gracias, adiós |
| `informacion_carreras` | Lista de todas las carreras | carreras, programas, técnicas, estudios |
| `inscripcion_admision` | Proceso de inscripción | inscripción, admisión, matricula, aplicar |
| `requisitos_ingreso` | Requisitos y documentos | requisitos, documentos, PIENSE, diploma |
| `horarios_duracion` | Horarios y duración de carreras | horarios, duración, tiempo, jornada |
| `becas_financiamiento` | Opciones de financiamiento | becas, financiamiento, IFARHU, BID |
| `contacto_ubicacion` | Contacto y ubicación del ITSE | contacto, teléfono, email, ubicación, dirección |
| `faq_general` | Información general del ITSE | información, datos, CAIPI, CIIECYT, reconocimientos |
| `fuera_dominio` | Consultas fuera del alcance | fuera, otro tema |

---

## 🔧 Uso en el Código

El chatbot carga estos archivos JSON automáticamente al inicializarse:

```python
# En tyr_chatbot.py
class TYR:
    def __init__(self, ...):
        # Carga automática desde JSON
        self.carreras_itse = self._cargar_carreras_desde_json()
        self.respuestas_base = self._cargar_respuestas_desde_json()
```

**Sistema de fallback:**
- Si los archivos JSON no se encuentran, el sistema usa versiones hardcodeadas en el código
- Esto garantiza que el chatbot siempre funciona, incluso sin los archivos JSON

---

## ✏️ Cómo Actualizar

### Actualizar Información de Carreras

1. Abrir [`carreras_itse.json`](carreras_itse.json)
2. Localizar la carrera a actualizar
3. Modificar los campos necesarios
4. Actualizar `_metadata.fecha_actualizacion`
5. Guardar el archivo
6. Reiniciar el chatbot

**Ejemplo:**
```json
"desarrollo de software": {
  "creditos": 115,  // Cambiar de 112 a 115
  "duracion": {
    "diurna": "2 años 6 meses",  // Actualizar duración
    "nocturna": "3 años"
  }
}
```

### Actualizar Respuestas Base

1. Abrir [`respuestas_base.json`](respuestas_base.json)
2. Localizar la intención a actualizar
3. Modificar el campo `respuesta` o `keywords`
4. Actualizar `_metadata.fecha_actualizacion`
5. Guardar el archivo
6. Reiniciar el chatbot

**Ejemplo:**
```json
"contacto_ubicacion": {
  "respuesta": "📍 **Contacto e Información ITSE:**\n\n📞 **Teléfono:** +507 524-4444\n...",
  "keywords": ["contacto", "teléfono", "email", "ubicación", "dirección"]
}
```

### Agregar Nueva Carrera

1. Abrir [`carreras_itse.json`](carreras_itse.json)
2. Agregar nueva entrada siguiendo la estructura existente
3. Actualizar `_metadata.total_carreras`
4. Actualizar `_metadata.fecha_actualizacion`
5. Guardar el archivo

**Template:**
```json
"nombre_clave_carrera": {
  "nombre": "T.S. en Nombre Completo",
  "escuela": "Nombre de la Escuela",
  "creditos": 0,
  "duracion": {
    "diurna": "X años",
    "nocturna": "Y años"
  },
  "jornadas": ["diurna", "nocturna"],
  "aprendizaje": "Descripción...",
  "campo_ocupacional": ["Cargo 1", "Cargo 2"],
  "enlace": "https://www.itse.ac.pa/..."
}
```

---

## ✅ Validación

Después de cualquier modificación, es importante validar que el chatbot sigue funcionando:

### 1. Validar formato JSON

```bash
# Verificar que el JSON es válido
python -m json.tool data/carreras_itse.json
python -m json.tool data/respuestas_base.json
```

### 2. Ejecutar tests

```bash
# Verificar que no se rompió nada
pytest tests/ -v
```

**Salida esperada:**
```
59 passed in 2.39s
```

### 3. Probar el chatbot

```bash
# Probar interactivamente
streamlit run tyr_app.py
```

---

## 🎯 Ventajas de la Externalización

### Antes (Hardcoded)
- ❌ Modificar información requería editar código Python
- ❌ Riesgo de introducir bugs al editar
- ❌ Necesitaba conocimientos de programación
- ❌ Difícil mantener actualizado
- ❌ No versionable independientemente

### Después (JSON)
- ✅ Modificar información solo requiere editar JSON
- ✅ Sin riesgo de romper el código
- ✅ No requiere conocimientos de programación
- ✅ Fácil de mantener y actualizar
- ✅ Versionable independientemente
- ✅ Puede ser actualizado por personal no técnico
- ✅ Sistema de fallback garantiza funcionamiento

---

## 📊 Métricas

| Métrica | Valor |
|---------|-------|
| **Carreras totales** | 16 |
| **Intenciones totales** | 9 |
| **Tamaño carreras_itse.json** | ~83 KB |
| **Tamaño respuestas_base.json** | ~8 KB |
| **Escuelas cubiertas** | 4 |
| **Tests passing** | 59/59 (100%) |

---

## 🔄 Historial de Versiones

### v1.0 - 23 de Noviembre 2025
- ✅ Externalización inicial de base de conocimiento
- ✅ 16 carreras migradas a JSON
- ✅ 9 respuestas base migradas a JSON
- ✅ Sistema de fallback implementado
- ✅ Tests validados (59/59 passing)
- ✅ Documentación completa

---

## 🐛 Solución de Problemas

### El chatbot no encuentra los archivos JSON

**Síntoma:** Log muestra "No se encontró data/carreras_itse.json, usando base hardcodeada"

**Solución:**
1. Verificar que los archivos existen en `data/`
2. Verificar que el directorio de trabajo es correcto
3. El chatbot funcionará con la base hardcodeada de todas formas

### Error al cargar JSON

**Síntoma:** Log muestra "Error cargando carreras desde JSON"

**Solución:**
1. Validar sintaxis JSON: `python -m json.tool data/carreras_itse.json`
2. Verificar encoding UTF-8
3. Corregir errores de sintaxis
4. El chatbot funcionará con la base hardcodeada de todas formas

### Tests fallan después de actualizar JSON

**Síntoma:** `pytest tests/ -v` muestra fallos

**Solución:**
1. Verificar que no se modificaron las claves principales
2. Verificar que el formato de respuestas es correcto
3. Ejecutar tests individuales para identificar el problema
4. Restaurar versión anterior del JSON y aplicar cambios gradualmente

---

## 📞 Soporte

Para preguntas o problemas con la base de conocimiento:

**Estudiante:** Martín Bundy
**Proyecto:** TYR - Asistente Virtual ITSE
**Email:** [tu-email@itse.ac.pa]

---

## 📚 Referencias

- [Especificación JSON](https://www.json.org/)
- [Documentación del Proyecto TYR](../README.md)
- [Tests Automatizados](../tests/README.md)

---

**Última actualización:** 23 de Noviembre 2025
**Versión:** 1.0
**Estado:** ✅ Producción
