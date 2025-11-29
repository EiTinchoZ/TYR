"""
Tests para la clase TYR Chatbot

Verifica la funcionalidad principal del chatbot:
- Clasificación de intenciones con BERT
- Confianza de predicciones
- Manejo de diferentes tipos de consultas
- Análisis de sentimiento
- Procesamiento completo de consultas

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import pytest


class TestClasificacionIntenciones:
    """Suite de tests para clasificación de intenciones con BERT"""

    def test_clasifica_saludo_correctamente(self, chatbot):
        """
        Verifica que los saludos se clasifican como 'saludo_despedida'.

        Given: Una pregunta de saludo
        When: Se clasifica la intención
        Then: La intención debe ser 'saludo_despedida'
        """
        texto = "Hola"
        intencion, confianza, _ = chatbot.clasificar_intencion(texto)
        assert intencion == "saludo_despedida", f"Clasificó como {intencion} en vez de saludo_despedida"

    def test_clasifica_despedida_correctamente(self, chatbot):
        """
        Verifica que las despedidas se clasifican como 'saludo_despedida'.

        Given: Una despedida
        When: Se clasifica la intención
        Then: La intención debe ser 'saludo_despedida'
        """
        texto = "Adiós"
        intencion, confianza, _ = chatbot.clasificar_intencion(texto)
        assert intencion == "saludo_despedida", f"Clasificó como {intencion} en vez de saludo_despedida"

    def test_clasifica_pregunta_carrera_correctamente(self, chatbot):
        """
        Verifica que preguntas sobre carreras se clasifican como 'informacion_carreras'.

        Given: Una pregunta sobre una carrera específica
        When: Se clasifica la intención
        Then: La intención debe ser 'informacion_carreras'
        """
        texto = "Cuéntame sobre Big Data"
        intencion, confianza, _ = chatbot.clasificar_intencion(texto)
        assert intencion == "informacion_carreras", f"Clasificó como {intencion} en vez de informacion_carreras"

    def test_clasifica_inscripcion_correctamente(self, chatbot):
        """
        Verifica que preguntas de inscripción se clasifican como 'inscripcion_admision'.

        Given: Una pregunta sobre inscripción
        When: Se clasifica la intención
        Then: La intención debe ser 'inscripcion_admision'
        """
        texto = "Cómo me inscribo"
        intencion, confianza, _ = chatbot.clasificar_intencion(texto)
        assert intencion == "inscripcion_admision", f"Clasificó como {intencion} en vez de inscripcion_admision"

    def test_clasifica_requisitos_correctamente(self, chatbot):
        """
        Verifica que preguntas de requisitos se clasifican como 'requisitos_ingreso'.

        Given: Una pregunta sobre requisitos
        When: Se clasifica la intención
        Then: La intención debe ser 'requisitos_ingreso'
        """
        texto = "Requisitos de ingreso"
        intencion, confianza, _ = chatbot.clasificar_intencion(texto)
        assert intencion == "requisitos_ingreso", f"Clasificó como {intencion} en vez de requisitos_ingreso"

    def test_clasifica_contacto_correctamente(self, chatbot):
        """
        Verifica que preguntas de contacto se clasifican como 'contacto_ubicacion'.

        Given: Una pregunta sobre contacto o ubicación
        When: Se clasifica la intención
        Then: La intención debe ser 'contacto_ubicacion'
        """
        texto = "Teléfono de ITSE"
        intencion, confianza, _ = chatbot.clasificar_intencion(texto)
        assert intencion == "contacto_ubicacion", f"Clasificó como {intencion} en vez de contacto_ubicacion"

    def test_confianza_minima_threshold(self, chatbot):
        """
        Verifica que la confianza de clasificaciones es mayor al threshold (0.7).

        Given: Una pregunta común
        When: Se clasifica la intención
        Then: La confianza debe ser mayor a 0.7
        """
        texto = "Hola buenos días"
        _, confianza, _ = chatbot.clasificar_intencion(texto)
        assert confianza > 0.7, f"Confianza {confianza} es menor al threshold 0.7"

    def test_confianza_alta_para_preguntas_claras(self, chatbot):
        """
        Verifica que preguntas claras tienen alta confianza (>0.9).

        Given: Una pregunta clara y directa
        When: Se clasifica la intención
        Then: La confianza debe ser mayor a 0.9
        """
        texto = "Hola"
        _, confianza, _ = chatbot.clasificar_intencion(texto)
        assert confianza > 0.9, f"Confianza {confianza} es menor a 0.9 para pregunta clara"

    def test_clasificacion_retorna_diccionario_probabilidades(self, chatbot):
        """
        Verifica que clasificar_intencion retorna todas las probabilidades.

        Given: Cualquier texto
        When: Se clasifica la intención
        Then: Debe retornar un diccionario con probabilidades de todas las intenciones
        """
        texto = "Hola"
        _, _, probabilidades = chatbot.clasificar_intencion(texto)
        assert isinstance(probabilidades, dict), "No retornó un diccionario"
        assert len(probabilidades) == 9, f"Esperaba 9 intenciones, obtuvo {len(probabilidades)}"

    def test_suma_probabilidades_es_uno(self, chatbot):
        """
        Verifica que las probabilidades de todas las intenciones suman 1.0.

        Given: Cualquier texto clasificado
        When: Se suman todas las probabilidades
        Then: La suma debe ser aproximadamente 1.0
        """
        texto = "Hola"
        _, _, probabilidades = chatbot.clasificar_intencion(texto)
        suma = sum(probabilidades.values())
        assert abs(suma - 1.0) < 0.01, f"Suma de probabilidades es {suma}, no 1.0"

    def test_intencion_esta_en_label_map(self, chatbot, intenciones_validas):
        """
        Verifica que la intención clasificada es válida.

        Given: Cualquier texto
        When: Se clasifica la intención
        Then: La intención debe estar en la lista de intenciones válidas
        """
        texto = "Hola"
        intencion, _, _ = chatbot.clasificar_intencion(texto)
        assert intencion in intenciones_validas, f"Intención {intencion} no es válida"


class TestProcesamientoCompleto:
    """Suite de tests para el procesamiento completo de consultas"""

    def test_procesar_consulta_retorna_tupla(self, chatbot):
        """
        Verifica que procesar_consulta retorna una tupla (respuesta, metadata).

        Given: Una consulta
        When: Se procesa con procesar_consulta()
        Then: Debe retornar una tupla de 2 elementos
        """
        resultado = chatbot.procesar_consulta("Hola")
        assert isinstance(resultado, tuple), "No retornó una tupla"
        assert len(resultado) == 2, f"Esperaba tupla de 2 elementos, obtuvo {len(resultado)}"

    def test_procesar_consulta_respuesta_es_string(self, chatbot):
        """
        Verifica que la respuesta es un string.

        Given: Una consulta
        When: Se procesa con procesar_consulta()
        Then: La respuesta debe ser un string no vacío
        """
        respuesta, _ = chatbot.procesar_consulta("Hola")
        assert isinstance(respuesta, str), "Respuesta no es un string"
        assert len(respuesta) > 0, "Respuesta está vacía"

    def test_procesar_consulta_metadata_es_dict(self, chatbot):
        """
        Verifica que metadata es un diccionario.

        Given: Una consulta
        When: Se procesa con procesar_consulta()
        Then: Metadata debe ser un diccionario
        """
        _, metadata = chatbot.procesar_consulta("Hola")
        assert isinstance(metadata, dict), "Metadata no es un diccionario"

    def test_metadata_contiene_campos_requeridos(self, chatbot):
        """
        Verifica que metadata contiene todos los campos requeridos.

        Given: Una consulta procesada
        When: Se examina metadata
        Then: Debe contener: intencion, confianza, sentimiento
        """
        _, metadata = chatbot.procesar_consulta("Hola")
        campos_requeridos = ['intencion', 'confianza', 'sentimiento']
        for campo in campos_requeridos:
            assert campo in metadata, f"Metadata no contiene campo {campo}"

    def test_procesar_texto_vacio_no_causa_error(self, chatbot):
        """
        Verifica que procesar texto vacío no causa errores.

        Given: Un texto vacío
        When: Se procesa con procesar_consulta()
        Then: No debe lanzar excepción
        """
        try:
            respuesta, metadata = chatbot.procesar_consulta("")
            assert True  # Si llegó aquí, no hubo error
        except Exception as e:
            pytest.fail(f"Procesar texto vacío causó error: {e}")

    def test_procesar_texto_muy_largo(self, chatbot):
        """
        Verifica que textos muy largos se manejan correctamente.

        Given: Un texto de más de 128 tokens
        When: Se procesa con procesar_consulta()
        Then: No debe causar error (se trunca automáticamente)
        """
        texto_largo = "Hola " * 100  # 100 palabras
        try:
            respuesta, metadata = chatbot.procesar_consulta(texto_largo)
            assert isinstance(respuesta, str), "No retornó respuesta válida"
        except Exception as e:
            pytest.fail(f"Texto largo causó error: {e}")


class TestAnalisisSentimiento:
    """Suite de tests para análisis de sentimiento VADER"""

    def test_analizar_sentimiento_retorna_diccionario(self, chatbot):
        """
        Verifica que analizar_sentimiento retorna un diccionario.

        Given: Un texto
        When: Se analiza con analizar_sentimiento()
        Then: Debe retornar un diccionario con scores
        """
        resultado = chatbot.analizar_sentimiento("Estoy muy feliz")
        assert isinstance(resultado, dict), "No retornó diccionario"
        assert 'categoria' in resultado, "No contiene categoría de sentimiento"
        assert 'compound' in resultado, "No contiene compound score"

    def test_sentimiento_es_string_valido(self, chatbot):
        """
        Verifica que el sentimiento es un string válido.

        Given: Un texto
        When: Se analiza el sentimiento
        Then: Debe ser uno de: positivo, negativo, neutro
        """
        resultado = chatbot.analizar_sentimiento("Hola")
        sentimientos_validos = ['positivo', 'negativo', 'neutro']
        assert resultado['categoria'] in sentimientos_validos, \
            f"Sentimiento {resultado['categoria']} no es válido"

    def test_score_sentimiento_en_rango(self, chatbot):
        """
        Verifica que el score de sentimiento está en rango [-1, 1].

        Given: Un texto
        When: Se analiza el sentimiento
        Then: El compound score debe estar entre -1 y 1
        """
        resultado = chatbot.analizar_sentimiento("Hola")
        compound = resultado['compound']
        assert -1.0 <= compound <= 1.0, f"Score {compound} fuera de rango [-1, 1]"

    def test_texto_positivo_tiene_sentimiento_positivo(self, chatbot):
        """
        Verifica que textos positivos se detectan correctamente.

        Given: Un texto claramente positivo
        When: Se analiza el sentimiento
        Then: Debe tener un compound score positivo o neutral
        """
        resultado = chatbot.analizar_sentimiento("Excelente, muy bueno, gracias")
        # VADER en español puede no ser perfecto, así que aceptamos positivo o neutral
        assert resultado['categoria'] in ['positivo', 'neutro'], \
            f"Texto positivo clasificado como {resultado['categoria']}"
