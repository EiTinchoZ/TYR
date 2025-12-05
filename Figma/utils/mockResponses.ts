/**
 * Respuestas mock para modo demo (cuando no hay backend disponible)
 * Simula las respuestas del modelo BERT basándose en palabras clave
 */

interface MockResponse {
  respuesta: string;
  intencion: string;
  confianza: number;
  sentimiento: string;
  sentimiento_compound: number;
  entidades?: {
    [key: string]: string[];
  };
}

const MOCK_RESPONSES: Record<string, MockResponse> = {
  default: {
    respuesta: "¡Hola! Soy TYR, tu asistente virtual del ITSE. Este es un **modo demo**. Para experimentar la versión completa con IA, el backend debe estar en ejecución.\n\nPuedo ayudarte con:\n- 📚 Información sobre las 16 carreras técnicas\n- 📝 Proceso de admisión e inscripción\n- 💰 Becas y opciones de financiamiento\n- 🏫 Información general del ITSE\n\n¿Qué te gustaría saber?",
    intencion: "saludo",
    confianza: 0.95,
    sentimiento: "positivo",
    sentimiento_compound: 0.8,
    entidades: {
      "ORGANIZACION": ["itse"]
    }
  },

  carreras: {
    respuesta: "El ITSE ofrece **16 carreras técnicas** en áreas de tecnología:\n\n**Desarrollo de Software:**\n- Desarrollo de Software\n- Desarrollo de Videojuegos\n- Big Data\n- Inteligencia Artificial\n\n**Redes y Seguridad:**\n- Redes Informáticas\n- Ciberseguridad\n\n**Diseño:**\n- Diseño Gráfico\n- Diseño de Experiencia de Usuario (UX/UI)\n\n**Otras áreas:**\n- Electrónica Industrial\n- Mecatrónica\n- Y más...\n\nTodas tienen **duración de 2-3 años** y otorgan título de Técnico Superior.\n\n¿Sobre cuál carrera te gustaría saber más?",
    intencion: "informacion_carreras",
    confianza: 0.98,
    sentimiento: "neutro",
    sentimiento_compound: 0.0,
    entidades: {
      "ORGANIZACION": ["itse"],
      "PERIODO": ["2-3 años"]
    }
  },

  admision: {
    respuesta: "El **proceso de admisión** al ITSE es sencillo:\n\n**Pasos:**\n1. **Llenar solicitud** en línea o presencial\n2. **Entregar documentos:**\n   - Copia de cédula\n   - Diploma de secundaria (original)\n   - 2 fotos tamaño carnet\n   - Paz y salvo (si vienes de otra institución)\n\n3. **Examen de admisión** (conocimientos básicos)\n4. **Entrevista** (opcional según carrera)\n5. **Matrícula** una vez aceptado\n\n**Fechas importantes:**\n- Inscripciones: Enero-Febrero y Julio-Agosto\n- Inicio de clases: Marzo y Septiembre\n\n**Costo de matrícula:** $300-400 (varía según carrera)\n\n¿Necesitas más información sobre algún paso?",
    intencion: "proceso_admision",
    confianza: 0.96,
    sentimiento: "neutro",
    sentimiento_compound: 0.1,
    entidades: {
      "ORGANIZACION": ["itse"],
      "REQUISITO": ["cédula", "diploma", "fotos"]
    }
  },

  becas: {
    respuesta: "El ITSE ofrece varias **opciones de financiamiento y becas:**\n\n**Becas disponibles:**\n- 🎓 **Beca por excelencia académica** (50-100%)\n- 💼 **Beca socioeconómica** (según ingreso familiar)\n- 🏆 **Beca deportiva** (para atletas destacados)\n- 👥 **Descuento por hermanos** (10-15% adicional)\n\n**Planes de pago:**\n- Pago completo (5% descuento)\n- 2 cuotas semestrales\n- 4 cuotas trimestrales\n\n**Requisitos generales:**\n- Promedio mínimo de 3.0\n- Documentación de ingresos (beca socioeconómica)\n- Carta de motivación\n\n**Contacto:** becas@itse.ac.pa\n\n¿Te gustaría información sobre alguna beca específica?",
    intencion: "informacion_becas",
    confianza: 0.97,
    sentimiento: "positivo",
    sentimiento_compound: 0.6,
    entidades: {
      "ORGANIZACION": ["itse"],
      "SERVICIO": ["becas"]
    }
  },

  ia: {
    respuesta: "La carrera de **Inteligencia Artificial** es una de las más demandadas:\n\n**¿Qué aprenderás?**\n- Machine Learning y Deep Learning\n- Procesamiento de Lenguaje Natural (NLP)\n- Visión por Computadora\n- Redes Neuronales\n- Python, TensorFlow, PyTorch\n- Ética en IA\n\n**Duración:** 2.5 años\n\n**Perfil del graduado:**\n- Desarrollar soluciones con IA\n- Crear chatbots y asistentes virtuales\n- Análisis de datos con ML\n- Trabajar en empresas tech\n\n**Oportunidades laborales:**\n- Data Scientist\n- ML Engineer\n- AI Developer\n- Salario promedio: $1,500-2,500/mes\n\n¿Quieres saber sobre los requisitos de ingreso?",
    intencion: "informacion_carrera_especifica",
    confianza: 0.99,
    sentimiento: "positivo",
    sentimiento_compound: 0.7,
    entidades: {
      "CARRERA": ["inteligencia artificial"]
    }
  },

  ciberseguridad: {
    respuesta: "La **T.S. en Ciberseguridad** es una de nuestras carreras más demandadas del ITSE:\n\n**📚 Escuela:** Innovación Digital\n\n**⏱️ Duración:** • Jornada Diurna: 2 años 4 meses • Jornada Nocturna: 3 años • Total: 122 créditos\n\n**💡 ¿Qué aprenderás?**\nPrevenir y detectar amenazas de seguridad. Recuperar incidentes, proteger datos y sistemas. Aplicar normativas, políticas y procedimientos de seguridad informática.\n\n**💼 Campo Ocupacional:**\n• Analista de seguridad informática\n• Administrador redes sistemas seguros\n• Auditor de ciberseguridad\n• Consultor seguridad informática\n• Ingeniero de seguridad\n• ...y 7 opciones más\n\n**💰 Becas disponibles:**\nEl ITSE ofrece becas del IFARHU y programas de ayuda financiera.\n\n**📍 Ubicación:** Tocumen, Panamá\n\n**🔗 Más información:** [Oferta académica ITSE](https://www.itse.ac.pa/oferta-academica/tecnico-superior-en-ciberseguridad)\n\n¿Te gustaría saber sobre el proceso de inscripción o requisitos?",
    intencion: "informacion_carrera_especifica",
    confianza: 0.967,
    sentimiento: "positivo",
    sentimiento_compound: 0.8,
    entidades: {
      "CARRERA": ["ciberseguridad"],
      "ORGANIZACION": ["itse", "ifarhu"],
      "UBICACION": ["tocumen"]
    }
  },

  horarios: {
    respuesta: "**Horarios de atención del ITSE:**\n\n📞 **Teléfono:**\n- Lunes a Viernes: 8:00 AM - 5:00 PM\n- Sábados: 9:00 AM - 1:00 PM\n- Tel: +507 524-3333\n\n🏫 **Oficinas administrativas:**\n- Lunes a Viernes: 8:00 AM - 4:30 PM\n\n📧 **Email:**\n- info@itse.ac.pa\n- Respuesta en 24-48 horas\n\n📍 **Ubicación:**\n- Tocumen, Panamá\n- Frente al Aeropuerto Internacional\n\n¿Necesitas direcciones o más información de contacto?",
    intencion: "horarios_contacto",
    confianza: 0.94,
    sentimiento: "neutro",
    sentimiento_compound: 0.05,
    entidades: {
      "ORGANIZACION": ["itse"],
      "UBICACION": ["tocumen", "panamá"],
      "PERIODO": ["lunes a viernes", "sábados"]
    }
  }
};

export function getMockResponse(mensaje: string): MockResponse {
  const mensajeLower = mensaje.toLowerCase();

  // Detectar carreras específicas primero (más específico)
  if (mensajeLower.match(/ciberseguridad|ciber seguridad|cyber|seguridad informática/)) {
    return MOCK_RESPONSES.ciberseguridad;
  }

  if (mensajeLower.match(/inteligencia artificial|ia|machine learning|ml/)) {
    return MOCK_RESPONSES.ia;
  }

  // Detectar intención basándose en palabras clave (más general)
  if (mensajeLower.match(/carrera|programa|estudi|técnic|disponible/)) {
    return MOCK_RESPONSES.carreras;
  }

  if (mensajeLower.match(/admis|inscri|ingresar|entrar|matricul/)) {
    return MOCK_RESPONSES.admision;
  }

  if (mensajeLower.match(/beca|financ|pago|costo|precio|descuento/)) {
    return MOCK_RESPONSES.becas;
  }

  if (mensajeLower.match(/horario|contacto|teléfono|email|ubicación|dirección/)) {
    return MOCK_RESPONSES.horarios;
  }

  // Respuesta por defecto
  return MOCK_RESPONSES.default;
}

export function isBackendAvailable(apiUrl: string): boolean {
  // Simple check - en producción podrías hacer un ping real
  return apiUrl !== "http://localhost:8000" || false;
}
