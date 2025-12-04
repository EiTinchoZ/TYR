"""
Tests para el módulo NER (Named Entity Recognition)
Valida la extracción de entidades específicas del dominio ITSE

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import sys
from pathlib import Path

# Agregar directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from ner_module import NERExtractor


class TestNERExtractor:
    """Tests para el extractor de entidades nombradas."""

    @pytest.fixture
    def ner(self):
        """Fixture para inicializar el extractor NER."""
        return NERExtractor()

    def test_inicializacion(self, ner):
        """Test: Verificar que el NER se inicializa correctamente."""
        assert ner is not None
        assert hasattr(ner, 'carreras')
        assert hasattr(ner, 'servicios')
        assert hasattr(ner, 'organizaciones')
        assert len(ner.carreras) > 0

    def test_extraer_carrera_simple(self, ner):
        """Test: Extraer nombre de carrera simple."""
        texto = "Quiero información sobre Big Data"
        entidades = ner.extraer_entidades(texto)

        assert len(entidades) > 0
        carreras = [e for e in entidades if e['tipo'] == 'CARRERA']
        assert len(carreras) == 1
        assert carreras[0]['texto'] == 'big data'

    def test_extraer_carrera_compuesta(self, ner):
        """Test: Extraer nombre de carrera compuesta."""
        texto = "Información sobre desarrollo de software"
        entidades = ner.extraer_entidades(texto)

        carreras = [e for e in entidades if e['tipo'] == 'CARRERA']
        assert len(carreras) == 1
        assert 'desarrollo de software' in carreras[0]['texto']

    def test_extraer_organizacion(self, ner):
        """Test: Extraer organizaciones."""
        texto = "El ITSE tiene convenio con IFARHU"
        entidades = ner.extraer_entidades(texto)

        organizaciones = [e for e in entidades if e['tipo'] == 'ORGANIZACION']
        assert len(organizaciones) == 2

        textos_org = [e['texto'] for e in organizaciones]
        assert 'itse' in textos_org
        assert 'ifarhu' in textos_org

    def test_extraer_servicio(self, ner):
        """Test: Extraer servicios institucionales."""
        texto = "¿Tiene guardería CAIPI?"
        entidades = ner.extraer_entidades(texto)

        servicios = [e for e in entidades if e['tipo'] == 'SERVICIO']
        assert len(servicios) >= 1

        textos_serv = [e['texto'] for e in servicios]
        assert 'caipi' in textos_serv

    def test_extraer_ubicacion(self, ner):
        """Test: Extraer ubicaciones geográficas."""
        texto = "El instituto está en Tocumen, Panamá"
        entidades = ner.extraer_entidades(texto)

        ubicaciones = [e for e in entidades if e['tipo'] == 'UBICACION']
        assert len(ubicaciones) == 2

        textos_ubic = [e['texto'] for e in ubicaciones]
        assert 'tocumen' in textos_ubic
        assert 'panamá' in textos_ubic

    def test_extraer_requisitos(self, ner):
        """Test: Extraer requisitos académicos."""
        texto = "Necesito mi título de bachiller y cédula"
        entidades = ner.extraer_entidades(texto)

        requisitos = [e for e in entidades if e['tipo'] == 'REQUISITO']
        assert len(requisitos) >= 2

        textos_req = [e['texto'] for e in requisitos]
        assert 'bachiller' in textos_req
        assert any('c' in t and 'dula' in t for t in textos_req)  # cédula o cedula

    def test_extraer_periodo_horario(self, ner):
        """Test: Extraer referencias temporales."""
        texto = "El horario es de lunes a viernes de 8 am a 5 pm"
        entidades = ner.extraer_entidades(texto)

        periodos = [e for e in entidades if e['tipo'] == 'PERIODO']
        assert len(periodos) >= 2

        textos_periodo = [e['texto'] for e in periodos]
        assert 'lunes' in textos_periodo
        assert 'viernes' in textos_periodo

    def test_multiples_entidades(self, ner):
        """Test: Extraer múltiples tipos de entidades."""
        texto = "Quiero estudiar Big Data en el ITSE de Tocumen"
        entidades = ner.extraer_entidades(texto)

        # Debe haber al menos 3 entidades: carrera, organización, ubicación
        assert len(entidades) >= 3

        tipos = [e['tipo'] for e in entidades]
        assert 'CARRERA' in tipos
        assert 'ORGANIZACION' in tipos
        assert 'UBICACION' in tipos

    def test_texto_sin_entidades(self, ner):
        """Test: Texto sin entidades reconocibles."""
        texto = "Hola buenos días"
        entidades = ner.extraer_entidades(texto)

        assert len(entidades) == 0

    def test_case_insensitive(self, ner):
        """Test: Verificar que la extracción es case-insensitive."""
        texto1 = "BIG DATA"
        texto2 = "big data"
        texto3 = "Big Data"

        entidades1 = ner.extraer_entidades(texto1)
        entidades2 = ner.extraer_entidades(texto2)
        entidades3 = ner.extraer_entidades(texto3)

        assert len(entidades1) > 0
        assert len(entidades2) > 0
        assert len(entidades3) > 0

    def test_obtener_resumen(self, ner):
        """Test: Verificar resumen de entidades por tipo."""
        texto = "Estudiar Ciberseguridad en ITSE de Tocumen"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        assert isinstance(resumen, dict)
        assert 'CARRERA' in resumen
        assert 'ORGANIZACION' in resumen
        assert 'UBICACION' in resumen

    def test_formatear_salida(self, ner):
        """Test: Verificar formato de salida legible."""
        texto = "Big Data en ITSE"
        entidades = ner.extraer_entidades(texto)
        salida = ner.formatear_salida(entidades)

        assert isinstance(salida, str)
        assert len(salida) > 0
        assert 'Entidades detectadas' in salida

    def test_entidades_sin_solapamiento(self, ner):
        """Test: Verificar que no hay entidades solapadas."""
        texto = "Desarrollo de software y big data en ITSE"
        entidades = ner.extraer_entidades(texto)

        # Verificar que no hay solapamiento
        for i in range(len(entidades)):
            for j in range(i + 1, len(entidades)):
                ent1 = entidades[i]
                ent2 = entidades[j]

                # No debe haber solapamiento
                assert (ent1['fin'] <= ent2['inicio']) or (ent1['inicio'] >= ent2['fin'])

    def test_posiciones_correctas(self, ner):
        """Test: Verificar que las posiciones inicio/fin son correctas."""
        texto = "Información sobre Big Data"
        entidades = ner.extraer_entidades(texto)

        for entidad in entidades:
            assert 'inicio' in entidad
            assert 'fin' in entidad
            assert entidad['inicio'] >= 0
            assert entidad['fin'] > entidad['inicio']
            assert entidad['fin'] <= len(texto)

            # Verificar que el texto extraído coincide
            texto_extraido = texto[entidad['inicio']:entidad['fin']].lower()
            assert entidad['texto'] in texto_extraido or texto_extraido in entidad['texto']

    def test_caso_complejo_real(self, ner):
        """Test: Caso de uso real complejo."""
        texto = "¿Qué requisitos necesito para estudiar Ciberseguridad en el ITSE? Tengo mi bachiller."
        entidades = ner.extraer_entidades(texto)

        resumen = ner.obtener_resumen(entidades)

        # Debe detectar carrera, organización y requisito
        assert 'CARRERA' in resumen
        assert 'ciberseguridad' in resumen['CARRERA']

        assert 'ORGANIZACION' in resumen
        assert 'itse' in resumen['ORGANIZACION']

        assert 'REQUISITO' in resumen
        assert 'bachiller' in resumen['REQUISITO']


class TestNERIntegration:
    """Tests de integración NER con casos de uso reales del ITSE."""

    @pytest.fixture
    def ner(self):
        return NERExtractor()

    def test_consulta_carrera_con_ubicacion(self, ner):
        """Test: Consulta típica sobre carrera con ubicación."""
        texto = "Quiero estudiar Big Data en el ITSE de Tocumen"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        assert 'big data' in resumen.get('CARRERA', [])
        assert 'itse' in resumen.get('ORGANIZACION', [])
        assert 'tocumen' in resumen.get('UBICACION', [])

    def test_consulta_becas_ifarhu(self, ner):
        """Test: Consulta sobre becas IFARHU."""
        texto = "Información sobre becas IFARHU para desarrollo de software"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        assert 'desarrollo de software' in resumen.get('CARRERA', [])
        assert 'ifarhu' in resumen.get('ORGANIZACION', [])

    def test_consulta_servicio_caipi(self, ner):
        """Test: Consulta sobre servicio CAIPI."""
        texto = "¿El ITSE tiene guardería CAIPI?"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        assert 'itse' in resumen.get('ORGANIZACION', [])
        assert 'caipi' in resumen.get('SERVICIO', [])

    def test_consulta_horarios(self, ner):
        """Test: Consulta sobre horarios."""
        texto = "¿Cuál es el horario de lunes a viernes?"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        assert 'PERIODO' in resumen
        assert 'lunes' in resumen['PERIODO']
        assert 'viernes' in resumen['PERIODO']

    def test_consulta_requisitos_matricula(self, ner):
        """Test: Consulta sobre requisitos de matrícula."""
        texto = "Necesito título de bachiller y cédula para inscribirme"
        entidades = ner.extraer_entidades(texto)
        resumen = ner.obtener_resumen(entidades)

        assert 'REQUISITO' in resumen
        requisitos = resumen['REQUISITO']
        assert 'bachiller' in requisitos
        assert any('dula' in r for r in requisitos)  # cédula o cedula


if __name__ == "__main__":
    # Ejecutar tests
    pytest.main([__file__, "-v", "--tb=short"])
