"""
SESIÓN 5A: CLASE TYR - INTEGRACIÓN COMPLETA
Chatbot Inteligente para ITSE

Integra:
- Modelo BERT (clasificación de intenciones)
- Análisis VADER (sentimientos)
- Base de respuestas ITSE

Estudiante: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
"""

import torch
import json
import logging
import unicodedata
from typing import Dict, Tuple, Optional
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TYR:
    """
    TYR - Asistente Virtual ITSE

    Chatbot inteligente que combina:
    - BERT para clasificación de intenciones
    - VADER para análisis de sentimientos
    - Base de conocimiento ITSE

    Attributes:
        modelo: Modelo BERT fine-tuneado
        tokenizer: Tokenizer de BERT
        vader: Analizador de sentimientos VADER
        label_map: Mapeo de índices a nombres de intenciones
        respuestas_base: Diccionario con respuestas por intención
    """

    def __init__(
        self,
        modelo_path: str = "modelo_bert_tyr_4358",
        max_length: int = 128,
        device: Optional[str] = None
    ):
        """
        Inicializar chatbot TYR.

        Args:
            modelo_path: Ruta al directorio del modelo BERT entrenado
            max_length: Longitud máxima de tokens
            device: Dispositivo (cpu/cuda). Si None, detecta automáticamente
        """
        logger.info("Inicializando TYR - Asistente Virtual ITSE")

        # Configurar dispositivo
        if device is None:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.device = torch.device(device)

        logger.info(f"Dispositivo: {self.device}")

        # Parámetros
        self.max_length = max_length
        self.modelo_path = Path(modelo_path)

        # Cargar modelo y tokenizer
        self._cargar_modelo()

        # Inicializar VADER
        self.vader = SentimentIntensityAnalyzer()
        logger.info("VADER inicializado")

        # Cargar base de respuestas
        self._cargar_respuestas_base()

        logger.info("TYR inicializado correctamente")

    def _cargar_modelo(self):
        """Cargar modelo BERT y tokenizer."""
        try:
            # Cargar tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(str(self.modelo_path))
            logger.info("Tokenizer cargado")

            # Cargar label_map PRIMERO
            label_map_path = self.modelo_path / "label_map.json"
            if label_map_path.exists():
                with open(label_map_path, 'r', encoding='utf-8') as f:
                    label_data = json.load(f)
                    # Extraer id2label si existe, sino usar el diccionario completo
                    self.label_map = label_data.get("id2label", label_data)
                logger.info(f"Label map cargado: {len(self.label_map)} intenciones")
            else:
                # Label map por defecto (9 clases - SIN informacion_institucional)
                self.label_map = {
                    "0": "becas_financiamiento",
                    "1": "contacto_ubicacion",
                    "2": "faq_general",
                    "3": "fuera_dominio",
                    "4": "horarios_duracion",
                    "5": "informacion_carreras",
                    "6": "inscripcion_admision",
                    "7": "requisitos_ingreso",
                    "8": "saludo_despedida"
                }
                logger.warning("Label map no encontrado, usando valores por defecto")

            # Crear id2label y label2id
            id2label = {int(k): v for k, v in self.label_map.items()}
            label2id = {v: int(k) for k, v in self.label_map.items()}

            # Cargar modelo con labels EXPLÍCITOS
            # IMPORTANTE: NO pasar num_labels, id2label, label2id para forzar uso del config.json
            self.modelo = AutoModelForSequenceClassification.from_pretrained(
                str(self.modelo_path)
            )
            self.modelo.to(self.device)
            self.modelo.eval()
            logger.info(f"Modelo BERT cargado ({self.modelo.num_labels} clases)")

        except Exception as e:
            logger.error(f"Error cargando modelo: {e}")
            raise

    def _cargar_respuestas_base(self):
        """
        Cargar base de respuestas ITSE desde archivos JSON externos.

        Carga:
        - data/carreras_itse.json: Información de las 16 carreras
        - data/respuestas_base.json: Respuestas predefinidas por intención
        """
        # Cargar carreras desde JSON
        self.carreras_itse = self._cargar_carreras_desde_json()

        # Cargar respuestas base desde JSON
        self.respuestas_base = self._cargar_respuestas_desde_json()

        logger.info(f"Base de respuestas cargada: {len(self.respuestas_base)} intenciones")
        logger.info(f"Base de carreras ITSE cargada: {len(self.carreras_itse)} carreras")

    def _cargar_carreras_desde_json(self) -> Dict:
        """
        Cargar información de carreras desde archivo JSON.

        Returns:
            Dict con información de todas las carreras ITSE

        Raises:
            FileNotFoundError: Si no se encuentra el archivo
            json.JSONDecodeError: Si el JSON está mal formado
        """
        try:
            # Buscar archivo relativo a la ubicación de este script
            base_dir = Path(__file__).parent
            json_path = base_dir / "data" / "carreras_itse.json"

            if not json_path.exists():
                logger.warning(f"No se encontró {json_path}, usando base hardcodeada")
                return self._obtener_carreras_hardcodeadas()

            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Remover metadata si existe
            carreras = {k: v for k, v in data.items() if not k.startswith('_')}

            logger.info(f"Carreras cargadas desde JSON: {len(carreras)}")
            return carreras

        except Exception as e:
            logger.error(f"Error cargando carreras desde JSON: {e}")
            logger.warning("Usando base de carreras hardcodeada")
            return self._obtener_carreras_hardcodeadas()

    def _cargar_respuestas_desde_json(self) -> Dict:
        """
        Cargar respuestas base desde archivo JSON.

        Returns:
            Dict con respuestas predefinidas por intención

        Raises:
            FileNotFoundError: Si no se encuentra el archivo
            json.JSONDecodeError: Si el JSON está mal formado
        """
        try:
            # Buscar archivo relativo a la ubicación de este script
            base_dir = Path(__file__).parent
            json_path = base_dir / "data" / "respuestas_base.json"

            if not json_path.exists():
                logger.warning(f"No se encontró {json_path}, usando base hardcodeada")
                return self._obtener_respuestas_hardcodeadas()

            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Remover metadata si existe
            respuestas = {k: v for k, v in data.items() if not k.startswith('_')}

            logger.info(f"Respuestas base cargadas desde JSON: {len(respuestas)}")
            return respuestas

        except Exception as e:
            logger.error(f"Error cargando respuestas desde JSON: {e}")
            logger.warning("Usando base de respuestas hardcodeada")
            return self._obtener_respuestas_hardcodeadas()

    def _obtener_carreras_hardcodeadas(self) -> Dict:
        """
        Retorna base de conocimiento hardcodeada de carreras (fallback).

        Returns:
            Dict con información de las 16 carreras ITSE
        """
        return {
            # ESCUELA DE INNOVACIÓN DIGITAL (4 carreras)
            "desarrollo de software": {
                "nombre": "T.S. en Desarrollo de Software",
                "escuela": "Innovación Digital",
                "creditos": 112,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": "3 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Analizar, diseñar, programar e implementar aplicaciones usando Java, Python, C#, JavaScript. Frameworks ágiles (SCRUM, DevOps), bases de datos SQL/NoSQL, IA, cloud computing, IoT.",
                "campo_ocupacional": [
                    "Desarrollador Full-Stack, Back-end, Front-end",
                    "Programador junior",
                    "Desarrollador de aplicaciones",
                    "Evaluador o tester de software",
                    "Arquitecto de software",
                    "Líder/gestor de proyectos software",
                    "Analista de sistemas",
                    "Consultor tecnológico",
                    "Desarrollador de apps móviles",
                    "Programador web",
                    "Especialista integración y despliegue",
                    "Emprendedor en soluciones tecnológicas"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/ts-en-desarrollo-de-software"
            },
            "big data": {
                "nombre": "T.S. en Big Data y Ciencia de Datos",
                "escuela": "Innovación Digital",
                "creditos": 113,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": "3 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Analizar y gestionar grandes volúmenes de datos. Identificar patrones, generar visualizaciones, proponer soluciones basadas en datos para finanzas, salud, marketing, logística.",
                "campo_ocupacional": [
                    "Científico/a de Datos Junior",
                    "Analista de Datos",
                    "Desarrollador/a de Soluciones Big Data",
                    "Asistente en proyectos ciencia datos",
                    "Técnico/a procesamiento visualización",
                    "Consultor/a Big Data e IA",
                    "Gestor/a bases de datos en nube",
                    "Analista de negocios basado en datos",
                    "Profesional minería de datos"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-big-data"
            },
            "ciberseguridad": {
                "nombre": "T.S. en Ciberseguridad",
                "escuela": "Innovación Digital",
                "creditos": 122,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": "3 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Prevenir y detectar amenazas de seguridad. Recuperar incidentes, proteger datos y sistemas. Aplicar normativas, políticas y procedimientos de seguridad informática.",
                "campo_ocupacional": [
                    "Analista de seguridad informática",
                    "Administrador redes sistemas seguros",
                    "Auditor de ciberseguridad",
                    "Consultor seguridad informática",
                    "Ingeniero de seguridad",
                    "Especialista seguridad información",
                    "Penetration tester",
                    "Investigador forense digital",
                    "Especialista seguridad aplicaciones",
                    "Investigador ciberseguridad",
                    "Docente/formador ciberseguridad",
                    "Emprendedor servicios ciberseguridad"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-ciberseguridad"
            },
            "inteligencia artificial": {
                "nombre": "T.S. en Inteligencia Artificial",
                "escuela": "Innovación Digital",
                "creditos": 126,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": None},
                "jornadas": ["diurna"],
                "aprendizaje": "Analizar, diseñar, implementar y gestionar sistemas inteligentes. Desarrollar modelos machine learning, algoritmos IA. Monitorear y optimizar sistemas, análisis datos, soluciones IA éticas.",
                "campo_ocupacional": [
                    "Especialista sistemas inteligentes",
                    "Ingeniero IA junior",
                    "Científico datos especializado IA",
                    "Implementador soluciones IA",
                    "Consultor transformación digital",
                    "Desarrollador aplicaciones inteligentes",
                    "Especialista machine learning"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tsinteligenciaartificial"
            },

            # ESCUELA DE TECNOLOGÍA INDUSTRIAL (7 carreras)
            "electricidad industrial": {
                "nombre": "T.S. en Electricidad Industrial",
                "escuela": "Tecnología Industrial",
                "creditos": 135,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": None},
                "jornadas": ["diurna"],
                "aprendizaje": "Instalar, mantener y supervisar sistemas eléctricos industriales. Normas seguridad, diagnosticar fallas, interpretar planos, precisión con herramientas.",
                "campo_ocupacional": [
                    "Área mantenimiento producción industrial",
                    "Plantas distribución generación eléctrica",
                    "Constructoras e inmobiliarias",
                    "Empresas automatización control",
                    "Talleres reparación equipos eléctricos",
                    "Laboratorios pruebas eléctricas",
                    "Profesional independiente"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-electricidad"
            },
            "mantenimiento de aeronaves": {
                "nombre": "T.S. en Mantenimiento de Aeronaves",
                "escuela": "Tecnología Industrial",
                "creditos": 139,
                "duracion": {"diurna": "2 años 8 meses", "nocturna": None},
                "jornadas": ["diurna"],
                "aprendizaje": "Inspecciones, mantenimiento preventivo/correctivo. Reparación componentes estructurales, mecánicos, eléctricos. Estándares seguridad internacionales.",
                "campo_ocupacional": [
                    "Aerolíneas comerciales y carga",
                    "Centros mantenimiento reparación",
                    "Fabricantes aeronaves",
                    "Proveedores de partes",
                    "Aeropuertos servicios navegación",
                    "Aeronáutica Civil",
                    "Empresas arrendamiento aeronaves"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-mantenimiento-de-aeronaves"
            },
            "mantenimiento industrial": {
                "nombre": "T.S. en Mantenimiento Industrial",
                "escuela": "Tecnología Industrial",
                "creditos": 137,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": None},
                "jornadas": ["diurna"],
                "aprendizaje": "Identificar fallas, mantenimiento preventivo/correctivo/predictivo. Interpretar planos, herramientas especializadas, normas seguridad.",
                "campo_ocupacional": [
                    "Industrias manufactureras",
                    "Plantas producción",
                    "Constructoras",
                    "Empresas energéticas",
                    "Mantenimiento mecánico, eléctrico, electromecánico"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-mantenimiento-industrial"
            },
            "metalmecánicas": {
                "nombre": "T.S. en Tecnologías Metalmecánicas",
                "escuela": "Tecnología Industrial",
                "creditos": 138,
                "duracion": {"diurna": "2 años 4 meses", "nocturna": "2 años 4 meses"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Procesos mecanizado, soldadura, montaje, ajuste. Conformado elementos metálicos. Interpretar planos, maquinaria especializada, normas técnicas.",
                "campo_ocupacional": [
                    "Talleres industriales",
                    "Empresas metalmecánicas",
                    "Constructoras",
                    "Astilleros",
                    "Industrias manufactura mantenimiento"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-metalmecanicas"
            },
            "automotriz liviano": {
                "nombre": "T.S. en Tecnología Automotriz (Vehículos Livianos)",
                "escuela": "Tecnología Industrial",
                "creditos": 91,
                "duracion": {"diurna": "2 años", "nocturna": "2 años 8 meses"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Diagnósticos, reparación en sedanes, camionetas. Sistemas mecánicos, eléctricos, electrónicos. Herramientas escaneo, software especializado.",
                "campo_ocupacional": [
                    "Industrias automotrices",
                    "Distribuidoras automóviles",
                    "Talleres autorizados",
                    "Talleres aseguradoras",
                    "Empresas inspección técnica",
                    "Técnico automotriz independiente"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-automotriz-liviano"
            },
            "automotriz pesado": {
                "nombre": "T.S. en Tecnología Automotriz (Equipo Pesado)",
                "escuela": "Tecnología Industrial",
                "creditos": 87,
                "duracion": {"diurna": "2 años", "nocturna": "2 años 8 meses"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Mantenimiento vehículos pesados, tractores, equipos. Reparación especificaciones fabricantes. Sistemas mecánicos, eléctricos, electrónicos.",
                "campo_ocupacional": [
                    "Talleres mantenimiento reparación",
                    "Empresas transporte cargas",
                    "Industria minera, portuaria, construcción",
                    "Empresas alquiler maquinaria",
                    "Concesionarios servicios post-venta",
                    "Emprendimientos mantenimiento"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-tecnologia-automotriz-pesado"
            },
            "construcción": {
                "nombre": "T.S. en Construcción",
                "escuela": "Tecnología Industrial",
                "creditos": 94,
                "duracion": {"diurna": "2 años", "nocturna": "2 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Seguridad obra, lectura planos, selección materiales. Cálculo costos, presupuestos, planificación obras. Procesos ejecución, supervisión, control calidad.",
                "campo_ocupacional": [
                    "Asistente residente obra",
                    "Inspector campo",
                    "Estimador costos",
                    "Asistente planificación",
                    "Dibujante técnico",
                    "Técnico laboratorios materiales"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-construccion"
            },

            # ESCUELA DE NEGOCIOS (3 carreras)
            "gestión ejecutiva": {
                "nombre": "T.S. en Gestión Ejecutiva Bilingüe",
                "escuela": "Negocios",
                "creditos": 91,
                "duracion": {"diurna": "2 años", "nocturna": "3 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Asistencia altos mandos, administración, servicio cliente, contabilidad, RRHH, comercio internacional. Comunicación bilingüe español-inglés.",
                "campo_ocupacional": [
                    "Asistente ejecutivo bilingüe",
                    "Secretario/a ejecutivo/a",
                    "Coordinador/a administrativo/a",
                    "Asistente gerencia",
                    "Oficinista empresas internacionales",
                    "Asistente ONGs",
                    "Encargado apoyo logístico"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-gestion-ejecutiva"
            },
            "operaciones logísticas": {
                "nombre": "T.S. en Operaciones Logísticas",
                "escuela": "Negocios",
                "creditos": 90,
                "duracion": {"diurna": "2 años", "nocturna": "2 años 8 meses"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Planificar, ejecutar, optimizar procesos logísticos. Transporte, distribución, almacenamiento. Gestión documental internacional, equipos especializados.",
                "campo_ocupacional": [
                    "Asistente logístico",
                    "Coordinador operaciones",
                    "Supervisor almacén/bodega",
                    "Despachador mercancía",
                    "Analista transporte distribución",
                    "Auxiliar compras suministros",
                    "Gestor inventarios",
                    "Auxiliar agencias aduanales"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-operaciones-logisticas"
            },
            "servicios empresariales": {
                "nombre": "T.S. en Servicios Empresariales",
                "escuela": "Negocios",
                "creditos": 91,
                "duracion": {"diurna": "2 años", "nocturna": "2 años 8 meses"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Contabilidad, administración, RRHH, mercadeo, servicio cliente. Gestionar procesos comerciales, elaborar informes, sistemas gestión integral.",
                "campo_ocupacional": [
                    "Asistente administrativo",
                    "Gestor operaciones organizacionales",
                    "Auxiliar contable",
                    "Asistente financiero",
                    "Apoyo estudios mercado",
                    "Asistente proyectos empresariales",
                    "Colaborador planes estratégicos"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-servicios-especiales"
            },

            # ESCUELA DE HOSPITALIDAD Y TURISMO (2 carreras)
            "artes culinarias": {
                "nombre": "T.S. en Artes Culinarias",
                "escuela": "Hospitalidad y Turismo",
                "creditos": 91,
                "duracion": {"diurna": "2 años", "nocturna": "3 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Técnicas culinarias profesionales, gastronomía nacional e internacional, gestión de cocina.",
                "campo_ocupacional": [
                    "Chef profesional",
                    "Cocinero en hoteles y restaurantes",
                    "Gestor de servicios de alimentación",
                    "Emprendedor gastronómico"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica"
            },
            "operaciones hoteleras": {
                "nombre": "T.S. en Operaciones Hoteleras",
                "escuela": "Hospitalidad y Turismo",
                "creditos": 93,
                "duracion": {"diurna": "2 años", "nocturna": "3 años"},
                "jornadas": ["diurna", "nocturna"],
                "aprendizaje": "Gestión hotelera, servicio al cliente de excelencia, operaciones de alojamiento, administración turística.",
                "campo_ocupacional": [
                    "Gestor hotelero",
                    "Coordinador de operaciones hoteleras",
                    "Supervisor de servicios de alojamiento",
                    "Profesional en turismo"
                ],
                "enlace": "https://www.itse.ac.pa/oferta-academica"
            }
        }

        self.respuestas_base = {
            "becas_financiamiento": {
                "respuesta": (
                    "💰 **Becas y Financiamiento en ITSE:**\n\n"
                    "ITSE ofrece varias opciones de ayuda económica:\n\n"
                    "• **IFARHU-SENACYT**: Becas para carreras tecnológicas\n"
                    "• **BID (Banco Interamericano de Desarrollo)**: Financiamiento para estudiantes destacados\n"
                    "• **Alianzas empresariales**: Convenios con empresas del sector tecnológico\n"
                    "• **Planes de pago**: Opciones flexibles de financiamiento institucional\n\n"
                    "📞 Para más información sobre becas:\n"
                    "Teléfono: +507 524-3333\n"
                    "Email: becas@itse.ac.pa"
                ),
                "keywords": ["becas", "financiamiento", "ayuda económica", "IFARHU", "BID"]
            },

            "contacto_ubicacion": {
                "respuesta": (
                    "📍 **Contacto e Información ITSE:**\n\n"
                    "📞 **Teléfono:** +507 524-3333\n"
                    "📧 **Email:** info@itse.ac.pa\n"
                    "🌐 **Web:** www.itse.ac.pa\n\n"
                    "📍 **Ubicación:**\n"
                    "Avenida Domingo Díaz, Tocumen\n"
                    "Panamá, República de Panamá\n\n"
                    "🕐 **Horario de Atención:**\n"
                    "Lunes a Viernes: 8:00 AM - 8:00 PM\n"
                    "Sábados: 8:00 AM - 12:00 PM"
                ),
                "keywords": ["contacto", "teléfono", "email", "ubicación", "dirección"]
            },

            "faq_general": {
                "respuesta": (
                    "❓ **Preguntas Frecuentes sobre ITSE:**\n\n"
                    "📊 **Datos clave:**\n"
                    "• Más de 4,000 estudiantes activos\n"
                    "• 80% inserción laboral de egresados (2025)\n"
                    "• Metodología 70% práctica, 30% teórica\n"
                    "• Certificación técnica reconocida nacionalmente\n\n"
                    "🏆 **Reconocimientos Internacionales:**\n"
                    "• Foro Económico Mundial: 1 de 8 casos de éxito mundial en ciberseguridad\n"
                    "• Unión Europea: Caso de éxito en vinculación academia-sector productivo (Global Gateway)\n"
                    "• Hackathon Internacional de Logística 2025: 1er y 3er lugar\n\n"
                    "🤝 **Alianzas Estratégicas:**\n"
                    "• Canal de Panamá - Formación en logística y operaciones\n"
                    "• Copa Airlines - Especialización en aviación y mantenimiento\n"
                    "• 15 empresas europeas validan nuestro modelo educativo\n\n"
                    "🏫 **Servicios Especiales:**\n"
                    "• CAIPI: Centro de atención integral para hijos/as de estudiantes (guardería, salud, nutrición)\n"
                    "• CIIECYT: Centro de Investigación e Innovación en Ciencia y Tecnología\n"
                    "• Laboratorios de tecnología de punta\n"
                    "• Profesores con experiencia profesional activa\n"
                    "• Pasantías en empresas líderes del sector\n"
                    "• Bolsa de trabajo exclusiva para egresados\n\n"
                    "¿Tienes alguna pregunta específica sobre ITSE?"
                ),
                "keywords": ["información", "datos", "estadísticas", "general", "sobre ITSE", "caipi", "ciiecyt", "reconocimientos", "alianzas", "guardería"]
            },

            "fuera_dominio": {
                "respuesta": (
                    "🤖 **Lo siento, no puedo ayudarte con esa consulta.**\n\n"
                    "Estoy diseñado específicamente para responder preguntas sobre:\n\n"
                    "✓ Carreras y programas académicos de ITSE\n"
                    "✓ Proceso de inscripción y admisión\n"
                    "✓ Requisitos de ingreso\n"
                    "✓ Becas y financiamiento\n"
                    "✓ Horarios y duración de carreras\n"
                    "✓ Información de contacto y ubicación\n"
                    "✓ Preguntas generales sobre ITSE\n\n"
                    "Por favor, reformula tu pregunta relacionada con ITSE o "
                    "contacta directamente a info@itse.ac.pa para consultas específicas."
                ),
                "keywords": ["fuera", "otro tema", "no relacionado"]
            },

            "horarios_duracion": {
                "respuesta": (
                    "⏰ **Horarios y Duración de Carreras ITSE:**\n\n"
                    "**Jornada Diurna:**\n"
                    "• Duración: 2 años (6 cuatrimestres)\n"
                    "• Horario: Lunes a Viernes, 8:00 AM - 2:00 PM\n"
                    "• Modalidad intensiva\n\n"
                    "**Jornada Nocturna:**\n"
                    "• Duración: 3 años (9 cuatrimestres)\n"
                    "• Horario: Lunes a Viernes, 6:00 PM - 10:00 PM\n"
                    "• Ideal para personas que trabajan\n\n"
                    "**Sábados (algunas carreras):**\n"
                    "• Horario: 8:00 AM - 4:00 PM\n"
                    "• Consultar disponibilidad por carrera\n\n"
                    "📞 Para horarios específicos de tu carrera de interés: +507 524-3333"
                ),
                "keywords": ["horarios", "duración", "tiempo", "cuánto dura", "jornada"]
            },

            "informacion_carreras": {
                "respuesta": (
                    "🎓 **Carreras Disponibles en ITSE:**\n\n"
                    "**Escuela de Innovación Digital:**\n"
                    "• T.S. en Desarrollo de Software\n"
                    "• T.S. en Big Data y Ciencia de Datos\n"
                    "• T.S. en Ciberseguridad\n"
                    "• T.S. en Inteligencia Artificial\n\n"
                    "**Escuela de Tecnología Industrial:**\n"
                    "• T.S. en Tecnología Automotriz de Vehículo Liviano\n"
                    "• T.S. en Construcción\n"
                    "• T.S. en Electricidad Industrial\n"
                    "• T.S. en Mantenimiento de Aeronaves\n"
                    "• T.S. en Mantenimiento Industrial\n"
                    "• T.S. en Tecnologías Metalmecánicas\n"
                    "• T.S. en Tecnología Automotriz de Equipo Pesado\n\n"
                    "**Escuela de Hospitalidad y Turismo:**\n"
                    "• T.S. en Artes Culinarias\n"
                    "• T.S. en Operaciones Hoteleras\n\n"
                    "**Escuela de Negocios:**\n"
                    "• T.S. en Gestión Ejecutiva Bilingüe\n"
                    "• T.S. en Operaciones Logísticas\n"
                    "• T.S. en Servicios Empresariales\n\n"
                    "📚 Todas las carreras son Técnico Superior (T.S.) con:\n"
                    "✓ Certificación técnica oficial\n"
                    "✓ Prácticas empresariales\n"
                    "✓ Metodología 70% práctica\n\n"
                    "Más información: https://www.itse.ac.pa/oferta-academica\n\n"
                    "¿Te interesa alguna carrera en específico?"
                ),
                "keywords": ["carreras", "programas", "técnicas", "estudios", "qué ofrece"]
            },

            "inscripcion_admision": {
                "respuesta": (
                    "📝 **Proceso de Inscripción y Admisión ITSE:**\n\n"
                    "**Fase 1: Pre-inscripción**\n"
                    "• Completar formulario en línea: www.itse.ac.pa/inscripcion\n"
                    "• Subir documentos escaneados\n"
                    "• Seleccionar carrera de interés\n\n"
                    "**Fase 2: Evaluación**\n"
                    "• Prueba PIENSE II (obligatoria)\n"
                    "• Entrevista personal (algunas carreras)\n"
                    "• Revisión de expediente académico\n\n"
                    "**Fase 3: Matrícula**\n"
                    "• Presentar documentos originales\n"
                    "• Pago de matrícula\n"
                    "• Asignación de horario\n"
                    "• Recibir credencial estudiantil\n\n"
                    "📅 **Fechas importantes:**\n"
                    "• Inscripciones: Enero, Mayo, Septiembre\n"
                    "• Inicio de clases: Febrero, Junio, Octubre\n\n"
                    "📞 Más información: +507 524-3333 ext. 102"
                ),
                "keywords": ["inscripción", "admisión", "matricula", "aplicar", "proceso"]
            },

            "requisitos_ingreso": {
                "respuesta": (
                    "📄 **Requisitos de Ingreso a ITSE:**\n\n"
                    "**Documentos Obligatorios:**\n"
                    "1. Diploma de Bachiller (original y copia)\n"
                    "2. Certificado de notas de secundaria\n"
                    "3. Copia de cédula (legible)\n"
                    "4. 2 fotos tamaño carnet\n"
                    "5. Certificado de salud\n"
                    "6. Certificado de buena conducta (Policía Nacional)\n\n"
                    "**Requisitos Académicos:**\n"
                    "• Aprobar prueba PIENSE II (mínimo 800 puntos)\n"
                    "• Promedio mínimo de 2.5 en secundaria\n"
                    "• Conocimientos básicos de matemáticas y comprensión lectora\n\n"
                    "**Requisitos Adicionales (según carrera):**\n"
                    "• Algunas carreras requieren portfolio o prueba específica\n"
                    "• Carreras técnicas: conocimientos básicos en el área\n\n"
                    "💡 **Importante:**\n"
                    "La prueba PIENSE II se programa durante el proceso de inscripción.\n\n"
                    "📞 Consultas: +507 524-3333"
                ),
                "keywords": ["requisitos", "documentos", "necesito", "PIENSE", "diploma"]
            },

            "saludo_despedida": {
                "respuesta": (
                    "👋 ¡Hola! Soy TYR, el asistente virtual de ITSE.\n\n"
                    "Estoy aquí para ayudarte con información sobre:\n"
                    "• Carreras y programas académicos\n"
                    "• Proceso de inscripción\n"
                    "• Becas y financiamiento\n"
                    "• Horarios y contacto\n\n"
                    "¿En qué puedo ayudarte hoy? 😊"
                ),
                "keywords": ["hola", "saludos", "buenos días", "gracias", "adiós"]
            }
        }

        logger.info(f"Base de respuestas cargada: {len(self.respuestas_base)} intenciones")
        logger.info(f"Base de carreras ITSE cargada: {len(self.carreras_itse)} carreras")

    def _obtener_respuestas_hardcodeadas(self) -> Dict:
        """
        Retorna base de respuestas hardcodeadas (fallback).

        Returns:
            Dict con respuestas predefinidas por intención
        """
        return {
            "becas_financiamiento": {
                "respuesta": (
                    "💰 **Becas y Financiamiento en ITSE:**\n\n"
                    "ITSE ofrece varias opciones de ayuda económica:\n\n"
                    "• **IFARHU-SENACYT**: Becas para carreras tecnológicas\n"
                    "• **BID (Banco Interamericano de Desarrollo)**: Financiamiento para estudiantes destacados\n"
                    "• **Alianzas empresariales**: Convenios con empresas del sector tecnológico\n"
                    "• **Planes de pago**: Opciones flexibles de financiamiento institucional\n\n"
                    "📞 Para más información sobre becas:\n"
                    "Teléfono: +507 524-3333\n"
                    "Email: becas@itse.ac.pa"
                ),
                "keywords": ["becas", "financiamiento", "ayuda económica", "IFARHU", "BID"]
            },

            "contacto_ubicacion": {
                "respuesta": (
                    "📍 **Contacto e Información ITSE:**\n\n"
                    "📞 **Teléfono:** +507 524-3333\n"
                    "📧 **Email:** info@itse.ac.pa\n"
                    "🌐 **Web:** www.itse.ac.pa\n\n"
                    "📍 **Ubicación:**\n"
                    "Avenida Domingo Díaz, Tocumen\n"
                    "Panamá, República de Panamá\n\n"
                    "🕐 **Horario de Atención:**\n"
                    "Lunes a Viernes: 8:00 AM - 8:00 PM\n"
                    "Sábados: 8:00 AM - 12:00 PM"
                ),
                "keywords": ["contacto", "teléfono", "email", "ubicación", "dirección"]
            },

            "faq_general": {
                "respuesta": (
                    "❓ **Preguntas Frecuentes sobre ITSE:**\n\n"
                    "📊 **Datos clave:**\n"
                    "• Más de 4,000 estudiantes activos\n"
                    "• 80% inserción laboral de egresados (2025)\n"
                    "• Metodología 70% práctica, 30% teórica\n"
                    "• Certificación técnica reconocida nacionalmente\n\n"
                    "🏆 **Reconocimientos Internacionales:**\n"
                    "• Foro Económico Mundial: 1 de 8 casos de éxito mundial en ciberseguridad\n"
                    "• Unión Europea: Caso de éxito en vinculación academia-sector productivo (Global Gateway)\n"
                    "• Hackathon Internacional de Logística 2025: 1er y 3er lugar\n\n"
                    "🤝 **Alianzas Estratégicas:**\n"
                    "• Canal de Panamá - Formación en logística y operaciones\n"
                    "• Copa Airlines - Especialización en aviación y mantenimiento\n"
                    "• 15 empresas europeas validan nuestro modelo educativo\n\n"
                    "🏫 **Servicios Especiales:**\n"
                    "• CAIPI: Centro de atención integral para hijos/as de estudiantes (guardería, salud, nutrición)\n"
                    "• CIIECYT: Centro de Investigación e Innovación en Ciencia y Tecnología\n"
                    "• Laboratorios de tecnología de punta\n"
                    "• Profesores con experiencia profesional activa\n"
                    "• Pasantías en empresas líderes del sector\n"
                    "• Bolsa de trabajo exclusiva para egresados\n\n"
                    "¿Tienes alguna pregunta específica sobre ITSE?"
                ),
                "keywords": ["información", "datos", "estadísticas", "general", "sobre ITSE", "caipi", "ciiecyt", "reconocimientos", "alianzas", "guardería"]
            },

            "fuera_dominio": {
                "respuesta": (
                    "🤖 **Lo siento, no puedo ayudarte con esa consulta.**\n\n"
                    "Estoy diseñado específicamente para responder preguntas sobre:\n\n"
                    "✓ Carreras y programas académicos de ITSE\n"
                    "✓ Proceso de inscripción y admisión\n"
                    "✓ Requisitos de ingreso\n"
                    "✓ Becas y financiamiento\n"
                    "✓ Horarios y duración de carreras\n"
                    "✓ Información de contacto y ubicación\n"
                    "✓ Preguntas generales sobre ITSE\n\n"
                    "Por favor, reformula tu pregunta relacionada con ITSE o "
                    "contacta directamente a info@itse.ac.pa para consultas específicas."
                ),
                "keywords": ["fuera", "otro tema", "no relacionado"]
            },

            "horarios_duracion": {
                "respuesta": (
                    "⏰ **Horarios y Duración de Carreras ITSE:**\n\n"
                    "**Jornada Diurna:**\n"
                    "• Duración: 2 años (6 cuatrimestres)\n"
                    "• Horario: Lunes a Viernes, 8:00 AM - 2:00 PM\n"
                    "• Modalidad intensiva\n\n"
                    "**Jornada Nocturna:**\n"
                    "• Duración: 3 años (9 cuatrimestres)\n"
                    "• Horario: Lunes a Viernes, 6:00 PM - 10:00 PM\n"
                    "• Ideal para personas que trabajan\n\n"
                    "**Sábados (algunas carreras):**\n"
                    "• Horario: 8:00 AM - 4:00 PM\n"
                    "• Consultar disponibilidad por carrera\n\n"
                    "📞 Para horarios específicos de tu carrera de interés: +507 524-3333"
                ),
                "keywords": ["horarios", "duración", "tiempo", "cuánto dura", "jornada"]
            },

            "informacion_carreras": {
                "respuesta": (
                    "🎓 **Carreras Disponibles en ITSE:**\n\n"
                    "**Escuela de Innovación Digital:**\n"
                    "• T.S. en Desarrollo de Software\n"
                    "• T.S. en Big Data y Ciencia de Datos\n"
                    "• T.S. en Ciberseguridad\n"
                    "• T.S. en Inteligencia Artificial\n\n"
                    "**Escuela de Tecnología Industrial:**\n"
                    "• T.S. en Tecnología Automotriz de Vehículo Liviano\n"
                    "• T.S. en Construcción\n"
                    "• T.S. en Electricidad Industrial\n"
                    "• T.S. en Mantenimiento de Aeronaves\n"
                    "• T.S. en Mantenimiento Industrial\n"
                    "• T.S. en Tecnologías Metalmecánicas\n"
                    "• T.S. en Tecnología Automotriz de Equipo Pesado\n\n"
                    "**Escuela de Hospitalidad y Turismo:**\n"
                    "• T.S. en Artes Culinarias\n"
                    "• T.S. en Operaciones Hoteleras\n\n"
                    "**Escuela de Negocios:**\n"
                    "• T.S. en Gestión Ejecutiva Bilingüe\n"
                    "• T.S. en Operaciones Logísticas\n"
                    "• T.S. en Servicios Empresariales\n\n"
                    "📚 Todas las carreras son Técnico Superior (T.S.) con:\n"
                    "✓ Certificación técnica oficial\n"
                    "✓ Prácticas empresariales\n"
                    "✓ Metodología 70% práctica\n\n"
                    "Más información: https://www.itse.ac.pa/oferta-academica\n\n"
                    "¿Te interesa alguna carrera en específico?"
                ),
                "keywords": ["carreras", "programas", "técnicas", "estudios", "qué ofrece"]
            },

            "inscripcion_admision": {
                "respuesta": (
                    "📝 **Proceso de Inscripción y Admisión ITSE:**\n\n"
                    "**Fase 1: Pre-inscripción**\n"
                    "• Completar formulario en línea: www.itse.ac.pa/inscripcion\n"
                    "• Subir documentos escaneados\n"
                    "• Seleccionar carrera de interés\n\n"
                    "**Fase 2: Evaluación**\n"
                    "• Prueba PIENSE II (obligatoria)\n"
                    "• Entrevista personal (algunas carreras)\n"
                    "• Revisión de expediente académico\n\n"
                    "**Fase 3: Matrícula**\n"
                    "• Presentar documentos originales\n"
                    "• Pago de matrícula\n"
                    "• Asignación de horario\n"
                    "• Recibir credencial estudiantil\n\n"
                    "📅 **Fechas importantes:**\n"
                    "• Inscripciones: Enero, Mayo, Septiembre\n"
                    "• Inicio de clases: Febrero, Junio, Octubre\n\n"
                    "📞 Más información: +507 524-3333 ext. 102"
                ),
                "keywords": ["inscripción", "admisión", "matricula", "aplicar", "proceso"]
            },

            "requisitos_ingreso": {
                "respuesta": (
                    "📄 **Requisitos de Ingreso a ITSE:**\n\n"
                    "**Documentos Obligatorios:**\n"
                    "1. Diploma de Bachiller (original y copia)\n"
                    "2. Certificado de notas de secundaria\n"
                    "3. Copia de cédula (legible)\n"
                    "4. 2 fotos tamaño carnet\n"
                    "5. Certificado de salud\n"
                    "6. Certificado de buena conducta (Policía Nacional)\n\n"
                    "**Requisitos Académicos:**\n"
                    "• Aprobar prueba PIENSE II (mínimo 800 puntos)\n"
                    "• Promedio mínimo de 2.5 en secundaria\n"
                    "• Conocimientos básicos de matemáticas y comprensión lectora\n\n"
                    "**Requisitos Adicionales (según carrera):**\n"
                    "• Algunas carreras requieren portfolio o prueba específica\n"
                    "• Carreras técnicas: conocimientos básicos en el área\n\n"
                    "💡 **Importante:**\n"
                    "La prueba PIENSE II se programa durante el proceso de inscripción.\n\n"
                    "📞 Consultas: +507 524-3333"
                ),
                "keywords": ["requisitos", "documentos", "necesito", "PIENSE", "diploma"]
            },

            "saludo_despedida": {
                "respuesta": (
                    "👋 ¡Hola! Soy TYR, el asistente virtual de ITSE.\n\n"
                    "Estoy aquí para ayudarte con información sobre:\n"
                    "• Carreras y programas académicos\n"
                    "• Proceso de inscripción\n"
                    "• Becas y financiamiento\n"
                    "• Horarios y contacto\n\n"
                    "¿En qué puedo ayudarte hoy? 😊"
                ),
                "keywords": ["hola", "saludos", "buenos días", "gracias", "adiós"]
            }
        }

    def procesar_entrada(self, texto: str) -> str:
        """
        Preprocesar entrada del usuario.

        Normaliza el texto para ser más tolerante con:
        - Tildes/acentos (café = cafe)
        - Mayúsculas/minúsculas (HOLA = hola)
        - Espacios múltiples
        - Caracteres especiales

        Args:
            texto: Texto ingresado por el usuario

        Returns:
            Texto limpio y normalizado
        """
        # Limpieza básica
        texto = texto.strip()

        # Normalizar espacios múltiples
        texto = " ".join(texto.split())

        # IMPORTANTE: NO convertir a minúsculas ni eliminar tildes/acentos
        # El modelo fue entrenado con texto original que incluye mayúsculas y acentos
        # Cualquier preprocesamiento que altere esto causará predicciones incorrectas

        return texto

    def clasificar_intencion(
        self,
        texto: str,
        threshold: float = 0.7
    ) -> Tuple[str, float, Dict[str, float]]:
        """
        Clasificar intención del texto usando BERT.

        Args:
            texto: Texto a clasificar
            threshold: Umbral de confianza mínimo

        Returns:
            (intencion, confianza, probabilidades_todas)
        """
        try:
            # Tokenizar
            inputs = self.tokenizer(
                texto,
                return_tensors="pt",
                max_length=self.max_length,
                padding="max_length",
                truncation=True
            )

            # Mover a dispositivo
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # Inferencia
            with torch.no_grad():
                outputs = self.modelo(**inputs)
                logits = outputs.logits
                probs = torch.softmax(logits, dim=1)[0]

            # Obtener predicción
            pred_idx = torch.argmax(probs).item()
            confianza = probs[pred_idx].item()

            # Obtener nombre de intención
            intencion = self.label_map.get(str(pred_idx), "desconocida")

            # Si confianza baja, marcar como fuera_dominio
            if confianza < threshold:
                intencion = "fuera_dominio"
                logger.warning(f"Baja confianza ({confianza:.2f}), clasificado como fuera_dominio")

            # Probabilidades de todas las clases
            todas_probs = {
                self.label_map.get(str(i), f"clase_{i}"): probs[i].item()
                for i in range(len(probs))
            }

            logger.info(f"Intención: {intencion} (confianza: {confianza:.2%})")

            return intencion, confianza, todas_probs

        except Exception as e:
            logger.error(f"Error en clasificación: {e}")
            return "fuera_dominio", 0.0, {}

    def analizar_sentimiento(self, texto: str) -> Dict[str, float]:
        """
        Analizar sentimiento del texto usando VADER.

        Args:
            texto: Texto a analizar

        Returns:
            Diccionario con scores de sentimiento
        """
        try:
            scores = self.vader.polarity_scores(texto)

            # Determinar sentimiento categórico
            compound = scores['compound']
            if compound >= 0.05:
                sentimiento_cat = "positivo"
            elif compound <= -0.05:
                sentimiento_cat = "negativo"
            else:
                sentimiento_cat = "neutro"

            resultado = {
                "compound": compound,
                "positive": scores['pos'],
                "negative": scores['neg'],
                "neutral": scores['neu'],
                "categoria": sentimiento_cat
            }

            logger.debug(f"Sentimiento: {sentimiento_cat} (compound: {compound:.3f})")

            return resultado

        except Exception as e:
            logger.error(f"Error en análisis de sentimiento: {e}")
            return {
                "compound": 0.0,
                "positive": 0.0,
                "negative": 0.0,
                "neutral": 1.0,
                "categoria": "neutro"
            }

    def buscar_carrera_en_texto(self, texto: str) -> Optional[Dict]:
        """
        Buscar si el texto menciona alguna carrera específica.

        Args:
            texto: Texto del usuario

        Returns:
            Información de la carrera si se encuentra, None si no
        """
        texto_lower = " " + texto.lower() + " "  # Agregar espacios para búsqueda de palabras completas

        # Palabras clave por carrera (expandidas para mejor detección)
        keywords_carreras = {
            "desarrollo de software": ["desarrollo de software", "desarrollo", "software", "programación", "programador", "desarrollo web", "apps", "aplicaciones"],
            "big data": ["big data", "bigdata", "datos", "data", "ciencia de datos", "científico de datos", "analista de datos", "data science"],
            "ciberseguridad": ["ciberseguridad", "ciber seguridad", "seguridad informática", "seguridad", "hacker", "hacking ético", "pentesting"],
            "inteligencia artificial": ["inteligencia artificial", " ia ", " ai ", "machine learning", "aprendizaje automático", "deep learning", "redes neuronales"],
            "electricidad industrial": ["electricidad industrial", "electricidad", "eléctrica", "electricista", "sistemas eléctricos"],
            "mantenimiento de aeronaves": ["mantenimiento de aeronaves", "aeronaves", "aviones", "aviación", "aeronáutica", "mantenimiento aeronáutico"],
            "mantenimiento industrial": ["mantenimiento industrial", "mantenimiento", "mecánica industrial"],
            "metalmecánicas": ["metalmecánica", "metalmecánicas", "soldadura", "mecánica", "mecanizado", "metalurgia"],
            "automotriz liviano": ["automotriz liviano", "automotriz", "vehículos livianos", "carros", "automóviles", "mecánica automotriz"],
            "automotriz pesado": ["automotriz pesado", "equipo pesado", "maquinaria pesada", "vehículos pesados", "tractores"],
            "construcción": ["construcción", "obras", "edificación", "obras civiles", "ingeniero constructor"],
            "gestión ejecutiva": ["gestión ejecutiva", "ejecutiva", "secretariado", "bilingüe", "asistente ejecutivo", "secretaria"],
            "operaciones logísticas": ["logística", "operaciones logísticas", "supply chain", "cadena de suministro", "almacén"],
            "servicios empresariales": ["servicios empresariales", "administración", "negocios", "gestión empresarial"],
            "artes culinarias": ["culinaria", "culinarias", "cocina", "chef", "gastronomía", "artes culinarias", "cocinero"],
            "operaciones hoteleras": ["hotel", "hotelera", "hotelería", "turismo", "operaciones hoteleras", "hospitalidad"]
        }

        # Buscar coincidencias
        for carrera_key, keywords in keywords_carreras.items():
            for keyword in keywords:
                if keyword in texto_lower:
                    return self.carreras_itse.get(carrera_key)

        return None

    def buscar_info_especifica_faq(self, texto: str) -> Optional[str]:
        """
        Buscar si el usuario pregunta por información específica dentro de FAQ.

        Args:
            texto: Texto del usuario

        Returns:
            Respuesta específica si se encuentra, None si no
        """
        texto_lower = texto.lower()

        # Keywords para información específica
        if any(word in texto_lower for word in ["caipi", "guarderia", "guardería", "hijos", "primera infancia"]):
            return (
                "🏫 **CAIPI - Centro de Atención Integral a la Primera Infancia**\n\n"
                "El ITSE cuenta con un centro especial que promueve equidad educativa:\n\n"
                "**Servicios que ofrece:**\n"
                "• Guardería con servicios educativos de calidad para hijos/as de estudiantes\n"
                "• Salud preventiva y atención médica\n"
                "• Nutrición balanceada durante la jornada\n"
                "• Acompañamiento psicosocial\n\n"
                "**Objetivo:**\n"
                "Permitir que estudiantes con responsabilidades familiares alcancen sus metas académicas "
                "en un entorno seguro y enriquecedor para sus hijos/as.\n\n"
                "📞 Para más información: +507 524-3333"
            )

        if any(word in texto_lower for word in ["ciiecyt", "investigación", "investigacion", "innovación", "innovacion", "investigar"]):
            return (
                "🔬 **CIIECYT - Centro de Investigación e Innovación Educativa, Ciencia y Tecnología**\n\n"
                "Centro que impulsa proyectos de innovación y emprendimiento, fortaleciendo la misión "
                "de contribuir a un Panamá más justo y competitivo.\n\n"
                "**Actividades:**\n"
                "• Proyectos de investigación aplicada\n"
                "• Desarrollo de innovaciones tecnológicas\n"
                "• Apoyo a emprendimientos estudiantiles\n"
                "• Vinculación con sector productivo\n\n"
                "📞 Para más información: +507 524-3333"
            )

        if any(word in texto_lower for word in ["reconocimiento", "premio", "galardón", "logro", "éxito", "foro económico", "unión europea"]):
            return (
                "🏆 **Reconocimientos Internacionales del ITSE**\n\n"
                "**Foro Económico Mundial:**\n"
                "• ITSE es uno de **8 casos de éxito mundial** en ciberseguridad y "
                "alianzas público-privadas\n\n"
                "**Unión Europea:**\n"
                "• Distinguido como **caso de éxito en vinculación academia-sector productivo** "
                "dentro de la estrategia Global Gateway en Transición Digital\n\n"
                "**Hackathon Internacional de Logística 2025:**\n"
                "• 1er lugar: Estudiantes ITSE ganaron el primer puesto 🥇\n"
                "• 3er lugar: Otro equipo ITSE logró el tercer puesto 🥉\n\n"
                "Estos reconocimientos validan la calidad educativa y el impacto del ITSE a nivel mundial."
            )

        if any(word in texto_lower for word in ["alianza", "convenio", "empresa", "canal de panamá", "canal", "copa airlines", "copa", "socio"]):
            return (
                "🤝 **Alianzas Estratégicas del ITSE**\n\n"
                "El ITSE mantiene alianzas clave con empresas líderes:\n\n"
                "**Canal de Panamá:**\n"
                "• Formación especializada en logística y operaciones portuarias\n"
                "• Prácticas profesionales en instalaciones del Canal\n"
                "• Inserción laboral directa\n\n"
                "**Copa Airlines:**\n"
                "• Especialización en aviación y mantenimiento de aeronaves\n"
                "• Capacitación con estándares internacionales\n"
                "• Oportunidades de empleo\n\n"
                "**15 Empresas Europeas:**\n"
                "• Validación del modelo educativo ITSE\n"
                "• Intercambios y capacitaciones\n\n"
                "**Sector Privado Panameño:**\n"
                "• Vinculación directa a empleabilidad\n"
                "• Pasantías garantizadas\n"
                "• Bolsa de trabajo exclusiva\n\n"
                "📊 Resultado: **80% de inserción laboral** de egresados (2025)"
            )

        if any(word in texto_lower for word in ["inserción laboral", "insercion laboral", "empleo", "trabajo", "empleabilidad", "graduados"]):
            return (
                "💼 **Indicadores de Éxito ITSE (2025)**\n\n"
                "**Inserción Laboral:**\n"
                "• **80% de egresados** se insertan exitosamente en el mercado laboral\n"
                "• **10% de egresados** emprenden negocios propios\n"
                "• **10% de egresados** continúan estudios superiores\n\n"
                "**Matrícula y Crecimiento:**\n"
                "• Más de **4,000 estudiantes activos**\n"
                "• Escuela de Innovación Digital: **800+ estudiantes**\n"
                "• Más del **50% mujeres** en Innovación Digital\n"
                "• **60% crecimiento anual** en matrícula\n\n"
                "**Graduados 2025:**\n"
                "• **276 estudiantes** (IV promoción)\n"
                "• Ocupación del campus: **97%**\n\n"
                "Estas cifras demuestran el compromiso del ITSE con la empleabilidad y el éxito profesional."
            )

        return None

    def formatear_info_carrera(self, carrera: Dict) -> str:
        """
        Formatear información detallada de una carrera.

        Args:
            carrera: Diccionario con información de la carrera

        Returns:
            Texto formateado con toda la información
        """
        # Construir respuesta detallada
        respuesta = f"🎓 **{carrera['nombre']}**\n\n"
        respuesta += f"**Escuela:** {carrera['escuela']}\n\n"

        # Duración y jornadas
        respuesta += "⏰ **Duración:**\n"
        if carrera['duracion']['diurna']:
            respuesta += f"• Jornada Diurna: {carrera['duracion']['diurna']}\n"
        if carrera['duracion']['nocturna']:
            respuesta += f"• Jornada Nocturna: {carrera['duracion']['nocturna']}\n"
        else:
            respuesta += f"• Solo disponible en jornada diurna\n"
        respuesta += f"• Total: {carrera['creditos']} créditos\n\n"

        # Qué aprenderás
        respuesta += "📚 **¿Qué aprenderás?**\n"
        respuesta += f"{carrera['aprendizaje']}\n\n"

        # Campo ocupacional
        respuesta += "💼 **Campo Ocupacional:**\n"
        for campo in carrera['campo_ocupacional'][:5]:  # Mostrar primeros 5
            respuesta += f"• {campo}\n"
        if len(carrera['campo_ocupacional']) > 5:
            respuesta += f"• ...y {len(carrera['campo_ocupacional']) - 5} opciones más\n"

        # Enlace directo
        respuesta += f"\n🔗 **Más información:** {carrera['enlace']}\n\n"
        respuesta += "¿Te gustaría saber sobre el proceso de inscripción o requisitos?"

        return respuesta

    def generar_respuesta(
        self,
        intencion: str,
        sentimiento: Dict[str, float],
        texto_original: str = ""
    ) -> str:
        """
        Generar respuesta basada en intención y sentimiento.

        Args:
            intencion: Intención detectada
            sentimiento: Análisis de sentimiento
            texto_original: Texto original del usuario (para búsqueda de carreras)

        Returns:
            Respuesta del chatbot
        """
        # PRIORIDAD 1: Buscar si pregunta por carrera específica (SIEMPRE, sin importar intención)
        # Esto corrige casos donde BERT clasifica mal (ej: "Cuéntame sobre Big Data" → fuera_dominio)
        if texto_original:
            carrera_info = self.buscar_carrera_en_texto(texto_original)
            if carrera_info:
                logger.info(f"Carrera encontrada en texto: {carrera_info['nombre']}")
                return self.formatear_info_carrera(carrera_info)

        # PRIORIDAD 2: Buscar información específica en FAQ (CAIPI, reconocimientos, alianzas, etc.)
        if texto_original:
            info_especifica = self.buscar_info_especifica_faq(texto_original)
            if info_especifica:
                logger.info(f"Información específica encontrada en FAQ")
                return info_especifica

        # PRIORIDAD 3: Obtener respuesta base
        respuesta_info = self.respuestas_base.get(
            intencion,
            self.respuestas_base["fuera_dominio"]
        )
        respuesta = respuesta_info["respuesta"]

        # Ajustar tono según sentimiento
        compound = sentimiento["compound"]

        if compound < -0.3:
            # Usuario posiblemente frustrado
            prefijo = "Entiendo que puedas estar preocupado/a. "
        elif compound > 0.5:
            # Usuario positivo
            prefijo = "¡Me alegra poder ayudarte! "
        else:
            # Neutro (mayoría de casos)
            prefijo = ""

        # Respuesta especial para saludo_despedida
        if intencion == "saludo_despedida":
            if compound < 0:
                # Despedida
                return "¡Gracias por contactar a ITSE! Fue un placer ayudarte. 👋\n\nSi tienes más preguntas, aquí estaré. ¡Que tengas un excelente día!"
            else:
                # Saludo
                return respuesta

        # Combinar prefijo + respuesta
        respuesta_final = prefijo + respuesta

        return respuesta_final

    def procesar_consulta(self, user_input: str) -> Tuple[str, Dict]:
        """
        Pipeline completo de procesamiento de consulta.

        Args:
            user_input: Entrada del usuario

        Returns:
            (respuesta, metadata)

        Example:
            >>> chatbot = TYR()
            >>> respuesta, metadata = chatbot.procesar_consulta("Hola, qué carreras tienen?")
            >>> print(respuesta)
            >>> print(metadata['intencion'])
        """
        logger.info(f"Procesando consulta: '{user_input}'")

        try:
            # 1. Preprocesar entrada
            texto_limpio = self.procesar_entrada(user_input)

            # 2. Clasificar intención
            intencion, confianza, todas_probs = self.clasificar_intencion(texto_limpio)

            # 3. Analizar sentimiento
            sentimiento = self.analizar_sentimiento(texto_limpio)

            # 4. Generar respuesta (pasar texto original para búsqueda de carreras)
            respuesta = self.generar_respuesta(intencion, sentimiento, texto_limpio)

            # 5. Preparar metadata
            metadata = {
                "intencion": intencion,
                "confianza": confianza,
                "sentimiento": sentimiento["categoria"],
                "sentimiento_compound": sentimiento["compound"],
                "todas_probabilidades": todas_probs,
                "texto_procesado": texto_limpio
            }

            logger.info(f"Consulta procesada exitosamente. Intención: {intencion}")

            return respuesta, metadata

        except Exception as e:
            logger.error(f"Error procesando consulta: {e}")
            respuesta_error = (
                "Lo siento, ocurrió un error al procesar tu consulta. "
                "Por favor, intenta nuevamente o contacta a info@itse.ac.pa"
            )
            metadata_error = {
                "intencion": "error",
                "confianza": 0.0,
                "sentimiento": "neutro",
                "error": str(e)
            }
            return respuesta_error, metadata_error


# Función auxiliar para pruebas rápidas
def main():
    """Función de prueba del chatbot."""
    # Configurar encoding para Windows
    import sys
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')

    print("="*80)
    print("TYR - ASISTENTE VIRTUAL ITSE")
    print("="*80)
    print("\nInicializando chatbot...\n")

    # Inicializar chatbot
    try:
        chatbot = TYR(modelo_path="modelo_bert_tyr_4358")
    except Exception as e:
        print(f"Error al inicializar: {e}")
        print("Asegúrate de que el modelo esté en la carpeta 'modelo_bert_tyr_4358'")
        return

    # Ejemplos de prueba
    ejemplos = [
        "Hola, buenos días",
        "Qué carreras de programación tienen?",
        "Cómo me inscribo?",
        "Cuánto cuesta la matrícula?",
        "Tienen becas disponibles?",
        "Dónde está ubicado ITSE?",
        "Cuánto dura la carrera de desarrollo de software?",
        "Qué necesito para aplicar?",
        "Gracias por la información!",
        "Quién ganó el mundial de fútbol?"
    ]

    print("PROBANDO CHATBOT CON EJEMPLOS:\n")
    print("="*80)

    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"\n[{i}] Usuario: {ejemplo}")
        print("-"*80)

        respuesta, metadata = chatbot.procesar_consulta(ejemplo)

        print(f"\nTYR: {respuesta}\n")
        print(f"📊 Metadata:")
        print(f"   Intención: {metadata['intencion']}")
        print(f"   Confianza: {metadata['confianza']:.1%}")
        print(f"   Sentimiento: {metadata['sentimiento']} ({metadata['sentimiento_compound']:.3f})")
        print("="*80)

    print("\n✅ Pruebas completadas")


if __name__ == "__main__":
    main()
