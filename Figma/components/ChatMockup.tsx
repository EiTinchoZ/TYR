import { MessageCircle, Users, Send } from "lucide-react";
import { motion } from "motion/react";

export function ChatMockup() {
  return (
    <motion.div
      initial={{ opacity: 0, x: 100 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className="w-full max-w-[450px] mx-auto"
      style={{
        background: '#1E3A5F',
        border: '2px solid #2E5A8F',
        borderRadius: '16px',
        boxShadow: '0 20px 60px rgba(0, 102, 204, 0.3)',
        overflow: 'hidden'
      }}
    >
      {/* Header */}
      <div className="bg-gradient-to-r from-[#0066CC] to-[#004C99] p-4 flex items-center gap-3">
        <div className="size-10 rounded-full bg-white/10 flex items-center justify-center">
          <MessageCircle className="size-6 text-[#FAFAFA]" />
        </div>
        <div className="text-[#FAFAFA]">
          <p className="font-semibold" style={{ fontFamily: 'Inter', fontWeight: 600 }}>TYR - Asistente Virtual</p>
          <p className="text-xs opacity-90" style={{ fontFamily: 'IBM Plex Sans' }}>En línea</p>
        </div>
      </div>

      {/* Messages */}
      <div className="p-6 space-y-4 bg-[#0e1117] min-h-[400px]">
        {/* Primer mensaje del bot - Bienvenida */}
        <div className="flex gap-3">
          <div className="size-8 rounded-full bg-gradient-to-br from-[#0066CC] to-[#004C99] flex items-center justify-center flex-shrink-0">
            <MessageCircle className="size-4 text-[#FAFAFA]" />
          </div>
          <div className="bg-[#262730] rounded-2xl rounded-tl-sm p-4 border border-[#31333F] max-w-[80%]">
            <p className="text-[#FAFAFA] text-sm" style={{ fontFamily: 'IBM Plex Sans', lineHeight: 1.5 }}>
              ¡Hola! 👋 Soy TYR, tu asistente virtual del ITSE. ¿En qué puedo ayudarte hoy?
            </p>
          </div>
        </div>

        {/* Mensaje del usuario */}
        <div className="flex gap-3 justify-end">
          <div className="bg-[#0066CC] rounded-2xl rounded-tr-sm p-4 max-w-[80%]">
            <p className="text-[#FAFAFA] text-sm" style={{ fontFamily: 'IBM Plex Sans', lineHeight: 1.5 }}>
              Cuéntame sobre Big Data
            </p>
          </div>
          <div className="size-8 rounded-full bg-[#31333F] flex items-center justify-center flex-shrink-0">
            <Users className="size-4 text-[#B3B3B3]" />
          </div>
        </div>

        {/* Respuesta del bot sobre Big Data */}
        <div className="flex gap-3">
          <div className="size-8 rounded-full bg-gradient-to-br from-[#0066CC] to-[#004C99] flex items-center justify-center flex-shrink-0">
            <MessageCircle className="size-4 text-[#FAFAFA]" />
          </div>
          <div className="bg-[#262730] rounded-2xl rounded-tl-sm p-4 border border-[#31333F] max-w-[80%]">
            <p className="text-[#FAFAFA] text-sm" style={{ fontFamily: 'IBM Plex Sans', lineHeight: 1.5 }}>
              ¡Excelente elección! 🎓 La <strong>T.S. en Big Data</strong> es una carrera de 3 años donde aprenderás a manejar grandes volúmenes de datos, análisis predictivo y herramientas como Python, Hadoop y Spark. ¿Te gustaría conocer los requisitos de admisión o el plan de estudios?
            </p>
          </div>
        </div>

        {/* Indicador de escritura */}
        <div className="flex gap-3">
          <div className="size-8 rounded-full bg-gradient-to-br from-[#0066CC] to-[#004C99] flex items-center justify-center flex-shrink-0">
            <MessageCircle className="size-4 text-[#FAFAFA]" />
          </div>
          <div className="bg-[#262730] rounded-2xl rounded-tl-sm p-4 border border-[#31333F]">
            <div className="flex gap-1">
              <motion.div
                className="size-2 rounded-full bg-[#B3B3B3]"
                animate={{ opacity: [0.3, 1, 0.3] }}
                transition={{ duration: 1.5, repeat: Infinity, delay: 0 }}
              />
              <motion.div
                className="size-2 rounded-full bg-[#B3B3B3]"
                animate={{ opacity: [0.3, 1, 0.3] }}
                transition={{ duration: 1.5, repeat: Infinity, delay: 0.2 }}
              />
              <motion.div
                className="size-2 rounded-full bg-[#B3B3B3]"
                animate={{ opacity: [0.3, 1, 0.3] }}
                transition={{ duration: 1.5, repeat: Infinity, delay: 0.4 }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Input simulado */}
      <div className="p-4 border-t border-[#31333F] bg-[#262730]">
        <div className="flex gap-2 items-center bg-[#0e1117] rounded-full px-4 py-3 border border-[#31333F]">
          <input
            type="text"
            placeholder="Escribe tu pregunta..."
            className="flex-1 bg-transparent outline-none text-[#FAFAFA] placeholder:text-[#B3B3B3] text-sm"
            style={{ fontFamily: 'IBM Plex Sans' }}
            disabled
          />
          <div className="size-8 rounded-full bg-[#0066CC] hover:bg-[#004C99] flex items-center justify-center cursor-pointer transition-colors">
            <Send className="size-4 text-[#FAFAFA]" />
          </div>
        </div>
      </div>
    </motion.div>
  );
}
