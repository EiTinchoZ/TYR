# 🎤 GUIÓN PRESENTACIÓN TYR - LENGUAJES DE PROGRAMACIÓN PARA LA IA
## Proyecto Final - Arquitectura y Desarrollo
**Estudiante:** Martín Bundy
**Materia:** Lenguajes de Programación para la IA
**Fecha:** Diciembre 2025
**Duración:** 15-20 minutos

---

# 📋 ESTRUCTURA DE LA PRESENTACIÓN

1. [Introducción (2 min)](#1-introducción-2-min)
2. [Arquitectura del Sistema (4 min)](#2-arquitectura-del-sistema-4-min)
3. [Lenguajes y Ecosistemas (5 min)](#3-lenguajes-y-ecosistemas-5-min)
4. [Decisiones Técnicas y Patrones (4 min)](#4-decisiones-técnicas-y-patrones-4-min)
5. [Demostración Técnica (3 min)](#5-demostración-técnica-3-min)
6. [Integración y Deploy (2 min)](#6-integración-y-deploy-2-min)
7. [Conclusiones (1 min)](#7-conclusiones-1-min)

---

# 1. INTRODUCCIÓN (≈2 MIN)

Buenos días/tardes. Soy Martín Bundy y hoy presento **TYR**, un chatbot inteligente para el ITSE, desde la perspectiva de **Lenguajes de Programación para la IA**.

En PLN demostré las técnicas de procesamiento de lenguaje natural. Hoy quiero mostrarles **cómo se programa y construye** un sistema de IA completo en producción.

## ¿Por qué este proyecto?

Decidí construir TYR como mi primer proyecto real individual, donde puse a prueba:
- **Arquitectura full-stack** con múltiples lenguajes
- **Integración de modelos de IA** en producción
- **Diseño de APIs** y sistemas escalables
- **Programación orientada a objetos** y funcional
- **Testing automatizado** y buenas prácticas

TYR (dios nórdico de la justicia) simboliza **precisión y confiabilidad técnica**.

## Lo que verán hoy:

1. Cómo integrar **Python + TypeScript** en un sistema de IA
2. Patrones de diseño para aplicaciones de machine learning
3. Arquitectura API REST con FastAPI
4. Manejo de modelos transformer en producción
5. Testing y validación automatizada

---

# 2. ARQUITECTURA DEL SISTEMA (≈4 MIN)

## Stack Tecnológico Multi-Lenguaje

TYR está construido con **3 lenguajes principales**, cada uno elegido estratégicamente:

### **Python 3.14** (Backend + IA)
```
├── tyr_chatbot.py       (Clase principal - 1,400 líneas)
├── ner_module.py        (NER personalizado - 391 líneas)
├── main.py              (API FastAPI - 150 líneas)
└── tyr_simple.py        (Wrapper - 80 líneas)
```

**¿Por qué Python?**
- Ecosistema de IA/ML más maduro (PyTorch, Transformers, VADER)
- Sintaxis clara para algoritmos complejos
- Librerías científicas optimizadas (NumPy, etc.)
- Rápido desarrollo de prototipos

### **TypeScript** (Frontend)
```
├── TYRChat.tsx          (Componente React - 1,100 líneas)
├── mockResponses.ts     (Sistema demo - 140 líneas)
└── Interfaces           (Type safety)
```

**¿Por qué TypeScript sobre JavaScript?**
- **Type safety**: Detección de errores en tiempo de compilación
- **Interfaces explícitas**: Contratos claros entre frontend-backend
- **IntelliSense**: Autocompletado y navegación de código
- **Refactoring seguro**: Cambios sin romper dependencias

### **JSON** (Configuración y Datos)
```
├── config.json          (Configuración modelo BERT)
├── label_map.json       (Mapeo de intenciones)
├── carreras_itse.json   (Base de conocimiento - 16 carreras)
└── respuestas_base.json (Respuestas por intención)
```

**¿Por qué JSON?**
- Formato universal entre lenguajes
- Fácil versionado y modificación
- Legible para humanos y máquinas

---

## Arquitectura de 3 Capas

```
┌─────────────────────────────────────────────┐
│         CAPA DE PRESENTACIÓN                │
│  React + TypeScript + Tailwind CSS          │
│  - Componentes funcionales con hooks        │
│  - Estado con useState/useEffect            │
│  - Type-safe interfaces                     │
└─────────────────┬───────────────────────────┘
                  │ HTTP/JSON (REST API)
┌─────────────────▼───────────────────────────┐
│         CAPA DE APLICACIÓN                  │
│  FastAPI + Pydantic + Uvicorn               │
│  - Validación automática con Pydantic       │
│  - Documentación auto-generada (OpenAPI)    │
│  - Async/await para concurrencia            │
└─────────────────┬───────────────────────────┘
                  │ OOP + Función calls
┌─────────────────▼───────────────────────────┐
│         CAPA DE LÓGICA DE IA                │
│  PyTorch + Transformers + VADER + NER       │
│  - Clase TYR (OOP)                          │
│  - Módulos especializados                   │
│  - GPU/CPU abstraction                      │
└─────────────────────────────────────────────┘
```

**Ventajas de esta arquitectura:**
- **Separación de responsabilidades**: Cada capa tiene un propósito claro
- **Escalabilidad**: Puedo escalar frontend y backend independientemente
- **Mantenibilidad**: Cambios en UI no afectan la lógica de IA
- **Testeable**: Cada capa se puede testear aisladamente

---

## Flujo de Datos End-to-End

1. **Usuario escribe** en el frontend (TypeScript)
2. **Fetch API** envía POST a `/chat` (HTTP/JSON)
3. **FastAPI recibe** y valida con Pydantic models
4. **tyr_simple.py** procesa la consulta:
   - Instancia clase `TYR`
   - Ejecuta `procesar_consulta()`
5. **tyr_chatbot.py** ejecuta pipeline:
   - Normalización de texto
   - Tokenización con BERT
   - Clasificación con PyTorch
   - NER con regex personalizado
   - Análisis VADER
6. **Respuesta JSON** retorna con estructura:
   ```json
   {
     "respuesta": "...",
     "intencion": "informacion_carreras",
     "confianza": 0.989,
     "sentimiento": "positivo",
     "sentimiento_compound": 0.8,
     "entidades": {...}
   }
   ```
7. **Frontend renderiza** con React + visualización

---

# 3. LENGUAJES Y ECOSISTEMAS (≈5 MIN)

## 3.1 Python - Backend y Machine Learning

### Características del Lenguaje Usadas:

#### **Programación Orientada a Objetos**
```python
class TYR:
    """Clase principal del chatbot"""

    def __init__(self, modelo_path: str, max_length: int = 128):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.max_length = max_length
        self._cargar_modelo()
        self._cargar_respuestas_base()

    def procesar_consulta(self, mensaje: str) -> Tuple[str, Dict]:
        """Pipeline completo de procesamiento"""
        # 1. Normalizar
        mensaje_norm = self._normalizar_texto(mensaje)
        # 2. Clasificar
        intencion, confianza = self._clasificar_intencion(mensaje_norm)
        # 3. Extraer entidades
        entidades = self.ner.extraer_entidades(mensaje)
        # 4. Generar respuesta
        return self._generar_respuesta(intencion, entidades)
```

**Ventajas OOP aplicadas:**
- **Encapsulación**: Métodos privados (`_cargar_modelo`) ocultan complejidad
- **Estado interno**: `self.modelo`, `self.tokenizer` se mantienen en memoria
- **Reutilización**: Una instancia sirve para múltiples consultas

#### **Type Hints (Python 3.5+)**
```python
from typing import Dict, Tuple, Optional, List

def extraer_entidades(self, texto: str) -> List[Dict[str, any]]:
    """
    Extrae entidades nombradas del texto.

    Args:
        texto: String a analizar

    Returns:
        Lista de diccionarios con entidades detectadas
    """
    entidades: List[Dict[str, any]] = []
    # ... lógica
    return entidades
```

**Beneficios:**
- Documentación viva en el código
- Detección de errores con mypy
- Mejor IDE support

#### **List/Dict Comprehensions**
```python
# Filtrado eficiente de entidades
entidades_unicas = [
    e for e in entidades
    if e['tipo'] == 'CARRERA' and e['confianza'] > 0.8
]

# Agrupación por tipo
entidades_por_tipo = {
    tipo: [e['texto'] for e in entidades if e['tipo'] == tipo]
    for tipo in ['CARRERA', 'ORGANIZACION', 'UBICACION']
}
```

**Ventaja:** Código más conciso y legible que loops tradicionales

#### **Context Managers**
```python
with torch.no_grad():
    outputs = self.modelo(**inputs)
    logits = outputs.logits
```

**Ventaja:** Manejo automático de recursos (aquí, desactivar gradientes para inferencia)

#### **Decoradores**
```python
@torch.no_grad()
def predecir(self, texto: str) -> int:
    """Predicción sin calcular gradientes"""
    return self.modelo(texto)
```

---

### Librerías Clave y su Rol:

#### **PyTorch** (ML Framework)
```python
import torch
from torch import nn

# Device abstraction
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Inferencia
with torch.no_grad():
    outputs = modelo(**inputs)
    prediccion = torch.argmax(outputs.logits, dim=1).item()
```

**Por qué PyTorch:**
- Pythonic: Se siente como Python nativo
- Debugging fácil: Ejecución eager
- Soporte GPU automático
- Ecosistema Transformers

#### **Transformers (Hugging Face)**
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("modelo_bert_tyr_4358")
modelo = AutoModelForSequenceClassification.from_pretrained("modelo_bert_tyr_4358")
```

**Abstracción clave:** `Auto*` clases detectan automáticamente la arquitectura

#### **FastAPI** (API Framework)
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    mensaje: str = Field(..., min_length=1, max_length=500)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    respuesta = tyr.procesar_consulta(request.mensaje)
    return ChatResponse(**respuesta)
```

**Características usadas:**
- **Pydantic models**: Validación automática de tipos
- **Async/await**: Concurrencia con asyncio
- **Decoradores**: Routing con `@app.post`
- **Type hints**: Documentación OpenAPI automática

---

## 3.2 TypeScript - Frontend Type-Safe

### Ventajas sobre JavaScript:

#### **Interfaces Explícitas**
```typescript
interface Message {
  id: string;
  texto: string;
  esUsuario: boolean;
  timestamp: Date;
  intencion?: string;
  confianza?: number;
  sentimiento?: string;
  sentimiento_compound?: number;
  entidades?: {
    [key: string]: string[];
  };
}

interface ChatResponse {
  respuesta: string;
  intencion: string;
  confianza: number;
  sentimiento: string;
  sentimiento_compound: number;
  entidades?: { [key: string]: string[] };
}
```

**Ventaja:** Contrato claro con el backend. Si la API cambia, TypeScript me avisa.

#### **Generics y Type Safety**
```typescript
const [mensajes, setMensajes] = useState<Message[]>([]);
const [conversaciones, setConversaciones] = useState<Conversation[]>([]);

// TypeScript sabe que 'mensaje' es tipo Message
mensajes.map((mensaje: Message) => (
  <div key={mensaje.id}>
    {mensaje.texto}
  </div>
))
```

#### **Union Types**
```typescript
type SentimentType = "positivo" | "negativo" | "neutro";

function getEmojiForSentiment(sentiment: SentimentType): string {
  switch (sentiment) {
    case "positivo": return "😊";
    case "negativo": return "😟";
    case "neutro": return "😐";
  }
}
```

**Ventaja:** TypeScript garantiza que solo se usen valores válidos.

---

### React Patterns Usados:

#### **Functional Components + Hooks**
```typescript
export function TYRChat() {
  const [mensajes, setMensajes] = useState<Message[]>([]);
  const [cargando, setCargando] = useState(false);
  const mensajesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Auto-scroll al último mensaje
    mensajesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [mensajes]);

  const enviarMensaje = async (texto: string) => {
    setCargando(true);
    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje: texto })
      });
      const data: ChatResponse = await response.json();
      // Agregar mensaje...
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setCargando(false);
    }
  };

  return (/* JSX */);
}
```

**Patterns:**
- **useState**: Estado local del componente
- **useEffect**: Efectos secundarios (scroll automático)
- **useRef**: Referencias directas al DOM
- **async/await**: Manejo de promesas limpio

---

## 3.3 JSON - Configuración Declarativa

### Separación de Código y Datos

#### **config.json** (Configuración BERT)
```json
{
  "_name_or_path": "dccuchile/bert-base-spanish-wwm-uncased",
  "architectures": ["BertForSequenceClassification"],
  "num_labels": 9,
  "max_position_embeddings": 512,
  "hidden_size": 768,
  "num_attention_heads": 12,
  "num_hidden_layers": 12
}
```

**Ventaja:** Cambiar configuración sin tocar código Python

#### **label_map.json** (Mapeo Intenciones)
```json
{
  "id2label": {
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
}
```

**Ventaja:** Agregar nuevas intenciones modificando solo JSON

#### **carreras_itse.json** (Base de Conocimiento)
```json
{
  "big_data": {
    "nombre_completo": "Técnico Superior en Big Data",
    "escuela": "Innovación Digital",
    "duracion_diurna": "2 años 4 meses",
    "creditos": 122,
    "descripcion": "...",
    "campo_ocupacional": [...]
  }
}
```

**Ventaja:** Actualizar contenido sin re-entrenar modelo

---

# 4. DECISIONES TÉCNICAS Y PATRONES (≈4 MIN)

## 4.1 Patrones de Diseño Implementados

### **Singleton Pattern** (Instancia única del modelo)
```python
# tyr_simple.py
tyr_instance = None

def get_tyr_instance():
    global tyr_instance
    if tyr_instance is None:
        tyr_instance = TYR(modelo_path="modelo_bert_tyr_4358")
    return tyr_instance
```

**Por qué:** Cargar BERT en memoria es costoso (500MB+). Una sola instancia sirve todas las peticiones.

### **Strategy Pattern** (Múltiples estrategias de respuesta)
```python
def _generar_respuesta(self, intencion: str, entidades: dict) -> str:
    estrategias = {
        "informacion_carreras": self._responder_carreras,
        "becas_financiamiento": self._responder_becas,
        "fuera_dominio": self._responder_fuera_dominio
    }
    estrategia = estrategias.get(intencion, self._respuesta_default)
    return estrategia(entidades)
```

**Por qué:** Cada intención puede tener lógica de respuesta diferente.

### **Factory Pattern** (Creación de entidades)
```python
class NERExtractor:
    def _crear_entidad(self, texto: str, tipo: str, inicio: int, fin: int) -> dict:
        return {
            "texto": texto.lower(),
            "tipo": tipo,
            "inicio": inicio,
            "fin": fin,
            "confianza": self._calcular_confianza(texto, tipo)
        }
```

---

## 4.2 Decisiones Arquitectónicas Clave

### **¿Por qué FastAPI sobre Flask/Django?**

| Característica | FastAPI | Flask | Django |
|---------------|---------|-------|--------|
| **Performance** | Muy alta (async) | Media | Media |
| **Validación** | Automática (Pydantic) | Manual | ORM |
| **Documentación** | Auto (OpenAPI) | Manual | Manual |
| **Type hints** | Nativo | Opcional | Opcional |
| **Async/await** | Sí | Limitado | Limitado |

**Decisión:** FastAPI por performance y validación automática.

### **¿Por qué React sobre Vue/Angular?**

- **Ecosistema**: Mayor cantidad de librerías (jsPDF, html2canvas, etc.)
- **TypeScript support**: Excelente integración
- **Comunidad**: Más recursos y ejemplos
- **Hooks**: Simplicidad sobre class components

### **¿Por qué NER personalizado sobre SpaCy?**

```python
# SpaCy (librería genérica)
import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("Estudiar Big Data en ITSE")
# Problema: No reconoce "Big Data" ni "ITSE" como entidades

# Mi NER personalizado
ner = NERExtractor()
entidades = ner.extraer_entidades("Estudiar Big Data en ITSE")
# Resultado: CARRERA: big data, ORGANIZACION: itse
```

**Razones:**
1. **Mayor precisión**: 95% vs 60-70% de SpaCy genérico
2. **Zero dependencias**: Puro Python + regex
3. **Compatibilidad**: Python 3.14 tiene conflictos con SpaCy
4. **Control total**: Puedo agregar nuevas entidades fácilmente

---

## 4.3 Manejo de Errores y Edge Cases

### **Validación en múltiples capas**

#### **Capa 1: Frontend (TypeScript)**
```typescript
if (mensaje.trim().length === 0) {
  return; // No enviar mensajes vacíos
}

if (mensaje.length > 500) {
  alert("Mensaje muy largo (máx 500 caracteres)");
  return;
}
```

#### **Capa 2: API (Pydantic)**
```python
class ChatRequest(BaseModel):
    mensaje: str = Field(..., min_length=1, max_length=500)

    @validator('mensaje')
    def validar_mensaje(cls, v):
        if not v.strip():
            raise ValueError('Mensaje vacío')
        return v.strip()
```

#### **Capa 3: Lógica (Python)**
```python
def procesar_consulta(self, mensaje: str) -> Tuple[str, Dict]:
    try:
        # Procesamiento...
    except Exception as e:
        logger.error(f"Error procesando: {e}")
        return (
            "Disculpa, ocurrió un error. Intenta reformular tu pregunta.",
            {"error": str(e)}
        )
```

### **Fallback a Mock Responses**
```typescript
try {
  const response = await fetch(`${API_URL}/chat`, {...});
  const data = await response.json();
} catch (err) {
  console.warn("Backend no disponible, usando mock");
  const mockData = getMockResponse(mensaje);
  // Continuar con datos de prueba
}
```

**Ventaja:** La app funciona incluso si el backend está caído (modo demo).

---

## 4.4 Optimizaciones de Performance

### **Carga diferida de modelo**
```python
class TYR:
    def __init__(self):
        # Modelo se carga una vez
        self._cargar_modelo()

    def procesar_consulta(self, mensaje: str):
        # Reutiliza modelo ya cargado
        with torch.no_grad():  # Sin gradientes = más rápido
            outputs = self.modelo(**inputs)
```

### **Memoización de respuestas**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def _obtener_respuesta_carrera(self, carrera: str) -> str:
    # Cache de respuestas frecuentes
    return self.carreras_itse[carrera]["descripcion"]
```

### **Batch processing (preparado)**
```python
# Actualmente: una consulta a la vez
# Futuro: procesar múltiples consultas en batch
def procesar_batch(self, mensajes: List[str]) -> List[Dict]:
    inputs = self.tokenizer(mensajes, padding=True, truncation=True)
    with torch.no_grad():
        outputs = self.modelo(**inputs)
    return self._parsear_outputs(outputs)
```

---

# 5. DEMOSTRACIÓN TÉCNICA (≈3 MIN)

## Live Coding: Agregar Nueva Intención

Voy a mostrar cómo se agrega una nueva intención al sistema en **3 archivos**:

### **Paso 1: Actualizar label_map.json**
```json
{
  "id2label": {
    ...
    "9": "eventos_actividades"  // ← Nueva intención
  }
}
```

### **Paso 2: Agregar respuesta en respuestas_base.json**
```json
{
  "eventos_actividades": {
    "respuesta_base": "El ITSE organiza hackathons, ferias tech...",
    "contexto": ["eventos", "actividades", "hackathon", "feria"]
  }
}
```

### **Paso 3: Re-entrenar modelo (o agregar rule-based)**
```python
# Opción rápida: detección por keywords
def _clasificar_intencion(self, mensaje: str):
    if any(kw in mensaje for kw in ["evento", "actividad", "hackathon"]):
        return "eventos_actividades", 0.95

    # Sino, usar BERT normal
    return self._clasificar_con_bert(mensaje)
```

**Resultado:** Nueva funcionalidad en minutos sin reescribir todo.

---

## Demo: Pipeline de Inferencia

### **Input del usuario:**
```
"Quiero estudiar Ciberseguridad en el ITSE de Tocumen"
```

### **Paso 1: Normalización**
```python
# Input: "Quiero estudiar Ciberseguridad en el ITSE de Tocumen"
mensaje_norm = self._normalizar_texto(mensaje)
# Output: "quiero estudiar ciberseguridad en el itse de tocumen"
```

### **Paso 2: Tokenización**
```python
tokens = self.tokenizer(mensaje_norm, return_tensors="pt")
# Output: {
#   'input_ids': tensor([[101, 2543, 9876, ...]]),
#   'attention_mask': tensor([[1, 1, 1, ...]])
# }
```

### **Paso 3: Clasificación**
```python
with torch.no_grad():
    outputs = self.modelo(**tokens)
    logits = outputs.logits
    prediccion = torch.argmax(logits, dim=1).item()
# Output: prediccion = 5 → "informacion_carreras"
```

### **Paso 4: NER**
```python
entidades = self.ner.extraer_entidades(mensaje)
# Output: [
#   {"tipo": "CARRERA", "texto": "ciberseguridad"},
#   {"tipo": "ORGANIZACION", "texto": "itse"},
#   {"tipo": "UBICACION", "texto": "tocumen"}
# ]
```

### **Paso 5: Respuesta**
```python
respuesta_final = self._generar_respuesta("informacion_carreras", entidades)
# Output: "La T.S. en Ciberseguridad del ITSE es una carrera..."
```

---

# 6. INTEGRACIÓN Y DEPLOY (≈2 MIN)

## 6.1 Testing Automatizado

### **Unit Tests (pytest)**
```python
# tests/test_chatbot.py
def test_clasificacion_intencion():
    tyr = TYR()
    intencion, conf = tyr._clasificar_intencion("Quiero información sobre becas")
    assert intencion == "becas_financiamiento"
    assert conf > 0.90

# tests/test_ner.py
def test_extraccion_carrera():
    ner = NERExtractor()
    entidades = ner.extraer_entidades("Big Data")
    assert entidades[0]["tipo"] == "CARRERA"
    assert entidades[0]["texto"] == "big data"
```

**Resultado:** 80 tests, 91% coverage

### **Integration Tests**
```python
# tests/test_api.py
from fastapi.testclient import TestClient

def test_chat_endpoint():
    client = TestClient(app)
    response = client.post("/chat", json={"mensaje": "Hola"})
    assert response.status_code == 200
    assert "respuesta" in response.json()
```

---

## 6.2 Deploy y Producción

### **Backend Deploy (Render/Railway)**
```bash
# Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **Frontend Deploy (Vercel/Netlify)**
```bash
# Build
npm run build

# Deploy
vercel deploy --prod
```

### **Environment Variables**
```bash
# Backend
MODELO_PATH=./modelo_bert_tyr_4358
MAX_LENGTH=128
DEVICE=cpu

# Frontend
VITE_API_URL=https://api-tyr.onrender.com
```

---

## 6.3 Versionado y Git

```bash
TYR/
├── .git/
├── .gitignore
├── backend/
│   ├── tyr_chatbot.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   └── package.json
└── modelo_bert_tyr_4358/  # .gitignore (muy pesado)
```

**Commits importantes:**
```
feat: add sentiment analysis visualization
feat: add Named Entity Recognition module
fix: improve BERT classification accuracy
docs: add comprehensive API documentation
```

---

# 7. CONCLUSIONES (≈1 MIN)

## Logros Técnicos

### **Arquitectura Multi-Lenguaje**
- ✅ **Python** para backend y ML (1,400+ líneas)
- ✅ **TypeScript** para frontend type-safe (1,100+ líneas)
- ✅ **JSON** para configuración declarativa

### **Patrones de Diseño**
- ✅ **Singleton**: Instancia única del modelo
- ✅ **Strategy**: Múltiples estrategias de respuesta
- ✅ **Factory**: Creación de entidades NER

### **Integración de Librerías**
- ✅ **PyTorch + Transformers**: Modelo BERT en producción
- ✅ **FastAPI + Pydantic**: API REST con validación automática
- ✅ **React + Hooks**: UI moderna y reactiva

### **Calidad de Código**
- ✅ **80 tests automatizados** con 91% coverage
- ✅ **Type safety** en frontend y backend
- ✅ **Manejo de errores** en múltiples capas
- ✅ **Documentación** OpenAPI automática

### **Performance**
- ✅ **98.93% accuracy** en clasificación
- ✅ **95% precisión** en NER personalizado
- ✅ **<500ms** tiempo de respuesta promedio
- ✅ **Singleton pattern** para eficiencia de memoria

---

## Aprendizajes Clave

1. **Elegir el lenguaje correcto para cada tarea**
   - Python para IA/ML
   - TypeScript para frontend robusto
   - JSON para configuración

2. **Arquitectura en capas facilita mantenimiento**
   - Frontend, API y ML independientes
   - Cada capa testeada aisladamente

3. **Type safety previene errores**
   - TypeScript + Pydantic detectan problemas antes de runtime
   - Interfaces claras entre componentes

4. **Testing automatizado da confianza**
   - 80 tests garantizan estabilidad
   - Refactoring seguro

5. **Patrones de diseño resuelven problemas reales**
   - Singleton para modelos pesados
   - Strategy para múltiples comportamientos

---

## TYR en Números

```
📊 Métricas de Código:
- 2,500+ líneas de código de producción
- 3 lenguajes principales
- 80 tests automatizados
- 91% code coverage

🤖 Métricas de IA:
- 98.93% accuracy BERT
- 95% precisión NER
- 9 intenciones clasificadas
- 6 tipos de entidades

🏗️ Arquitectura:
- 3 capas (UI, API, ML)
- 5 patrones de diseño
- 10+ librerías integradas
- REST API con OpenAPI
```

---

## Preguntas que puedo responder:

- ¿Por qué elegiste Python sobre otros lenguajes para IA?
- ¿Cómo manejas la memoria con modelos de 500MB+?
- ¿Qué patrones de diseño usarías para escalar a millones de usuarios?
- ¿Cómo implementarías streaming de respuestas (como ChatGPT)?
- ¿Qué ventajas tiene FastAPI sobre Flask para APIs de ML?

**Gracias por su atención. Quedo abierto a preguntas técnicas.**

---

**Archivos de referencia:**
- Código fuente: [GitHub - TYR](https://github.com/EiTinchoZ/TYR)
- Documentación API: `http://localhost:8000/docs` (OpenAPI)
- Tests: `pytest -v --cov`
