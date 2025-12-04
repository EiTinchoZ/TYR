"""
TYR Simple - Versión simplificada para FastAPI
Wrapper del chatbot original con formato compatible para API REST
"""

import torch
from pathlib import Path
from typing import Dict, Tuple
import sys

# Añadir directorio padre al path
sys.path.append(str(Path(__file__).parent.parent))

from tyr_chatbot import TYR as TYROriginal


class TYRSimple:
    """
    Wrapper simplificado de TYR para FastAPI.

    Convierte el formato de respuesta del chatbot original
    a un formato JSON-friendly para la API REST.
    """

    def __init__(self, modelo_path: str = None):
        """
        Inicializar TYR Simple.

        Args:
            modelo_path: Ruta al modelo BERT. Si es None, usa ruta por defecto.
        """
        if modelo_path is None:
            modelo_path = str(Path(__file__).parent.parent / "modelo_bert_tyr_4358")

        # Inicializar chatbot original
        self.tyr = TYROriginal(modelo_path=modelo_path)

    def procesar_mensaje(self, mensaje: str) -> Dict:
        """
        Procesar mensaje del usuario y retornar respuesta en formato API.

        Args:
            mensaje: Texto del usuario

        Returns:
            Dict con estructura:
            {
                "respuesta": str,
                "intencion": str,
                "confianza": float,
                "sentimiento": str,
                "sentimiento_compound": float
            }
        """
        try:
            # Llamar al chatbot original
            respuesta_str, metadata = self.tyr.procesar_consulta(mensaje)

            # Convertir a formato API
            return {
                "respuesta": respuesta_str,
                "intencion": metadata.get("intencion", "unknown"),
                "confianza": float(metadata.get("confianza", 0.0)),
                "sentimiento": metadata.get("sentimiento", "neutro"),
                "sentimiento_compound": float(metadata.get("sentimiento_compound", 0.0)),
                "entidades": metadata.get("entidades", {}),
                "entidades_detalladas": metadata.get("entidades_detalladas", [])
            }

        except Exception as e:
            # En caso de error, retornar respuesta de fallback
            return {
                "respuesta": "Lo siento, tuve un problema procesando tu mensaje. ¿Podrías reformularlo?",
                "intencion": "error",
                "confianza": 0.0,
                "sentimiento": "neutro",
                "sentimiento_compound": 0.0
            }
