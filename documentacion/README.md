# 📚 Documentación del Proyecto TYR

Este directorio contiene toda la documentación técnica y reportes del proyecto TYR - Asistente Virtual ITSE.

---

## 📋 Índice de Documentación

### 📊 Documento Principal

- **[PROYECTO_TYR_LOG_COMPLETO.md](PROYECTO_TYR_LOG_COMPLETO.md)** - Log maestro completo del proyecto
  - Historial completo de desarrollo
  - Todas las sesiones documentadas (1-6 + mejoras 1-5)
  - Métricas finales y resultados
  - Evolución del proyecto

---

### 🏗️ Arquitectura y Diseño

- **[ARQUITECTURA_SISTEMA.md](ARQUITECTURA_SISTEMA.md)** - Documentación de arquitectura
  - 6 diagramas Mermaid del sistema
  - Arquitectura de 4 capas
  - Flujo de procesamiento
  - Componentes del sistema
  - Stack tecnológico
  - Base de datos y almacenamiento

---

### 📝 Reportes de Sesiones

Directorio: **[reportes/](reportes/)**

1. **[REPORTE_SESION1_TESTS.md](reportes/REPORTE_SESION1_TESTS.md)**
   - Tests automatizados con pytest
   - 59 tests implementados (100% passing)
   - Coverage: 73.75%
   - Fixtures y configuración

2. **[REPORTE_SESION2_JSON.md](reportes/REPORTE_SESION2_JSON.md)**
   - Externalización de base de conocimiento
   - 16 carreras + 9 respuestas a JSON
   - Sistema de fallback
   - ~91 KB de datos externalizados

3. **[REPORTE_SESION3_VISUALIZACIONES.md](reportes/REPORTE_SESION3_VISUALIZACIONES.md)**
   - Matriz de confusión (99.60% accuracy)
   - Gráficas de evolución de modelos
   - Distribución de intenciones
   - Script de generación automatizado

4. **[REPORTE_SESION4_ARQUITECTURA.md](reportes/REPORTE_SESION4_ARQUITECTURA.md)**
   - 6 diagramas Mermaid creados
   - 8 badges profesionales
   - Documentación de arquitectura completa
   - README mejorado

5. **[REPORTE_SESION5_DEMO_FINAL.md](reportes/REPORTE_SESION5_DEMO_FINAL.md)**
   - 7 screenshots profesionales
   - Sección Demo completa
   - LICENSE MIT
   - Revisión final y preparación GitHub

---

### 📊 Visualizaciones

Directorio: **[visualizaciones/](visualizaciones/)**

- `matriz_confusion_4358.png` - Matriz de confusión 9x9
- `distribucion_intenciones.png` - Distribución del dataset
- `evolucion_modelos.png` - Comparativa v1→v2→v3
- `metricas_clasificacion.txt` - Classification report detallado

**Métricas del modelo:**
- Accuracy: 99.60% en muestra de validación
- 4,358 ejemplos en total
- 9 intenciones clasificadas

---

### 📸 Screenshots del Sistema

Directorio: **[screenshots/](screenshots/)**

- `01_pantalla_inicial.png` - Interfaz principal
- `02_consulta_bigdata.png` - Consulta sobre carrera
- `03_consulta_caipi.png` - Información institucional
- `04_consulta_inscripcion.png` - Proceso de admisión
- `05_consulta_ciberseguridad.png` - Segunda carrera
- `07_tolerancia_errores.png` - Demostración de robustez
- `08_metadata.png` - Métricas del sistema

Total: **7 screenshots profesionales** (1.9 MB)

---

### 📖 Guías de Usuario

Directorio: **[guias/](guias/)**

- **[GUIA_EJECUCION.md](guias/GUIA_EJECUCION.md)**
  - Cómo ejecutar la aplicación
  - Requisitos del sistema
  - Resolución de problemas

- **[INSTRUCCIONES_REENTRENAMIENTO.md](guias/INSTRUCCIONES_REENTRENAMIENTO.md)**
  - Cómo re-entrenar el modelo
  - Modificar el dataset
  - Google Colab workflow

---

## 📊 Resumen de Documentación

| Categoría | Archivos | Descripción |
|-----------|----------|-------------|
| **Principal** | 1 | Log maestro completo |
| **Arquitectura** | 1 | Diseño del sistema |
| **Reportes** | 5 | Sesiones de mejora |
| **Visualizaciones** | 4 | Gráficas y matrices |
| **Screenshots** | 7 | Demo del sistema |
| **Guías** | 2 | Manuales de usuario |
| **TOTAL** | **20 documentos** | Documentación completa |

---

## 🎯 Navegación Rápida

**Para entender el proyecto:**
1. Leer [PROYECTO_TYR_LOG_COMPLETO.md](PROYECTO_TYR_LOG_COMPLETO.md)
2. Ver [ARQUITECTURA_SISTEMA.md](ARQUITECTURA_SISTEMA.md)
3. Revisar screenshots en [screenshots/](screenshots/)

**Para usar el sistema:**
1. Leer [guias/GUIA_EJECUCION.md](guias/GUIA_EJECUCION.md)
2. Consultar README principal en raíz

**Para desarrollo:**
1. Ver [reportes/](reportes/) para entender las mejoras
2. Revisar tests en `/tests/`
3. Consultar [guias/INSTRUCCIONES_REENTRENAMIENTO.md](guias/INSTRUCCIONES_REENTRENAMIENTO.md)

---

## 📈 Métricas Finales del Proyecto

| Métrica | Resultado |
|---------|-----------|
| **Accuracy** | 98.93% (modelo) / 99.60% (validación) |
| **F1-Score** | 98.92% |
| **Tests** | 59/59 passing (100%) |
| **Coverage** | 73.75% |
| **Dataset** | 4,358 ejemplos |
| **Intenciones** | 9 categorías |
| **Carreras** | 16 del ITSE |
| **Calificación** | 9.8/10 ⭐ |

---

## 🏆 Logros Documentados

1. ✅ Tests automatizados (Sesión 1)
2. ✅ Base externalizada a JSON (Sesión 2)
3. ✅ Visualizaciones profesionales (Sesión 3)
4. ✅ Diagramas de arquitectura (Sesión 4)
5. ✅ Demo visual completo (Sesión 5)

---

**Última actualización:** 24 de Noviembre 2025
**Estado:** ✅ Documentación completa
**Proyecto:** TYR - Asistente Virtual ITSE
**Autor:** Martín Bundy
