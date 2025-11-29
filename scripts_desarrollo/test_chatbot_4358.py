#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar el modelo BERT 4358

Autor: Martin Bundy
Fecha: Noviembre 2025
"""

from pathlib import Path
from tyr_chatbot import TYR

def test_chatbot():
    """Probar chatbot con preguntas reales"""

    print("=" * 80)
    print("PRUEBAS CHATBOT TYR - MODELO modelo_bert_tyr_4358")
    print("=" * 80)
    print()

    # Inicializar chatbot con nuevo modelo
    print("Cargando modelo modelo_bert_tyr_4358...")
    modelo_path = Path("modelo_bert_tyr_4358")

    try:
        chatbot = TYR(modelo_path=str(modelo_path))
        print("OK: Modelo cargado exitosamente")
        print()
    except Exception as e:
        print(f"ERROR: No se pudo cargar el modelo: {e}")
        return

    # Preguntas de prueba (las que antes fallaban)
    preguntas_prueba = [
        "Cuéntame sobre Big Data",
        "Qué es CAIPI?",
        "Reconocimientos del ITSE",
        "Alianzas con empresas",
        "Qué es CIIECYT?",
        "Información sobre Inteligencia Artificial",
        "Háblame sobre la carrera de Desarrollo de Software",
        "Qué hace un técnico en Ciberseguridad?",
        "Cuánto dura la carrera de Big Data?",
        "Requisitos para inscribirse"
    ]

    print("=" * 80)
    print("EJECUTANDO PRUEBAS")
    print("=" * 80)
    print()

    # Probar cada pregunta
    for i, pregunta in enumerate(preguntas_prueba, 1):
        print(f"\n{'='*80}")
        print(f"PRUEBA {i}/{len(preguntas_prueba)}")
        print(f"{'='*80}")
        print(f"Pregunta: {pregunta}")
        print("-" * 80)

        try:
            respuesta = chatbot.procesar_consulta(pregunta)
            print(f"\nRespuesta:\n{respuesta}")

            # Verificar que no sea fuera_dominio para las preguntas específicas de ITSE
            if "no puedo ayudarte" in respuesta.lower() and i <= 5:
                print("\nADVERTENCIA: La pregunta fue clasificada como fuera_dominio")
            else:
                print("\nOK: Respuesta generada correctamente")

        except Exception as e:
            print(f"\nERROR: {e}")

    print("\n" + "=" * 80)
    print("PRUEBAS COMPLETADAS")
    print("=" * 80)

if __name__ == "__main__":
    test_chatbot()
