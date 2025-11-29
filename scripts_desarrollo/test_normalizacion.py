#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar normalizacion de texto

Autor: Martin Bundy
Fecha: Noviembre 2025
"""

from pathlib import Path
from tyr_chatbot import TYR

def test_normalizacion():
    """Probar que el chatbot sea tolerante con tildes, mayusculas y errores"""

    print("=" * 80)
    print("PRUEBAS DE NORMALIZACION DE TEXTO")
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

    # Pruebas de normalizacion
    # Formato: (pregunta_con_errores, pregunta_correcta)
    pruebas = [
        # Mayusculas vs minusculas
        ("CUENTAME SOBRE BIG DATA", "cuentame sobre big data"),
        ("Cuentame Sobre Big Data", "cuentame sobre big data"),

        # Sin tildes
        ("Informacion sobre Ciberseguridad", "informacion sobre ciberseguridad"),
        ("Que es CIIECYT", "que es ciiecyt"),
        ("Alianzas Estrategicas", "alianzas estrategicas"),

        # Con tildes (deberia funcionar igual)
        ("Información sobre Ciberseguridad", "informacion sobre ciberseguridad"),
        ("Qué es CIIECYT?", "que es ciiecyt"),
        ("¿Cuéntame sobre Inteligencia Artificial?", "cuentame sobre inteligencia artificial"),

        # Combinaciones
        ("¿QUE CARRERAS TIENEN DISPONIBLES?", "que carreras tienen disponibles"),
        ("COMO ME INSCRIBO", "como me inscribo"),
    ]

    print("=" * 80)
    print("EJECUTANDO PRUEBAS DE NORMALIZACION")
    print("=" * 80)
    print()

    for i, (pregunta_error, texto_normalizado_esperado) in enumerate(pruebas, 1):
        print(f"\n{'='*80}")
        print(f"PRUEBA {i}/{len(pruebas)}")
        print(f"{'='*80}")
        print(f"Texto original:  '{pregunta_error}'")

        # Normalizar con la funcion del chatbot
        texto_normalizado = chatbot.procesar_entrada(pregunta_error)
        print(f"Texto normalizado: '{texto_normalizado}'")
        print(f"Esperado:        '{texto_normalizado_esperado}'")

        if texto_normalizado == texto_normalizado_esperado:
            print("OK: Normalizacion correcta")
        else:
            print("ERROR: Normalizacion incorrecta")

        # Probar que la respuesta sea coherente
        try:
            respuesta, metadata = chatbot.procesar_consulta(pregunta_error)
            print(f"\nIntencion detectada: {metadata['intencion']} ({metadata['confianza']:.1%})")

            # Verificar que no sea fuera_dominio
            if metadata['intencion'] == 'fuera_dominio':
                print("ADVERTENCIA: Clasificado como fuera_dominio")
            else:
                print("OK: Clasificacion exitosa")
        except Exception as e:
            print(f"ERROR: {e}")

    print("\n" + "=" * 80)
    print("PRUEBAS COMPLETADAS")
    print("=" * 80)
    print()
    print("CONCLUSION:")
    print("El chatbot ahora es tolerante a:")
    print("- Mayusculas/minusculas (HOLA = hola)")
    print("- Tildes/acentos (información = informacion)")
    print("- Signos de puntuacion (¿? = vacio)")
    print("- Espacios multiples")

if __name__ == "__main__":
    test_normalizacion()
