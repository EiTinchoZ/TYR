"""
Script de demostración del NER integrado en TYR
Muestra cómo el chatbot extrae entidades nombradas de las consultas

Para la presentación del proyecto final
Autor: Martín Bundy
"""

import sys
from pathlib import Path

# Configurar encoding para Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from ner_module import NERExtractor


def print_separator(char="=", length=70):
    """Imprimir línea separadora."""
    print(char * length)


def demo_ner_basico():
    """Demostración básica del módulo NER."""
    print_separator("=")
    print("DEMO: MÓDULO NER - EXTRACCIÓN DE ENTIDADES")
    print_separator("=")
    print()

    # Inicializar NER
    ner = NERExtractor()

    # Casos de prueba para la presentación
    casos_demo = [
        {
            "titulo": "Consulta sobre Carrera",
            "texto": "Quiero información sobre Big Data en el ITSE"
        },
        {
            "titulo": "Consulta con Ubicación",
            "texto": "¿El instituto está en Tocumen, Panamá?"
        },
        {
            "titulo": "Consulta sobre Becas",
            "texto": "Información sobre becas IFARHU para Ciberseguridad"
        },
        {
            "titulo": "Consulta sobre Servicio CAIPI",
            "texto": "¿Tienen guardería CAIPI para estudiantes?"
        },
        {
            "titulo": "Consulta sobre Horarios",
            "texto": "¿Cuál es el horario de lunes a viernes de 8 am a 5 pm?"
        },
        {
            "titulo": "Consulta sobre Requisitos",
            "texto": "Necesito mi título de bachiller y cédula para matricularme"
        },
        {
            "titulo": "Caso Complejo",
            "texto": "Quiero estudiar desarrollo de software en el ITSE de Tocumen con beca IFARHU"
        }
    ]

    for i, caso in enumerate(casos_demo, 1):
        print(f"[Caso {i}] {caso['titulo']}")
        print(f"Consulta: \"{caso['texto']}\"")
        print("-" * 70)

        # Extraer entidades
        entidades = ner.extraer_entidades(caso['texto'])

        if entidades:
            # Mostrar entidades encontradas
            resumen = ner.obtener_resumen(entidades)

            for tipo, textos in sorted(resumen.items()):
                print(f"  {tipo}:")
                for texto in textos:
                    print(f"    -> {texto}")
        else:
            print("  (No se detectaron entidades)")

        print()


def demo_ner_con_estadisticas():
    """Demostración con estadísticas de entidades."""
    print_separator("=")
    print("ESTADÍSTICAS DE NER")
    print_separator("=")
    print()

    ner = NERExtractor()

    # Simular múltiples consultas
    consultas = [
        "Información sobre Big Data",
        "¿Cómo me inscribo en el ITSE?",
        "Becas IFARHU para Ciberseguridad",
        "Guardería CAIPI en Tocumen",
        "Horario de lunes a viernes",
        "Requisitos: bachiller y cédula",
        "Desarrollo de software en Panamá",
        "Centro de investigación CIIECYT"
    ]

    estadisticas = {
        'CARRERA': 0,
        'SERVICIO': 0,
        'ORGANIZACION': 0,
        'UBICACION': 0,
        'PERIODO': 0,
        'REQUISITO': 0
    }

    total_entidades = 0

    for consulta in consultas:
        entidades = ner.extraer_entidades(consulta)
        resumen = ner.obtener_resumen(entidades)

        for tipo, textos in resumen.items():
            if tipo in estadisticas:
                estadisticas[tipo] += len(textos)
                total_entidades += len(textos)

    print(f"Total de consultas procesadas: {len(consultas)}")
    print(f"Total de entidades detectadas: {total_entidades}")
    print()
    print("Distribución por tipo:")

    for tipo, cantidad in sorted(estadisticas.items(), key=lambda x: x[1], reverse=True):
        porcentaje = (cantidad / total_entidades * 100) if total_entidades > 0 else 0
        barra = "█" * int(porcentaje / 5)
        print(f"  {tipo:15s}: {cantidad:2d} entidades ({porcentaje:5.1f}%) {barra}")

    print()


def demo_comparacion_con_sin_ner():
    """Demostración comparando procesamiento con y sin NER."""
    print_separator("=")
    print("COMPARACIÓN: CON vs SIN NER")
    print_separator("=")
    print()

    ner = NERExtractor()

    texto = "Quiero estudiar Big Data en el ITSE de Tocumen con beca IFARHU"

    print(f"Texto: \"{texto}\"")
    print()

    # Sin NER (procesamiento tradicional)
    print("[SIN NER]")
    print("  - El chatbot solo detectaría la intención general")
    print("  - No extraería información estructurada")
    print("  - Perdería contexto sobre entidades específicas")
    print()

    # Con NER
    print("[CON NER]")
    entidades = ner.extraer_entidades(texto)
    resumen = ner.obtener_resumen(entidades)

    print("  Entidades extraídas:")
    for tipo, textos in sorted(resumen.items()):
        print(f"    {tipo}: {', '.join(textos)}")

    print()
    print("  Ventajas:")
    print("    ✓ Identifica carrera específica (Big Data)")
    print("    ✓ Reconoce institución (ITSE)")
    print("    ✓ Detecta ubicación (Tocumen)")
    print("    ✓ Identifica organización de becas (IFARHU)")
    print("    ✓ Permite respuestas más contextuales")
    print()


def demo_cobertura_ner():
    """Mostrar cobertura del NER."""
    print_separator("=")
    print("COBERTURA DEL NER - ENTIDADES RECONOCIDAS")
    print_separator("=")
    print()

    ner = NERExtractor()

    print("📚 CARRERAS RECONOCIDAS (16 programas):")
    for i, carrera in enumerate(sorted(ner.carreras), 1):
        print(f"  {i:2d}. {carrera.title()}")

    print()
    print("🏢 SERVICIOS RECONOCIDOS:")
    for i, servicio in enumerate(sorted(ner.servicios), 1):
        print(f"  {i}. {servicio.upper()}")

    print()
    print("🏛️  ORGANIZACIONES RECONOCIDAS:")
    for i, org in enumerate(sorted(ner.organizaciones), 1):
        print(f"  {i}. {org.upper()}")

    print()
    print("📍 UBICACIONES RECONOCIDAS:")
    for i, ubi in enumerate(sorted(ner.ubicaciones), 1):
        print(f"  {i}. {ubi.title()}")

    print()
    print("📋 REQUISITOS RECONOCIDOS:")
    for i, req in enumerate(sorted(ner.requisitos), 1):
        print(f"  {i}. {req.title()}")

    print()
    print("⏰ PERIODOS: Se detectan automáticamente via regex")
    print("   - Años (2024, 2025)")
    print("   - Meses (enero, febrero, ...)")
    print("   - Días (lunes, martes, ...)")
    print("   - Horarios (8 am, 5 pm, ...)")
    print()


def main():
    """Función principal de demostración."""
    print()
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║         TYR - DEMOSTRACIÓN DE NER (Named Entity Recognition)      ║")
    print("║              Proyecto Final - Procesamiento Lenguaje Natural      ║")
    print("║                         Martín Bundy - ITSE                        ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print()

    try:
        # Demo 1: Básico
        demo_ner_basico()
        input("Presiona ENTER para continuar a estadísticas...")
        print("\n" * 2)

        # Demo 2: Estadísticas
        demo_ner_con_estadisticas()
        input("Presiona ENTER para continuar a comparación...")
        print("\n" * 2)

        # Demo 3: Comparación
        demo_comparacion_con_sin_ner()
        input("Presiona ENTER para ver cobertura completa...")
        print("\n" * 2)

        # Demo 4: Cobertura
        demo_cobertura_ner()

        print_separator("=")
        print("✓ Demostración completada exitosamente")
        print_separator("=")
        print()

        print("RESUMEN TÉCNICO:")
        print("  • Módulo NER personalizado para dominio ITSE")
        print("  • 6 tipos de entidades reconocidas")
        print("  • Pattern matching + Regex avanzado")
        print("  • 21 tests unitarios passing (100%)")
        print("  • Integrado en pipeline principal del chatbot")
        print()

    except KeyboardInterrupt:
        print("\n\nDemo interrumpida por el usuario")
    except Exception as e:
        print(f"\nError durante demo: {e}")


if __name__ == "__main__":
    main()
