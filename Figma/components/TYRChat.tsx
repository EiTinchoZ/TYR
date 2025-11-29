/**
 * TYRChat - Componente de chat interactivo nativo
 * Conecta con el backend FastAPI para procesamiento con BERT
 */

import { useState, useRef, useEffect } from "react";
import { Send, Bot, User, RefreshCw, History, Download, Sun, Moon, Share2, Mic, MicOff } from "lucide-react";
import { Button } from "./ui/button";
import { Card, CardContent } from "./ui/card";
import jsPDF from "jspdf";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { getMockResponse } from "../utils/mockResponses";

interface Message {
  id: string;
  texto: string;
  esUsuario: boolean;
  timestamp: Date;
  intencion?: string;
  confianza?: number;
}

interface ChatResponse {
  respuesta: string;
  intencion: string;
  confianza: number;
  sentimiento: string;
  sentimiento_compound: number;
}

interface Conversation {
  id: string;
  title: string;
  messages: Message[];
  createdAt: Date;
  lastMessageAt: Date;
}

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

// Preguntas sugeridas para usuarios nuevos
const SUGGESTED_QUESTIONS = [
  "¿Qué carreras hay disponibles?",
  "¿Cómo me inscribo?",
  "Cuéntame sobre becas",
  "¿Qué es Inteligencia Artificial?",
  "Información sobre Ciberseguridad",
  "Horarios de atención",
];

const STORAGE_KEY = "tyr_conversations";
const CURRENT_CONVERSATION_KEY = "tyr_current_conversation";

// Temas de color (basados en branding oficial)
const THEMES = {
  dark: {
    card: "#1E3A5F",
    cardBorder: "#2E5A8F",
    header: "linear-gradient(135deg, #0066CC 0%, #004C99 100%)",
    messagesArea: "url('/branding/04_backgrounds/patterns/pattern_noise_texture.png'), linear-gradient(to bottom, #0a0e14, #0e1117)",
    inputArea: "linear-gradient(to bottom, #1A2F4F, #1E3A5F)",
    userBubble: "linear-gradient(to bottom right, #3399FF, #0066CC)",
    tyrBubble: "#1E2533",
    tyrBubbleBorder: "#2E3A4F",
    inputBg: "#0e1117",
    inputBorder: "#2E3A4F",
    text: "#FAFAFA",
    textSecondary: "#B3B3B3",
  },
  light: {
    card: "#F5F8FA",
    cardBorder: "#E1E8ED",
    header: "linear-gradient(135deg, #3399FF 0%, #0066CC 100%)",
    messagesArea: "url('/branding/04_backgrounds/patterns/pattern_dots.png'), linear-gradient(to bottom, #FFFFFF, #F5F8FA)",
    inputArea: "linear-gradient(to bottom, #F0F4F8, #E8EDF2)",
    userBubble: "linear-gradient(to bottom right, #3399FF, #0066CC)",
    tyrBubble: "#FFFFFF",
    tyrBubbleBorder: "#E1E8ED",
    inputBg: "#FFFFFF",
    inputBorder: "#D1D9E0",
    text: "#1A1A1A",
    textSecondary: "#666666",
  },
};

export function TYRChat() {
  const [mensajes, setMensajes] = useState<Message[]>([
    {
      id: "welcome",
      texto: "¡Hola! Soy TYR, tu asistente virtual del ITSE. ¿En qué puedo ayudarte hoy? Puedo informarte sobre carreras, admisiones, becas y más.",
      esUsuario: false,
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showSuggestions, setShowSuggestions] = useState(true);
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [currentConversationId, setCurrentConversationId] = useState<string | null>(null);
  const [showHistory, setShowHistory] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(true); // Por defecto modo oscuro
  const [isListening, setIsListening] = useState(false);
  const [isVoiceAvailable, setIsVoiceAvailable] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const recognitionRef = useRef<any>(null);

  // Tema actual
  const theme = isDarkMode ? THEMES.dark : THEMES.light;

  // Cargar conversaciones del localStorage al iniciar
  useEffect(() => {
    const savedConversations = localStorage.getItem(STORAGE_KEY);
    const savedCurrentId = localStorage.getItem(CURRENT_CONVERSATION_KEY);

    if (savedConversations) {
      const parsed = JSON.parse(savedConversations);
      // Convertir strings de fechas a objetos Date
      const conversationsWithDates = parsed.map((conv: any) => ({
        ...conv,
        createdAt: new Date(conv.createdAt),
        lastMessageAt: new Date(conv.lastMessageAt),
        messages: conv.messages.map((msg: any) => ({
          ...msg,
          timestamp: new Date(msg.timestamp),
        })),
      }));
      setConversations(conversationsWithDates);
    }

    if (savedCurrentId) {
      setCurrentConversationId(savedCurrentId);
    }
  }, []);

  // Guardar conversación actual cuando cambien los mensajes
  useEffect(() => {
    if (mensajes.length > 1) { // Solo guardar si hay más que el mensaje de bienvenida
      saveCurrentConversation();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mensajes]);

  // Inicializar reconocimiento de voz
  useEffect(() => {
    // Verificar si el navegador soporta Web Speech API con múltiples prefijos
    const SpeechRecognition =
      (window as any).SpeechRecognition ||
      (window as any).webkitSpeechRecognition ||
      (window as any).mozSpeechRecognition ||
      (window as any).msSpeechRecognition;

    if (SpeechRecognition) {
      try {
        const recognition = new SpeechRecognition();

        // Configuración para mejor compatibilidad
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = "es-ES"; // Español de España
        recognition.maxAlternatives = 1;

        recognition.onresult = (event: any) => {
          const transcript = event.results[0][0].transcript;
          setInputValue(transcript);
          setIsListening(false);
        };

        recognition.onerror = (event: any) => {
          console.error("Error en reconocimiento de voz:", event.error);
          let errorMsg = "Error en el reconocimiento de voz.";

          switch(event.error) {
            case 'not-allowed':
            case 'permission-denied':
              errorMsg = "Permiso de micrófono denegado. Activa el micrófono en la configuración.";
              break;
            case 'no-speech':
              errorMsg = "No se detectó voz. Intenta de nuevo.";
              break;
            case 'network':
              errorMsg = "Error de red. Verifica tu conexión.";
              break;
            case 'aborted':
              // No mostrar error si el usuario cancela
              break;
            default:
              errorMsg = `Error: ${event.error}`;
          }

          if (event.error !== 'aborted') {
            console.warn(errorMsg);
          }
          setIsListening(false);
        };

        recognition.onend = () => {
          setIsListening(false);
        };

        recognition.onspeechend = () => {
          recognition.stop();
        };

        recognitionRef.current = recognition;
        setIsVoiceAvailable(true);
        console.log("✅ Reconocimiento de voz inicializado correctamente");
      } catch (error) {
        console.error("Error al inicializar reconocimiento de voz:", error);
        setIsVoiceAvailable(false);
      }
    } else {
      console.warn("⚠️ Tu navegador no soporta Web Speech API. Usa Chrome, Edge o Safari.");
      setIsVoiceAvailable(false);
    }
  }, []);

  const saveCurrentConversation = () => {
    const conversationTitle = getConversationTitle(mensajes);
    const now = new Date();

    let updatedConversations = [...conversations];

    if (currentConversationId) {
      // Actualizar conversación existente
      const index = updatedConversations.findIndex(c => c.id === currentConversationId);
      if (index !== -1) {
        updatedConversations[index] = {
          ...updatedConversations[index],
          messages: mensajes,
          lastMessageAt: now,
          title: conversationTitle,
        };
      }
    } else {
      // Crear nueva conversación
      const newId = Date.now().toString();
      const newConversation: Conversation = {
        id: newId,
        title: conversationTitle,
        messages: mensajes,
        createdAt: now,
        lastMessageAt: now,
      };
      updatedConversations.unshift(newConversation);
      setCurrentConversationId(newId);
      localStorage.setItem(CURRENT_CONVERSATION_KEY, newId);
    }

    setConversations(updatedConversations);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(updatedConversations));
  };

  const getConversationTitle = (messages: Message[]): string => {
    // Usar el primer mensaje del usuario como título
    const firstUserMessage = messages.find(m => m.esUsuario);
    if (firstUserMessage) {
      return firstUserMessage.texto.slice(0, 40) + (firstUserMessage.texto.length > 40 ? "..." : "");
    }
    return "Nueva conversación";
  };

  const startNewConversation = () => {
    setMensajes([
      {
        id: "welcome",
        texto: "¡Hola! Soy TYR, tu asistente virtual del ITSE. ¿En qué puedo ayudarte hoy? Puedo informarte sobre carreras, admisiones, becas y más.",
        esUsuario: false,
        timestamp: new Date(),
      },
    ]);
    setCurrentConversationId(null);
    setShowSuggestions(true);
    setError(null);
    localStorage.removeItem(CURRENT_CONVERSATION_KEY);
  };

  const loadConversation = (conversationId: string) => {
    const conversation = conversations.find(c => c.id === conversationId);
    if (conversation) {
      setMensajes(conversation.messages);
      setCurrentConversationId(conversationId);
      setShowSuggestions(false);
      setShowHistory(false);
      localStorage.setItem(CURRENT_CONVERSATION_KEY, conversationId);
    }
  };

  // Auto-scroll al último mensaje (solo dentro del contenedor del chat)
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth", block: "nearest" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [mensajes, isLoading]);

  const enviarMensaje = async (mensajeTexto?: string) => {
    const texto = mensajeTexto || inputValue;
    if (!texto.trim() || isLoading) return;

    // Ocultar sugerencias después del primer mensaje del usuario
    if (showSuggestions) {
      setShowSuggestions(false);
    }

    const mensajeUsuario: Message = {
      id: Date.now().toString(),
      texto: texto,
      esUsuario: true,
      timestamp: new Date(),
    };

    setMensajes((prev) => [...prev, mensajeUsuario]);
    setInputValue("");
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          mensaje: texto,
        }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data: ChatResponse = await response.json();

      // Simular typing realista: delay basado en longitud de respuesta (40-60ms por palabra)
      const palabras = data.respuesta.split(" ").length;
      const typingDelay = Math.min(Math.max(palabras * 50, 500), 2000); // Entre 500ms y 2s

      await new Promise(resolve => setTimeout(resolve, typingDelay));

      const mensajeTYR: Message = {
        id: (Date.now() + 1).toString(),
        texto: data.respuesta,
        esUsuario: false,
        timestamp: new Date(),
        intencion: data.intencion,
        confianza: data.confianza,
      };

      setMensajes((prev) => [...prev, mensajeTYR]);
    } catch (err) {
      // Si falla la conexión al backend, usar respuestas mock (modo demo)
      console.warn("Backend no disponible, usando modo demo con respuestas mock");

      // Obtener respuesta mock basada en el mensaje
      const mockData = getMockResponse(texto);

      // Simular delay realista
      const palabras = mockData.respuesta.split(" ").length;
      const typingDelay = Math.min(Math.max(palabras * 50, 500), 2000);
      await new Promise(resolve => setTimeout(resolve, typingDelay));

      const mensajeTYR: Message = {
        id: (Date.now() + 1).toString(),
        texto: mockData.respuesta,
        esUsuario: false,
        timestamp: new Date(),
        intencion: mockData.intencion,
        confianza: mockData.confianza,
      };

      setMensajes((prev) => [...prev, mensajeTYR]);

      // Mostrar aviso discreto de que está en modo demo (opcional)
      setError(null); // No mostrar error, modo demo funciona bien
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      e.stopPropagation();
      enviarMensaje();
    }
  };

  const handleSubmit = (e?: React.FormEvent) => {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    enviarMensaje();
  };

  const handleSuggestionClick = (question: string) => {
    enviarMensaje(question);
  };

  // Función para controlar el reconocimiento de voz
  const toggleVoiceInput = () => {
    if (!recognitionRef.current) {
      // Detectar el navegador para dar mensaje específico
      const userAgent = navigator.userAgent.toLowerCase();

      if (userAgent.includes("firefox")) {
        alert(
          "❌ Firefox no soporta Web Speech API actualmente.\n\n" +
          "📱 Alternativas:\n" +
          "• Usa Google Chrome, Microsoft Edge o Safari\n" +
          "• Instala la extensión 'Voice Control for ChatGPT' en Firefox\n" +
          "• Usa un servicio de transcripción externo"
        );
      } else if (userAgent.includes("safari") && !userAgent.includes("chrome")) {
        alert("❌ Safari requiere permisos especiales. Verifica la configuración de privacidad.");
      } else {
        alert(
          "❌ Reconocimiento de voz no disponible.\n\n" +
          "✅ Navegadores compatibles:\n" +
          "• Google Chrome\n" +
          "• Microsoft Edge\n" +
          "• Safari (iOS/macOS)"
        );
      }
      return;
    }

    if (isListening) {
      recognitionRef.current.stop();
      setIsListening(false);
    } else {
      try {
        recognitionRef.current.start();
        setIsListening(true);
      } catch (error: any) {
        console.error("Error al iniciar reconocimiento de voz:", error);

        // Mensajes de error específicos
        if (error.name === "NotAllowedError") {
          alert(
            "🎤 Permiso denegado\n\n" +
            "Por favor permite el acceso al micrófono:\n" +
            "1. Haz clic en el ícono de candado/información en la barra de direcciones\n" +
            "2. Permite el acceso al micrófono\n" +
            "3. Recarga la página"
          );
        } else if (error.name === "InvalidStateError") {
          // Ya está grabando, detener primero
          recognitionRef.current.stop();
          setIsListening(false);
        } else {
          alert(`❌ Error al iniciar grabación: ${error.message || "Desconocido"}`);
        }

        setIsListening(false);
      }
    }
  };

  // Función para compartir conversación
  const shareConversation = async () => {
    // Crear texto plano de la conversación
    let conversationText = "🤖 TYR - Conversación ITSE\n\n";

    mensajes.forEach((mensaje) => {
      const sender = mensaje.esUsuario ? "👤 Usuario" : "🤖 TYR";
      const time = mensaje.timestamp.toLocaleTimeString("es-PA", {
        hour: "2-digit",
        minute: "2-digit",
      });
      conversationText += `${sender} (${time}):\n${mensaje.texto}\n\n`;
    });

    conversationText += "\n---\nGenerado por TYR - Asistente Virtual ITSE";

    // Intentar usar Web Share API si está disponible
    if (navigator.share) {
      try {
        await navigator.share({
          title: "Conversación con TYR",
          text: conversationText,
        });
      } catch (err) {
        // Si el usuario cancela, no hacer nada
        if ((err as Error).name !== "AbortError") {
          console.error("Error compartiendo:", err);
        }
      }
    } else {
      // Fallback: copiar al portapapeles
      try {
        await navigator.clipboard.writeText(conversationText);
        alert("✅ Conversación copiada al portapapeles");
      } catch (err) {
        console.error("Error copiando al portapapeles:", err);
        alert("❌ No se pudo copiar la conversación");
      }
    }
  };

  // Función para limpiar texto y hacerlo compatible con PDF
  const sanitizeTextForPDF = (text: string): string => {
    return text
      // Reemplazar bullets y símbolos especiales
      .replace(/•/g, "-")
      .replace(/●/g, "-")
      .replace(/○/g, "-")
      .replace(/►/g, ">")
      .replace(/▪/g, "-")
      .replace(/▫/g, "-")
      // Reemplazar emojis comunes con texto
      .replace(/📚/g, "[Libro]")
      .replace(/🎓/g, "[Graduacion]")
      .replace(/💼/g, "[Trabajo]")
      .replace(/🏫/g, "[Escuela]")
      .replace(/📝/g, "[Nota]")
      .replace(/✅/g, "[OK]")
      .replace(/❌/g, "[X]")
      .replace(/⭐/g, "*")
      .replace(/🔹/g, "-")
      .replace(/🔸/g, "-")
      // Reemplazar otros símbolos problemáticos
      .replace(/[""]/g, '"')
      .replace(/['']/g, "'")
      .replace(/–/g, "-")
      .replace(/—/g, "-")
      .replace(/…/g, "...")
      // Normalizar caracteres acentuados (mantenerlos pero asegurar encoding correcto)
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      // Mantener solo caracteres ASCII imprimibles y letras españolas comunes
      .replace(/[^\x20-\x7E\u00C0-\u00FF]/g, "");
  };

  const exportToPDF = () => {
    const doc = new jsPDF();
    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();
    const margin = 20;
    const maxWidth = pageWidth - 2 * margin;
    let yPosition = margin;

    // Título
    doc.setFontSize(18);
    doc.setFont("helvetica", "bold");
    doc.text("TYR - Conversacion ITSE", margin, yPosition);
    yPosition += 10;

    // Fecha
    doc.setFontSize(10);
    doc.setFont("helvetica", "normal");
    doc.text(`Fecha: ${new Date().toLocaleDateString("es-PA")}`, margin, yPosition);
    yPosition += 15;

    // Mensajes
    mensajes.forEach((mensaje) => {
      // Verificar si necesitamos nueva página
      if (yPosition > pageHeight - 40) {
        doc.addPage();
        yPosition = margin;
      }

      // Encabezado del mensaje
      doc.setFontSize(10);
      doc.setFont("helvetica", "bold");
      const remitente = mensaje.esUsuario ? "Usuario" : "TYR";
      const hora = mensaje.timestamp.toLocaleTimeString("es-PA", {
        hour: "2-digit",
        minute: "2-digit",
      });
      doc.text(`${remitente} - ${hora}`, margin, yPosition);
      yPosition += 6;

      // Contenido del mensaje (sanitizado)
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      const textoLimpio = sanitizeTextForPDF(mensaje.texto);
      const lines = doc.splitTextToSize(textoLimpio, maxWidth);
      doc.text(lines, margin + 5, yPosition);
      yPosition += lines.length * 5;

      // Metadata (solo para mensajes de TYR)
      if (!mensaje.esUsuario && mensaje.intencion) {
        doc.setFontSize(8);
        doc.setTextColor(100, 100, 100);
        const metadataText = `Intencion: ${mensaje.intencion} | Confianza: ${((mensaje.confianza || 0) * 100).toFixed(1)}%`;
        doc.text(
          sanitizeTextForPDF(metadataText),
          margin + 5,
          yPosition
        );
        doc.setTextColor(0, 0, 0);
        yPosition += 5;
      }

      yPosition += 5; // Espacio entre mensajes
    });

    // Footer en la última página
    doc.setFontSize(8);
    doc.setTextColor(150, 150, 150);
    doc.text(
      "TYR - Asistente Virtual ITSE | 98.93% precision",
      pageWidth / 2,
      pageHeight - 10,
      { align: "center" }
    );

    // Descargar
    const fileName = `TYR_Chat_${new Date().toISOString().split("T")[0]}.pdf`;
    doc.save(fileName);
  };

  return (
    <Card
      className="w-full max-w-[1000px] h-[850px] flex flex-col overflow-hidden transition-colors duration-300"
      style={{
        backgroundColor: theme.card,
        borderColor: theme.cardBorder,
        boxShadow: "0 30px 60px rgba(0, 102, 204, 0.2)",
      }}
    >
      {/* Header */}
      <div
        className="px-6 py-5 border-b backdrop-blur-lg transition-all duration-300"
        style={{
          background: theme.header,
          borderColor: isDarkMode ? "rgba(46, 90, 143, 0.5)" : "rgba(225, 232, 237, 0.5)",
        }}
      >
        <div className="flex items-center gap-4">
          <div className="relative">
            <div className="size-12 rounded-full bg-gradient-to-br from-[#FFFFFF]/30 to-[#FFFFFF]/10 flex items-center justify-center shadow-lg backdrop-blur-md border-2 border-[#FFFFFF]/20 overflow-hidden">
              <img
                src="/branding/01_logos/logo_icon_dark_bg.png"
                alt="TYR Logo"
                className="size-10 object-contain"
              />
            </div>
            <div className="absolute bottom-0 right-0 size-3.5 bg-[#00D26A] rounded-full border-2 border-[#0066CC]"></div>
          </div>
          <div className="flex-1">
            <h3
              className="text-[19px] text-[#FFFFFF] mb-0.5"
              style={{ fontFamily: "Inter", fontWeight: 700, letterSpacing: "-0.02em" }}
            >
              TYR - Asistente ITSE
            </h3>
            <div className="flex items-center gap-2">
              <div className="flex items-center gap-1.5">
                <div className="size-2 bg-[#00D26A] rounded-full animate-pulse"></div>
                <p
                  className="text-[13px] text-[#FFFFFF]/90"
                  style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
                >
                  En línea
                </p>
              </div>
              <span className="text-[#FFFFFF]/50">•</span>
              <p
                className="text-[13px] text-[#FFFFFF]/90"
                style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
              >
                98.93% precisión
              </p>
            </div>
          </div>

          {/* Botones de control */}
          <div className="flex items-center gap-2">
            <button
              onClick={() => setIsDarkMode(!isDarkMode)}
              className="p-2 hover:bg-[#FFFFFF]/10 rounded-lg transition-colors"
              title={isDarkMode ? "Modo claro" : "Modo oscuro"}
            >
              {isDarkMode ? (
                <Sun className="size-5 text-[#FFFFFF]" />
              ) : (
                <Moon className="size-5 text-[#FFFFFF]" />
              )}
            </button>
            <button
              onClick={shareConversation}
              disabled={mensajes.length <= 1}
              className="p-2 hover:bg-[#FFFFFF]/10 rounded-lg transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
              title="Compartir conversación"
            >
              <Share2 className="size-5 text-[#FFFFFF]" />
            </button>
            <button
              onClick={exportToPDF}
              disabled={mensajes.length <= 1}
              className="p-2 hover:bg-[#FFFFFF]/10 rounded-lg transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
              title="Descargar chat como PDF"
            >
              <Download className="size-5 text-[#FFFFFF]" />
            </button>
            <button
              onClick={startNewConversation}
              className="p-2 hover:bg-[#FFFFFF]/10 rounded-lg transition-colors"
              title="Nueva conversación"
            >
              <RefreshCw className="size-5 text-[#FFFFFF]" />
            </button>
            <button
              onClick={() => setShowHistory(!showHistory)}
              className="p-2 hover:bg-[#FFFFFF]/10 rounded-lg transition-colors relative"
              title="Historial"
            >
              <History className="size-5 text-[#FFFFFF]" />
              {conversations.length > 0 && (
                <span className="absolute top-1 right-1 size-2 bg-[#00D26A] rounded-full"></span>
              )}
            </button>
          </div>
        </div>

        {/* Dropdown de historial */}
        {showHistory && conversations.length > 0 && (
          <div className="mt-4 max-h-[300px] overflow-y-auto bg-[#FFFFFF]/10 rounded-lg p-2 backdrop-blur-md">
            <p className="text-[12px] text-[#FFFFFF]/80 mb-2 px-2" style={{ fontFamily: "IBM Plex Sans", fontWeight: 600 }}>
              Conversaciones anteriores ({conversations.length})
            </p>
            {conversations.map((conv) => (
              <button
                key={conv.id}
                onClick={() => loadConversation(conv.id)}
                className={`w-full text-left px-3 py-2 rounded-md mb-1 transition-all ${
                  currentConversationId === conv.id
                    ? "bg-[#3399FF]/30 border border-[#3399FF]/50"
                    : "hover:bg-[#FFFFFF]/10"
                }`}
              >
                <p className="text-[13px] text-[#FFFFFF] font-medium truncate" style={{ fontFamily: "IBM Plex Sans" }}>
                  {conv.title}
                </p>
                <p className="text-[11px] text-[#FFFFFF]/60" style={{ fontFamily: "IBM Plex Sans" }}>
                  {conv.lastMessageAt.toLocaleDateString("es-PA")} • {conv.messages.length} mensajes
                </p>
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Messages Area */}
      <CardContent
        className="flex-1 overflow-y-auto p-8 space-y-6 transition-colors duration-300"
        style={{ background: theme.messagesArea }}
      >
        {mensajes.map((mensaje) => (
          <div
            key={mensaje.id}
            className={`flex gap-4 items-end ${mensaje.esUsuario ? "flex-row-reverse" : "flex-row"}`}
          >
            {/* Avatar */}
            <div
              className={`size-10 rounded-full flex items-center justify-center flex-shrink-0 shadow-lg overflow-hidden ${
                mensaje.esUsuario
                  ? "bg-gradient-to-br from-[#3399FF] to-[#0066CC]"
                  : "bg-gradient-to-br from-[#0066CC] to-[#004C99]"
              }`}
            >
              {mensaje.esUsuario ? (
                <User className="size-5 text-[#FFFFFF]" />
              ) : (
                <img
                  src="/branding/03_illustrations/avatares/avatar_bot_default.png"
                  alt="TYR Avatar"
                  className="size-full object-cover"
                />
              )}
            </div>

            {/* Message Bubble Container */}
            <div className={`flex flex-col gap-1 max-w-[75%] ${mensaje.esUsuario ? "items-end" : "items-start"}`}>
              {/* Message Bubble */}
              <div
                className={`relative rounded-[20px] px-5 py-3.5 shadow-lg transition-all hover:shadow-xl ${
                  mensaje.esUsuario
                    ? "text-[#FFFFFF] rounded-br-[6px]"
                    : `rounded-bl-[6px] ${isDarkMode ? "border" : "border"}`
                }`}
                style={{
                  backdropFilter: "blur(10px)",
                  background: mensaje.esUsuario ? theme.userBubble : theme.tyrBubble,
                  borderColor: mensaje.esUsuario ? "transparent" : theme.tyrBubbleBorder,
                  color: mensaje.esUsuario ? "#FFFFFF" : theme.text,
                }}
              >
                {mensaje.esUsuario ? (
                  <p
                    className="text-[15px] leading-[1.6] whitespace-pre-wrap"
                    style={{ fontFamily: "IBM Plex Sans", fontWeight: 400 }}
                  >
                    {mensaje.texto}
                  </p>
                ) : (
                  <div
                    className="text-[15px] leading-[1.6] prose prose-invert prose-sm max-w-none"
                    style={{ fontFamily: "IBM Plex Sans", fontWeight: 400 }}
                  >
                    <ReactMarkdown
                      remarkPlugins={[remarkGfm]}
                      components={{
                        // Estilos custom para elementos markdown
                        strong: ({ children }) => <strong className="font-bold text-[#3399FF]">{children}</strong>,
                        em: ({ children }) => <em className="italic text-[#FAFAFA]">{children}</em>,
                        a: ({ href, children }) => (
                          <a href={href} target="_blank" rel="noopener noreferrer" className="text-[#3399FF] underline hover:text-[#66B3FF]">
                            {children}
                          </a>
                        ),
                        ul: ({ children }) => <ul className="list-disc list-inside my-2 space-y-1">{children}</ul>,
                        ol: ({ children }) => <ol className="list-decimal list-inside my-2 space-y-1">{children}</ol>,
                        li: ({ children }) => <li className="text-[#FAFAFA]">{children}</li>,
                        code: ({ children }) => (
                          <code className="bg-[#0066CC]/20 text-[#3399FF] px-1.5 py-0.5 rounded text-[13px] font-mono">
                            {children}
                          </code>
                        ),
                        pre: ({ children }) => (
                          <pre className="bg-[#0a0e14] p-3 rounded-lg overflow-x-auto my-2 border border-[#2E3A4F]">
                            {children}
                          </pre>
                        ),
                      }}
                    >
                      {mensaje.texto}
                    </ReactMarkdown>
                  </div>
                )}

                {/* Metadata (solo para mensajes de TYR) */}
                {!mensaje.esUsuario && mensaje.intencion && (
                  <div className="mt-3 pt-3 border-t border-[#2E3A4F]/50">
                    <div className="flex items-center gap-2 text-[11px] text-[#8B96A8]">
                      <span className="px-2 py-0.5 bg-[#0066CC]/20 rounded-full text-[#3399FF] font-medium">
                        {mensaje.intencion}
                      </span>
                      <span className="text-[#B3B3B3]">•</span>
                      <span className="font-medium text-[#3399FF]">
                        {((mensaje.confianza || 0) * 100).toFixed(1)}% confianza
                      </span>
                    </div>
                  </div>
                )}
              </div>

              {/* Timestamp */}
              <p
                className={`text-[11px] px-2 ${
                  mensaje.esUsuario ? "text-[#7A8499]" : "text-[#6B7280]"
                }`}
                style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
              >
                {mensaje.timestamp.toLocaleTimeString("es-PA", {
                  hour: "2-digit",
                  minute: "2-digit",
                })}
              </p>
            </div>
          </div>
        ))}

        {/* Loading Indicator con animación mejorada */}
        {isLoading && (
          <div className="flex gap-4 items-end animate-fade-in">
            <div className="size-10 rounded-full bg-gradient-to-br from-[#0066CC] to-[#004C99] flex items-center justify-center shadow-lg overflow-hidden">
              <img
                src="/branding/03_illustrations/avatares/avatar_bot_default.png"
                alt="TYR Avatar"
                className="size-full object-cover"
              />
            </div>
            <div
              className="rounded-[20px] rounded-bl-[6px] px-5 py-3.5 shadow-lg backdrop-blur-md"
              style={{
                background: isDarkMode
                  ? "linear-gradient(135deg, rgba(30, 37, 51, 0.95) 0%, rgba(20, 25, 35, 0.95) 100%)"
                  : "linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(245, 248, 250, 0.95) 100%)",
                border: `1px solid ${isDarkMode ? "#2E3A4F" : "#E0E7EF"}`,
              }}
            >
              <div className="flex items-center gap-3">
                <div className="flex items-center gap-1">
                  <div className="w-2 h-2 bg-[#0066CC] rounded-full animate-bounce" style={{ animationDelay: "0ms" }}></div>
                  <div className="w-2 h-2 bg-[#3399FF] rounded-full animate-bounce" style={{ animationDelay: "150ms" }}></div>
                  <div className="w-2 h-2 bg-[#66B3FF] rounded-full animate-bounce" style={{ animationDelay: "300ms" }}></div>
                </div>
                <p
                  className="text-[15px]"
                  style={{
                    fontFamily: "IBM Plex Sans",
                    color: isDarkMode ? "#B3B3B3" : "#64748B"
                  }}
                >
                  TYR está escribiendo...
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Error Message */}
        {error && (
          <div className="mx-auto max-w-md">
            <div className="bg-red-500/10 border-2 border-red-500/30 rounded-[16px] px-5 py-4 shadow-lg backdrop-blur-sm">
              <p
                className="text-[13px] text-red-400 text-center"
                style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
              >
                ⚠️ {error}
              </p>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </CardContent>

      {/* Input Area */}
      <div
        className="px-6 py-5 border-t transition-colors duration-300"
        style={{
          background: theme.inputArea,
          borderColor: isDarkMode ? "rgba(46, 90, 143, 0.5)" : "rgba(225, 232, 237, 0.5)",
        }}
      >
        {/* Sugerencias de preguntas */}
        {showSuggestions && (
          <div className="mb-4">
            <p
              className="text-[12px] text-[#B3B3B3] mb-2"
              style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
            >
              Preguntas sugeridas:
            </p>
            <div className="flex flex-wrap gap-2">
              {SUGGESTED_QUESTIONS.map((question, index) => (
                <button
                  key={index}
                  onClick={() => handleSuggestionClick(question)}
                  disabled={isLoading}
                  className="px-4 py-2 bg-[#0066CC]/20 hover:bg-[#0066CC]/40 text-[#3399FF] text-[13px] rounded-full border border-[#3399FF]/30 transition-all duration-200 hover:border-[#3399FF]/60 hover:shadow-md disabled:opacity-50 disabled:cursor-not-allowed"
                  style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
                >
                  {question}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Mensaje informativo si la voz no está disponible (solo en Firefox) */}
        {!isVoiceAvailable && navigator.userAgent.toLowerCase().includes("firefox") && (
          <div className="mb-3 p-3 bg-orange-500/10 border border-orange-500/30 rounded-lg">
            <p className="text-[12px] text-orange-400" style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}>
              ℹ️ <strong>Firefox no soporta entrada de voz.</strong> Usa Chrome, Edge o Safari para esta función.
            </p>
          </div>
        )}

        <form onSubmit={(e) => { e.preventDefault(); handleSubmit(); }} className="flex gap-3 items-center">
          <div className="flex-1 relative">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder={isListening ? "Escuchando..." : "Escribe tu mensaje..."}
              disabled={isLoading}
              className={`w-full rounded-[24px] px-6 py-3.5 text-[15px] focus:outline-none focus:border-[#3399FF] focus:ring-2 focus:ring-[#3399FF]/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-inner border-2 ${
                isVoiceAvailable ? "pr-14" : ""
              }`}
              style={{
                fontFamily: "IBM Plex Sans",
                fontWeight: 400,
                backgroundColor: theme.inputBg,
                borderColor: theme.inputBorder,
                color: theme.text,
              }}
            />
            {/* Botón de micrófono dentro del input - Solo visible si está disponible */}
            {isVoiceAvailable && (
              <button
                type="button"
                onClick={toggleVoiceInput}
                disabled={isLoading}
                className={`absolute right-3 top-1/2 -translate-y-1/2 p-2 rounded-full transition-all ${
                  isListening
                    ? "bg-red-500 hover:bg-red-600 animate-pulse"
                    : "bg-[#3399FF]/20 hover:bg-[#3399FF]/40"
                } disabled:opacity-40 disabled:cursor-not-allowed`}
                title={isListening ? "Detener grabación" : "Hablar"}
              >
                {isListening ? (
                  <MicOff className="size-4 text-white" />
                ) : (
                  <Mic className="size-4 text-[#3399FF]" />
                )}
              </button>
            )}
          </div>
          <Button
            type="button"
            onClick={(e) => { e.preventDefault(); handleSubmit(); }}
            disabled={isLoading || !inputValue.trim()}
            className={`bg-gradient-to-br from-[#3399FF] to-[#0066CC] hover:from-[#0066CC] hover:to-[#004C99] text-[#FFFFFF] size-12 rounded-full transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed shadow-lg hover:shadow-xl hover:scale-105 active:scale-95 flex items-center justify-center ${
              inputValue.trim() && !isLoading ? "animate-pulse-subtle" : ""
            }`}
          >
            {isLoading ? (
              <div className="flex items-center justify-center">
                <div className="w-2 h-2 bg-white rounded-full animate-bounce mr-1" style={{ animationDelay: "0ms" }}></div>
                <div className="w-2 h-2 bg-white rounded-full animate-bounce mr-1" style={{ animationDelay: "150ms" }}></div>
                <div className="w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: "300ms" }}></div>
              </div>
            ) : (
              <Send className="size-5" />
            )}
          </Button>
        </form>

        <p
          className="text-[11px] text-[#7A8499] mt-3 text-center"
          style={{ fontFamily: "IBM Plex Sans", fontWeight: 500 }}
        >
          TYR usa IA para responder • Las respuestas son orientativas
        </p>
      </div>
    </Card>
  );
}
