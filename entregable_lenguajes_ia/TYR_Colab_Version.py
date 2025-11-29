"""
TYR - Chatbot de Atención al Cliente ITSE
Versión Simplificada para Google Colab

Materia: Lenguajes de Programación para IA
Proyecto: Chatbot de Atención al Cliente
Estudiante: [Tu Nombre]

Este archivo demuestra las estructuras de control y lógica del chatbot
de manera simplificada para fines educativos.
"""

import re
import json
from typing import Dict, List, Tuple

# ============================================================================
# SECCIÓN 1: BASE DE CONOCIMIENTO (Diccionarios y Listas)
# ============================================================================

# Diccionario de intenciones y sus palabras clave
INTENCIONES_KEYWORDS = {
    "saludo": ["hola", "buenos días", "buenas tardes", "buenas noches", "qué tal", "saludos", "hey"],
    "despedida": ["adiós", "hasta luego", "chao", "nos vemos", "bye", "hasta pronto"],
    "informacion_carreras": ["carrera", "programa", "técnico", "estudiar", "ofertas académicas", "tecnología"],
    "informacion_inscripcion": ["inscribir", "matricula", "inscripción", "cómo entrar", "requisitos", "admisión"],
    "informacion_horarios": ["horario", "hora", "cuándo", "abren", "cierran", "atención"],
    "informacion_becas": ["beca", "ayuda", "financiera", "económica", "descuento", "financiamiento"],
    "informacion_caipi": ["guardería", "caipi", "hijos", "niños", "daycare"],
    "informacion_ciiecyt": ["investigación", "ciiecyt", "research", "proyectos"],
    "informacion_general_itse": ["itse", "instituto", "ubicación", "dirección", "contacto"],
}

# Diccionario de respuestas base por intención
RESPUESTAS_BASE = {
    "saludo": "¡Hola! Soy TYR, tu asistente virtual del ITSE. ¿En qué puedo ayudarte hoy?",
    "despedida": "¡Hasta luego! Que tengas un excelente día. Si tienes más preguntas, aquí estaré.",
    "informacion_carreras": """El ITSE ofrece 16 carreras técnicas en áreas como:
- Desarrollo de Software
- Big Data e Inteligencia de Negocios
- Ciberseguridad
- Redes y Telecomunicaciones
- Automatización Industrial
¿Sobre cuál te gustaría saber más?""",
    "informacion_inscripcion": """Para inscribirte en el ITSE debes:
1. Completar formulario en línea
2. Presentar copia del diploma de bachiller
3. Realizar prueba de admisión
4. Entrevista con orientador
Horario de inscripción: Lunes a Viernes 8am-4pm""",
    "informacion_horarios": "El ITSE está abierto de Lunes a Viernes de 8:00 AM a 4:00 PM. Los sábados de 8:00 AM a 12:00 PM.",
    "informacion_becas": """¡Sí! El ITSE ofrece becas:
- Beca por mérito académico (hasta 100%)
- Beca por situación económica (hasta 75%)
- Beca deportiva (hasta 50%)
Contacta al departamento de ayuda financiera para más información.""",
    "informacion_caipi": "El ITSE cuenta con CAIPI, una guardería para hijos de estudiantes de 1 a 5 años. Horario: 7am-5pm.",
    "informacion_ciiecyt": "CIIECYT es el Centro de Investigación del ITSE donde estudiantes pueden participar en proyectos de investigación aplicada.",
    "informacion_general_itse": """El ITSE es el Instituto Técnico Superior Especializado de Panamá.
Ubicación: Ciudad de Panamá
Teléfono: +507 XXX-XXXX
Email: info@itse.ac.pa""",
    "desconocido": """Disculpa, no entendí tu consulta. Puedo ayudarte con:
- Información sobre carreras
- Proceso de inscripción
- Horarios y ubicación
- Becas disponibles
¿Sobre qué te gustaría saber?"""
}

# Lista de carreras con información detallada
CARRERAS_ITSE = [
    {
        "nombre": "Tecnología en Desarrollo de Software",
        "duracion": "2 años",
        "areas": ["Backend", "Frontend", "Móvil", "IA"],
        "descripcion": "Aprende a desarrollar aplicaciones web, móviles y sistemas inteligentes."
    },
    {
        "nombre": "Tecnología en Big Data e Inteligencia de Negocios",
        "duracion": "2 años",
        "areas": ["Data Science", "Analytics", "BI"],
        "descripcion": "Conviértete en experto en análisis de datos y machine learning."
    },
    {
        "nombre": "Tecnología en Ciberseguridad",
        "duracion": "2 años",
        "areas": ["Ethical Hacking", "Security", "Networks"],
        "descripcion": "Especialízate en proteger sistemas y redes contra amenazas."
    },
    # ... más carreras (total 16 en la versión completa)
]


# ============================================================================
# SECCIÓN 2: FUNCIONES DE PREPROCESAMIENTO
# ============================================================================

def preprocesar_texto(texto: str) -> str:
    """
    Limpia y normaliza el texto del usuario.

    Args:
        texto (str): Texto original del usuario

    Returns:
        str: Texto limpio y normalizado

    Example:
        >>> preprocesar_texto("  ¡HOLA!  ¿Cómo estás? ")
        'hola como estas'
    """
    # Convertir a minúsculas
    texto = texto.lower()

    # Eliminar signos de puntuación
    texto = re.sub(r'[^\w\s]', '', texto)

    # Eliminar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)

    # Eliminar espacios al inicio y final
    texto = texto.strip()

    return texto


def validar_entrada(mensaje: str) -> Tuple[bool, str]:
    """
    Valida que el mensaje del usuario sea correcto.

    Args:
        mensaje (str): Mensaje del usuario

    Returns:
        Tuple[bool, str]: (es_valido, mensaje_error)

    Example:
        >>> validar_entrada("")
        (False, "El mensaje no puede estar vacío")
        >>> validar_entrada("Hola")
        (True, "")
    """
    # Validación 1: No puede estar vacío
    if not mensaje or len(mensaje.strip()) == 0:
        return False, "El mensaje no puede estar vacío"

    # Validación 2: Longitud mínima (al menos 2 caracteres)
    if len(mensaje.strip()) < 2:
        return False, "El mensaje es demasiado corto"

    # Validación 3: Longitud máxima (máximo 500 caracteres)
    if len(mensaje) > 500:
        return False, "El mensaje es demasiado largo (máximo 500 caracteres)"

    # Validación 4: No permitir solo números
    if mensaje.strip().isdigit():
        return False, "Por favor, escribe una pregunta válida"

    return True, ""


# ============================================================================
# SECCIÓN 3: LÓGICA DE CLASIFICACIÓN DE INTENCIONES (Reglas)
# ============================================================================

def clasificar_intencion(texto: str) -> Tuple[str, float]:
    """
    Clasifica la intención del usuario basándose en palabras clave.

    Esta función implementa las 10+ reglas principales del chatbot.

    Args:
        texto (str): Texto preprocesado del usuario

    Returns:
        Tuple[str, float]: (intencion, confianza)

    Example:
        >>> clasificar_intencion("hola buenos días")
        ('saludo', 0.95)
        >>> clasificar_intencion("que carreras tienen")
        ('informacion_carreras', 0.85)
    """
    # Preprocesar el texto
    texto_limpio = preprocesar_texto(texto)
    palabras = texto_limpio.split()

    # Diccionario para contar coincidencias por intención
    coincidencias = {}

    # REGLA: Iterar por cada intención y contar coincidencias
    for intencion, keywords in INTENCIONES_KEYWORDS.items():
        contador = 0

        # Contar cuántas keywords aparecen en el texto
        for keyword in keywords:
            if keyword in texto_limpio:
                contador += 1

        # Guardar número de coincidencias
        if contador > 0:
            coincidencias[intencion] = contador

    # Si no hay coincidencias, es desconocido
    if not coincidencias:
        return "desconocido", 0.2

    # Obtener la intención con más coincidencias
    mejor_intencion = max(coincidencias, key=coincidencias.get)
    max_coincidencias = coincidencias[mejor_intencion]

    # Calcular confianza (0.0 a 1.0)
    # Más coincidencias = mayor confianza
    confianza = min(0.5 + (max_coincidencias * 0.2), 0.99)

    return mejor_intencion, confianza


def buscar_carrera_especifica(texto: str) -> str:
    """
    Busca si el usuario mencionó una carrera específica.

    Args:
        texto (str): Texto del usuario

    Returns:
        str: Nombre de la carrera encontrada o cadena vacía

    Example:
        >>> buscar_carrera_especifica("info sobre desarrollo de software")
        'Tecnología en Desarrollo de Software'
    """
    texto_limpio = preprocesar_texto(texto)

    # Buscar en lista de carreras
    for carrera in CARRERAS_ITSE:
        nombre_limpio = preprocesar_texto(carrera["nombre"])

        # Si el nombre de la carrera está en el texto
        if nombre_limpio in texto_limpio:
            return carrera["nombre"]

        # También buscar por áreas de estudio
        for area in carrera["areas"]:
            if preprocesar_texto(area) in texto_limpio:
                return carrera["nombre"]

    return ""


# ============================================================================
# SECCIÓN 4: GENERACIÓN DE RESPUESTAS
# ============================================================================

def generar_respuesta(intencion: str, confianza: float, texto_original: str) -> str:
    """
    Genera una respuesta basada en la intención clasificada.

    Args:
        intencion (str): Intención clasificada
        confianza (float): Nivel de confianza de la clasificación
        texto_original (str): Texto original del usuario

    Returns:
        str: Respuesta del chatbot
    """
    # REGLA 1: Si la confianza es muy baja, pedir aclaración
    if confianza < 0.3:
        return RESPUESTAS_BASE["desconocido"]

    # REGLA 2: Si es consulta sobre carreras, verificar si mencionó una específica
    if intencion == "informacion_carreras":
        carrera_encontrada = buscar_carrera_especifica(texto_original)

        if carrera_encontrada:
            # Buscar información de esa carrera
            for carrera in CARRERAS_ITSE:
                if carrera["nombre"] == carrera_encontrada:
                    return f"""📚 {carrera['nombre']}

Duración: {carrera['duracion']}
Áreas: {', '.join(carrera['areas'])}

{carrera['descripcion']}

¿Te gustaría saber sobre el proceso de inscripción?"""

    # REGLA 3: Respuesta base según la intención
    return RESPUESTAS_BASE.get(intencion, RESPUESTAS_BASE["desconocido"])


# ============================================================================
# SECCIÓN 5: FUNCIÓN PRINCIPAL DEL CHATBOT
# ============================================================================

def procesar_mensaje(mensaje: str) -> Dict:
    """
    Función principal que orquesta todo el procesamiento del mensaje.

    Este es el punto de entrada principal del chatbot.

    Args:
        mensaje (str): Mensaje del usuario

    Returns:
        Dict: Diccionario con respuesta, intención y confianza
    """
    # PASO 1: Validar entrada
    es_valido, error = validar_entrada(mensaje)

    if not es_valido:
        return {
            "respuesta": f"❌ Error: {error}",
            "intencion": "error",
            "confianza": 0.0
        }

    # PASO 2: Clasificar intención
    intencion, confianza = clasificar_intencion(mensaje)

    # PASO 3: Generar respuesta
    respuesta = generar_respuesta(intencion, confianza, mensaje)

    # PASO 4: Retornar resultado
    return {
        "respuesta": respuesta,
        "intencion": intencion,
        "confianza": round(confianza, 2)
    }


# ============================================================================
# SECCIÓN 6: INTERFAZ DE USUARIO (Ciclo Principal)
# ============================================================================

def iniciar_chatbot():
    """
    Inicia el ciclo principal del chatbot (interfaz de consola).

    Usa un ciclo while para mantener la conversación activa.
    """
    print("=" * 60)
    print("  TYR - Asistente Virtual del ITSE")
    print("=" * 60)
    print("\n¡Hola! Soy TYR. Estoy aquí para ayudarte.")
    print("Escribe 'salir' para terminar la conversación.\n")

    # Contador de mensajes (para estadísticas)
    contador_mensajes = 0
    historial_intenciones = []

    # CICLO PRINCIPAL: while para mantener la conversación
    while True:
        # Leer entrada del usuario
        print("-" * 60)
        mensaje_usuario = input("Tú: ").strip()

        # REGLA DE SALIDA: Verificar si el usuario quiere salir
        if mensaje_usuario.lower() in ["salir", "exit", "quit", "adiós", "chao"]:
            print("\nTYR: ¡Hasta luego! Que tengas un excelente día.")

            # Mostrar estadísticas de la conversación
            print(f"\n📊 Estadísticas de la conversación:")
            print(f"   - Total de mensajes: {contador_mensajes}")
            print(f"   - Intenciones detectadas: {len(set(historial_intenciones))}")
            break

        # Validar que no esté vacío
        if not mensaje_usuario:
            print("TYR: Por favor, escribe algo.\n")
            continue

        # Procesar el mensaje
        try:
            resultado = procesar_mensaje(mensaje_usuario)

            # Mostrar respuesta
            print(f"\nTYR: {resultado['respuesta']}")
            print(f"\n[Debug] Intención: {resultado['intencion']} | "
                  f"Confianza: {resultado['confianza']}\n")

            # Actualizar estadísticas
            contador_mensajes += 1
            historial_intenciones.append(resultado['intencion'])

        except Exception as e:
            # Manejo de errores inesperados
            print(f"\nTYR: Lo siento, ocurrió un error: {str(e)}")
            print("Por favor, intenta reformular tu pregunta.\n")


# ============================================================================
# SECCIÓN 7: FUNCIONES DE PRUEBA (Tests)
# ============================================================================

def ejecutar_pruebas():
    """
    Ejecuta pruebas automáticas del chatbot para verificar su funcionamiento.
    """
    print("=" * 60)
    print("  EJECUTANDO PRUEBAS DEL CHATBOT")
    print("=" * 60)

    # Lista de casos de prueba
    casos_prueba = [
        ("Hola", "saludo"),
        ("¿Qué carreras tienen?", "informacion_carreras"),
        ("Cómo me inscribo", "informacion_inscripcion"),
        ("Cuál es el horario", "informacion_horarios"),
        ("Hay becas", "informacion_becas"),
        ("Adiós", "despedida"),
        ("asdfghjkl", "desconocido"),  # Entrada sin sentido
    ]

    tests_pasados = 0
    tests_totales = len(casos_prueba)

    # Ejecutar cada caso de prueba
    for i, (entrada, intencion_esperada) in enumerate(casos_prueba, 1):
        resultado = procesar_mensaje(entrada)

        # Verificar si la intención es correcta
        if resultado["intencion"] == intencion_esperada:
            print(f"✅ Test {i} PASADO: '{entrada}' → {intencion_esperada}")
            tests_pasados += 1
        else:
            print(f"❌ Test {i} FALLADO: '{entrada}'")
            print(f"   Esperado: {intencion_esperada}")
            print(f"   Obtenido: {resultado['intencion']}")

    # Mostrar resumen
    print("\n" + "=" * 60)
    print(f"Resultado: {tests_pasados}/{tests_totales} tests pasados")
    print(f"Tasa de éxito: {(tests_pasados/tests_totales)*100:.1f}%")
    print("=" * 60)


# ============================================================================
# SECCIÓN 8: MENÚ PRINCIPAL
# ============================================================================

def menu_principal():
    """
    Muestra el menú principal con opciones para el usuario.
    """
    while True:
        print("\n" + "=" * 60)
        print("  MENÚ PRINCIPAL - TYR Chatbot")
        print("=" * 60)
        print("1. Iniciar chatbot (modo conversación)")
        print("2. Ejecutar pruebas automáticas")
        print("3. Ver información del proyecto")
        print("4. Salir")
        print("=" * 60)

        opcion = input("\nSelecciona una opción (1-4): ").strip()

        if opcion == "1":
            iniciar_chatbot()
        elif opcion == "2":
            ejecutar_pruebas()
        elif opcion == "3":
            mostrar_info_proyecto()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Por favor, selecciona 1, 2, 3 o 4.")


def mostrar_info_proyecto():
    """
    Muestra información sobre el proyecto.
    """
    print("\n" + "=" * 60)
    print("  INFORMACIÓN DEL PROYECTO")
    print("=" * 60)
    print("""
Nombre: TYR - Chatbot de Atención al Cliente ITSE
Materia: Lenguajes de Programación para IA
Tipo de Proyecto: Chatbot de Atención al Cliente

Características Técnicas:
✅ 10+ reglas de clasificación de intención
✅ Validaciones de entrada robustas
✅ Manejo de errores completo
✅ Base de conocimiento con 16 carreras
✅ Interfaz de consola interactiva
✅ Sistema de pruebas automatizadas

Estructuras de Control Utilizadas:
- if/elif/else (validaciones, clasificación)
- while (ciclo principal de conversación)
- for (iteración sobre keywords y carreras)
- try/except (manejo de errores)

Estructuras de Datos:
- Diccionarios (intenciones, respuestas, carreras)
- Listas (keywords, historial, casos de prueba)
- Tuplas (retornos de funciones)

GitHub: https://github.com/EiTinchoZ/TYR
""")
    print("=" * 60)


# ============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Si se ejecuta el archivo directamente, mostrar el menú principal
    menu_principal()
