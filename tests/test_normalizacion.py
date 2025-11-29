"""
Tests para normalización de texto en TYR

Verifica que el preprocesamiento de texto funciona correctamente:
- Conversión a minúsculas
- Remoción de tildes (normalización Unicode)
- Remoción de puntuación
- Normalización de espacios

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import pytest


class TestNormalizacion:
    """Suite de tests para normalización de texto"""

    def test_normaliza_mayusculas_correctamente(self, chatbot):
        """
        Verifica que el texto en MAYÚSCULAS se convierte a minúsculas.

        Given: Un texto en mayúsculas
        When: Se procesa con procesar_entrada()
        Then: Debe retornar el texto en minúsculas
        """
        entrada = "HOLA"
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "hola", "No convirtió correctamente a minúsculas"

    def test_normaliza_tildes_correctamente(self, chatbot):
        """
        Verifica que los tildes se remueven correctamente usando normalización Unicode.

        Given: Un texto con tildes
        When: Se procesa con procesar_entrada()
        Then: Debe retornar el texto sin tildes
        """
        entrada = "información"
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "informacion", "No removió tildes correctamente"

    def test_normaliza_puntuacion_correctamente(self, chatbot):
        """
        Verifica que la puntuación se remueve del texto.

        Given: Un texto con signos de puntuación
        When: Se procesa con procesar_entrada()
        Then: Debe retornar el texto sin puntuación
        """
        entrada = "¿Hola?"
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "hola", "No removió puntuación correctamente"

    def test_normaliza_espacios_multiples(self, chatbot):
        """
        Verifica que múltiples espacios se reducen a uno solo.

        Given: Un texto con espacios múltiples
        When: Se procesa con procesar_entrada()
        Then: Debe retornar el texto con espacios únicos
        """
        entrada = "hola    mundo"
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "hola mundo", "No normalizó espacios correctamente"

    def test_normaliza_texto_con_tildes_y_mayusculas(self, chatbot):
        """
        Verifica que la normalización funciona con tildes Y mayúsculas combinadas.

        Given: Un texto con MAYÚSCULAS y tildes
        When: Se procesa con procesar_entrada()
        Then: Debe retornar texto en minúsculas sin tildes
        """
        entrada = "INFORMACIÓN"
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "informacion", "No normalizó correctamente texto mixto"

    def test_normaliza_texto_con_todo_combinado(self, chatbot):
        """
        Verifica la normalización completa: mayúsculas, tildes, puntuación y espacios.

        Given: Un texto con todos los elementos a normalizar
        When: Se procesa con procesar_entrada()
        Then: Debe retornar texto completamente normalizado
        """
        entrada = "  ¿INSCRIPCIÓN?  "
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "inscripcion", "No normalizó correctamente texto completo"

    def test_normaliza_texto_vacio(self, chatbot):
        """
        Verifica el manejo de texto vacío.

        Given: Un string vacío
        When: Se procesa con procesar_entrada()
        Then: Debe retornar un string vacío
        """
        entrada = ""
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "", "No manejó correctamente texto vacío"

    def test_normaliza_solo_espacios(self, chatbot):
        """
        Verifica el manejo de texto con solo espacios.

        Given: Un string con solo espacios
        When: Se procesa con procesar_entrada()
        Then: Debe retornar un string vacío
        """
        entrada = "   "
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == "", "No manejó correctamente texto con solo espacios"

    @pytest.mark.parametrize("entrada,esperado", [
        ("HOLA", "hola"),
        ("INFORMACIÓN", "informacion"),
        ("BIG DATA", "big data"),
        ("información", "informacion"),
        ("inscripción", "inscripcion"),
        ("¿Hola?", "hola"),
        ("¡Buenos días!", "buenos dias"),
        ("hola    mundo", "hola mundo"),
        ("  texto  con  espacios  ", "texto con espacios"),
        ("¿INFORMACIÓN?", "informacion"),
    ])
    def test_normalizacion_parametrizada(self, chatbot, entrada, esperado):
        """
        Test parametrizado que verifica múltiples casos de normalización.

        Given: Diferentes tipos de texto de entrada
        When: Se procesan con procesar_entrada()
        Then: Deben retornar el texto normalizado esperado
        """
        resultado = chatbot.procesar_entrada(entrada)
        assert resultado == esperado, f"Falló para entrada: {entrada}"

    def test_normaliza_caracteres_especiales(self, chatbot):
        """
        Verifica que caracteres especiales se manejan correctamente.

        Given: Texto con caracteres especiales
        When: Se procesa con procesar_entrada()
        Then: Debe retornar texto normalizado
        """
        entrada = "¿Cómo me @inscribo? #ITSE"
        resultado = chatbot.procesar_entrada(entrada)
        # Verificar que se normalizó el texto principal
        assert "como" in resultado, "No normalizó correctamente"
        assert "inscribo" in resultado, "No procesó correctamente el texto"

    def test_normaliza_numeros(self, chatbot):
        """
        Verifica que los números se mantienen en el texto normalizado.

        Given: Texto con números
        When: Se procesa con procesar_entrada()
        Then: Los números deben permanecer en el texto
        """
        entrada = "Big Data 2024"
        resultado = chatbot.procesar_entrada(entrada)
        assert "2024" in resultado, "Removió números del texto"
        assert "big" in resultado, "No normalizó correctamente el texto"
        assert "data" in resultado, "No normalizó correctamente el texto"
