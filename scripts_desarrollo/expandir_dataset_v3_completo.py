"""
Script para expandir dataset TYR de 1835 a 3000+ ejemplos
Enfoque especial en preguntas sobre carreras con múltiples variaciones
Incluye información actualizada v3 del ITSE
"""

import json
import random
from typing import List, Tuple

def cargar_dataset_existente() -> List[Tuple[str, str]]:
    """Carga el dataset expandido actual"""
    with open('Dataset_TYR_3000_EXPANDIDO.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"OK Dataset actual cargado: {len(data)} ejemplos")
    return data

def generar_preguntas_carreras() -> List[Tuple[str, str]]:
    """Genera preguntas variadas sobre las 16 carreras del ITSE"""

    # Las 16 carreras oficiales del ITSE organizadas por escuela
    carreras = {
        "Escuela de Ingeniería y Tecnología": [
            "Desarrollo de Software",
            "Big Data",
            "Ciberseguridad",
            "Inteligencia Artificial",
            "Ingeniería Electrónica",
            "Electrotecnia Industrial",
            "Electricidad Industrial",
            "Mecatrónica"
        ],
        "Escuela de Logística y Transporte Multimodal": [
            "Operaciones Portuarias",
            "Logística",
            "Operaciones Aeroportuarias"
        ],
        "Escuela de Turismo, Hotelería y Gastronomía": [
            "Artes Culinarias",
            "Gestión Ejecutiva en Empresas Turísticas y Hoteleras"
        ],
        "Escuela de Economía Creativa y Negocios": [
            "Negocios Digitales",
            "Producción de Medios Audiovisuales",
            "Fotografía"
        ]
    }

    # Variaciones de preguntas (incluyendo las que fallaban antes)
    patrones = [
        "Cuéntame sobre {carrera}",
        "Cuéntame de {carrera}",
        "Qué es {carrera}",
        "Qué es la carrera de {carrera}",
        "Información sobre {carrera}",
        "Información de {carrera}",
        "Info de {carrera}",
        "Háblame de {carrera}",
        "Háblame sobre {carrera}",
        "Dime sobre {carrera}",
        "Dime de {carrera}",
        "Me interesa {carrera}",
        "Quiero estudiar {carrera}",
        "Quiero saber de {carrera}",
        "Quiero información de {carrera}",
        "Quisiera saber sobre {carrera}",
        "Quisiera información de {carrera}",
        "Necesito info de {carrera}",
        "Detalles de {carrera}",
        "Detalles sobre {carrera}",
        "{carrera} qué es?",
        "{carrera} de qué trata?",
        "{carrera} tiene salida laboral?",
        "{carrera} cuánto dura?",
        "{carrera} es buena carrera?",
        "Qué se aprende en {carrera}?",
        "Qué aprendo en {carrera}?",
        "En qué trabaja un egresado de {carrera}?",
        "Cuál es la malla de {carrera}?",
        "Programa de {carrera}",
        "Plan de estudios de {carrera}",
        "Cuántos créditos tiene {carrera}?",
        "Duración de {carrera}",
        "Horarios de {carrera}",
        "{carrera} tiene jornada nocturna?",
        "{carrera} se puede estudiar de noche?",
        "Me gustaría estudiar {carrera}",
        "Estoy interesado en {carrera}",
        "Quiero inscribirme en {carrera}",
        "Cómo es la carrera de {carrera}?",
        "Vale la pena estudiar {carrera}?",
        "Por qué estudiar {carrera} en el ITSE?",
        "{carrera} en el ITSE",
        "ITSE tiene {carrera}?",
        "Ofrecen {carrera}?",
        "Hay carrera de {carrera}?",
        "Existe {carrera} en ITSE?",
        "Información carrera {carrera}",
        "Dame info de la carrera de {carrera}",
    ]

    # Sinónimos y variaciones de nombres de carreras
    variaciones_nombres = {
        "Desarrollo de Software": ["desarrollo de software", "software", "programación", "desarrollo"],
        "Big Data": ["big data", "bigdata", "datos", "ciencia de datos", "data science"],
        "Ciberseguridad": ["ciberseguridad", "ciber seguridad", "seguridad informática", "hacking ético"],
        "Inteligencia Artificial": ["inteligencia artificial", "IA", "AI", "machine learning"],
        "Ingeniería Electrónica": ["ingeniería electrónica", "electrónica", "ing electrónica"],
        "Electrotecnia Industrial": ["electrotecnia industrial", "electrotecnia"],
        "Electricidad Industrial": ["electricidad industrial", "electricidad"],
        "Mecatrónica": ["mecatrónica", "mecatronica"],
        "Operaciones Portuarias": ["operaciones portuarias", "portuaria", "puertos"],
        "Logística": ["logística", "logistica"],
        "Operaciones Aeroportuarias": ["operaciones aeroportuarias", "aeroportuaria", "aeropuertos"],
        "Artes Culinarias": ["artes culinarias", "culinaria", "gastronomía", "chef"],
        "Gestión Ejecutiva en Empresas Turísticas y Hoteleras": ["gestión ejecutiva", "turismo", "hotelería", "hoteles"],
        "Negocios Digitales": ["negocios digitales", "negocios", "marketing digital"],
        "Producción de Medios Audiovisuales": ["producción audiovisual", "medios audiovisuales", "audiovisuales"],
        "Fotografía": ["fotografía", "fotografia", "foto"]
    }

    ejemplos = []

    # Generar preguntas para cada carrera
    for escuela, lista_carreras in carreras.items():
        for carrera in lista_carreras:
            # Usar todas las variaciones de nombre
            nombres = variaciones_nombres.get(carrera, [carrera.lower()])

            for patron in patrones:
                for nombre in nombres:
                    pregunta = patron.replace("{carrera}", nombre)
                    ejemplos.append([pregunta, "informacion_carreras"])

    print(f"OK Generadas {len(ejemplos)} preguntas sobre carreras")
    return ejemplos

def generar_preguntas_faq_v3() -> List[Tuple[str, str]]:
    """Genera preguntas FAQ con información actualizada v3"""

    preguntas_faq = [
        # Información general ITSE
        ["Qué es el ITSE?", "faq_general"],
        ["Cuéntame sobre el ITSE", "faq_general"],
        ["Qué significa ITSE?", "faq_general"],
        ["Para qué sirve el ITSE?", "faq_general"],
        ["Cuándo se fundó el ITSE?", "faq_general"],
        ["En qué año abrió el ITSE?", "faq_general"],
        ["Quién fundó el ITSE?", "faq_general"],
        ["Por qué existe el ITSE?", "faq_general"],

        # CAIPI (Centro de Atención Integral a la Primera Infancia)
        ["Qué es CAIPI?", "faq_general"],
        ["Tienen guardería?", "faq_general"],
        ["Hay cuidado de niños?", "faq_general"],
        ["Puedo llevar a mi hijo?", "faq_general"],
        ["Tienen servicio de cuido infantil?", "faq_general"],
        ["CAIPI qué es?", "faq_general"],
        ["Centro de cuido para hijos de estudiantes?", "faq_general"],

        # CIIECYT (Centro de Investigación e Innovación)
        ["Qué es CIIECYT?", "faq_general"],
        ["Tienen centro de investigación?", "faq_general"],
        ["Hacen investigación en ITSE?", "faq_general"],
        ["Puedo investigar en el ITSE?", "faq_general"],
        ["Centro de innovación ITSE?", "faq_general"],

        # Reconocimientos internacionales
        ["El ITSE tiene reconocimientos?", "faq_general"],
        ["Qué premios tiene el ITSE?", "faq_general"],
        ["El ITSE está reconocido internacionalmente?", "faq_general"],
        ["Foro Económico Mundial reconoce al ITSE?", "faq_general"],
        ["Unión Europea reconoce al ITSE?", "faq_general"],
        ["ITSE World Economic Forum", "faq_general"],
        ["Premios internacionales del ITSE", "faq_general"],

        # Alianzas estratégicas
        ["Tienen alianzas con empresas?", "faq_general"],
        ["Qué empresas trabajan con el ITSE?", "faq_general"],
        ["ITSE tiene convenio con Canal de Panamá?", "faq_general"],
        ["Copa Airlines trabaja con el ITSE?", "faq_general"],
        ["Alianzas estratégicas del ITSE", "faq_general"],
        ["Convenios con empresas europeas", "faq_general"],

        # Modelo educativo
        ["Cómo es el modelo educativo del ITSE?", "faq_general"],
        ["Qué porcentaje es práctica?", "faq_general"],
        ["Es más práctica o teoría?", "faq_general"],
        ["60-40 qué significa en ITSE?", "faq_general"],
        ["Modelo 60% académico 40% práctico", "faq_general"],

        # Éxito laboral
        ["Cuántos graduados consiguen trabajo?", "faq_general"],
        ["Tasa de empleabilidad ITSE", "faq_general"],
        ["80% inserción laboral es verdad?", "faq_general"],
        ["Los egresados consiguen trabajo?", "faq_general"],

        # Autoridades
        ["Quién es el rector del ITSE?", "faq_general"],
        ["Quién dirige el ITSE?", "faq_general"],
        ["Autoridades del ITSE", "faq_general"],
        ["Dra Milena Gómez quién es?", "faq_general"],
        ["Gerente Educativa del ITSE", "faq_general"],

        # Instalaciones
        ["Dónde queda el ITSE?", "contacto_ubicacion"],
        ["Ubicación del ITSE", "contacto_ubicacion"],
        ["Cómo llego al ITSE?", "contacto_ubicacion"],
        ["Dirección del ITSE", "contacto_ubicacion"],
        ["Campus del ITSE", "contacto_ubicacion"],

        # Valores institucionales
        ["Cuáles son los valores del ITSE?", "faq_general"],
        ["Misión del ITSE", "faq_general"],
        ["Visión del ITSE", "faq_general"],
        ["Compromiso académico ITSE", "faq_general"],
    ]

    print(f"OK Generadas {len(preguntas_faq)} preguntas FAQ v3")
    return preguntas_faq

def generar_preguntas_admision() -> List[Tuple[str, str]]:
    """Genera preguntas sobre inscripción y admisión"""

    preguntas = [
        # Proceso de inscripción
        ["Cómo me inscribo?", "inscripcion_admision"],
        ["Cómo aplico al ITSE?", "inscripcion_admision"],
        ["Cuál es el proceso de inscripción?", "inscripcion_admision"],
        ["Pasos para inscribirme", "inscripcion_admision"],
        ["Quiero inscribirme qué hago?", "inscripcion_admision"],
        ["Proceso de admisión", "inscripcion_admision"],
        ["Cómo aplico?", "inscripcion_admision"],

        # Fechas y plazos
        ["Cuándo son las inscripciones?", "inscripcion_admision"],
        ["Cuándo abren inscripciones?", "inscripcion_admision"],
        ["Hasta cuándo puedo inscribirme?", "inscripcion_admision"],
        ["Fecha límite de inscripción", "inscripcion_admision"],
        ["Plazo de inscripción", "inscripcion_admision"],

        # Requisitos
        ["Qué necesito para inscribirme?", "requisitos_ingreso"],
        ["Requisitos de ingreso", "requisitos_ingreso"],
        ["Qué documentos necesito?", "requisitos_ingreso"],
        ["Qué papeles piden?", "requisitos_ingreso"],
        ["Necesito diploma?", "requisitos_ingreso"],
        ["Piden certificado de nacimiento?", "requisitos_ingreso"],

        # Examen de admisión
        ["Hay examen de ingreso?", "requisitos_ingreso"],
        ["Tengo que hacer prueba?", "requisitos_ingreso"],
        ["Qué evalúan en la prueba?", "requisitos_ingreso"],
        ["PIENSE qué es?", "requisitos_ingreso"],
        ["Prueba de matemáticas?", "requisitos_ingreso"],
        ["Examen de comprensión lectora", "requisitos_ingreso"],
    ]

    print(f"OK Generadas {len(preguntas)} preguntas de admision")
    return preguntas

def generar_preguntas_becas() -> List[Tuple[str, str]]:
    """Genera preguntas sobre becas y financiamiento"""

    preguntas = [
        # Becas generales
        ["Hay becas?", "becas_financiamiento"],
        ["Tienen becas disponibles?", "becas_financiamiento"],
        ["Cómo consigo beca?", "becas_financiamiento"],
        ["Puedo aplicar a beca?", "becas_financiamiento"],
        ["Qué becas ofrecen?", "becas_financiamiento"],
        ["Tipos de becas", "becas_financiamiento"],

        # IFARHU
        ["Tienen convenio con IFARHU?", "becas_financiamiento"],
        ["Puedo usar IFARHU?", "becas_financiamiento"],
        ["IFARHU aplica en ITSE?", "becas_financiamiento"],
        ["Beca IFARHU", "becas_financiamiento"],

        # Financiamiento
        ["Puedo pagar en cuotas?", "becas_financiamiento"],
        ["Hay financiamiento?", "becas_financiamiento"],
        ["Planes de pago", "becas_financiamiento"],
        ["Cómo financiar mis estudios?", "becas_financiamiento"],

        # Ayuda económica
        ["Necesito ayuda económica", "becas_financiamiento"],
        ["Asistencia financiera", "becas_financiamiento"],
        ["No tengo dinero para pagar", "becas_financiamiento"],
        ["Costo de la carrera", "becas_financiamiento"],
    ]

    print(f"OK Generadas {len(preguntas)} preguntas de becas")
    return preguntas

def generar_preguntas_horarios() -> List[Tuple[str, str]]:
    """Genera preguntas sobre horarios y duración"""

    preguntas = [
        # Horarios
        ["Qué horarios tienen?", "horarios_duracion"],
        ["Horarios disponibles", "horarios_duracion"],
        ["Hay clases nocturnas?", "horarios_duracion"],
        ["Puedo estudiar de noche?", "horarios_duracion"],
        ["Tienen jornada diurna?", "horarios_duracion"],
        ["A qué hora son las clases?", "horarios_duracion"],
        ["Horario de clases", "horarios_duracion"],

        # Duración
        ["Cuánto dura la carrera?", "horarios_duracion"],
        ["Años de estudio", "horarios_duracion"],
        ["Duración del programa", "horarios_duracion"],
        ["Cuánto tiempo toma graduarse?", "horarios_duracion"],
        ["En cuánto me gradúo?", "horarios_duracion"],

        # Créditos
        ["Cuántos créditos son?", "horarios_duracion"],
        ["Total de créditos", "horarios_duracion"],
        ["Sistema de créditos", "horarios_duracion"],
    ]

    print(f"OK Generadas {len(preguntas)} preguntas de horarios")
    return preguntas

def generar_preguntas_saludos() -> List[Tuple[str, str]]:
    """Genera saludos y despedidas"""

    preguntas = [
        # Saludos
        ["Hola", "saludo_despedida"],
        ["Buenas", "saludo_despedida"],
        ["Buenos días", "saludo_despedida"],
        ["Buenas tardes", "saludo_despedida"],
        ["Buenas noches", "saludo_despedida"],
        ["Qué tal", "saludo_despedida"],
        ["Hey", "saludo_despedida"],
        ["Holi", "saludo_despedida"],

        # Despedidas
        ["Adiós", "saludo_despedida"],
        ["Chao", "saludo_despedida"],
        ["Hasta luego", "saludo_despedida"],
        ["Nos vemos", "saludo_despedida"],
        ["Gracias", "saludo_despedida"],
        ["Muchas gracias", "saludo_despedida"],
        ["Gracias por la info", "saludo_despedida"],
        ["Ok gracias", "saludo_despedida"],
        ["Entendido gracias", "saludo_despedida"],
    ]

    print(f"OK Generadas {len(preguntas)} saludos y despedidas")
    return preguntas

def generar_preguntas_fuera_dominio() -> List[Tuple[str, str]]:
    """Genera ejemplos de preguntas fuera del dominio ITSE"""

    preguntas = [
        # Política
        ["Quién ganó las elecciones?", "fuera_dominio"],
        ["Qué opinas de la política?", "fuera_dominio"],
        ["Quién es el presidente?", "fuera_dominio"],

        # Deportes
        ["Quién ganó el mundial?", "fuera_dominio"],
        ["Resultados de fútbol", "fuera_dominio"],
        ["Cuándo juega Panamá?", "fuera_dominio"],

        # Entretenimiento
        ["Cuál es la mejor película?", "fuera_dominio"],
        ["Recomiéndame una serie", "fuera_dominio"],
        ["Qué música escuchas?", "fuera_dominio"],

        # Otros temas
        ["Cómo está el clima?", "fuera_dominio"],
        ["Qué hora es?", "fuera_dominio"],
        ["Cuánto es 2+2?", "fuera_dominio"],
        ["Qué es el amor?", "fuera_dominio"],
        ["Receta de arroz", "fuera_dominio"],
    ]

    print(f"OK Generadas {len(preguntas)} preguntas fuera de dominio")
    return preguntas

def mezclar_y_guardar(dataset_existente: List, nuevos_ejemplos: List, archivo_salida: str):
    """Combina datasets, elimina duplicados y guarda"""

    # Combinar datasets
    dataset_completo = dataset_existente + nuevos_ejemplos

    # Eliminar duplicados (conservando orden)
    dataset_unico = []
    textos_vistos = set()

    for ejemplo in dataset_completo:
        texto = ejemplo[0].lower().strip()
        if texto not in textos_vistos:
            textos_vistos.add(texto)
            dataset_unico.append(ejemplo)

    # Mezclar aleatoriamente
    random.shuffle(dataset_unico)

    # Guardar
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(dataset_unico, f, ensure_ascii=False, indent=2)

    print(f"\nOK Dataset final guardado: {archivo_salida}")
    print(f"Total de ejemplos: {len(dataset_unico)}")

    # Mostrar distribución
    from collections import Counter
    intenciones = Counter([x[1] for x in dataset_unico])
    print("\nDistribucion por intencion:")
    for intencion, count in sorted(intenciones.items()):
        print(f"  {intencion}: {count}")

    return len(dataset_unico)

def main():
    print("=" * 60)
    print("EXPANDIENDO DATASET TYR A 3000+ EJEMPLOS")
    print("=" * 60)
    print()

    # 1. Cargar dataset existente
    print("PASO 1: Cargando dataset existente...")
    dataset_existente = cargar_dataset_existente()
    print()

    # 2. Generar nuevos ejemplos
    print("PASO 2: Generando nuevos ejemplos...")
    nuevos_ejemplos = []

    nuevos_ejemplos.extend(generar_preguntas_carreras())
    nuevos_ejemplos.extend(generar_preguntas_faq_v3())
    nuevos_ejemplos.extend(generar_preguntas_admision())
    nuevos_ejemplos.extend(generar_preguntas_becas())
    nuevos_ejemplos.extend(generar_preguntas_horarios())
    nuevos_ejemplos.extend(generar_preguntas_saludos())
    nuevos_ejemplos.extend(generar_preguntas_fuera_dominio())

    print(f"\nTotal nuevos ejemplos generados: {len(nuevos_ejemplos)}")
    print()

    # 3. Combinar y guardar
    print("PASO 3: Combinando y guardando dataset final...")
    total = mezclar_y_guardar(
        dataset_existente,
        nuevos_ejemplos,
        'Dataset_TYR_3000_FINAL.json'
    )

    print()
    print("=" * 60)
    print(f"COMPLETADO! Dataset expandido a {total} ejemplos")
    print("=" * 60)

if __name__ == "__main__":
    main()
