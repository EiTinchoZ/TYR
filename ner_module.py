"""
Módulo NER (Named Entity Recognition) Personalizado para TYR
Extrae entidades específicas del dominio ITSE

Tipos de entidades reconocidas:
- CARRERA: Programas técnicos del ITSE
- SERVICIO: Servicios institucionales (CAIPI, CIIECYT)
- ORGANIZACION: Organizaciones y entidades
- UBICACION: Ubicaciones geográficas
- PERIODO: Referencias temporales
- REQUISITO: Requisitos académicos

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import re
from typing import List, Dict, Tuple
import json
from pathlib import Path


class NERExtractor:
    """
    Extractor de entidades nombradas específico para el dominio del ITSE.

    Utiliza pattern matching y reglas específicas del dominio para identificar
    entidades relevantes en consultas de estudiantes.
    """

    def __init__(self, data_path: str = "data"):
        """
        Inicializar el extractor NER.

        Args:
            data_path: Ruta al directorio con los datos JSON
        """
        self.data_path = Path(data_path)
        self._cargar_entidades()

    def _cargar_entidades(self):
        """Cargar catálogos de entidades conocidas desde los archivos JSON."""

        # Carreras técnicas del ITSE
        self.carreras = [
            "big data",
            "ciberseguridad",
            "desarrollo de software",
            "redes y telecomunicaciones",
            "hardware y soporte técnico",
            "diseño gráfico",
            "diseño de videojuegos",
            "animación digital",
            "producción de audio",
            "producción de video",
            "mecatrónica",
            "electricidad",
            "electrónica",
            "refrigeración",
            "telecomunicaciones",
            "networking"
        ]

        # Servicios institucionales
        self.servicios = [
            "caipi",
            "ciiecyt",
            "centro de atención integral",
            "centro de investigación",
            "guardería",
            "biblioteca",
            "laboratorios"
        ]

        # Organizaciones
        self.organizaciones = [
            "itse",
            "instituto técnico superior especializado",
            "meduca",
            "ministerio de educación",
            "ifarhu",
            "unesco",
            "abet",
            "microsoft",
            "cisco"
        ]

        # Ubicaciones
        self.ubicaciones = [
            "panamá",
            "tocumen",
            "ciudad de panamá",
            "torre plaza",
            "vía españa"
        ]

        # Periodos temporales
        self.periodos_regex = [
            r'\b\d{4}\b',  # Años (2024, 2025)
            r'\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b',
            r'\b(lunes|martes|miércoles|miercoles|jueves|viernes|sábado|sabado|domingo)\b',
            r'\b(mañana|tarde|noche)\b',
            r'\b\d{1,2}\s*(am|pm|a\.?m\.?|p\.?m\.?)\b'
        ]

        # Requisitos académicos
        self.requisitos = [
            "bachiller",
            "diploma",
            "título",
            "certificado",
            "secundaria",
            "cédula",
            "cedula",
            "notas",
            "promedio"
        ]

    def extraer_entidades(self, texto: str) -> List[Dict[str, str]]:
        """
        Extraer todas las entidades del texto.

        Args:
            texto: Texto de entrada para análisis

        Returns:
            Lista de diccionarios con entidades encontradas.
            Cada diccionario contiene 'texto', 'tipo', 'inicio', 'fin'
        """
        texto_lower = texto.lower()
        entidades = []

        # Extraer carreras
        entidades.extend(self._extraer_por_lista(
            texto_lower, self.carreras, "CARRERA"
        ))

        # Extraer servicios
        entidades.extend(self._extraer_por_lista(
            texto_lower, self.servicios, "SERVICIO"
        ))

        # Extraer organizaciones
        entidades.extend(self._extraer_por_lista(
            texto_lower, self.organizaciones, "ORGANIZACION"
        ))

        # Extraer ubicaciones
        entidades.extend(self._extraer_por_lista(
            texto_lower, self.ubicaciones, "UBICACION"
        ))

        # Extraer requisitos
        entidades.extend(self._extraer_por_lista(
            texto_lower, self.requisitos, "REQUISITO"
        ))

        # Extraer periodos temporales (regex)
        entidades.extend(self._extraer_por_regex(
            texto_lower, self.periodos_regex, "PERIODO"
        ))

        # Ordenar por posición y eliminar duplicados
        entidades = self._eliminar_duplicados(entidades)
        entidades.sort(key=lambda x: x['inicio'])

        return entidades

    def _extraer_por_lista(
        self,
        texto: str,
        lista_entidades: List[str],
        tipo: str
    ) -> List[Dict[str, str]]:
        """
        Extraer entidades que coincidan con una lista predefinida.

        Args:
            texto: Texto en minúsculas
            lista_entidades: Lista de entidades a buscar
            tipo: Tipo de entidad (CARRERA, SERVICIO, etc.)

        Returns:
            Lista de entidades encontradas
        """
        entidades = []

        for entidad in lista_entidades:
            # Buscar todas las ocurrencias
            pattern = r'\b' + re.escape(entidad) + r'\b'
            matches = re.finditer(pattern, texto)

            for match in matches:
                entidades.append({
                    'texto': match.group(),
                    'tipo': tipo,
                    'inicio': match.start(),
                    'fin': match.end()
                })

        return entidades

    def _extraer_por_regex(
        self,
        texto: str,
        patrones: List[str],
        tipo: str
    ) -> List[Dict[str, str]]:
        """
        Extraer entidades usando expresiones regulares.

        Args:
            texto: Texto en minúsculas
            patrones: Lista de patrones regex
            tipo: Tipo de entidad

        Returns:
            Lista de entidades encontradas
        """
        entidades = []

        for pattern in patrones:
            matches = re.finditer(pattern, texto, re.IGNORECASE)

            for match in matches:
                entidades.append({
                    'texto': match.group(),
                    'tipo': tipo,
                    'inicio': match.start(),
                    'fin': match.end()
                })

        return entidades

    def _eliminar_duplicados(
        self,
        entidades: List[Dict[str, str]]
    ) -> List[Dict[str, str]]:
        """
        Eliminar entidades duplicadas o solapadas.

        Regla: Si dos entidades se solapan, mantener la más específica (más larga).

        Args:
            entidades: Lista de entidades

        Returns:
            Lista de entidades sin duplicados
        """
        if not entidades:
            return []

        # Ordenar por inicio y longitud (más largas primero)
        entidades_sorted = sorted(
            entidades,
            key=lambda x: (x['inicio'], -(x['fin'] - x['inicio']))
        )

        resultado = []

        for entidad in entidades_sorted:
            # Verificar si solapa con alguna entidad ya añadida
            solapa = False
            for ent_guardada in resultado:
                if self._hay_solapamiento(entidad, ent_guardada):
                    solapa = True
                    break

            if not solapa:
                resultado.append(entidad)

        return resultado

    def _hay_solapamiento(
        self,
        ent1: Dict[str, str],
        ent2: Dict[str, str]
    ) -> bool:
        """
        Verificar si dos entidades se solapan.

        Args:
            ent1, ent2: Entidades a comparar

        Returns:
            True si hay solapamiento
        """
        return not (ent1['fin'] <= ent2['inicio'] or ent1['inicio'] >= ent2['fin'])

    def obtener_resumen(self, entidades: List[Dict[str, str]]) -> Dict[str, List[str]]:
        """
        Generar resumen de entidades por tipo.

        Args:
            entidades: Lista de entidades extraídas

        Returns:
            Diccionario con entidades agrupadas por tipo
        """
        resumen = {}

        for entidad in entidades:
            tipo = entidad['tipo']
            texto = entidad['texto']

            if tipo not in resumen:
                resumen[tipo] = []

            if texto not in resumen[tipo]:
                resumen[tipo].append(texto)

        return resumen

    def formatear_salida(
        self,
        entidades: List[Dict[str, str]],
        incluir_posiciones: bool = False
    ) -> str:
        """
        Formatear entidades para display.

        Args:
            entidades: Lista de entidades
            incluir_posiciones: Si True, incluye inicio/fin

        Returns:
            String formateado con las entidades
        """
        if not entidades:
            return "No se detectaron entidades."

        resumen = self.obtener_resumen(entidades)

        lineas = ["[NER] Entidades detectadas:\n"]

        for tipo, textos in sorted(resumen.items()):
            lineas.append(f"  {tipo}:")
            for texto in textos:
                if incluir_posiciones:
                    # Buscar posiciones
                    ent = next(e for e in entidades if e['texto'] == texto and e['tipo'] == tipo)
                    lineas.append(f"    - {texto} [{ent['inicio']}:{ent['fin']}]")
                else:
                    lineas.append(f"    - {texto}")
            lineas.append("")

        return "\n".join(lineas)


# Función de conveniencia para uso rápido
def extraer_entidades_rapido(texto: str) -> List[Dict[str, str]]:
    """
    Función helper para extraer entidades rápidamente.

    Args:
        texto: Texto a analizar

    Returns:
        Lista de entidades encontradas
    """
    extractor = NERExtractor()
    return extractor.extraer_entidades(texto)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear extractor
    ner = NERExtractor()

    # Casos de prueba
    casos_prueba = [
        "Quiero información sobre Big Data en el ITSE",
        "¿Qué requisitos necesito para estudiar Ciberseguridad?",
        "¿El ITSE tiene guardería CAIPI en Tocumen?",
        "Información sobre becas IFARHU para desarrollo de software",
        "¿Cuál es el horario de lunes a viernes de 8 am a 5 pm?",
        "Necesito mi título de bachiller y cédula para matricularme"
    ]

    print("=" * 70)
    print("DEMOSTRACIÓN NER - TYR")
    print("=" * 70)

    for i, texto in enumerate(casos_prueba, 1):
        print(f"\n[Caso {i}] {texto}")
        print("-" * 70)

        entidades = ner.extraer_entidades(texto)

        if entidades:
            print(ner.formatear_salida(entidades))
        else:
            print("  No se detectaron entidades.\n")
