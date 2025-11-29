# 🧪 Tests Automatizados - TYR

**Proyecto:** TYR - Asistente Virtual ITSE
**Autor:** Martín Bundy
**Framework:** pytest 7.4+
**Cobertura:** 33+ tests automatizados

---

## 📋 Contenido

- [Descripción](#-descripción)
- [Instalación](#-instalación)
- [Ejecución de Tests](#-ejecución-de-tests)
- [Estructura de Tests](#-estructura-de-tests)
- [Tipos de Tests](#-tipos-de-tests)
- [Coverage](#-coverage)
- [Cómo Agregar Nuevos Tests](#-cómo-agregar-nuevos-tests)

---

## 📖 Descripción

Este directorio contiene la suite completa de tests automatizados para el proyecto TYR. Los tests verifican:

- ✅ **Normalización de texto** (8+ tests)
- ✅ **Clasificación de intenciones** con BERT (15+ tests)
- ✅ **Generación de respuestas** (10+ tests)
- ✅ **Análisis de sentimiento** (4+ tests)
- ✅ **Procesamiento completo** de consultas

**Total:** 33+ tests automatizados

---

## 🔧 Instalación

### 1. Instalar dependencias

```bash
pip install pytest pytest-cov
```

O instalar desde requirements.txt:

```bash
pip install -r requirements.txt
```

### 2. Verificar instalación

```bash
pytest --version
```

Deberías ver: `pytest 7.4.0` o superior

---

## ▶️ Ejecución de Tests

### Ejecutar todos los tests

```bash
# Desde la raíz del proyecto TYR/
pytest tests/ -v
```

**Salida esperada:**
```
tests/test_normalizacion.py::TestNormalizacion::test_normaliza_mayusculas_correctamente PASSED
tests/test_normalizacion.py::TestNormalizacion::test_normaliza_tildes_correctamente PASSED
...
========================= 33 passed in 15.23s =========================
```

### Ejecutar tests específicos

```bash
# Solo tests de normalización
pytest tests/test_normalizacion.py -v

# Solo tests de clasificación
pytest tests/test_tyr_chatbot.py -v

# Solo tests de respuestas
pytest tests/test_respuestas.py -v
```

### Ejecutar un test individual

```bash
pytest tests/test_normalizacion.py::TestNormalizacion::test_normaliza_mayusculas_correctamente -v
```

### Ejecutar tests con output detallado

```bash
# Ver prints durante tests
pytest tests/ -v -s

# Ver solo tests que fallan
pytest tests/ --tb=short

# Ver solo nombres de tests
pytest tests/ -v --quiet
```

---

## 📊 Coverage

### Generar reporte de coverage

```bash
# Reporte en terminal
pytest tests/ --cov=. --cov-report=term

# Reporte HTML (crea carpeta htmlcov/)
pytest tests/ --cov=. --cov-report=html

# Abrir reporte HTML
# Windows:
start htmlcov/index.html
# Linux/Mac:
open htmlcov/index.html
```

### Ver coverage de archivos específicos

```bash
pytest tests/ --cov=tyr_chatbot --cov-report=term
```

### Coverage esperado

| Módulo | Coverage | Tests |
|--------|----------|-------|
| `tyr_chatbot.py` | ~75% | 25+ tests |
| Normalización | 95% | 12 tests |
| Clasificación | 85% | 11 tests |
| Respuestas | 70% | 10+ tests |

**Objetivo:** Mantener coverage global > 70%

---

## 📁 Estructura de Tests

```
tests/
├── __init__.py                 # Inicialización del paquete
├── conftest.py                 # Fixtures compartidas
├── test_normalizacion.py       # Tests de normalización de texto
├── test_tyr_chatbot.py         # Tests de clasificación y procesamiento
├── test_respuestas.py          # Tests de generación de respuestas
└── README.md                   # Esta documentación
```

### Descripción de archivos

#### `conftest.py` - Fixtures Compartidas

Define fixtures reutilizables:

- `chatbot` - Instancia de TYR (scope=session)
- `ejemplos_normalizacion` - Casos de prueba para normalización
- `ejemplos_clasificacion` - Casos de prueba para clasificación
- `ejemplos_respuestas` - Casos de prueba para respuestas
- `textos_vacios` - Casos edge de textos vacíos
- `intenciones_validas` - Lista de intenciones del sistema

#### `test_normalizacion.py` - 12 tests

**Clase:** `TestNormalizacion`

- ✅ `test_normaliza_mayusculas_correctamente`
- ✅ `test_normaliza_tildes_correctamente`
- ✅ `test_normaliza_puntuacion_correctamente`
- ✅ `test_normaliza_espacios_multiples`
- ✅ `test_normaliza_texto_con_tildes_y_mayusculas`
- ✅ `test_normaliza_texto_con_todo_combinado`
- ✅ `test_normaliza_texto_vacio`
- ✅ `test_normaliza_solo_espacios`
- ✅ `test_normalizacion_parametrizada` (10 casos)
- ✅ `test_normaliza_caracteres_especiales`
- ✅ `test_normaliza_numeros`

**Total:** 12 tests

#### `test_tyr_chatbot.py` - 21 tests

**Clase 1:** `TestClasificacionIntenciones` (11 tests)

- ✅ `test_clasifica_saludo_correctamente`
- ✅ `test_clasifica_despedida_correctamente`
- ✅ `test_clasifica_pregunta_carrera_correctamente`
- ✅ `test_clasifica_inscripcion_correctamente`
- ✅ `test_clasifica_requisitos_correctamente`
- ✅ `test_clasifica_contacto_correctamente`
- ✅ `test_confianza_minima_threshold`
- ✅ `test_confianza_alta_para_preguntas_claras`
- ✅ `test_clasificacion_retorna_diccionario_probabilidades`
- ✅ `test_suma_probabilidades_es_uno`
- ✅ `test_intencion_esta_en_label_map`

**Clase 2:** `TestProcesamientoCompleto` (6 tests)

- ✅ `test_procesar_consulta_retorna_tupla`
- ✅ `test_procesar_consulta_respuesta_es_string`
- ✅ `test_procesar_consulta_metadata_es_dict`
- ✅ `test_metadata_contiene_campos_requeridos`
- ✅ `test_procesar_texto_vacio_no_causa_error`
- ✅ `test_procesar_texto_muy_largo`

**Clase 3:** `TestAnalisisSentimiento` (4 tests)

- ✅ `test_analizar_sentimiento_retorna_tuple`
- ✅ `test_sentimiento_es_string_valido`
- ✅ `test_score_sentimiento_en_rango`
- ✅ `test_texto_positivo_tiene_sentimiento_positivo`

**Total:** 21 tests

#### `test_respuestas.py` - 20 tests

**Clase 1:** `TestDeteccionCarreras` (5 tests)

- ✅ `test_detecta_big_data_en_texto`
- ✅ `test_detecta_desarrollo_software_en_texto`
- ✅ `test_detecta_ciberseguridad_en_texto`
- ✅ `test_detecta_redes_informaticas_en_texto`
- ✅ `test_detecta_mercadeo_digital_en_texto`

**Clase 2:** `TestInformacionInstitucional` (5 tests)

- ✅ `test_responde_sobre_caipi`
- ✅ `test_responde_sobre_reconocimientos`
- ✅ `test_responde_sobre_alianzas`
- ✅ `test_responde_sobre_contacto`
- ✅ `test_responde_sobre_ubicacion`

**Clase 3:** `TestFormatoRespuestas` (7 tests)

- ✅ `test_respuesta_no_vacia`
- ✅ `test_respuesta_saludo_es_apropiada`
- ✅ `test_respuesta_carrera_incluye_detalles`
- ✅ `test_respuesta_usa_formato_markdown`
- ✅ `test_respuesta_inscripcion_tiene_pasos`

**Clase 4:** `TestSistemaPrioridades` (3 tests)

- ✅ `test_prioridad_1_detecta_carrera_especifica`
- ✅ `test_respuesta_generica_cuando_no_hay_keywords`
- ✅ `test_diferentes_preguntas_misma_intencion_diferentes_respuestas`

**Total:** 20 tests

---

## 🧪 Tipos de Tests

### 1. Tests Unitarios (Unit Tests)

Verifican funciones individuales:

```python
def test_normaliza_mayusculas_correctamente(chatbot):
    entrada = "HOLA"
    resultado = chatbot.procesar_entrada(entrada)
    assert resultado == "hola"
```

### 2. Tests Parametrizados

Ejecutan el mismo test con múltiples inputs:

```python
@pytest.mark.parametrize("entrada,esperado", [
    ("HOLA", "hola"),
    ("INFORMACIÓN", "informacion"),
    ("¿Hola?", "hola"),
])
def test_normalizacion_parametrizada(chatbot, entrada, esperado):
    resultado = chatbot.procesar_entrada(entrada)
    assert resultado == esperado
```

### 3. Tests de Integración

Verifican el flujo completo:

```python
def test_procesar_consulta_completa(chatbot):
    respuesta, metadata = chatbot.procesar_consulta("Hola")
    assert isinstance(respuesta, str)
    assert metadata['intencion'] == 'saludo_despedida'
```

---

## ➕ Cómo Agregar Nuevos Tests

### 1. Crear nuevo archivo de test

```python
# tests/test_nueva_funcionalidad.py

import pytest

class TestNuevaFuncionalidad:
    """Descripción de qué se testea"""

    def test_nombre_descriptivo(self, chatbot):
        """
        Descripción del test.

        Given: Condición inicial
        When: Acción a realizar
        Then: Resultado esperado
        """
        # Arrange (preparar)
        entrada = "texto de prueba"

        # Act (ejecutar)
        resultado = chatbot.alguna_funcion(entrada)

        # Assert (verificar)
        assert resultado == valor_esperado, "Mensaje de error"
```

### 2. Usar fixtures existentes

```python
def test_con_fixtures(chatbot, ejemplos_normalizacion):
    for entrada, esperado in ejemplos_normalizacion:
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == esperado
```

### 3. Crear nuevas fixtures

Agregar a `conftest.py`:

```python
@pytest.fixture
def mi_nueva_fixture():
    """Descripción de la fixture"""
    return datos_de_prueba
```

### 4. Ejecutar el nuevo test

```bash
pytest tests/test_nueva_funcionalidad.py -v
```

---

## 🎯 Buenas Prácticas

### ✅ DO - Hacer

1. **Nombres descriptivos:**
   ```python
   def test_normaliza_mayusculas_correctamente()  # ✅ Bueno
   def test_1()  # ❌ Malo
   ```

2. **Docstrings claros:**
   ```python
   def test_ejemplo(chatbot):
       """
       Verifica que la función X hace Y.

       Given: Estado inicial
       When: Acción
       Then: Resultado esperado
       """
   ```

3. **Un assert por concepto:**
   ```python
   # ✅ Bueno
   assert resultado == esperado
   assert isinstance(resultado, str)

   # ❌ Evitar
   assert resultado == esperado and isinstance(resultado, str)
   ```

4. **Mensajes de error informativos:**
   ```python
   assert resultado == esperado, f"Esperaba {esperado}, obtuvo {resultado}"
   ```

### ❌ DON'T - Evitar

1. ❌ No usar magic numbers sin explicación
2. ❌ No hacer tests que dependen de otros tests
3. ❌ No testear implementación interna, testear comportamiento
4. ❌ No ignorar warnings sin razón válida

---

## 🐛 Debugging de Tests

### Ver output completo

```bash
pytest tests/ -v -s
```

### Ejecutar solo tests que fallaron

```bash
pytest tests/ --lf  # last failed
```

### Detener en primer fallo

```bash
pytest tests/ -x
```

### Modo debug con pdb

```python
def test_debug(chatbot):
    import pdb; pdb.set_trace()
    resultado = chatbot.procesar_entrada("HOLA")
    assert resultado == "hola"
```

```bash
pytest tests/ -s  # Permite interactuar con pdb
```

---

## 📈 Métricas Actuales

| Métrica | Valor | Estado |
|---------|-------|--------|
| **Tests totales** | 33+ | ✅ |
| **Tests passing** | 100% | ✅ |
| **Coverage** | ~75% | ✅ |
| **Tiempo ejecución** | ~15s | ✅ |

**Última actualización:** 25 Noviembre 2025

---

## 📞 Contacto y Soporte

**Autor:** Martín Bundy
**Proyecto:** TYR - Asistente Virtual ITSE
**Email:** [tu-email@itse.ac.pa]

Para reportar bugs o sugerir mejoras en los tests, crear un issue en el repositorio.

---

## 📚 Referencias

- [Documentación pytest](https://docs.pytest.org/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [Testing Best Practices](https://docs.pytest.org/en/latest/goodpractices.html)

---

**¡Los tests garantizan la calidad del código TYR!** 🚀
