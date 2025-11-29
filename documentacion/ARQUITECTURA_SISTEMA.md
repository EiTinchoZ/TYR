# 🏗️ Arquitectura del Sistema TYR

**Proyecto:** TYR - Asistente Virtual ITSE
**Autor:** Martín Bundy
**Fecha:** 23 de Noviembre 2025
**Versión:** 1.0

---

## 📋 Índice

1. [Arquitectura General del Sistema](#arquitectura-general)
2. [Flujo de Procesamiento de Consultas](#flujo-de-procesamiento)
3. [Componentes del Sistema](#componentes-del-sistema)
4. [Stack Tecnológico](#stack-tecnológico)
5. [Base de Datos y Almacenamiento](#base-de-datos)

---

## 🏛️ Arquitectura General del Sistema

```mermaid
graph TB
    subgraph "Capa de Presentación"
        UI[Streamlit Web UI<br/>tyr_app.py]
        Input[Input de Usuario<br/>st.chat_input]
        Display[Display de Respuestas<br/>st.chat_message]
    end

    subgraph "Capa de Lógica de Negocio"
        TYR[TYR Chatbot Core<br/>tyr_chatbot.py]
        Norm[Normalizador de Texto<br/>procesar_entrada]
        Router[Sistema de Prioridades<br/>3 capas]
    end

    subgraph "Capa de Machine Learning"
        BERT[BERT Classifier<br/>dccuchile/bert-base-spanish]
        VADER[VADER Sentiment<br/>vaderSentiment-es]
        Model[Modelo Entrenado<br/>modelo_bert_tyr_4358]
    end

    subgraph "Capa de Datos"
        JSON1[carreras_itse.json<br/>16 carreras]
        JSON2[respuestas_base.json<br/>9 intenciones]
        Dataset[Dataset_TYR_3000_FINAL.json<br/>4,358 ejemplos]
    end

    UI --> Input
    Input --> TYR
    TYR --> Norm
    Norm --> BERT
    BERT --> Model
    Model --> Router
    Router --> VADER
    VADER --> TYR
    TYR --> JSON1
    TYR --> JSON2
    TYR --> Display
    Display --> UI

    style UI fill:#4A90E2
    style TYR fill:#50C878
    style BERT fill:#F39C12
    style Model fill:#E74C3C
    style JSON1 fill:#9B59B6
    style JSON2 fill:#9B59B6
```

### Descripción de Capas

**Capa de Presentación (Streamlit)**
- Interfaz web moderna estilo ChatGPT
- Input fluido con soporte de Enter
- Historial de conversaciones
- Métricas en tiempo real

**Capa de Lógica de Negocio (TYR Core)**
- Normalización de texto (tolerancia a errores)
- Sistema de prioridades de 3 capas
- Enrutamiento inteligente de respuestas
- Análisis de sentimientos

**Capa de Machine Learning**
- BERT fine-tuned en español
- Clasificación de 9 intenciones
- Análisis de sentimientos con VADER
- Confianza > 80% para respuestas

**Capa de Datos**
- Base de conocimiento externalizada
- 16 carreras del ITSE
- 9 respuestas predefinidas
- Dataset de 4,358 ejemplos

---

## 🔄 Flujo de Procesamiento de Consultas

```mermaid
flowchart TD
    Start([Usuario ingresa consulta]) --> Input[Recibir input de usuario]
    Input --> Normalize[Normalizar texto<br/>- Minúsculas<br/>- Sin tildes<br/>- Sin puntuación]

    Normalize --> Tokenize[Tokenizar con BERT<br/>dccuchile/bert-base-spanish]
    Tokenize --> Classify[Clasificar intención<br/>9 clases posibles]

    Classify --> Confidence{Confianza<br/>>= 80%?}

    Confidence -->|No| FallbackGeneral[Respuesta genérica<br/>fuera_dominio]
    Confidence -->|Sí| Intent[Obtener intención clasificada]

    Intent --> Priority1{Prioridad 1:<br/>¿Carrera<br/>específica?}

    Priority1 -->|Sí| CareerDetect[Detectar carrera en texto<br/>16 carreras ITSE]
    Priority1 -->|No| Priority2

    CareerDetect --> CareerInfo[Generar respuesta<br/>específica de carrera]

    Priority2{Prioridad 2:<br/>¿Keywords<br/>especiales?}

    Priority2 -->|Sí| SpecialInfo[Respuesta contextual<br/>CAIPI, CIIECYT, etc.]
    Priority2 -->|No| Priority3

    Priority3[Prioridad 3:<br/>Respuesta base]
    Priority3 --> BaseResponse[Respuesta desde<br/>respuestas_base.json]

    CareerInfo --> Sentiment[Análisis de sentimiento<br/>VADER]
    SpecialInfo --> Sentiment
    BaseResponse --> Sentiment
    FallbackGeneral --> Sentiment

    Sentiment --> Metadata[Generar metadata<br/>- Intención<br/>- Confianza<br/>- Sentimiento]

    Metadata --> Display[Mostrar respuesta<br/>+ metadata en UI]
    Display --> End([Fin])

    style Start fill:#4A90E2
    style Normalize fill:#50C878
    style Classify fill:#F39C12
    style Sentiment fill:#E74C3C
    style Display fill:#9B59B6
    style End fill:#4A90E2
```

### Descripción del Flujo

**1. Entrada de Usuario**
- Usuario escribe consulta en interfaz Streamlit
- Input capturado con `st.chat_input()`

**2. Normalización (Paso crítico)**
- Conversión a minúsculas
- Eliminación de tildes con `unicodedata`
- Remoción de puntuación
- Limpieza de espacios múltiples

**3. Clasificación con BERT**
- Tokenización con tokenizer de BERT
- Forward pass por modelo fine-tuned
- Softmax para probabilidades
- Selección de intención con mayor confianza

**4. Sistema de Prioridades (3 Capas)**

**Prioridad 1:** Detección de carreras específicas
- Busca keywords de 16 carreras en texto normalizado
- Genera respuesta detallada de la carrera
- Ejemplo: "big data" → Info completa de T.S. en Big Data

**Prioridad 2:** Keywords especiales
- CAIPI, CIIECYT, reconocimientos, alianzas
- Respuestas contextuales específicas
- Información actualizada 2025

**Prioridad 3:** Respuesta base por intención
- Usa `respuestas_base.json`
- Respuesta genérica de la intención clasificada

**5. Análisis de Sentimiento**
- VADER-es analiza el sentimiento de la consulta
- Categoría: positivo/negativo/neutro
- Score compound: -1 a +1

**6. Generación de Metadata**
- Intención detectada
- Confianza del modelo (%)
- Sentimiento y score

---

## 🧩 Componentes del Sistema

```mermaid
graph LR
    subgraph "tyr_chatbot.py - Clase TYR"
        Init[__init__<br/>Inicialización]
        Load[_cargar_modelo_bert<br/>Cargar BERT]
        LoadData[_cargar_respuestas_base<br/>Cargar JSONs]
        Proc[procesar_entrada<br/>Normalización]
        Class[clasificar_intencion<br/>BERT]
        Sent[analizar_sentimiento<br/>VADER]
        Resp[generar_respuesta<br/>3 prioridades]
        ProcCon[procesar_consulta<br/>Orquestador]
    end

    subgraph "Modelos ML"
        BERTModel[BERT Model<br/>4358 params]
        Tokenizer[AutoTokenizer<br/>Spanish]
        VADERModel[VADER-es<br/>Sentiment]
    end

    subgraph "Datos Externos"
        Career[carreras_itse.json]
        Resp2[respuestas_base.json]
        LabelMap[label_map.json]
    end

    Init --> Load
    Load --> BERTModel
    Load --> Tokenizer
    Init --> LoadData
    LoadData --> Career
    LoadData --> Resp2
    LoadData --> LabelMap

    ProcCon --> Proc
    Proc --> Class
    Class --> BERTModel
    Class --> Tokenizer
    Class --> Resp
    Resp --> Sent
    Sent --> VADERModel

    style Init fill:#4A90E2
    style Load fill:#50C878
    style Class fill:#F39C12
    style BERTModel fill:#E74C3C
    style Career fill:#9B59B6
```

### Descripción de Componentes

**Clase TYR (tyr_chatbot.py)**

```python
class TYR:
    def __init__(self, modelo_path, device='cpu'):
        # Carga BERT, VADER, y datos JSON

    def procesar_entrada(self, texto: str) -> str:
        # Normalización completa de texto

    def clasificar_intencion(self, texto: str) -> tuple:
        # Clasificación con BERT
        # Returns: (intención, confianza, probabilidades)

    def analizar_sentimiento(self, texto: str) -> dict:
        # Análisis con VADER-es
        # Returns: {categoria, score_compound}

    def generar_respuesta(self, texto_norm: str, intencion: str) -> str:
        # Sistema de 3 prioridades
        # Returns: respuesta contextual

    def procesar_consulta(self, texto: str) -> tuple:
        # Orquestador principal
        # Returns: (respuesta, metadata)
```

**Métodos Privados**
- `_cargar_modelo_bert()`: Carga modelo desde disco
- `_cargar_carreras_desde_json()`: Carga 16 carreras
- `_cargar_respuestas_desde_json()`: Carga 9 respuestas
- `_obtener_carreras_hardcodeadas()`: Fallback carreras
- `_obtener_respuestas_hardcodeadas()`: Fallback respuestas

---

## 🛠️ Stack Tecnológico

```mermaid
graph TB
    subgraph "Frontend"
        ST[Streamlit 1.28.0<br/>Web Framework]
    end

    subgraph "Backend"
        PY[Python 3.8+<br/>Core Language]
    end

    subgraph "Machine Learning"
        HF[HuggingFace Transformers 4.35.0<br/>BERT Framework]
        PT[PyTorch 2.0.1<br/>Deep Learning]
        BERT[dccuchile/bert-base-spanish-wwm-cased<br/>Pre-trained Model]
        VADER[vaderSentiment-es 3.3.2<br/>Sentiment Analysis]
    end

    subgraph "Data Processing"
        NP[NumPy 1.24.3<br/>Numerical Computing]
        SKL[scikit-learn 1.3.0<br/>ML Utils]
        JSON[JSON<br/>Data Format]
    end

    subgraph "Visualization"
        MPL[matplotlib 3.7.2<br/>Plotting]
        SNS[seaborn 0.12.2<br/>Statistical Viz]
    end

    subgraph "Testing"
        PYT[pytest 9.0.1<br/>Testing Framework]
        COV[pytest-cov 7.0.0<br/>Coverage]
    end

    subgraph "Infrastructure"
        COLAB[Google Colab<br/>Training Platform]
        GPU[Tesla T4 GPU<br/>16GB VRAM]
    end

    ST --> PY
    PY --> HF
    HF --> PT
    HF --> BERT
    PY --> VADER
    PY --> NP
    PY --> SKL
    PY --> JSON
    PY --> MPL
    MPL --> SNS
    PY --> PYT
    PYT --> COV
    PT --> COLAB
    COLAB --> GPU

    style ST fill:#FF4B4B
    style BERT fill:#FFD43B
    style PT fill:#EE4C2C
    style PYT fill:#0A9EDC
    style COLAB fill:#F9AB00
```

### Versiones de Dependencias

| Componente | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.8+ | Lenguaje base |
| **transformers** | 4.35.0 | Framework BERT |
| **torch** | 2.0.1 | Deep learning |
| **streamlit** | 1.28.0 | Interfaz web |
| **vaderSentiment-es** | 3.3.2 | Análisis sentimientos |
| **numpy** | 1.24.3 | Computación numérica |
| **scikit-learn** | 1.3.0 | Métricas ML |
| **matplotlib** | 3.7.2 | Visualizaciones |
| **seaborn** | 0.12.2 | Gráficas estadísticas |
| **pytest** | 9.0.1 | Tests automatizados |
| **pytest-cov** | 7.0.0 | Coverage de tests |

---

## 💾 Base de Datos y Almacenamiento

```mermaid
erDiagram
    CARRERAS_JSON ||--o{ CARRERA : contiene
    RESPUESTAS_JSON ||--o{ RESPUESTA : contiene
    MODELO_BERT ||--|| LABEL_MAP : usa
    DATASET ||--o{ EJEMPLO : contiene

    CARRERAS_JSON {
        string _metadata "version, fecha, total"
        object carreras "16 carreras"
    }

    CARRERA {
        string nombre "T.S. en ..."
        string escuela "4 escuelas"
        int creditos "87-139"
        object duracion "diurna, nocturna"
        array jornadas "disponibles"
        string aprendizaje "descripción"
        array campo_ocupacional "empleos"
        string enlace "URL oficial"
    }

    RESPUESTAS_JSON {
        string _metadata "version, fecha"
        object respuestas "9 intenciones"
    }

    RESPUESTA {
        string respuesta "texto markdown"
        array keywords "palabras clave"
    }

    MODELO_BERT {
        string model_path "modelo_bert_tyr_4358/"
        object config "bert_config.json"
        object weights "pytorch_model.bin"
        object tokenizer "tokenizer files"
    }

    LABEL_MAP {
        int index "0-8"
        string label "nombre intención"
    }

    DATASET {
        int total "4358 ejemplos"
        string format "[[texto, label], ...]"
    }

    EJEMPLO {
        string texto "consulta usuario"
        string label "intención"
    }
```

### Estructura de Archivos JSON

**carreras_itse.json** (~83 KB)
```json
{
  "_metadata": {
    "version": "1.0",
    "fecha_actualizacion": "2025-11-23",
    "total_carreras": 16,
    "escuelas": [...]
  },
  "desarrollo de software": {
    "nombre": "T.S. en Desarrollo de Software",
    "escuela": "Innovación Digital",
    "creditos": 112,
    "duracion": {"diurna": "2 años 4 meses", "nocturna": "3 años"},
    "jornadas": ["diurna", "nocturna"],
    "aprendizaje": "...",
    "campo_ocupacional": [...],
    "enlace": "https://..."
  },
  ...
}
```

**respuestas_base.json** (~8 KB)
```json
{
  "_metadata": {
    "version": "1.0",
    "fecha_actualizacion": "2025-11-23",
    "total_intenciones": 9
  },
  "saludo_despedida": {
    "respuesta": "...",
    "keywords": [...]
  },
  ...
}
```

**label_map.json**
```json
{
  "0": "becas_financiamiento",
  "1": "contacto_ubicacion",
  "2": "faq_general",
  "3": "fuera_dominio",
  "4": "horarios_duracion",
  "5": "informacion_carreras",
  "6": "inscripcion_admision",
  "7": "requisitos_ingreso",
  "8": "saludo_despedida"
}
```

**Dataset_TYR_3000_FINAL.json** (4,358 ejemplos)
```json
[
  ["¿Cuéntame sobre Big Data?", "informacion_carreras"],
  ["¿Cómo me inscribo?", "inscripcion_admision"],
  ["¿Qué documentos necesito?", "requisitos_ingreso"],
  ...
]
```

---

## 🔐 Seguridad y Validación

```mermaid
graph TD
    Input[Input Usuario] --> Val1{Validación<br/>Input}
    Val1 -->|Texto vacío| Error1[Retornar error]
    Val1 -->|Texto válido| Norm[Normalización]

    Norm --> Val2{Longitud<br/><= 512 tokens?}
    Val2 -->|No| Trunc[Truncar a 512]
    Val2 -->|Sí| Process
    Trunc --> Process[Procesamiento]

    Process --> Val3{Confianza<br/>>= 80%?}
    Val3 -->|No| Fallback[Respuesta fallback]
    Val3 -->|Sí| Response[Respuesta confiable]

    Response --> Sanitize[Sanitizar output]
    Fallback --> Sanitize

    Sanitize --> Output[Output a usuario]

    style Val1 fill:#F39C12
    style Val2 fill:#F39C12
    style Val3 fill:#F39C12
    style Error1 fill:#E74C3C
    style Output fill:#50C878
```

### Medidas de Seguridad

1. **Validación de Input**
   - Verificación de texto no vacío
   - Sanitización de caracteres especiales
   - Límite de longitud (512 tokens)

2. **Validación de Output**
   - Confianza mínima 80%
   - Respuesta fallback para baja confianza
   - Sanitización de respuestas

3. **Manejo de Errores**
   - Try-catch en carga de modelos
   - Fallback a respuestas hardcodeadas
   - Logs de errores informativos

4. **Protección de Datos**
   - No almacenamiento de conversaciones
   - No logging de información personal
   - Procesamiento en memoria

---

## 📊 Métricas y Monitoreo

El sistema incluye métricas en tiempo real:

- **Confianza del modelo**: 0-100%
- **Intención clasificada**: 9 categorías
- **Sentimiento**: positivo/negativo/neutro
- **Score sentimiento**: -1 a +1
- **Tiempo de respuesta**: ~0.5-2 segundos

---

## 🎯 Conclusión

El sistema TYR implementa una arquitectura moderna de 4 capas que separa claramente:

- **Presentación** (Streamlit)
- **Lógica de negocio** (TYR Core)
- **Machine Learning** (BERT + VADER)
- **Datos** (JSON externalizados)

Esta separación permite:
- ✅ Fácil mantenimiento y actualización
- ✅ Testing independiente de componentes
- ✅ Escalabilidad horizontal
- ✅ Reutilización de componentes
- ✅ Actualización de datos sin código

---

**Fecha de creación:** 23 de Noviembre 2025
**Autor:** Martín Bundy
**Proyecto:** TYR - Asistente Virtual ITSE
