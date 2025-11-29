#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar respuestas especificas del chatbot

Autor: Martin Bundy
Fecha: Noviembre 2025
"""

from pathlib import Path
from tyr_chatbot import TYR

def test_respuestas_especificas():
    """Probar que el chatbot responda especificamente a cada pregunta"""

    print("=" * 80)
    print("PRUEBAS DE RESPUESTAS ESPECIFICAS - MODELO modelo_bert_tyr_4358")
    print("=" * 80)
    print()

    # Inicializar chatbot
    print("Cargando modelo modelo_bert_tyr_4358...")
    modelo_path = Path("modelo_bert_tyr_4358")

    try:
        chatbot = TYR(modelo_path=str(modelo_path))
        print("OK: Modelo cargado exitosamente")
        print()
    except Exception as e:
        print(f"ERROR: No se pudo cargar el modelo: {e}")
        return

    # Preguntas especificas
    preguntas_prueba = [
        ("Alianzas Estrategicas", "alianza"),
        ("Que es CAIPI?", "CAIPI"),
        ("Reconocimientos del ITSE", "Foro Economico"),
        ("Que es CIIECYT?", "CIIECYT"),
        ("Insercion laboral de egresados", "80%"),
        ("Cuentame sobre Big Data", "Big Data"),
        ("Informacion sobre Ciberseguridad", "Ciberseguridad"),
    ]

    print("=" * 80)
    print("EJECUTANDO PRUEBAS DE RESPUESTAS ESPECIFICAS")
    print("=" * 80)
    print()

    errores = 0
    aciertos = 0

    # Probar cada pregunta
    for i, (pregunta, keyword_esperado) in enumerate(preguntas_prueba, 1):
        print(f"\n{'='*80}")
        print(f"PRUEBA {i}/{len(preguntas_prueba)}")
        print(f"{'='*80}")
        print(f"Pregunta: {pregunta}")
        print(f"Keyword esperado en respuesta: '{keyword_esperado}'")
        print("-" * 80)

        try:
            respuesta, metadata = chatbot.procesar_consulta(pregunta)

            # Verificar que la respuesta contenga el keyword esperado
            if keyword_esperado.lower() in respuesta.lower():
                print(f"\nOK: Respuesta contiene '{keyword_esperado}'")
                print(f"Intencion: {metadata['intencion']} ({metadata['confianza']:.1%})")
                aciertos += 1
            else:
                print(f"\nERROR: Respuesta NO contiene '{keyword_esperado}'")
                print(f"Intencion: {metadata['intencion']} ({metadata['confianza']:.1%})")
                print(f"\nRespuesta recibida (primeros 200 chars):")
                print(respuesta[:200] + "...")
                errores += 1

        except Exception as e:
            print(f"\nERROR CRITICO: {e}")
            errores += 1

    print("\n" + "=" * 80)
    print("RESUMEN DE PRUEBAS")
    print("=" * 80)
    print(f"Total pruebas: {len(preguntas_prueba)}")
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")
    print(f"Tasa de exito: {(aciertos/len(preguntas_prueba)*100):.1f}%")
    print("=" * 80)

    if errores == 0:
        print("\nTODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    else:
        print(f"\nSE ENCONTRARON {errores} ERRORES")

if __name__ == "__main__":
    test_respuestas_especificas()
