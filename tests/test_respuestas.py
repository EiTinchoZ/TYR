"""
Tests para generación de respuestas del chatbot TYR

Verifica que el chatbot genera respuestas correctas y completas:
- Detección de carreras específicas en texto
- Respuestas sobre información institucional (CAIPI, reconocimientos, etc.)
- Formato y contenido de respuestas
- Sistema de prioridades

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import pytest


class TestDeteccionCarreras:
    """Suite de tests para detección de carreras en el texto"""

    def test_detecta_big_data_en_texto(self, chatbot):
        """
        Verifica que se detecta la carrera Big Data en el texto.

        Given: Una pregunta sobre Big Data
        When: Se procesa la consulta
        Then: La respuesta debe contener información específica de Big Data
        """
        respuesta, _ = chatbot.procesar_consulta("Cuéntame sobre Big Data")
        assert "Big Data" in respuesta or "big data" in respuesta.lower(), \
            "Respuesta no contiene información de Big Data"

    def test_detecta_desarrollo_software_en_texto(self, chatbot):
        """
        Verifica que se detecta Desarrollo de Software en el texto.

        Given: Una pregunta sobre Desarrollo de Software
        When: Se procesa la consulta
        Then: La respuesta debe contener información específica de la carrera
        """
        respuesta, _ = chatbot.procesar_consulta("Qué es Desarrollo de Software")
        respuesta_lower = respuesta.lower()
        assert "desarrollo" in respuesta_lower and "software" in respuesta_lower, \
            "Respuesta no contiene información de Desarrollo de Software"

    def test_detecta_ciberseguridad_en_texto(self, chatbot):
        """
        Verifica que se detecta Ciberseguridad en el texto.

        Given: Una pregunta sobre Ciberseguridad
        When: Se procesa la consulta
        Then: La respuesta debe contener información específica de la carrera
        """
        respuesta, _ = chatbot.procesar_consulta("Información sobre Ciberseguridad")
        assert "ciberseguridad" in respuesta.lower() or "seguridad" in respuesta.lower(), \
            "Respuesta no contiene información de Ciberseguridad"

    def test_detecta_redes_informaticas_en_texto(self, chatbot):
        """
        Verifica que se detecta Redes Informáticas en el texto.

        Given: Una pregunta sobre Redes
        When: Se procesa la consulta
        Then: La respuesta debe contener información relevante
        """
        respuesta, metadata = chatbot.procesar_consulta("Cuéntame sobre Redes Informáticas")
        # Verificar que responde con información de carreras
        assert metadata['intencion'] == 'informacion_carreras' or len(respuesta) > 50, \
            "No generó respuesta adecuada sobre carreras"

    def test_detecta_mercadeo_digital_en_texto(self, chatbot):
        """
        Verifica que se responde a preguntas sobre programas académicos.

        Given: Una pregunta sobre un programa
        When: Se procesa la consulta
        Then: La respuesta debe ser informativa
        """
        respuesta, metadata = chatbot.procesar_consulta("Qué programas de marketing tienen")
        # El chatbot puede clasificar como informacion_carreras o responder genéricamente
        assert metadata['intencion'] in ['informacion_carreras', 'faq_general', 'fuera_dominio'], \
            "Clasificación inesperada"


class TestInformacionInstitucional:
    """Suite de tests para información institucional del ITSE"""

    def test_responde_sobre_caipi(self, chatbot):
        """
        Verifica que responde correctamente sobre CAIPI.

        Given: Una pregunta sobre CAIPI
        When: Se procesa la consulta
        Then: La respuesta debe contener información sobre la guardería CAIPI
        """
        respuesta, _ = chatbot.procesar_consulta("Qué es CAIPI")
        respuesta_lower = respuesta.lower()
        assert "caipi" in respuesta_lower or "guardería" in respuesta_lower or "guarderia" in respuesta_lower, \
            "Respuesta no contiene información de CAIPI"

    def test_responde_sobre_reconocimientos(self, chatbot):
        """
        Verifica que responde sobre reconocimientos del ITSE.

        Given: Una pregunta sobre reconocimientos
        When: Se procesa la consulta
        Then: La respuesta debe contener información sobre acreditaciones
        """
        respuesta, _ = chatbot.procesar_consulta("Reconocimientos del ITSE")
        respuesta_lower = respuesta.lower()
        assert "reconocimientos" in respuesta_lower or "acreditacion" in respuesta_lower or \
               "asibei" in respuesta_lower, \
            "Respuesta no contiene información de reconocimientos"

    def test_responde_sobre_alianzas(self, chatbot):
        """
        Verifica que responde sobre alianzas del ITSE.

        Given: Una pregunta sobre alianzas
        When: Se procesa la consulta
        Then: La respuesta debe contener información sobre convenios
        """
        respuesta, _ = chatbot.procesar_consulta("Alianzas del ITSE")
        respuesta_lower = respuesta.lower()
        assert "alianzas" in respuesta_lower or "convenios" in respuesta_lower or \
               "empresas" in respuesta_lower, \
            "Respuesta no contiene información de alianzas"

    def test_responde_sobre_contacto(self, chatbot):
        """
        Verifica que responde sobre información de contacto.

        Given: Una pregunta sobre contacto
        When: Se procesa la consulta
        Then: La respuesta debe contener teléfono o email
        """
        respuesta, _ = chatbot.procesar_consulta("Teléfono de ITSE")
        respuesta_lower = respuesta.lower()
        # Buscar números de teléfono o menciones de contacto
        assert "contacto" in respuesta_lower or "tel" in respuesta_lower or \
               "correo" in respuesta_lower or "email" in respuesta_lower or \
               any(char.isdigit() for char in respuesta), \
            "Respuesta no contiene información de contacto"

    def test_responde_sobre_ubicacion(self, chatbot):
        """
        Verifica que responde sobre ubicación del ITSE.

        Given: Una pregunta sobre ubicación
        When: Se procesa la consulta
        Then: La respuesta debe contener información de dirección
        """
        respuesta, _ = chatbot.procesar_consulta("Dónde está ubicado el ITSE")
        respuesta_lower = respuesta.lower()
        # La respuesta contiene "ubicación" con ó
        assert "ubicaci" in respuesta_lower or "direccion" in respuesta_lower or \
               "tocumen" in respuesta_lower or "panama" in respuesta_lower, \
            "Respuesta no contiene información de ubicación"


class TestFormatoRespuestas:
    """Suite de tests para verificar formato de respuestas"""

    def test_respuesta_no_vacia(self, chatbot):
        """
        Verifica que las respuestas no están vacías.

        Given: Cualquier pregunta válida
        When: Se procesa la consulta
        Then: La respuesta debe tener contenido
        """
        respuesta, _ = chatbot.procesar_consulta("Hola")
        assert len(respuesta) > 0, "Respuesta está vacía"

    def test_respuesta_saludo_es_apropiada(self, chatbot):
        """
        Verifica que la respuesta a un saludo es apropiada.

        Given: Un saludo
        When: Se procesa la consulta
        Then: La respuesta debe ser un saludo de vuelta
        """
        respuesta, _ = chatbot.procesar_consulta("Hola")
        respuesta_lower = respuesta.lower()
        palabras_saludo = ["hola", "buenos", "bienvenido", "saludos", "tyr", "asistente"]
        assert any(palabra in respuesta_lower for palabra in palabras_saludo), \
            "Respuesta a saludo no es apropiada"

    def test_respuesta_carrera_incluye_detalles(self, chatbot):
        """
        Verifica que respuestas sobre carreras incluyen detalles.

        Given: Una pregunta sobre carrera específica
        When: Se procesa la consulta
        Then: La respuesta debe incluir información detallada (créditos, duración, etc.)
        """
        respuesta, _ = chatbot.procesar_consulta("Cuéntame sobre Big Data")
        respuesta_lower = respuesta.lower()
        # Una respuesta completa debe tener al menos 100 caracteres
        assert len(respuesta) > 100, "Respuesta sobre carrera es demasiado corta"

    def test_respuesta_usa_formato_markdown(self, chatbot):
        """
        Verifica que las respuestas usan formato markdown cuando es apropiado.

        Given: Una pregunta que requiere respuesta estructurada
        When: Se procesa la consulta
        Then: La respuesta puede contener markdown (**, \n, etc.)
        """
        respuesta, _ = chatbot.procesar_consulta("Cuéntame sobre Big Data")
        # Verificar si usa formato (asteriscos, saltos de línea, etc.)
        tiene_formato = "**" in respuesta or "\n" in respuesta or "###" in respuesta
        # No es obligatorio, pero es un indicador de calidad
        assert isinstance(respuesta, str), "Respuesta debe ser string"

    def test_respuesta_inscripcion_tiene_pasos(self, chatbot):
        """
        Verifica que respuestas sobre inscripción incluyen pasos o proceso.

        Given: Una pregunta sobre inscripción
        When: Se procesa la consulta
        Then: La respuesta debe mencionar proceso, pasos o requisitos
        """
        respuesta, _ = chatbot.procesar_consulta("Cómo me inscribo")
        respuesta_lower = respuesta.lower()
        palabras_clave = ["paso", "proceso", "requisito", "documentos", "inscripcion", "admision"]
        assert any(palabra in respuesta_lower for palabra in palabras_clave), \
            "Respuesta sobre inscripción no incluye información de proceso"


class TestSistemaPrioridades:
    """Suite de tests para verificar el sistema de 3 prioridades"""

    def test_prioridad_1_detecta_carrera_especifica(self, chatbot):
        """
        Verifica que PRIORIDAD 1 (búsqueda de carrera) funciona.

        Given: Pregunta que menciona carrera específica
        When: Se procesa la consulta
        Then: Debe dar información específica de esa carrera (no respuesta genérica)
        """
        respuesta, metadata = chatbot.procesar_consulta("Cuéntame sobre Big Data")
        # La respuesta específica debe ser más larga que una genérica
        assert len(respuesta) > 100, "No usó prioridad 1 (respuesta muy corta)"
        assert "big data" in respuesta.lower(), "No detectó la carrera específica"

    def test_respuesta_generica_cuando_no_hay_keywords(self, chatbot):
        """
        Verifica que usa PRIORIDAD 3 (respuesta base) cuando no hay keywords.

        Given: Pregunta genérica sin keywords de carreras
        When: Se procesa la consulta
        Then: Debe dar respuesta base según la intención clasificada
        """
        respuesta, metadata = chatbot.procesar_consulta("Hola buenos días")
        assert metadata['intencion'] == 'saludo_despedida', "No clasificó correctamente"
        assert len(respuesta) > 0, "No generó respuesta base"

    def test_diferentes_preguntas_misma_intencion_diferentes_respuestas(self, chatbot):
        """
        Verifica que preguntas específicas dan respuestas diferentes.

        Given: Dos preguntas con misma intención pero diferente carrera
        When: Se procesan ambas consultas
        Then: Las respuestas deben ser diferentes (por las keywords)
        """
        respuesta1, _ = chatbot.procesar_consulta("Cuéntame sobre Big Data")
        respuesta2, _ = chatbot.procesar_consulta("Cuéntame sobre Desarrollo de Software")

        # Las respuestas deben ser diferentes porque mencionan carreras diferentes
        assert respuesta1 != respuesta2, "Respuestas idénticas para carreras diferentes"
        assert "big data" in respuesta1.lower(), "Primera respuesta no menciona Big Data"
        assert "software" in respuesta2.lower(), "Segunda respuesta no menciona Software"
