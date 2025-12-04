"""
TYR Backend API - FastAPI
Endpoint REST para el chatbot TYR con modelo BERT

Endpoints:
- POST /chat: Procesar mensaje y devolver respuesta
- GET /health: Health check del servidor
- GET /stats: Estadísticas del modelo
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import sys
from pathlib import Path
import logging

# Añadir directorio padre al path para importar TYR
sys.path.append(str(Path(__file__).parent.parent))

from backend.tyr_simple import TYRSimple

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear aplicación FastAPI
app = FastAPI(
    title="TYR Chatbot API",
    description="API REST para el asistente virtual TYR del ITSE",
    version="1.0.0"
)

# Configurar CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
        "https://*.netlify.app",
        "https://*.netlify.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar chatbot TYR globalmente
tyr_bot: Optional[TYRSimple] = None


@app.on_event("startup")
async def startup_event():
    """Inicializar el modelo BERT al iniciar el servidor."""
    global tyr_bot
    try:
        logger.info("Cargando modelo TYR Simple...")
        modelo_path = Path(__file__).parent.parent / "modelo_bert_tyr_10_clases_COMPLETO"
        tyr_bot = TYRSimple(modelo_path=str(modelo_path))
        logger.info("✅ Modelo TYR Simple cargado exitosamente")
    except Exception as e:
        logger.error(f"❌ Error cargando modelo: {e}")
        raise


# Modelos Pydantic para request/response
class ChatRequest(BaseModel):
    """Request body para el endpoint /chat"""
    mensaje: str = Field(..., min_length=1, max_length=500, description="Mensaje del usuario")

    class Config:
        json_schema_extra = {
            "example": {
                "mensaje": "¿Qué carreras hay en el ITSE?"
            }
        }


class ChatResponse(BaseModel):
    """Response body para el endpoint /chat"""
    respuesta: str = Field(..., description="Respuesta generada por TYR")
    intencion: str = Field(..., description="Intención clasificada")
    confianza: float = Field(..., ge=0, le=1, description="Nivel de confianza (0-1)")
    sentimiento: str = Field(..., description="Categoría de sentimiento (positivo/negativo/neutro)")
    sentimiento_compound: float = Field(..., description="Score compound del sentimiento (-1 a 1)")
    entidades: dict = Field(default_factory=dict, description="Entidades NER extraídas del mensaje")
    entidades_detalladas: list = Field(default_factory=list, description="Entidades NER con posiciones")

    class Config:
        json_schema_extra = {
            "example": {
                "respuesta": "El ITSE ofrece 16 carreras técnicas en áreas de tecnología...",
                "intencion": "informacion_carreras",
                "confianza": 0.9893,
                "sentimiento": {
                    "neg": 0.0,
                    "neu": 0.8,
                    "pos": 0.2,
                    "compound": 0.5
                }
            }
        }


class HealthResponse(BaseModel):
    """Response body para el endpoint /health"""
    status: str
    modelo_cargado: bool
    version: str


class StatsResponse(BaseModel):
    """Response body para el endpoint /stats"""
    precision: float
    consultas_entrenadas: int
    carreras_disponibles: int
    intenciones_soportadas: int


@app.get("/", response_model=Dict[str, str])
async def root():
    """Endpoint raíz."""
    return {
        "mensaje": "TYR Backend API está funcionando",
        "documentacion": "/docs",
        "version": "1.0.0"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check del servidor.

    Retorna el estado del servidor y si el modelo está cargado.
    """
    return HealthResponse(
        status="healthy" if tyr_bot is not None else "unhealthy",
        modelo_cargado=tyr_bot is not None,
        version="1.0.0"
    )


@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    """
    Obtener estadísticas del modelo TYR.

    Retorna métricas clave del chatbot.
    """
    if tyr_bot is None:
        raise HTTPException(status_code=503, detail="Modelo no cargado")

    return StatsResponse(
        precision=98.93,
        consultas_entrenadas=4358,
        carreras_disponibles=16,
        intenciones_soportadas=len(tyr_bot.label_map) if hasattr(tyr_bot, 'label_map') else 0
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Procesar mensaje del usuario y devolver respuesta.

    Args:
        request: ChatRequest con el mensaje del usuario

    Returns:
        ChatResponse con la respuesta, intención, confianza y sentimiento

    Raises:
        HTTPException 503: Si el modelo no está cargado
        HTTPException 500: Si hay error procesando el mensaje
    """
    if tyr_bot is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo no cargado. Intenta nuevamente en unos segundos."
        )

    try:
        # Procesar mensaje con TYR Simple (retorna dict directo)
        logger.info(f"Procesando mensaje: '{request.mensaje}'")
        resultado = tyr_bot.procesar_mensaje(request.mensaje)

        # TYRSimple ya retorna el formato correcto
        return ChatResponse(**resultado)

    except Exception as e:
        logger.error(f"Error procesando consulta: {e}", exc_info=True)

        # Retornar respuesta de fallback amigable
        return ChatResponse(
            respuesta="Lo siento, estoy teniendo problemas técnicos. Por favor, intenta nuevamente en un momento.",
            intencion="error",
            confianza=0.0,
            sentimiento="neutro",
            sentimiento_compound=0.0
        )


if __name__ == "__main__":
    import uvicorn

    # Ejecutar servidor
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
