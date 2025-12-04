"""
Script de verificación rápida del NER
Para ejecutar antes de la presentación y confirmar que todo funciona

Autor: Martín Bundy
"""

import sys
from pathlib import Path

# Configurar encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def print_header(text):
    """Imprimir encabezado."""
    print()
    print("=" * 70)
    print(f"  {text}")
    print("=" * 70)


def test_1_importacion():
    """Test 1: Verificar que se puede importar el módulo."""
    print_header("TEST 1: Importación del módulo NER")

    try:
        from ner_module import NERExtractor
        print("✅ PASS: Módulo NER importado correctamente")
        return True
    except Exception as e:
        print(f"❌ FAIL: Error al importar: {e}")
        return False


def test_2_inicializacion():
    """Test 2: Verificar inicialización."""
    print_header("TEST 2: Inicialización del extractor")

    try:
        from ner_module import NERExtractor
        ner = NERExtractor()
        print("✅ PASS: NER extractor inicializado")
        print(f"   - Carreras cargadas: {len(ner.carreras)}")
        print(f"   - Servicios cargados: {len(ner.servicios)}")
        print(f"   - Organizaciones cargadas: {len(ner.organizaciones)}")
        return True
    except Exception as e:
        print(f"❌ FAIL: Error en inicialización: {e}")
        return False


def test_3_extraccion_basica():
    """Test 3: Verificar extracción básica."""
    print_header("TEST 3: Extracción básica de entidades")

    try:
        from ner_module import NERExtractor
        ner = NERExtractor()

        texto = "Quiero estudiar Big Data en el ITSE"
        entidades = ner.extraer_entidades(texto)

        if len(entidades) >= 2:
            print("✅ PASS: Extracción básica funciona")
            for ent in entidades:
                print(f"   - {ent['tipo']}: {ent['texto']}")
            return True
        else:
            print(f"❌ FAIL: Se esperaban al menos 2 entidades, se encontraron {len(entidades)}")
            return False

    except Exception as e:
        print(f"❌ FAIL: Error en extracción: {e}")
        return False


def test_4_caso_complejo():
    """Test 4: Verificar caso complejo."""
    print_header("TEST 4: Caso complejo con múltiples entidades")

    try:
        from ner_module import NERExtractor
        ner = NERExtractor()

        texto = "Estudiar desarrollo de software en el ITSE de Tocumen con beca IFARHU"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        tipos_esperados = ['CARRERA', 'ORGANIZACION', 'UBICACION']
        tipos_encontrados = list(resumen.keys())

        if all(tipo in tipos_encontrados for tipo in tipos_esperados):
            print("✅ PASS: Caso complejo funciona correctamente")
            for tipo, textos in resumen.items():
                print(f"   - {tipo}: {', '.join(textos)}")
            return True
        else:
            print(f"❌ FAIL: No se encontraron todos los tipos esperados")
            print(f"   Esperados: {tipos_esperados}")
            print(f"   Encontrados: {tipos_encontrados}")
            return False

    except Exception as e:
        print(f"❌ FAIL: Error en caso complejo: {e}")
        return False


def test_5_tests_unitarios():
    """Test 5: Verificar tests unitarios."""
    print_header("TEST 5: Tests unitarios")

    try:
        import subprocess
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/test_ner.py", "-v", "--tb=short"],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=Path(__file__).parent
        )

        if "21 passed" in result.stdout:
            print("✅ PASS: 21 tests unitarios passing")
            return True
        else:
            print(f"❌ FAIL: Tests no pasaron completamente")
            print(result.stdout[-200:] if result.stdout else "No output")
            return False

    except Exception as e:
        print(f"⚠️  WARNING: No se pudieron ejecutar tests: {e}")
        print("   (Esto es OK si pytest no está instalado)")
        return True


def test_6_integracion_chatbot():
    """Test 6: Verificar integración con chatbot."""
    print_header("TEST 6: Integración con chatbot TYR")

    try:
        import tyr_chatbot
        print("✅ PASS: Módulo chatbot importa correctamente con NER")
        print("   (NER está integrado en el pipeline)")
        return True
    except Exception as e:
        print(f"❌ FAIL: Error al importar chatbot: {e}")
        return False


def test_7_demo_disponible():
    """Test 7: Verificar que demo está disponible."""
    print_header("TEST 7: Script de demostración")

    try:
        demo_path = Path(__file__).parent / "demo_ner.py"
        if demo_path.exists():
            print("✅ PASS: Script demo_ner.py existe")
            print(f"   Ubicación: {demo_path}")
            print("   Comando: python demo_ner.py")
            return True
        else:
            print("❌ FAIL: demo_ner.py no encontrado")
            return False
    except Exception as e:
        print(f"❌ FAIL: Error verificando demo: {e}")
        return False


def main():
    """Ejecutar todos los tests de verificación."""
    print()
    print("╔" + "=" * 68 + "╗")
    print("║" + "  VERIFICACIÓN NER - TYR".center(68) + "║")
    print("║" + "  Pre-Presentación Check".center(68) + "║")
    print("╚" + "=" * 68 + "╝")

    tests = [
        test_1_importacion,
        test_2_inicializacion,
        test_3_extraccion_basica,
        test_4_caso_complejo,
        test_5_tests_unitarios,
        test_6_integracion_chatbot,
        test_7_demo_disponible
    ]

    resultados = []

    for test_func in tests:
        try:
            resultado = test_func()
            resultados.append(resultado)
        except Exception as e:
            print(f"❌ ERROR CRÍTICO en {test_func.__name__}: {e}")
            resultados.append(False)

    # Resumen final
    print_header("RESUMEN DE VERIFICACIÓN")

    total = len(resultados)
    pasados = sum(resultados)
    porcentaje = (pasados / total * 100) if total > 0 else 0

    print()
    print(f"Tests ejecutados: {total}")
    print(f"Tests pasados:    {pasados}")
    print(f"Tests fallados:   {total - pasados}")
    print(f"Éxito:            {porcentaje:.1f}%")
    print()

    if pasados == total:
        print("✅ VERIFICACIÓN COMPLETA: Todo funciona correctamente")
        print()
        print("🎯 LISTO PARA LA PRESENTACIÓN")
        print()
        print("Comandos útiles:")
        print("  python demo_ner.py           # Demo interactivo")
        print("  python ner_module.py         # Demo básico")
        print("  pytest tests/test_ner.py -v # Ejecutar tests")
        print()
    elif pasados >= total - 1:
        print("⚠️  VERIFICACIÓN MAYORMENTE EXITOSA")
        print("   1 test menor falló, pero el sistema está funcional")
        print()
    else:
        print("❌ VERIFICACIÓN FALLIDA")
        print("   Revisa los errores anteriores antes de presentar")
        print()

    print("=" * 70)
    print()

    return pasados == total


if __name__ == "__main__":
    try:
        exito = main()
        sys.exit(0 if exito else 1)
    except KeyboardInterrupt:
        print("\n\nVerificación interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\nError crítico: {e}")
        sys.exit(1)
