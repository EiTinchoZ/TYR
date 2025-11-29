"""
Fixtures compartidas para tests de TYR

Este archivo contiene fixtures de pytest que son compartidas
entre todos los tests del proyecto.

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import pytest
import sys
from pathlib import Path

# Añadir directorio raíz al path para importar módulos
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from tyr_chatbot import TYR


@pytest.fixture(scope="session")
def chatbot():
    """
    Fixture que crea una instancia única de TYR para toda la sesión de tests.

    Scope: session - Se crea una sola vez y se reutiliza en todos los tests.

    Returns:
        TYR: Instancia del chatbot TYR inicializado

    Note:
        Esta fixture carga el modelo BERT, lo cual puede tomar varios segundos.
        Usar scope="session" asegura que solo se cargue una vez.
    """
    return TYR(modelo_path="modelo_bert_tyr_4358", device="cpu")


@pytest.fixture
def ejemplos_normalizacion():
    """
    Fixture con ejemplos de normalización de texto.

    Returns:
        list: Lista de tuplas (input, expected_output)
    """
    return [
        # Mayúsculas
        ("HOLA", "hola"),
        ("INFORMACIÓN", "informacion"),
        ("BIG DATA", "big data"),

        # Tildes
        ("información", "informacion"),
        ("inscripción", "inscripcion"),
        ("requisitos académicos", "requisitos academicos"),

        # Puntuación
        ("¿Hola?", "hola"),
        ("¡Buenos días!", "buenos dias"),
        ("¿Qué carreras tienen?", "que carreras tienen"),

        # Espacios múltiples
        ("hola    mundo", "hola mundo"),
        ("  texto  con  espacios  ", "texto con espacios"),

        # Casos mixtos
        ("¿INFORMACIÓN?", "informacion"),
        ("  ¡INSCRIPCIÓN!  ", "inscripcion"),
    ]


@pytest.fixture
def ejemplos_clasificacion():
    """
    Fixture con ejemplos de clasificación de intenciones.

    Returns:
        list: Lista de tuplas (pregunta, intencion_esperada)
    """
    return [
        # Saludos
        ("Hola", "saludo_despedida"),
        ("Buenos días", "saludo_despedida"),
        ("Qué tal", "saludo_despedida"),
        ("Adiós", "saludo_despedida"),

        # Información de carreras
        ("Cuéntame sobre Big Data", "informacion_carreras"),
        ("Qué es Desarrollo de Software", "informacion_carreras"),
        ("Información sobre Ciberseguridad", "informacion_carreras"),

        # Inscripción
        ("Cómo me inscribo", "inscripcion_admision"),
        ("Proceso de admisión", "inscripcion_admision"),
        ("Quiero inscribirme", "inscripcion_admision"),

        # Requisitos
        ("Requisitos de ingreso", "requisitos_ingreso"),
        ("Qué necesito para entrar", "requisitos_ingreso"),

        # Contacto
        ("Teléfono de ITSE", "contacto_ubicacion"),
        ("Dónde está ubicado", "contacto_ubicacion"),
        ("Dirección del instituto", "contacto_ubicacion"),
    ]


@pytest.fixture
def ejemplos_respuestas():
    """
    Fixture con ejemplos de preguntas y palabras clave esperadas en respuestas.

    Returns:
        list: Lista de tuplas (pregunta, palabras_clave_esperadas)
    """
    return [
        # Carreras específicas
        ("Cuéntame sobre Big Data", ["Big Data", "ciencia de datos", "análisis"]),
        ("Qué es Desarrollo de Software", ["Desarrollo de Software", "programación", "aplicaciones"]),
        ("Información sobre Ciberseguridad", ["Ciberseguridad", "seguridad", "redes"]),

        # Información institucional
        ("Qué es CAIPI", ["CAIPI", "guardería", "niños"]),
        ("Reconocimientos del ITSE", ["reconocimientos", "ASIBEI", "acreditación"]),
        ("Alianzas del ITSE", ["alianzas", "convenios", "empresas"]),
    ]


@pytest.fixture
def textos_vacios():
    """
    Fixture con ejemplos de textos vacíos o inválidos.

    Returns:
        list: Lista de strings vacíos o solo con espacios
    """
    return [
        "",
        " ",
        "   ",
        "\n",
        "\t",
        "  \n  \t  ",
    ]


@pytest.fixture
def intenciones_validas():
    """
    Fixture con lista de intenciones válidas del sistema.

    Returns:
        list: Lista de nombres de intenciones
    """
    return [
        "becas_financiamiento",
        "contacto_ubicacion",
        "faq_general",
        "fuera_dominio",
        "horarios_duracion",
        "informacion_carreras",
        "inscripcion_admision",
        "requisitos_ingreso",
        "saludo_despedida"
    ]
