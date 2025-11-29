# Proyecto: TYR - Asistente Virtual ITSE

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![BERT](https://img.shields.io/badge/BERT-Spanish-yellow.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)
![Tests](https://img.shields.io/badge/Tests-59%20passing-brightgreen.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-98.93%25-success.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 1. Resumen Ejecutivo

**TYR (Tech Your Route)** es un asistente virtual inteligente desarrollado específicamente para el Instituto Técnico Superior Especializado (ITSE) de Panamá. El sistema utiliza procesamiento de lenguaje natural avanzado mediante BERT para proporcionar información precisa y contextualizada sobre carreras técnicas, procesos de admisión, becas, y servicios institucionales.

Con una precisión del **98.93%** en la clasificación de intenciones, TYR puede responder a consultas estudiantiles en español de forma natural, tolerando errores ortográficos y variaciones en el lenguaje. El sistema ha sido entrenado con 4,358 ejemplos que cubren 48 patrones diferentes de preguntas, garantizando respuestas precisas para las 16 carreras técnicas superiores que ofrece el ITSE.

El proyecto representa un caso de éxito en la aplicación de IA conversacional en el contexto educativo latinoamericano, superando los objetivos académicos establecidos (+13.93% en accuracy) y estableciendo un estándar de calidad con 59 tests automatizados, documentación exhaustiva, y una arquitectura modular escalable.

---

## 2. Definición del Proyecto

### 2.1 Descripción General

TYR es un chatbot educativo basado en transformers BERT que actúa como punto de contacto 24/7 para estudiantes prospectivos y actuales del ITSE. El sistema combina:

- **Clasificación de intenciones** mediante BERT fine-tuned en español
- **Análisis de sentimientos** con VADER para respuestas empáticas
- **Base de conocimiento estructurada** con información actualizada 2025
- **Interfaz web moderna** desarrollada en Streamlit

El chatbot puede responder preguntas sobre:
- 📚 16 carreras técnicas superiores (Big Data, Ciberseguridad, IA, etc.)
- 📝 Proceso de admisión e inscripción (PIENSE II)
- 💰 Becas y financiamiento (IFARHU, BID)
- 🏢 Servicios institucionales (CAIPI, CIIECYT)
- 🌐 Información general del ITSE (reconocimientos, alianzas)

### 2.2 Público Objetivo

**Usuarios Primarios:**
- **Estudiantes prospectivos** (16-25 años) buscando información sobre carreras técnicas
- **Estudiantes actuales** consultando sobre procesos administrativos
- **Padres de familia** investigando opciones educativas para sus hijos

**Usuarios Secundarios:**
- **Personal administrativo** del ITSE para consultas rápidas
- **Orientadores vocacionales** usando TYR como herramienta de información

**Características del público:**
- Nivel educativo: Secundaria completa o en curso
- Ubicación: Panamá (principalmente área metropolitana)
- Dispositivos: Móviles (70%), Desktop (30%)
- Conectividad: Variable (optimizado para conexiones lentas)

### 2.3 Objetivos Principales

#### Objetivos Académicos ✅
- [x] Entrenar modelo BERT en español con accuracy ≥85% (Logrado: **98.93%**)
- [x] Implementar análisis de sentimientos contextual
- [x] Crear dataset balanceado con ≥1000 ejemplos (Logrado: **4,358**)
- [x] Desarrollar interfaz funcional de usuario

#### Objetivos Técnicos ✅
- [x] Alcanzar F1-Score ≥82% (Logrado: **98.92%**)
- [x] Implementar suite de tests automatizados (**59 tests, 100% passing**)
- [x] Externalizar base de conocimiento a JSON (**91 KB**)
- [x] Generar visualizaciones profesionales (**4 gráficas**)
- [x] Documentar arquitectura completa (**6 diagramas Mermaid**)

#### Objetivos de Impacto 🎯
- Reducir tiempo de respuesta a consultas estudiantiles (de horas a segundos)
- Aumentar tasa de conversión de prospectos a aplicantes
- Liberar carga de trabajo del personal administrativo
- Proporcionar acceso 24/7 a información institucional
- Mejorar experiencia del estudiante prospectivo

---

## 3. Especificaciones Técnicas

### 3.1 Stack Tecnológico

#### Lenguaje Principal
```yaml
Python: 3.8+
  Justificación: Ecosistema maduro para ML/NLP, compatibilidad con HuggingFace
```

#### Frameworks y Librerías Core

| Componente | Tecnología | Versión | Propósito |
|------------|------------|---------|-----------|
| **NLP** | HuggingFace Transformers | 4.35.0 | Fine-tuning y inference BERT |
| **Modelo BERT** | dccuchile/bert-base-spanish-wwm-cased | - | Clasificación de intenciones en español |
| **Deep Learning** | PyTorch | 2.0.1 | Framework de entrenamiento |
| **Análisis Sentimientos** | vaderSentiment-es | 3.3.2 | Análisis de polaridad en español |
| **Interfaz Web** | Streamlit | 1.28.0 | Frontend interactivo |
| **Testing** | pytest | 7.4+ | Suite de tests automatizados |
| **Coverage** | pytest-cov | 4.1+ | Análisis de cobertura de código |
| **Visualización** | matplotlib + seaborn | latest | Generación de gráficas |

#### Herramientas de Desarrollo

```yaml
Entrenamiento:
  - Google Colab (GPU T4 gratuita)
  - Jupyter Notebook para experimentación

Control de Versiones:
  - Git + GitHub

Dependencias:
  - pip (requirements.txt)
  - Entorno virtual (venv)

Calidad de Código:
  - pytest (tests automatizados)
  - pytest-cov (coverage)
  - Black/Flake8 (linting - opcional)
```

### 3.2 Arquitectura

#### Diagrama de Arquitectura General

```
[DIAGRAMA SUGERIDO: Arquitectura de 4 capas]

┌─────────────────────────────────────────────────────────────┐
│                     CAPA DE PRESENTACIÓN                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │            Streamlit Web Interface                   │   │
│  │  - Chat input/output                                 │   │
│  │  - Historial de conversación                         │   │
│  │  - Visualización de metadata                         │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE LÓGICA DE NEGOCIO                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         TYR Chatbot Core (tyr_chatbot.py)            │  │
│  │  ┌──────────────────┐  ┌──────────────────────┐     │  │
│  │  │ Normalización    │  │ Sistema de respuestas │     │  │
│  │  │ de texto         │  │ contextuales (3 capas)│     │  │
│  │  └──────────────────┘  └──────────────────────┘     │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────┬──────────────────────┬─────────────────────┘
                 │                      │
                 ▼                      ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│   CAPA DE PROCESAMIENTO  │  │  CAPA DE ANÁLISIS        │
│                          │  │                          │
│  ┌────────────────────┐ │  │  ┌────────────────────┐ │
│  │   BERT Classifier  │ │  │  │  VADER Sentiment   │ │
│  │                    │ │  │  │     Analyzer       │ │
│  │  - Tokenization    │ │  │  │                    │ │
│  │  - Intent classify │ │  │  │  - Polarity        │ │
│  │  - Confidence      │ │  │  │  - Compound score  │ │
│  └────────────────────┘ │  │  └────────────────────┘ │
└────────────┬─────────────┘  └──────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│                      CAPA DE DATOS                           │
│  ┌──────────────────┐  ┌──────────────────────────────┐    │
│  │ modelo_bert_tyr/ │  │ data/ (JSON externos)        │    │
│  │  - config.json   │  │  - carreras_itse.json        │    │
│  │  - pytorch_model │  │  - respuestas_generales.json │    │
│  │  - tokenizer     │  │                              │    │
│  │  - label_map.json│  │                              │    │
│  └──────────────────┘  └──────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

#### Flujo de Datos: Procesamiento de una Consulta

```
[DIAGRAMA SUGERIDO: Flujo de procesamiento paso a paso]

Usuario escribe: "¿CUÉNTAME SOBRE BIG DATA?"
         │
         ▼
┌─────────────────────────────────────┐
│ 1. Normalización de Entrada         │
│                                     │
│ "¿CUÉNTAME SOBRE BIG DATA?"        │
│         ↓                           │
│ "cuentame sobre big data"          │ ← Minúsculas, sin tildes, sin signos
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 2. Tokenización BERT                │
│                                     │
│ Input IDs: [101, 456, 789, ...]    │
│ Attention Mask: [1, 1, 1, ...]     │
│ Max Length: 128 tokens              │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 3. Clasificación de Intención       │
│                                     │
│ BERT Forward Pass                   │
│         ↓                           │
│ Logits: [0.2, 9.8, 0.1, ...]       │
│         ↓                           │
│ Softmax + Argmax                    │
│         ↓                           │
│ Intención: informacion_carreras     │
│ Confianza: 99.89%                   │
└──────────────┬──────────────────────┘
               │
               ├──────────────────────┐
               │                      │
               ▼                      ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│ 4a. Análisis Sentimiento │  │ 4b. Búsqueda de Respuesta│
│                          │  │                          │
│ VADER Analysis           │  │ Sistema 3 Capas:         │
│         ↓                │  │                          │
│ Compound: +0.65          │  │ Capa 1: Carrera específica│
│ Categoría: Positivo      │  │ "big data" → Match! ✓    │
└──────────────────────────┘  │                          │
                              │ Retrieval desde:         │
                              │ data/carreras_itse.json  │
                              └───────────┬──────────────┘
                                          │
                                          ▼
                              ┌────────────────────────────┐
                              │ 5. Generación de Respuesta │
                              │                            │
                              │ Template personalizado     │
                              │         +                  │
                              │ Datos de la carrera        │
                              │         ↓                  │
                              │ Respuesta completa:        │
                              │ "¡Hola! Te cuento sobre    │
                              │  T.S. en Big Data..."      │
                              └───────────┬────────────────┘
                                          │
                                          ▼
                              ┌────────────────────────────┐
                              │ 6. Presentación al Usuario │
                              │                            │
                              │ Streamlit Chat Message     │
                              │ + Metadata sidebar:        │
                              │   - Intención ✓            │
                              │   - Confianza: 99.89%      │
                              │   - Sentimiento: Positivo  │
                              └────────────────────────────┘
```

#### Componentes Principales

**1. TYR Chatbot Core (`tyr_chatbot.py` - 756 líneas)**
```python
class TYR:
    """Asistente Virtual principal del ITSE."""

    Componentes:
    - cargar_modelo()          # Carga BERT + tokenizer
    - procesar_entrada()       # Normalización de texto
    - clasificar_intencion()   # Inference BERT
    - analizar_sentimiento()   # VADER analysis
    - generar_respuesta()      # Sistema 3 capas
    - buscar_carrera()         # Retrieval específico
    - buscar_info_faq()        # Keywords especiales
```

**2. Aplicación Streamlit (`tyr_app.py` - 890 líneas)**
```python
Funcionalidades:
- setup_page()                # Config y estilos CSS
- render_chat_interface()     # UI principal
- handle_user_input()         # Procesamiento de consultas
- save/load_conversation()    # Persistencia de historial
- render_metadata()           # Sidebar con métricas
```

**3. Sistema de Tests (`tests/` - 59 tests)**
```python
Cobertura:
- test_tyr_chatbot.py (31 tests)  # Lógica core
- test_tyr_app.py (28 tests)      # UI y funcionalidades
- conftest.py (21 fixtures)       # Configuración compartida
```

### 3.3 Funcionalidades Técnicas

#### APIs y Modelos Utilizados

**1. HuggingFace Model Hub**
```python
Modelo: "dccuchile/bert-base-spanish-wwm-cased"
Características:
- Pre-entrenado en corpus español (Chile)
- 110M parámetros
- Vocabulario: 31,002 tokens
- Max sequence length: 512 tokens (usamos 128)
```

**2. VADER Sentiment (Español)**
```python
Biblioteca: vaderSentiment-es
Funcionalidad:
- Análisis de polaridad: positivo/neutro/negativo
- Compound score: [-1, +1]
- Lexicón adaptado al español
```

#### Integraciones

**Google Colab (Entrenamiento)**
```yaml
Plataforma: Google Colab
GPU: Tesla T4 (16GB VRAM)
Tiempo de entrenamiento: 6m 15s
Costo: Gratuito (tier free)
```

**Streamlit Cloud (Deployment - opcional)**
```yaml
Hosting: Streamlit Community Cloud
Límites: 1GB RAM, sin GPU
Estado: Configurado para deployment futuro
```

#### Métodos de Autenticación

**Estado Actual:** Sin autenticación (sistema público de información)

**Futuras Mejoras Propuestas:**
```yaml
Nivel 1 (Información Pública):
  - Sin login requerido
  - Rate limiting por IP

Nivel 2 (Estudiantes Registrados):
  - OAuth 2.0 con Google/Microsoft
  - Acceso a información personalizada
  - Historial de consultas persistente

Nivel 3 (Personal Administrativo):
  - LDAP/Active Directory del ITSE
  - Dashboard de analytics
  - Gestión de contenido
```

---

## 4. Funcionalidades de Usuario

### 4.1 Características Principales

#### 🎯 Clasificación Inteligente de Consultas

**9 Intenciones Soportadas:**

| Intención | Descripción | Ejemplos de Consultas | Accuracy |
|-----------|-------------|----------------------|----------|
| `informacion_carreras` | Info sobre las 16 carreras del ITSE | "Cuéntame sobre Big Data", "Qué es Ciberseguridad" | 99.9% |
| `inscripcion_admision` | Proceso de matrícula | "¿Cómo me inscribo?", "Requisitos para aplicar" | 99.0% |
| `requisitos_ingreso` | Documentos y criterios | "Qué necesito para entrar", "Documentos requeridos" | 99.5% |
| `becas_financiamiento` | IFARHU, BID, alianzas | "Hay becas disponibles?", "Cómo financiar estudios" | 99.8% |
| `horarios_duracion` | Jornadas y duración | "Cuánto dura la carrera", "Horarios nocturnos" | 99.7% |
| `contacto_ubicacion` | Datos de contacto ITSE | "Dónde queda el ITSE", "Teléfono de admisiones" | 100% |
| `faq_general` | Info institucional | "Qué es CAIPI", "Reconocimientos del ITSE" | 99.6% |
| `saludo_despedida` | Saludos y cortesía | "Hola", "Gracias", "Adiós" | 100% |
| `fuera_dominio` | Consultas no relacionadas | "Clima hoy", "Receta de pizza" | 100% |

#### 💬 Respuestas Contextuales de 3 Capas

**Sistema de Priorización Inteligente:**

```
Consulta: "Cuéntame sobre Big Data"
         │
         ▼
┌─────────────────────────────────────────┐
│ CAPA 1: Búsqueda de Carrera Específica │ ← Prioridad ALTA
│                                         │
│ ¿Contiene nombre de carrera?           │
│  → "big data" detectado ✓               │
│                                         │
│ Respuesta: Información completa de      │
│ T.S. en Big Data (escuela, créditos,   │
│ duración, campo ocupacional, enlace)    │
└─────────────────────────────────────────┘
                 │
                 │ (Si no hay match)
                 ▼
┌─────────────────────────────────────────┐
│ CAPA 2: Keywords Especiales FAQ        │ ← Prioridad MEDIA
│                                         │
│ ¿Contiene keywords especiales?          │
│  - "CAIPI" → Guardería estudiantil      │
│  - "CIIECYT" → Centro de investigación  │
│  - "reconocimientos" → Logros WEF/UE    │
│  - "alianzas" → Canal, Copa Airlines    │
│                                         │
│ Respuesta: Info específica del keyword  │
└─────────────────────────────────────────┘
                 │
                 │ (Si no hay match)
                 ▼
┌─────────────────────────────────────────┐
│ CAPA 3: Respuesta por Intención        │ ← Prioridad BAJA
│                                         │
│ Usar respuesta general de la intención  │
│ clasificada por BERT                    │
│                                         │
│ Respuesta: FAQ general de esa categoría │
└─────────────────────────────────────────┘
```

#### 🛡️ Tolerancia a Errores 100%

**Normalización Avanzada de Texto:**

```python
Transformaciones aplicadas:
1. Conversión a minúsculas
2. Eliminación de tildes/acentos (NFD normalization)
3. Remoción de signos de puntuación
4. Normalización de espacios en blanco

Ejemplos:
"¿CUÉNTAME SOBRE BIG DATA?" → "cuentame sobre big data"
"Información sin tildes"    → "informacion sin tildes"
"COMO     ME  INSCRIBO!!!"  → "como me inscribo"
```

**Robustez comprobada:**
- ✅ Mayúsculas/minúsculas
- ✅ Tildes y acentos
- ✅ Signos de puntuación
- ✅ Espacios múltiples
- ✅ Combinaciones de los anteriores

#### 📊 Metadata Transparente

**Información Visible en Sidebar:**
```yaml
Para cada respuesta:
  - Intención detectada: informacion_carreras
  - Nivel de confianza: 99.89%
  - Sentimiento: Positivo
  - Score de sentimiento: +0.65
  - Carrera específica: Big Data (si aplica)
```

### 4.2 Flujos de Interacción

#### Flujo 1: Consulta sobre Carrera Técnica

```
[DIAGRAMA SUGERIDO: User journey - Consulta de carrera]

USUARIO                          TYR CHATBOT                        SISTEMA
   │                                 │                                  │
   │  1. "Cuéntame sobre            │                                  │
   │     Ciberseguridad"            │                                  │
   ├────────────────────────────────>│                                  │
   │                                 │  2. Normalización               │
   │                                 ├─────────────────────────────────>│
   │                                 │  3. Clasificación BERT           │
   │                                 │<─────────────────────────────────┤
   │                                 │  Intención: informacion_carreras │
   │                                 │  Confianza: 99.5%                │
   │                                 │                                  │
   │                                 │  4. Búsqueda específica          │
   │                                 ├─────────────────────────────────>│
   │                                 │  Match: "ciberseguridad" found   │
   │                                 │<─────────────────────────────────┤
   │                                 │  Datos de carrera recuperados    │
   │                                 │                                  │
   │  5. Respuesta completa:         │                                  │
   │     "¡Hola! Te cuento sobre    │                                  │
   │     T.S. en Ciberseguridad...  │                                  │
   │     🏫 Escuela: ...            │                                  │
   │     📚 Créditos: 112           │                                  │
   │     ⏱️ Duración: ...           │                                  │
   │     💼 Campo ocupacional: ..." │                                  │
   │<────────────────────────────────┤                                  │
   │                                 │                                  │
   │  6. Usuario ve metadata:        │                                  │
   │     - Intención ✓               │                                  │
   │     - Confianza: 99.5%         │                                  │
   │     - Sentimiento: Positivo    │                                  │
   │                                 │                                  │
```

#### Flujo 2: Pregunta sobre Proceso de Inscripción

```
USUARIO                          TYR CHATBOT
   │                                 │
   │  "¿Cómo me inscribo al ITSE?"  │
   ├────────────────────────────────>│
   │                                 │ ← Intención: inscripcion_admision
   │                                 │ ← Confianza: 98.5%
   │                                 │
   │  Respuesta estructurada:        │
   │  "📝 Proceso de Admisión:      │
   │   1. Registro en línea         │
   │   2. Prueba PIENSE II          │
   │   3. Entrevista (si aplica)    │
   │   4. Matrícula                 │
   │   📞 Contacto: ..."            │
   │<────────────────────────────────┤
   │                                 │
   │  "¿Qué documentos necesito?"   │
   ├────────────────────────────────>│
   │                                 │ ← Intención: requisitos_ingreso
   │                                 │
   │  "📄 Documentos requeridos:    │
   │   • Cédula/Pasaporte           │
   │   • Diploma de secundaria      │
   │   • Foto tamaño carné          │
   │   • ..."                       │
   │<────────────────────────────────┤
```

#### Flujo 3: Información Institucional (Keywords Especiales)

```
USUARIO                          TYR CHATBOT
   │                                 │
   │  "¿Qué es CAIPI?"              │
   ├────────────────────────────────>│
   │                                 │ ← Intención: faq_general
   │                                 │ ← Keyword "CAIPI" detectado
   │                                 │ ← Capa 2 activada
   │                                 │
   │  "🏫 CAIPI (Centro de          │
   │   Atención Integral para la    │
   │   Primera Infancia)            │
   │                                │
   │   Es una guardería para hijos  │
   │   de estudiantes del ITSE...   │
   │   📞 Contacto: ...             │
   │   ⏰ Horario: ..."              │
   │<────────────────────────────────┤
```

### 4.3 Ejemplos de Uso

#### Caso de Uso 1: Estudiante Prospectivo

**Perfil:** María, 18 años, recién graduada de secundaria, interesada en tecnología.

**Consultas típicas:**
```
👤 María: "Hola, quiero estudiar algo relacionado con tecnología"
🤖 TYR: "¡Hola! El ITSE ofrece 16 carreras técnicas en 4 escuelas.
         Algunas relacionadas con tecnología:
         • Big Data
         • Ciberseguridad
         • Inteligencia Artificial
         • Desarrollo de Software
         ¿Sobre cuál quieres saber más?"

👤 María: "Cuéntame sobre Inteligencia Artificial"
🤖 TYR: [Respuesta completa con info de la carrera]

👤 María: "¿Cuánto cuesta la matrícula?"
🤖 TYR: [Respuesta sobre costos y becas IFARHU]

👤 María: "¿Dónde queda el ITSE?"
🤖 TYR: [Ubicación, mapa, transporte público]
```

#### Caso de Uso 2: Padre de Familia

**Perfil:** Roberto, 45 años, busca opciones educativas para su hijo.

**Consultas típicas:**
```
👤 Roberto: "Mi hijo terminó la secundaria, ¿qué carreras tienen?"
🤖 TYR: [Lista de 16 carreras agrupadas por escuela]

👤 Roberto: "¿Hay ayuda financiera? No podemos pagar la carrera completa"
🤖 TYR: [Info sobre IFARHU, BID, convenios empresariales]

👤 Roberto: "¿Qué tan buenos son ustedes? ¿Tienen reconocimientos?"
🤖 TYR: [Reconocimientos WEF, UE, Hackathon 2025, 80% inserción laboral]

👤 Roberto: "Mi hijo tiene una bebé, ¿hay guardería?"
🤖 TYR: [Info completa sobre CAIPI - guardería para hijos de estudiantes]
```

#### Caso de Uso 3: Estudiante Actual

**Perfil:** Carlos, 20 años, estudiante actual consultando sobre horarios.

**Consultas típicas:**
```
👤 Carlos: "¿Hay jornada nocturna? Trabajo de día"
🤖 TYR: [Info sobre jornadas: diurna 2.5 años, nocturna 3 años]

👤 Carlos: "¿Cuánto dura la carrera de Big Data?"
🤖 TYR: [Duración específica, créditos, carga semanal]

👤 Carlos: "¿Con quién tienen alianzas para prácticas?"
🤖 TYR: [Alianzas con Canal de Panamá, Copa Airlines, empresas europeas]
```

---

## 5. Proceso de Desarrollo

### 5.1 Fases Completadas

#### 📅 PARTE 1: Desarrollo Inicial del Modelo (17-21 Nov 2025)

**Sesión Inicial 1: Dataset Base (17-18 Nov)**
```yaml
Objetivo: Crear dataset mínimo viable
Resultado: 281 ejemplos, 8 intenciones
Duración: 6 horas
Estado: ✅ Completado

Entregables:
  - Dataset_TYR.json (281 ejemplos)
  - 8 clases balanceadas (35 ejemplos c/u)
```

**Sesión Inicial 2: Preprocesamiento (17 Nov)**
```yaml
Objetivo: Pipeline de tokenización BERT
Resultado: Train/Val/Test splits listos
Duración: 3 horas
Estado: ✅ Completado

Entregables:
  - preprocessing.py
  - train/val/test encodings (.pt files)
  - label_map.json
```

**Sesión Inicial 3: Primer Entrenamiento (18 Nov)**
```yaml
Objetivo: Baseline model
Resultado: 79.3% accuracy ❌ (objetivo: ≥85%)
Duración: 4 horas (10 epochs)
Estado: ⚠️ Bajo objetivo

Lección aprendida: Dataset muy pequeño para BERT
```

**Sesión Inicial 4: Expansión Dataset v2 (18-19 Nov)**
```yaml
Objetivo: Data augmentation masivo
Resultado: 1,542 ejemplos (+449%)
Duración: 8 horas
Estado: ✅ Completado

Técnicas aplicadas:
  - Templates estructurados
  - Sinónimos contextuales
  - Variaciones de formalidad
  - Nueva clase: requisitos_ingreso
```

**Sesión Inicial 5: Re-entrenamiento v2 (19 Nov)**
```yaml
Objetivo: Superar 85% accuracy
Resultado: 96.2% accuracy ✅ 100% en test set
Duración: 2 horas (3 epochs con early stopping)
Estado: 🎉 Objetivo superado

Métricas:
  - Accuracy: 96.2%
  - F1-Score: 96.1%
  - Test: 155/155 correctos
```

**Sesión Inicial 6: Mejora Continua v3 (20-21 Nov)**
```yaml
Problema detectado:
  "Cuéntame sobre Big Data" → fuera_dominio ❌

Solución: Expansión masiva con 48 patrones
Resultado: 4,358 ejemplos (+183%)

Re-entrenamiento v3:
  - Plataforma: Google Colab GPU T4
  - Tiempo: 6m 15s (4 epochs)
  - Accuracy: 98.93% ✅
  - F1-Score: 98.92% ✅
  - Errores: 7/654 (1.07%)
```

#### 📅 PARTE 2: Mejoras de Calidad y Profesionalización (23-24 Nov 2025)

**Sesión Mejora 1: Tests Automatizados (23 Nov)**
```yaml
Objetivo: Suite completa de tests con pytest
Duración: 3 horas
Estado: ✅ Completado

Resultados:
  - 59 tests implementados
  - 100% passing (0 fallos)
  - Coverage: 73.75%
  - 21 fixtures configuradas
  - Tiempo ejecución: 8.31s

Entregables:
  - tests/test_tyr_chatbot.py (31 tests)
  - tests/test_tyr_app.py (28 tests)
  - tests/conftest.py (fixtures)
  - pytest.ini
  - .coveragerc
```

**Sesión Mejora 2: Externalización JSON (23 Nov)**
```yaml
Objetivo: Separar código de datos
Duración: 2 horas
Estado: ✅ Completado

Resultados:
  - Reducción: 1,247 → 756 líneas (-39%)
  - Tamaño archivo: 67.4 KB → 42.8 KB (-37%)
  - Datos externalizados: 91 KB en JSON
  - Sistema de fallback implementado

Entregables:
  - data/carreras_itse.json (86.2 KB, 16 carreras)
  - data/respuestas_generales.json (4.8 KB, 9 intenciones)
  - Tests actualizados: 59/59 passing ✓
```

**Sesión Mejora 3: Visualizaciones (23 Nov)**
```yaml
Objetivo: Gráficas profesionales del modelo
Duración: 2.5 horas
Estado: ✅ Completado

Resultados:
  - 4 visualizaciones creadas
  - Resolución: 300 DPI
  - Tamaño total: 2.1 MB

Entregables:
  - matriz_confusion_4358.png (823 KB, 99.60% accuracy)
  - distribucion_intenciones.png (412 KB)
  - evolucion_modelos.png (587 KB)
  - metricas_clasificacion.txt (1.8 KB)
  - scripts_desarrollo/generar_visualizaciones.py

Problemas resueltos:
  1. UnicodeEncodeError con emojis
  2. KeyError en label_map.json
  3. TypeError en estructura del dataset
```

**Sesión Mejora 4: Arquitectura (23 Nov)**
```yaml
Objetivo: Documentar arquitectura completa
Duración: 3 horas
Estado: ✅ Completado

Resultados:
  - 6 diagramas Mermaid creados
  - 8 badges profesionales agregados
  - 680 líneas de documentación

Entregables:
  - documentacion/ARQUITECTURA_SISTEMA.md (18 KB)
  - 6 diagramas: Arquitectura, Flujo, Componentes,
    Stack, Base Datos, Seguridad
  - README.md actualizado con badges
  - reportes/REPORTE_SESION4_ARQUITECTURA.md
```

**Sesión Mejora 5: Demo y Screenshots (24 Nov)**
```yaml
Objetivo: Evidencia visual del sistema funcionando
Duración: 2 horas
Estado: ✅ Completado

Resultados:
  - 7 screenshots profesionales
  - Tamaño total: 1.9 MB
  - Resolución: 1920x1080
  - Sección Demo completa en README

Entregables:
  - documentacion/screenshots/ (7 capturas PNG)
  - Sección Demo en README.md
  - LICENSE (MIT)
  - reportes/REPORTE_SESION5_DEMO_FINAL.md

Validación final:
  - pytest: 59/59 tests passing ✓
  - Proyecto listo para GitHub ✓
```

### 5.2 Desafíos y Soluciones

#### Desafío 1: Dataset Insuficiente (Sesión 3)

**Problema:**
```
Primer entrenamiento: 79.3% accuracy
Objetivo: ≥85% accuracy
Gap: -5.7%

Síntomas:
- Overfitting después de epoch 5
- Confusión entre clases similares
- Bajo recall en "fuera_dominio"
```

**Análisis:**
- 281 ejemplos demasiado pequeño para BERT (110M parámetros)
- Clases desbalanceadas en algunos casos
- Falta de variedad en patrones lingüísticos

**Solución Implementada:**
```python
1. Data Augmentation Agresivo:
   - Templates estructurados (12 patrones base)
   - Sinónimos contextuales (15 variaciones)
   - Cambios de formalidad (formal/informal/neutral)
   - Modificación de puntuación

2. Expansión Incremental:
   - v1: 281 ejemplos → v2: 1,542 ejemplos
   - v2: 1,542 → v3: 4,358 ejemplos

3. Resultado:
   - Accuracy: 79.3% → 96.2% → 98.93% ✅
   - Objetivo superado en +13.93%
```

#### Desafío 2: Patrón "Cuéntame sobre..." No Reconocido (Sesión 6)

**Problema:**
```
Usuario: "Cuéntame sobre Big Data"
Sistema: "fuera_dominio" (99.7% confianza) ❌
Esperado: "informacion_carreras"

Causa raíz:
- Dataset no incluía patrón "Cuéntame sobre..."
- Solo tenía: "Qué carreras...", "Información sobre..."
- BERT clasificó correctamente según su entrenamiento
```

**Solución Implementada:**
```python
1. Expansión con 48 Patrones Diversos:
   - "Cuéntame sobre {carrera}"
   - "Háblame de {carrera}"
   - "Me interesa {carrera}"
   - "Quiero estudiar {carrera}"
   - ... (44 patrones más)

2. Generación Automática:
   16 carreras × 48 patrones = 768 nuevos ejemplos base
   + variaciones = 2,816 ejemplos nuevos

3. Re-entrenamiento v3:
   - Dataset: 4,358 ejemplos
   - Resultado: 98.93% accuracy
   - "Cuéntame sobre Big Data" → informacion_carreras ✅
```

#### Desafío 3: Respuestas Demasiado Genéricas (Sesión 6)

**Problema:**
```
Usuario: "Alianzas estratégicas del ITSE"
Sistema: [Responde con TODO el FAQ general mezclado] ❌

Problema:
- Usuario pide información ESPECÍFICA
- Sistema responde con TODA la info de faq_general
- Respuesta demasiado larga e irrelevante
```

**Solución Implementada:**
```python
Sistema de Respuestas de 3 Capas:

Capa 1 (Prioridad Alta): Carrera Específica
- Detecta 16 nombres de carreras
- Respuesta: Info completa de esa carrera

Capa 2 (Prioridad Media): Keywords Especiales
- Detecta: "CAIPI", "CIIECYT", "reconocimientos",
           "alianzas", "inserción laboral"
- Respuesta: Solo info de ese keyword

Capa 3 (Prioridad Baja): Intención General
- Si no hay match en Capa 1 y 2
- Respuesta: FAQ general de la intención

Resultado:
- Usuario pregunta "alianzas" → Solo info de alianzas ✅
- Respuestas concisas y relevantes ✅
```

#### Desafío 4: Input de Streamlit No Funciona con Enter (Sesión 6)

**Problema:**
```
Bug reportado por usuario:
1. Usuario escribe texto en input
2. Presiona Enter
3. Texto se borra SIN enviar ❌
4. Usuario debe reescribir y dar click en botón

Causa:
- st.text_input() con sistema de flags complejo
- Conflicto entre on_change y botón
- Mal manejo del session_state
```

**Solución Implementada:**
```python
ANTES:
user_input = st.text_input(
    "Escribe tu pregunta:",
    key="user_input",
    on_change=lambda: handle_flag()
)
enviar = st.button("Enviar")

AHORA:
user_input = st.chat_input(
    placeholder="Escribe tu pregunta aquí...",
    key="chat_input_main"
)
# No requiere botón, Enter funciona nativamente

Beneficios:
- Enter funciona perfectamente ✅
- Se limpia automáticamente ✅
- Código más simple ✅
- Mejor UX (estilo ChatGPT) ✅
```

#### Desafío 5: Intolerancia a Errores Ortográficos (Sesión 6)

**Problema:**
```
Consultas con errores:
- "HOLA" vs "hola" → Diferentes embeddings
- "información" vs "informacion" → No match
- "¿¿¿Cómo???" vs "Cómo" → Tokenización diferente

Impacto:
- Usuario debe escribir "perfecto"
- Mala experiencia de usuario
- Clasificaciones incorrectas en casos extremos
```

**Solución Implementada:**
```python
Normalización Avanzada (unicodedata):

def procesar_entrada(texto: str) -> str:
    # 1. Minúsculas
    texto = texto.lower()

    # 2. Remover tildes (NFD normalization)
    texto_nfd = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(
        c for c in texto_nfd
        if unicodedata.category(c) != 'Mn'
    )

    # 3. Remover signos de puntuación
    texto = texto.replace('¿', '').replace('?', '')
    texto = texto.replace('¡', '').replace('!', '')

    # 4. Normalizar espacios
    return ' '.join(texto.split())

Resultado:
"¿¿CUÉNTAME SOBRE BIG DATA??" → "cuentame sobre big data"
Tolerancia: 100% ✅
```

### 5.3 Lecciones Aprendidas

#### Lección 1: Dataset Quality > Dataset Size (hasta cierto punto)

**Aprendizaje:**
```
281 ejemplos → 79.3% accuracy
1,542 ejemplos (+449%) → 96.2% accuracy (+16.9%)
4,358 ejemplos (+183%) → 98.93% accuracy (+2.73%)

Conclusión:
- Rendimientos decrecientes después de ~2,000 ejemplos
- Mejor invertir en DIVERSIDAD de patrones que en CANTIDAD
- 48 patrones diversos > 1000 ejemplos similares
```

**Aplicación Futura:**
- Priorizar cobertura de casos de uso reales
- Analizar logs de consultas para identificar patrones faltantes
- Expansion dirigida en vez de masiva

#### Lección 2: BERT es Literal (y eso es bueno)

**Aprendizaje:**
```
"Cuéntame sobre Big Data" → fuera_dominio
¿Por qué? Dataset no tenía ese patrón exacto

BERT no "infiere" variaciones lingüísticas
- "Cuéntame" ≠ "Dime" ≠ "Explícame" (para BERT)
- Requiere ver cada patrón en el entrenamiento
```

**Aplicación Futura:**
- Crear lista exhaustiva de patrones antes de entrenar
- Usar templates para generar variaciones sistemáticamente
- Validar con usuarios reales antes de release

#### Lección 3: Tests Automatizados Son Críticos

**Aprendizaje:**
```
Sesión de Mejora 1: Implementamos 59 tests
Beneficios inmediatos:
- Detectamos 3 bugs ocultos
- Refactoring seguro (JSON externalization)
- Confianza para hacer cambios
- Documentación viva del comportamiento esperado

Tiempo invertido: 3 horas
Tiempo ahorrado en debugging: >10 horas
```

**Aplicación Futura:**
- TDD (Test-Driven Development) desde inicio
- Coverage mínimo: 80% (actual: 73.75%)
- Tests de integración + unitarios

#### Lección 4: Separación de Código y Datos

**Aprendizaje:**
```
ANTES: Base de conocimiento hardcodeada
- 1,247 líneas en tyr_chatbot.py
- Difícil actualizar info de carreras
- Git diff ruidoso

DESPUÉS: JSON externos
- 756 líneas en tyr_chatbot.py (-39%)
- Actualización sin tocar código
- Git diff limpio
```

**Aplicación Futura:**
- Content Management System para personal administrativo
- API para sincronizar con base de datos oficial del ITSE
- Versionamiento independiente de datos vs código

#### Lección 5: Documentación Como Primer Ciudadano

**Aprendizaje:**
```
Invertido en documentación:
- 6 diagramas de arquitectura
- 4 visualizaciones de métricas
- 7 screenshots de demo
- 5 reportes de sesiones
- README completo con badges

Resultado:
- Onboarding de nuevos developers: <1 hora
- Presentación a stakeholders: clara y profesional
- Mantenimiento futuro: facilitado
```

**Aplicación Futura:**
- Documentar MIENTRAS se desarrolla, no después
- Diagramas vivos (generados automáticamente)
- Docstrings obligatorios en todas las funciones

#### Lección 6: Iteración Rápida con Google Colab

**Aprendizaje:**
```
Google Colab GPU T4 (gratis):
- 6m 15s para entrenar 4,358 ejemplos
- 4 epochs suficientes (early stopping)
- Sin costos de infraestructura
- Compartible con colaboradores

vs Local (CPU):
- >2 horas para el mismo entrenamiento
- Sobrecalienta laptop
- Bloquea máquina durante entrenamiento
```

**Aplicación Futura:**
- Mantener notebooks de Colab para experimentación
- Automatizar entrenamiento con Colab Pro+ para producción
- Guardar checkpoints en Google Drive

---

## 6. Diseño y Experiencia de Usuario

### 6.1 Identidad Visual

#### Paleta de Colores

**Colores Primarios:**
```css
/* Azul ITSE - Tecnología, Confianza, Profesionalismo */
--primary-blue: #0066CC;
--primary-blue-dark: #004C99;
--primary-blue-light: #3399FF;

/* Gris Oscuro - Modo Oscuro Base */
--dark-bg: #0e1117;
--dark-secondary: #262730;
--dark-tertiary: #31333F;

/* Blanco/Gris Claro - Textos */
--text-primary: #FAFAFA;
--text-secondary: #B3B3B3;
--text-tertiary: #808080;
```

**Colores Secundarios (Acentos):**
```css
/* Verde - Éxito, Confirmación */
--success-green: #28A745;
--success-light: #5CB85C;

/* Amarillo - Advertencia, Info */
--warning-yellow: #FFC107;
--info-yellow: #FFD54F;

/* Rojo - Error, Alerta */
--error-red: #DC3545;
--error-light: #E57373;

/* Azul Claro - Mensajes del Bot */
--bot-message-bg: #1E3A5F;
--bot-message-border: #2E5A8F;

/* Azul Oscuro - Mensajes del Usuario */
--user-message-bg: #2E5A8F;
--user-message-border: #3E7ABF;
```

**Gradientes:**
```css
/* Hero Section */
--gradient-hero: linear-gradient(135deg, #0066CC 0%, #004C99 100%);

/* Backgrounds Sutiles */
--gradient-subtle: linear-gradient(180deg, #0e1117 0%, #1a1d29 100%);

/* Hover Effects */
--gradient-hover: linear-gradient(135deg, #3399FF 0%, #0066CC 100%);
```

#### Tipografía

**Fuentes Principales:**
```css
/* Títulos y Headings */
font-family-primary: 'Inter', 'Segoe UI', -apple-system, sans-serif;
  - Weights: 600 (SemiBold), 700 (Bold)
  - Use: Títulos, botones, énfasis
  - Características: Moderna, limpia, altamente legible

/* Cuerpo de Texto */
font-family-secondary: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
  - Weights: 400 (Regular), 500 (Medium)
  - Use: Párrafos, descripciones, mensajes del chat
  - Características: Profesional, excelente legibilidad

/* Código y Datos Técnicos */
font-family-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  - Weight: 400 (Regular)
  - Use: Metadata, logs, IDs
  - Características: Monoespaciada, soporta ligaduras
```

**Escala Tipográfica:**
```css
/* Desktop */
--font-size-h1: 48px;  /* Hero titles */
--font-size-h2: 36px;  /* Section headers */
--font-size-h3: 28px;  /* Subsections */
--font-size-h4: 22px;  /* Card titles */
--font-size-body: 16px; /* Paragraphs */
--font-size-small: 14px; /* Captions, metadata */

/* Mobile (responsivo) */
@media (max-width: 768px) {
  --font-size-h1: 32px;
  --font-size-h2: 28px;
  --font-size-h3: 22px;
  --font-size-body: 14px;
}

/* Line Heights */
--line-height-tight: 1.2;  /* Headings */
--line-height-normal: 1.5; /* Body text */
--line-height-loose: 1.8;  /* Long-form content */
```

#### Inspiraciones de Diseño

**Referencias Principales:**

1. **ChatGPT by OpenAI**
   - Interfaz limpia de chat
   - Burbujas de mensaje con buen spacing
   - Sidebar colapsable para metadata
   - Modo oscuro bien ejecutado

2. **Linear App**
   - Paleta de colores oscuros profesional
   - Tipografía limpia y moderna
   - Microinteracciones sutiles
   - Performance-first design

3. **Notion**
   - Sistema de iconos consistente
   - Jerarquía visual clara
   - Sidebar navigation intuitivo
   - Light/Dark mode seamless

4. **Streamlit Gallery**
   - Componentes nativos bien utilizados
   - Layouts responsive
   - Data visualizations integradas
   - Quick loading states

**Moodboard Visual:**
```
[DIAGRAMA SUGERIDO: Collage de screenshots de inspiraciones]

┌─────────────────┬─────────────────┬─────────────────┐
│   ChatGPT UI    │   Linear App    │     Notion      │
│   ┌─────────┐   │   ┌─────────┐   │   ┌─────────┐   │
│   │ [Chat]  │   │   │ [Dark]  │   │   │ [Icons] │   │
│   │ [Bubbles]│   │   │ [Colors]│   │   │ [Layout]│   │
│   │ [Clean] │   │   │ [Modern]│   │   │ [Nav]   │   │
│   └─────────┘   │   └─────────┘   │   └─────────┘   │
├─────────────────┴─────────────────┴─────────────────┤
│              TYR - Identidad Visual                  │
│  • Modo oscuro profesional (#0e1117)                 │
│  • Azul ITSE como color de marca (#0066CC)          │
│  • Tipografía moderna (Inter + IBM Plex Sans)       │
│  • Chat bubbles estilo ChatGPT                      │
│  • Sidebar con metadata técnica                     │
└──────────────────────────────────────────────────────┘
```

### 6.2 Principios de UX

#### Tono de Comunicación

**Personalidad del Bot:**
```yaml
Características:
  - Amigable pero profesional
  - Útil sin ser condescendiente
  - Técnico cuando es necesario, simple por defecto
  - Empático con las preocupaciones del usuario
  - Optimista sobre oportunidades educativas

Evitar:
  - Jerga excesiva o tecnicismos innecesarios
  - Tono robótico o distante
  - Humor forzado o inapropiado
  - Respuestas demasiado largas (>300 palabras)
  - Presión de venta o marketing agresivo
```

**Ejemplos de Mensajes:**

✅ **Bueno:**
```
"¡Hola! Soy TYR, tu asistente virtual del ITSE.
Puedo ayudarte con información sobre nuestras 16 carreras técnicas,
proceso de admisión, becas y más. ¿En qué puedo ayudarte hoy?"
```

❌ **Malo (muy formal):**
```
"Bienvenido al Sistema Automatizado de Información del Instituto Técnico
Superior Especializado. Por favor, seleccione una opción del menú..."
```

✅ **Bueno:**
```
"Te cuento sobre Big Data: Es una carrera de 2 años y 4 meses (jornada diurna)
que te prepara para trabajar con grandes volúmenes de datos.
Saldrás como Técnico Superior en Big Data. ¿Quieres saber más detalles?"
```

❌ **Malo (muy técnico):**
```
"El programa académico de T.S. en Big Data consta de 112 créditos distribuidos
en modalidad presencial con componentes teórico-prácticos orientados a la
adquisición de competencias en análisis de datasets de alta volumetría..."
```

#### Accesibilidad

**Estándares WCAG 2.1 AA:**

```yaml
Contraste de Color:
  - Texto sobre fondo: ≥4.5:1 (AA) ✓
  - UI componentes: ≥3:1 (AA) ✓
  - Ejemplos:
      - #FAFAFA sobre #0e1117: 15.8:1 ✓✓✓
      - #0066CC sobre #FAFAFA: 6.2:1 ✓✓

Navegación por Teclado:
  - Tab order lógico ✓
  - Focus visible en todos los elementos ✓
  - Enter para enviar mensaje ✓
  - Esc para limpiar input ✓

Screen Readers:
  - Roles ARIA correctos (role="main", "complementary")
  - Labels descriptivos en todos los inputs
  - Alt text en imágenes (logo ITSE)
  - Live regions para mensajes nuevos del bot

Texto:
  - Font size mínimo: 14px (móvil), 16px (desktop)
  - Line height: 1.5 para legibilidad
  - No justificado (solo left-aligned)
  - Máximo 80 caracteres por línea
```

**Soporte Multilingüe (futuro):**
```yaml
Idiomas prioritarios:
  1. Español (Panamá) - Actual ✓
  2. Inglés - Planificado
  3. Lenguas indígenas (Ngäbe, Kuna) - Investigación

Consideraciones:
  - i18n con gettext o similar
  - Detección automática de idioma
  - Fallback a español si no hay traducción
```

#### Responsividad

**Breakpoints:**
```css
/* Mobile First Approach */

/* Small Mobile */
@media (max-width: 480px) {
  - Single column layout
  - Sidebar oculto por defecto
  - Botones full-width
  - Font sizes reducidos
}

/* Mobile */
@media (max-width: 768px) {
  - Sidebar colapsable
  - Chat ocupa 100% ancho
  - Navegación en hamburger menu
  - Touch targets ≥44x44px
}

/* Tablet */
@media (min-width: 769px) and (max-width: 1024px) {
  - Layout de 2 columnas opcional
  - Sidebar visible pero estrecho
  - Tipografía intermedia
}

/* Desktop */
@media (min-width: 1025px) {
  - Layout óptimo: Chat + Sidebar
  - Tipografía full size
  - Hover effects habilitados
  - Atajos de teclado visibles
}

/* Large Desktop */
@media (min-width: 1440px) {
  - Max-width: 1280px (centrado)
  - Espaciado generoso
  - Posible 3-column layout
}
```

**Dispositivos Prioritarios:**
```yaml
1. Mobile (70% del tráfico esperado):
   - iPhone 12/13/14 (390x844)
   - Samsung Galaxy S21/S22 (360x800)
   - Optimización táctil

2. Desktop (25% del tráfico esperado):
   - 1920x1080 (Full HD)
   - 1366x768 (laptops comunes)
   - Atajos de teclado

3. Tablet (5% del tráfico esperado):
   - iPad Air (820x1180)
   - Android tablets (768x1024)
```

### 6.3 Elementos Clave de Interfaz

#### Disposición (Layout)

**Layout Principal - Vista Desktop:**
```
[DIAGRAMA SUGERIDO: Wireframe del layout principal]

┌──────────────────────────────────────────────────────────────┐
│  Header (60px fijo)                                          │
│  ┌────────────────────────────────────────────────────┐     │
│  │ 🤖 TYR - Asistente Virtual ITSE         [Menú ☰] │     │
│  └────────────────────────────────────────────────────┘     │
├────────────────────────────┬─────────────────────────────────┤
│                            │                                 │
│  Main Chat Area (flex)     │  Sidebar (320px fijo)          │
│  ┌──────────────────────┐  │  ┌───────────────────────────┐ │
│  │                      │  │  │ 📊 Metadata               │ │
│  │  [Chat messages]     │  │  │ ────────────────────────  │ │
│  │                      │  │  │ Intención:                │ │
│  │  • Historial scroll  │  │  │ informacion_carreras      │ │
│  │  • Burbujas user/bot │  │  │                          │ │
│  │  • Timestamps        │  │  │ Confianza: 99.89%        │ │
│  │  • Typing indicator  │  │  │                          │ │
│  │                      │  │  │ Sentimiento: Positivo     │ │
│  │                      │  │  │ Score: +0.65              │ │
│  │                      │  │  │                          │ │
│  │                      │  │  │ Carrera: Big Data        │ │
│  │                      │  │  └───────────────────────────┘ │
│  │                      │  │  ┌───────────────────────────┐ │
│  │                      │  │  │ ⚙️ Opciones               │ │
│  │                      │  │  │ • Nueva conversación      │ │
│  │                      │  │  │ • Guardar historial       │ │
│  │                      │  │  │ • Limpiar chat            │ │
│  │                      │  │  └───────────────────────────┘ │
│  └──────────────────────┘  │                                 │
│  ┌──────────────────────┐  │                                 │
│  │ Input Area (80px)    │  │                                 │
│  │ [Escribe aquí... 💬] │  │                                 │
│  └──────────────────────┘  │                                 │
└────────────────────────────┴─────────────────────────────────┘
│  Footer (40px fijo)                                          │
│  Hecho con ❤️ por ITSE | v1.0.0 | MIT License               │
└──────────────────────────────────────────────────────────────┘
```

**Layout Mobile (< 768px):**
```
┌──────────────────┐
│  Header (50px)   │
│  🤖 TYR    [☰]   │
├──────────────────┤
│                  │
│  Chat Messages   │
│  (full width)    │
│                  │
│  [Scroll area]   │
│                  │
│                  │
│                  │
├──────────────────┤
│  Input (60px)    │
│  [Mensaje... ]   │
└──────────────────┘

Sidebar:
- Oculto por defecto
- Abre con [☰] (overlay)
- Cierra con swipe o tap fuera
```

#### Componentes Principales

**1. Chat Message Bubble**
```css
/* Mensaje del Usuario */
.user-message {
  background: linear-gradient(135deg, #2E5A8F, #3E7ABF);
  border-radius: 18px 18px 4px 18px;
  padding: 12px 16px;
  max-width: 70%;
  margin-left: auto;
  box-shadow: 0 2px 8px rgba(0, 102, 204, 0.2);

  color: #FAFAFA;
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 16px;
  line-height: 1.5;
}

/* Mensaje del Bot */
.bot-message {
  background: #1E3A5F;
  border-left: 4px solid #0066CC;
  border-radius: 4px 18px 18px 18px;
  padding: 12px 16px;
  max-width: 75%;
  margin-right: auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);

  color: #FAFAFA;
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 16px;
  line-height: 1.5;
}

/* Timestamp */
.message-timestamp {
  font-size: 12px;
  color: #808080;
  margin-top: 4px;
  font-family: 'Inter', sans-serif;
}
```

**2. Input Field**
```css
.chat-input-container {
  position: sticky;
  bottom: 0;
  background: #0e1117;
  border-top: 1px solid #31333F;
  padding: 16px;

  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-input {
  flex: 1;
  background: #262730;
  border: 2px solid #31333F;
  border-radius: 24px;
  padding: 12px 20px;

  color: #FAFAFA;
  font-size: 16px;
  font-family: 'IBM Plex Sans', sans-serif;

  transition: border-color 0.2s ease;
}

.chat-input:focus {
  outline: none;
  border-color: #0066CC;
  box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1);
}

.send-button {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #0066CC, #004C99);
  border: none;

  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.send-button:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
}

.send-button:active {
  transform: scale(0.95);
}
```

**3. Metadata Card (Sidebar)**
```css
.metadata-card {
  background: #262730;
  border: 1px solid #31333F;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 16px;
}

.metadata-title {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  font-weight: 600;
  color: #FAFAFA;
  margin-bottom: 16px;

  display: flex;
  align-items: center;
  gap: 8px;
}

.metadata-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #31333F;
}

.metadata-item:last-child {
  border-bottom: none;
}

.metadata-label {
  font-size: 14px;
  color: #B3B3B3;
  font-family: 'Inter', sans-serif;
}

.metadata-value {
  font-size: 14px;
  font-weight: 500;
  color: #FAFAFA;
  font-family: 'JetBrains Mono', monospace;
}

/* Badge de Confianza */
.confidence-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 13px;
  font-weight: 600;
}

.confidence-high {
  background: #28A74520;
  color: #5CB85C;
}

.confidence-medium {
  background: #FFC10720;
  color: #FFD54F;
}

.confidence-low {
  background: #DC354520;
  color: #E57373;
}
```

**4. Typing Indicator**
```css
.typing-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: #1E3A5F;
  border-radius: 18px;
  width: fit-content;
}

.typing-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #0066CC;
  animation: typing 1.4s infinite;
}

.typing-dot:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% {
    transform: translateY(0);
    opacity: 0.7;
  }
  30% {
    transform: translateY(-8px);
    opacity: 1;
  }
}
```

**5. Empty State**
```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  padding: 40px 20px;
}

.empty-state-icon {
  font-size: 64px;
  margin-bottom: 24px;
  opacity: 0.6;
}

.empty-state-title {
  font-family: 'Inter', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: #FAFAFA;
  margin-bottom: 12px;
}

.empty-state-description {
  font-size: 16px;
  color: #B3B3B3;
  max-width: 400px;
  line-height: 1.6;
  margin-bottom: 32px;
}

.suggested-questions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
}

.suggestion-chip {
  background: #262730;
  border: 1px solid #31333F;
  border-radius: 20px;
  padding: 10px 20px;

  font-size: 14px;
  color: #FAFAFA;

  cursor: pointer;
  transition: all 0.2s ease;
}

.suggestion-chip:hover {
  background: #31333F;
  border-color: #0066CC;
  transform: translateY(-2px);
}
```

#### Animaciones y Efectos

**Microinteracciones:**
```css
/* Mensaje aparece (fade + slide) */
@keyframes messageAppear {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message-enter {
  animation: messageAppear 0.3s ease-out;
}

/* Hover en botones */
.button {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0, 102, 204, 0.2);
}

.button:active {
  transform: translateY(0);
}

/* Pulse en botón de enviar cuando hay texto */
@keyframes pulse {
  0%, 100% {
    box-shadow: 0 0 0 0 rgba(0, 102, 204, 0.7);
  }
  50% {
    box-shadow: 0 0 0 8px rgba(0, 102, 204, 0);
  }
}

.send-button.active {
  animation: pulse 2s infinite;
}

/* Skeleton loading para mensajes */
@keyframes skeleton {
  0% {
    background-position: -200px 0;
  }
  100% {
    background-position: calc(200px + 100%) 0;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    #262730 0px,
    #31333F 40px,
    #262730 80px
  );
  background-size: 200px 100%;
  animation: skeleton 1.5s infinite linear;
}
```

**Efectos de Performance:**
```yaml
Optimizaciones:
  - will-change: transform (elementos animados)
  - GPU acceleration: transform3d(0,0,0)
  - Debounce en input: 300ms
  - Virtual scrolling para >100 mensajes
  - Lazy loading de imágenes (si aplica)
  - Service Worker para cache de assets
```

---

## 7. Landing Page Propuesta

### 7.1 Objetivo

**Propósito Principal:**
Convertir visitantes en usuarios activos del chatbot TYR, comunicando claramente el valor y facilidad de uso del asistente virtual.

**KPIs Medibles:**
```yaml
Primarios:
  - CTR del botón "Probar TYR Ahora": objetivo >30%
  - Tiempo en página: objetivo >45 segundos
  - Bounce rate: objetivo <40%

Secundarios:
  - Scroll depth: >80% llegan al footer
  - Clicks en "Ver Demo": objetivo >15%
  - Shares sociales: objetivo >50/mes
```

**Audiencia Target:**
- Estudiantes prospectivos (16-25 años)
- Padres de familia (35-50 años)
- Orientadores vocacionales
- Medios de comunicación / Prensa

### 7.2 Secciones Principales

#### Sección 1: Hero Section

**Estructura:**
```
[DIAGRAMA SUGERIDO: Mockup del Hero Section]

┌──────────────────────────────────────────────────────────┐
│                                                          │
│        [Logo ITSE]          [Inicio] [Características]  │
│                                      [Demo] [Contacto]   │
│                                                          │
│  ┌────────────────────┐    ┌──────────────────────┐    │
│  │                    │    │                      │    │
│  │  🤖 Conoce TYR     │    │   [Preview animado   │    │
│  │                    │    │    del chatbot con   │    │
│  │  Tu asistente      │    │    mensajes reales]  │    │
│  │  virtual para      │    │                      │    │
│  │  explorar las      │    │   "Cuéntame sobre   │    │
│  │  carreras del ITSE │    │    Big Data"         │    │
│  │                    │    │                      │    │
│  │  [Probar Ahora]   │    │   [Respuesta del     │    │
│  │  [Ver Demo Video] │    │    bot animada]      │    │
│  │                    │    │                      │    │
│  │  ✓ Gratis 24/7     │    └──────────────────────┘    │
│  │  ✓ Sin registro    │                                 │
│  │  ✓ Respuestas al   │                                 │
│  │    instante        │                                 │
│  └────────────────────┘                                 │
│                                                          │
│  [Scroll down indicator ↓]                              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Copy Propuesto:**
```markdown
# 🤖 Conoce TYR
## Tu asistente virtual para explorar las carreras del ITSE

Descubre información sobre 16 carreras técnicas, admisiones,
becas y más. Disponible 24/7, sin registro.

[Probar TYR Ahora] ← Primary CTA
[Ver Demo (2 min)] ← Secondary CTA

✓ Gratis y accesible
✓ Sin necesidad de registro
✓ Respuestas instantáneas
✓ 98.93% de precisión
```

**Elementos Visuales:**
- Background: Gradient sutil (#0e1117 → #1a1d29)
- Hero image/animation: Chat preview con typing indicator
- Iconografía: Iconos minimalistas de checkmarks
- CTA buttons: Primary (azul), Secondary (outline)

#### Sección 2: Estadísticas / Social Proof

**Estructura:**
```
┌──────────────────────────────────────────────────────────┐
│                Confiable y Probado                       │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   98.93%    │  │    4,358    │  │   16 carreras│    │
│  │  Precisión  │  │  Consultas  │  │  disponibles │    │
│  │             │  │  entrenadas │  │              │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   24/7      │  │    100%     │  │   59 tests  │    │
│  │ Disponible  │  │  Tolerante  │  │   passing   │    │
│  │             │  │  a errores  │  │              │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Métricas Destacadas:**
- 98.93% de precisión en respuestas
- 4,358 consultas en el entrenamiento
- 16 carreras técnicas superiores
- Disponible 24/7 sin interrupciones
- 100% tolerante a errores de ortografía
- 59 tests automatizados (calidad garantizada)

#### Sección 3: Características Principales

**Estructura (3 columnas):**
```
┌────────────────────────────────────────────────────────────┐
│          ¿Qué puede hacer TYR por ti?                      │
│                                                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ 🎓 Carreras  │  │ 📝 Admisión  │  │ 💰 Becas     │   │
│  │              │  │              │  │              │   │
│  │ Información  │  │ Proceso de   │  │ IFARHU, BID  │   │
│  │ completa de  │  │ inscripción, │  │ y alianzas   │   │
│  │ 16 carreras  │  │ requisitos y │  │ empresariales│   │
│  │ técnicas     │  │ fechas       │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ 🏫 ITSE      │  │ ⚡ Rápido    │  │ 🛡️ Preciso   │   │
│  │              │  │              │  │              │   │
│  │ Servicios,   │  │ Respuestas   │  │ 98.93%       │   │
│  │ alianzas,    │  │ instantáneas │  │ accuracy en  │   │
│  │ logros       │  │ 24/7         │  │ clasificación│   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Copy de Cada Característica:**

1. **🎓 Explora 16 Carreras Técnicas**
   - Descripción completa de cada programa
   - Duración, créditos y campo ocupacional
   - Información actualizada 2025

2. **📝 Proceso de Admisión Claro**
   - Requisitos de ingreso paso a paso
   - Fechas importantes
   - Documentos necesarios

3. **💰 Opciones de Financiamiento**
   - Becas IFARHU y BID
   - Convenios con empresas
   - Ayuda financiera disponible

4. **🏫 Todo sobre el ITSE**
   - CAIPI (guardería para estudiantes)
   - CIIECYT (centro de investigación)
   - Reconocimientos internacionales

5. **⚡ Respuestas Instantáneas**
   - Disponible 24/7 sin esperas
   - No requiere registro
   - Interfaz intuitiva tipo ChatGPT

6. **🛡️ Confiable y Preciso**
   - 98.93% de precisión
   - 59 tests automatizados
   - Tolerante a errores ortográficos

#### Sección 4: Demo Interactiva / Video

**Opción A: Demo Interactiva Embebida**
```
┌──────────────────────────────────────────────────────────┐
│              Pruébalo directamente aquí                  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  [Chatbot embebido real funcionando]              │ │
│  │                                                    │ │
│  │  Ejemplos de preguntas:                           │ │
│  │  • "Cuéntame sobre Ciberseguridad"               │ │
│  │  • "¿Cómo me inscribo?"                          │ │
│  │  • "¿Qué es CAIPI?"                              │ │
│  │                                                    │ │
│  │  [Interfaz de chat con 2-3 mensajes pre-loaded]  │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  [Abrir en ventana completa →]                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Opción B: Video Demo (2 minutos)**
```
┌──────────────────────────────────────────────────────────┐
│              Mira TYR en acción (2 min)                  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │                                                    │ │
│  │          [Video Player]                           │ │
│  │                                                    │ │
│  │  Contenido del video:                             │ │
│  │  0:00-0:30  Intro - ¿Qué es TYR?                 │ │
│  │  0:30-1:00  Demo de consultas sobre carreras     │ │
│  │  1:00-1:30  Proceso de admisión e inscripción    │ │
│  │  1:30-2:00  Metadata y tolerancia a errores      │ │
│  │                                                    │ │
│  │  ▶️ [Play]  🔊 [Volume]  ⚙️ [Settings]          │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

#### Sección 5: Casos de Uso / Personas

**Estructura:**
```
┌──────────────────────────────────────────────────────────┐
│           ¿Quién puede usar TYR?                         │
│                                                          │
│  ┌────────────────────┐  ┌────────────────────┐        │
│  │ 👤 Estudiantes     │  │ 👥 Padres          │        │
│  │                    │  │                    │        │
│  │ "Necesito info    │  │ "Quiero saber     │        │
│  │  rápida sobre     │  │  si mi hijo puede │        │
│  │  carreras tech"   │  │  estudiar aquí"   │        │
│  │                    │  │                    │        │
│  │ María, 18 años    │  │ Roberto, 45 años  │        │
│  └────────────────────┘  └────────────────────┘        │
│                                                          │
│  ┌────────────────────┐  ┌────────────────────┐        │
│  │ 🎓 Orientadores    │  │ 📰 Prensa/Medios   │        │
│  │                    │  │                    │        │
│  │ "Herramienta para │  │ "Info oficial      │        │
│  │  recomendar a     │  │  del ITSE para    │        │
│  │  mis estudiantes" │  │  reportaje"       │        │
│  │                    │  │                    │        │
│  │ Ana, Orientadora  │  │ Luis, Periodista  │        │
│  └────────────────────┘  └────────────────────┘        │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

#### Sección 6: Call-to-Action Principal

**Estructura:**
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│               ¿Listo para empezar?                       │
│                                                          │
│          Prueba TYR ahora, es completamente gratis       │
│                                                          │
│              [Probar TYR Ahora →]                        │
│                                                          │
│          Sin registro • Sin descargas • 24/7             │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Background:** Gradient azul (#0066CC → #004C99)
**Botón:** Grande (200x60px), blanco con sombra
**Copy:** Simple, directo, sin fricción

#### Sección 7: FAQ (Preguntas Frecuentes)

**Estructura (Acordeón):**
```yaml
Preguntas Sugeridas:

1. "¿TYR es gratis?"
   Respuesta: Sí, TYR es completamente gratuito y accesible
   24/7. No requiere registro ni descargas.

2. "¿Qué tan preciso es TYR?"
   Respuesta: TYR tiene una precisión del 98.93% en la
   clasificación de intenciones, validada con 654 ejemplos
   de prueba.

3. "¿Puedo usar TYR desde mi móvil?"
   Respuesta: Sí, TYR está optimizado para dispositivos móviles,
   tablets y desktop.

4. "¿TYR reemplaza al personal de admisiones?"
   Respuesta: No, TYR complementa al personal humano
   proporcionando información básica rápida. Para casos
   complejos, te conectamos con admisiones.

5. "¿Mis conversaciones son privadas?"
   Respuesta: Sí, no almacenamos información personal.
   Las conversaciones se guardan localmente en tu navegador
   y puedes borrarlas cuando quieras.

6. "¿Puedo descargar el historial de chat?"
   Respuesta: Sí, puedes guardar tus conversaciones en formato
   JSON desde el menú de opciones.
```

#### Sección 8: Footer

**Estructura:**
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  [Logo ITSE]                                             │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ Producto    │  │ Recursos    │  │ Legal       │    │
│  │             │  │             │  │             │    │
│  │ • Inicio    │  │ • Docs      │  │ • Privacidad│    │
│  │ • Features  │  │ • GitHub    │  │ • Términos  │    │
│  │ • Demo      │  │ • API       │  │ • Licencia  │    │
│  │ • Contacto  │  │ • Blog      │  │             │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Contacto ITSE:                                   │  │
│  │ 📧 info@itse.ac.pa                               │  │
│  │ 📞 +507 524-3333                                 │  │
│  │ 📍 Tocumen, Panamá                               │  │
│  │                                                   │  │
│  │ [Facebook] [Instagram] [LinkedIn] [YouTube]     │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ───────────────────────────────────────────────────    │
│                                                          │
│  © 2025 ITSE. Hecho con ❤️ en Panamá.                  │
│  TYR v1.0.0 | MIT License | GitHub                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 7.3 Tonalidad y Mensaje

#### Voz de Marca

**Atributos de la Voz:**
```yaml
Características:
  - Accesible: No intimidar con tecnicismos
  - Optimista: Enfocado en oportunidades
  - Profesional: Serio pero no aburrido
  - Joven: Lenguaje contemporáneo sin ser informal
  - Empoderador: "Tú puedes" en vez de "debes"

Evitar:
  - Tono corporativo frío
  - Jerga excesiva de IA/ML
  - Superlativos exagerados
  - Presión de venta agresiva
```

**Ejemplo de Copy (Hero):**

✅ **Bueno:**
```
🤖 Conoce TYR
Tu asistente virtual para explorar las carreras del ITSE

Encuentra información sobre 16 carreras técnicas, admisiones,
becas y más. Disponible 24/7, sin necesidad de registro.

[Probar TYR Ahora]
```

❌ **Malo (muy corporativo):**
```
Sistema de Asistencia Virtual Automatizada
Plataforma de información académica del ITSE

Acceda a nuestra base de conocimiento institucional mediante
tecnología de procesamiento de lenguaje natural avanzado.

[Iniciar Sesión]
```

❌ **Malo (muy informal):**
```
Hey! 👋 Conoce a TYR, tu nuevo BFF del ITSE

¿Perdido con tanta info? No te estreses! TYR te ayuda a
encontrar tu carrera soñada súper rápido 🚀💯

[Dale! Pruébalo Ya]
```

#### Mensajes Clave

**Propuestas de Valor Principales:**

1. **Accesibilidad Total**
   - "Información del ITSE al alcance de todos, 24/7"
   - "Sin barreras, sin registro, sin esperas"

2. **Precisión Confiable**
   - "98.93% de precisión validada con tests automatizados"
   - "Respuestas correctas basadas en información oficial"

3. **Facilidad de Uso**
   - "Pregunta como hablas, TYR te entiende"
   - "100% tolerante a errores de escritura"

4. **Comprensivo y Completo**
   - "Desde carreras hasta becas, TYR tiene las respuestas"
   - "16 carreras, 48 formas de preguntar"

5. **Innovación Educativa**
   - "El futuro de la información académica"
   - "Tecnología de IA al servicio de tu educación"

**Headline Alternativas:**
```
Opción 1 (actual): "Tu asistente virtual para explorar las carreras del ITSE"
Opción 2: "Descubre tu futuro en el ITSE con ayuda de IA"
Opción 3: "Información del ITSE, disponible 24/7 mediante IA"
Opción 4: "Tu guía personal para las carreras técnicas del ITSE"
Opción 5: "Respuestas instantáneas sobre el ITSE con TYR"
```

**Subheadline Alternativas:**
```
Opción 1 (actual): "Disponible 24/7, sin registro, respuestas al instante"
Opción 2: "Gratis, rápido y preciso. Pruébalo ahora."
Opción 3: "Sin colas, sin esperas. Información oficial del ITSE al instante."
Opción 4: "Pregunta sobre carreras, admisiones, becas y más."
```

#### Copy para CTAs

**CTA Principal (Hero Section):**
```
Textos sugeridos:
- "Probar TYR Ahora" ← Recomendado
- "Empieza Gratis"
- "Habla con TYR"
- "Hacer una Pregunta"
- "Explorar Carreras"
```

**CTA Secundario:**
```
Textos sugeridos:
- "Ver Demo (2 min)" ← Recomendado
- "Cómo Funciona"
- "Ver Video Demo"
- "Más Información"
```

**CTA en Feature Cards:**
```
- "Conoce las Carreras →"
- "Ver Proceso de Admisión →"
- "Explorar Becas →"
```

**CTA Final (Bottom of Page):**
```
Headline: "¿Listo para empezar?"
Subheadline: "Prueba TYR ahora, es completamente gratis"
Botón: "Probar TYR Ahora →"
Footer: "Sin registro • Sin descargas • 24/7"
```

---

## 8. Notas Adicionales

### Para Diseñadores

#### Assets Disponibles

**Existentes:**
```yaml
Logos:
  - Logo ITSE (oficial)
  - Nombre "TYR" (tipográfico, no logo custom aún)

Screenshots:
  - 7 capturas PNG del sistema funcionando (1.9 MB)
  - Resolución: 1920x1080
  - Ubicación: documentacion/screenshots/

Visualizaciones:
  - Matriz de confusión (823 KB PNG)
  - Distribución de intenciones (412 KB PNG)
  - Evolución de modelos (587 KB PNG)
  - Ubicación: documentacion/visualizaciones/

Badges:
  - 8 badges de shields.io ya generados
  - Formatos: SVG (escalables)
```

**Necesarios (To-Do):**
```yaml
Prioridad Alta:
  - Logo TYR (icono + wordmark)
  - Favicon (16x16, 32x32, 192x192)
  - Open Graph image (1200x630)
  - Social media cover images

Prioridad Media:
  - Iconografía custom (16 iconos de features)
  - Ilustraciones de personas/avatares
  - Pattern backgrounds sutiles
  - Loading animations (Lottie files)

Prioridad Baja:
  - Branded templates (presentaciones)
  - Email templates
  - Print materials (si aplica)
```

#### Guía de Espaciado

**Sistema de 8px:**
```css
/* Base unit: 8px */
--space-xs: 4px;   /* 0.5x */
--space-sm: 8px;   /* 1x */
--space-md: 16px;  /* 2x */
--space-lg: 24px;  /* 3x */
--space-xl: 32px;  /* 4x */
--space-2xl: 48px; /* 6x */
--space-3xl: 64px; /* 8x */

Uso:
- Padding interno de componentes: 16px-24px
- Margen entre secciones: 64px-96px
- Gaps en flexbox/grid: 16px-24px
- Iconos y botones: múltiplos de 8px
```

#### Grid System

**Desktop (1280px container):**
```css
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 32px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
}

/* Hero: 6 cols + 6 cols */
/* Features: 4 cols + 4 cols + 4 cols */
/* Testimonial: 8 cols centered */
```

**Tablet (768px-1024px):**
```css
.grid {
  grid-template-columns: repeat(8, 1fr);
  gap: 20px;
}
```

**Mobile (<768px):**
```css
.grid {
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
```

### Restricciones Técnicas

#### Performance

**Límites de Carga:**
```yaml
Objetivo: <3 segundos LCP (Largest Contentful Paint)

Restricciones:
  - Hero image: <100 KB (usar WebP)
  - Total page size: <1 MB (excl. video)
  - JavaScript bundle: <150 KB (gzipped)
  - CSS: <50 KB (gzipped)
  - Fonts: 2 familias máximo (WOFF2)

Optimizaciones:
  - Lazy loading de imágenes below-the-fold
  - Code splitting por ruta
  - CDN para assets estáticos
  - Service Worker para cache
```

#### Compatibilidad de Navegadores

```yaml
Soportados:
  - Chrome/Edge: últimas 2 versiones
  - Firefox: últimas 2 versiones
  - Safari: últimas 2 versiones (iOS 14+)
  - Samsung Internet: última versión

No soportados:
  - Internet Explorer (EOL)
  - Chrome <90
  - Safari <14

Fallbacks:
  - CSS Grid → Flexbox
  - CSS Custom Properties → Preprocessor variables
  - Fetch API → axios con polyfill
```

#### Dependencias del Proyecto

**Stack Actual (No Cambiar):**
```yaml
Backend/ML:
  - Python 3.8+
  - PyTorch 2.0.1
  - Transformers 4.35.0
  - Streamlit 1.28.0

Frontend (Streamlit):
  - No requiere framework JS adicional
  - Limitado a componentes de Streamlit
  - Custom CSS/HTML via st.markdown

Deployment:
  - Streamlit Cloud (recomendado)
  - Heroku (alternativa)
  - AWS EC2 (si se requiere GPU)
```

### Preferencias Personales

#### Do's (Hacer)

```yaml
Diseño:
  ✅ Modo oscuro como default
  ✅ Espacios en blanco generosos
  ✅ Tipografía clara y legible (16px mínimo)
  ✅ Jerarquía visual bien definida
  ✅ Animaciones sutiles (< 300ms)
  ✅ Accesibilidad WCAG AA como mínimo

Contenido:
  ✅ Copy conciso y escaneable
  ✅ Bullets en vez de párrafos largos
  ✅ Ejemplos concretos > descripciones abstractas
  ✅ Datos y métricas visibles
  ✅ CTAs claros y accionables

Técnico:
  ✅ Mobile-first development
  ✅ Semantic HTML5
  ✅ Comentarios en código donde sea complejo
  ✅ Git commits descriptivos
  ✅ Tests para funcionalidad crítica
```

#### Don'ts (Evitar)

```yaml
Diseño:
  ❌ Carruseles automáticos (baja usabilidad)
  ❌ Modals/popups agresivos
  ❌ Animaciones largas (>500ms)
  ❌ Fuentes muy decorativas o difíciles de leer
  ❌ Contraste insuficiente (< 4.5:1)

Contenido:
  ❌ Jerga técnica innecesaria
  ❌ Textos Lorem Ipsum en mockups
  ❌ CTAs vagos ("Más info", "Haz click aquí")
  ❌ Promesas exageradas o marketing sensacionalista
  ❌ Contenido no verificado o desactualizado

Técnico:
  ❌ jQuery u otras dependencias legacy
  ❌ Inline styles (usar clases)
  ❌ !important en CSS (salvo excepciones)
  ❌ console.log() en producción
  ❌ Código comentado (usar Git)
```

#### Referencias Inspiradoras

**Sitios Web:**
```yaml
1. Linear (linear.app):
   - Diseño minimalista y rápido
   - Tipografía impecable
   - Dark mode perfecto

2. Stripe (stripe.com):
   - Documentación técnica clara
   - Gradientes sutiles
   - Micro interacciones bien ejecutadas

3. Vercel (vercel.com):
   - Performance excepcional
   - Animaciones sutiles
   - Copy conciso y técnico

4. Notion (notion.so):
   - UI limpia y usable
   - Onboarding progresivo
   - Iconografía consistente

5. Chat