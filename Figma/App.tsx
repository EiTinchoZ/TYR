import { lazy, Suspense, useEffect, useState } from "react";
import { ChatMockup } from "./components/ChatMockup";
import { StatsCard } from "./components/StatsCard";
import { FeatureCard } from "./components/FeatureCard";
import { PersonaCard } from "./components/PersonaCard";
import { Button } from "./components/ui/button";
import { Card, CardContent } from "./components/ui/card";
import { Badge } from "./components/ui/badge";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./components/ui/accordion";
import { Dialog, DialogContent } from "./components/ui/dialog";
import { MessageCircle, BookOpen, Users, Clock, GraduationCap, ArrowRight, CheckCircle, MessageSquare, Sparkles } from "lucide-react";
import { Header } from "./components/Header";
import { motion } from "motion/react";
import { useScrollAnimation } from "./hooks/useScrollAnimation";

// Lazy load del componente TYRChat para mejorar performance
const TYRChat = lazy(() => import("./components/TYRChat").then(module => ({ default: module.TYRChat })));

export default function App() {
  // Estado para controlar el modal del chat
  const [isChatOpen, setIsChatOpen] = useState(false);

  // Asegurar que la página siempre inicie en la parte superior
  useEffect(() => {
    // Forzar scroll al inicio después de que todo cargue
    window.scrollTo(0, 0);
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    
    // Prevenir cualquier scroll automático
    const preventScroll = () => {
      window.scrollTo(0, 0);
    };
    
    // Ejecutar varias veces para asegurar
    setTimeout(preventScroll, 0);
    setTimeout(preventScroll, 100);
    setTimeout(preventScroll, 300);
    
  }, []);
  
  // Prevenir scroll durante la carga inicial
  useEffect(() => {
    const preventAutoScroll = (e: Event) => {
      window.scrollTo(0, 0);
      e.preventDefault();
    };
    
    // Prevenir scroll por un momento al cargar
    window.addEventListener('scroll', preventAutoScroll, { passive: false });
    
    const cleanup = setTimeout(() => {
      window.removeEventListener('scroll', preventAutoScroll);
    }, 500);
    
    return () => {
      clearTimeout(cleanup);
      window.removeEventListener('scroll', preventAutoScroll);
    };
  }, []);
  return (
    <div className="min-h-screen bg-[#0e1117]">
      {/* Header */}
      <Header />

      {/* Hero Section con gradient animado */}
      <section
        id="hero"
        className="min-h-[100vh] flex items-center pt-[80px] md:pt-[64px] relative overflow-hidden"
        style={{
          background: 'linear-gradient(135deg, #0066CC 0%, #004C99 50%, #0066CC 100%)',
          backgroundImage: 'url(/branding/04_backgrounds/hero_bg_neural_network.png), linear-gradient(135deg, #0066CC 0%, #004C99 50%, #0066CC 100%)',
          backgroundSize: '200% 200%, cover',
          backgroundPosition: 'center',
          backgroundBlendMode: 'overlay',
          animation: 'gradient-shift 8s ease infinite'
        }}
      >
        <div className="container mx-auto px-4 md:px-6 lg:px-8 py-8 md:py-12">
          <div className="grid lg:grid-cols-2 gap-8 md:gap-12 items-center">
            {/* COLUMNA IZQUIERDA */}
            <div className="space-y-4 md:space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0 }}
                className="flex items-center gap-4"
              >
                <img
                  src="/branding/01_logos/logo_icon_dark_bg.png"
                  alt="TYR Logo"
                  className="w-16 h-16 md:w-20 md:h-20 object-contain rounded-2xl animate-float"
                />
                <h1
                  className="text-[32px] md:text-[40px] lg:text-[48px] text-[#FAFAFA]"
                  style={{ fontFamily: 'Inter', fontWeight: 700, lineHeight: 1.2 }}
                >
                  Conoce TYR
                </h1>
              </motion.div>
              
              <motion.h2 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0.1 }}
                className="text-[18px] md:text-[20px] lg:text-[24px] text-[#FAFAFA]" 
                style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400, opacity: 0.95, lineHeight: 1.5 }}
              >
                Tu asistente virtual para explorar las carreras del ITSE
              </motion.h2>

              <motion.p 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0.2 }}
                className="text-[14px] md:text-[16px] text-[#B3B3B3]" 
                style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400, lineHeight: 1.6 }}
              >
                Descubre información sobre 16 carreras técnicas, procesos de admisión, 
                becas y servicios del ITSE. Disponible 24/7, sin registro, con 98.93% 
                de precisión.
              </motion.p>

              <motion.div 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0.3 }}
                className="space-y-2 pt-2"
              >
                <div className="flex items-center gap-2 text-[#FAFAFA] group">
                  <CheckCircle className="size-5 text-[#3399FF] flex-shrink-0 transition-transform duration-300 group-hover:scale-110" />
                  <span className="text-[14px] md:text-[16px]" style={{ fontFamily: 'IBM Plex Sans' }}>Gratis y accesible 24/7</span>
                </div>
                <div className="flex items-center gap-2 text-[#FAFAFA] group">
                  <CheckCircle className="size-5 text-[#3399FF] flex-shrink-0 transition-transform duration-300 group-hover:scale-110" />
                  <span className="text-[14px] md:text-[16px]" style={{ fontFamily: 'IBM Plex Sans' }}>Sin necesidad de registro</span>
                </div>
                <div className="flex items-center gap-2 text-[#FAFAFA] group">
                  <CheckCircle className="size-5 text-[#3399FF] flex-shrink-0 transition-transform duration-300 group-hover:scale-110" />
                  <span className="text-[14px] md:text-[16px]" style={{ fontFamily: 'IBM Plex Sans' }}>Respuestas instantáneas</span>
                </div>
                <div className="flex items-center gap-2 text-[#FAFAFA] group">
                  <CheckCircle className="size-5 text-[#3399FF] flex-shrink-0 transition-transform duration-300 group-hover:scale-110" />
                  <span className="text-[14px] md:text-[16px]" style={{ fontFamily: 'IBM Plex Sans' }}>98.93% de precisión</span>
                </div>
              </motion.div>

              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0.4 }}
                className="flex flex-col sm:flex-row gap-3 md:gap-4 pt-4"
              >
                <button
                  onClick={() => setIsChatOpen(true)}
                  className="w-full sm:w-auto bg-[#FFFFFF] text-[#0066CC] px-[32px] py-[12px] rounded-[24px] transition-all duration-300 hover:scale-105 hover:shadow-[0_20px_60px_rgba(255,255,255,0.6)] active:scale-95 cursor-pointer flex items-center justify-center gap-2 animate-glow"
                  style={{
                    fontFamily: 'IBM Plex Sans',
                    fontSize: '16px',
                    fontWeight: 600
                  }}
                >
                  Probar TYR Ahora
                  <ArrowRight className="size-5" />
                </button>
                <button
                  onClick={() => setIsChatOpen(true)}
                  className="w-full sm:w-auto bg-transparent border-2 border-[#FFFFFF] text-[#FFFFFF] px-[32px] py-[12px] rounded-[24px] transition-all duration-300 hover:bg-[#FFFFFF] hover:text-[#0066CC] hover:scale-105 cursor-pointer flex items-center justify-center gap-2"
                  style={{
                    fontFamily: 'IBM Plex Sans',
                    fontSize: '16px',
                    fontWeight: 600
                  }}
                >
                  Ver Demo (2 min)
                </button>
              </motion.div>
            </div>

            {/* COLUMNA DERECHA - Chat Preview */}
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: 0.3 }}
              className="relative hidden lg:block"
            >
              <ChatMockup />
            </motion.div>
          </div>
        </div>
      </section>

      {/* Estadísticas Section */}
      <section className="bg-[#0e1117] py-[48px] md:py-[64px] lg:py-[80px] px-4 md:px-6 lg:px-8">
        <div className="container mx-auto max-w-6xl">
          {/* Feature Cards Visuales Destacadas */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div className="relative overflow-hidden rounded-2xl">
              <img
                src="/branding/03_illustrations/feature_cards/feature_card_accuracy.png"
                alt="98.93% Precisión"
                className="w-full h-auto rounded-2xl"
                loading="lazy"
              />
            </div>
            <div className="relative overflow-hidden rounded-2xl">
              <img
                src="/branding/03_illustrations/feature_cards/feature_card_24_7.png"
                alt="Disponible 24/7"
                className="w-full h-auto rounded-2xl"
                loading="lazy"
              />
            </div>
            <div className="relative overflow-hidden rounded-2xl">
              <img
                src="/branding/03_illustrations/feature_cards/feature_card_tests.png"
                alt="59 Tests Passing"
                className="w-full h-auto rounded-2xl"
                loading="lazy"
              />
            </div>
          </div>

          {/* Stats Cards Adicionales */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6 lg:gap-8">
            <StatsCard number="4,358" label="Consultas Entrenadas" />
            <StatsCard number="16" label="Carreras Disponibles" />
            <StatsCard number="100%" label="Tolerancia a Errores" />
          </div>
        </div>
      </section>

      {/* Características Section */}
      <section 
        className="py-[48px] md:py-[72px] lg:py-[96px] px-4 md:px-6 lg:px-8"
        style={{
          background: 'linear-gradient(180deg, #0e1117 0%, #1a1d29 100%)'
        }}
      >
        <div className="container mx-auto max-w-6xl">
          <h2 
            className="text-[28px] md:text-[32px] lg:text-[36px] text-[#FAFAFA] text-center mb-[48px] md:mb-[56px] lg:mb-[64px]"
            style={{ 
              fontFamily: 'Inter', 
              fontWeight: 700,
              lineHeight: 1.2
            }}
          >
            ¿Qué puede hacer TYR por ti?
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-[24px]">
            <FeatureCard
              iconSrc="/branding/02_icons/features/icon_01_carreras.png"
              title="Explora 16 Carreras Técnicas"
              description="Descubre todas las opciones académicas disponibles, desde Big Data hasta Diseño Gráfico. Información detallada sobre cada programa."
            />
            <FeatureCard
              iconSrc="/branding/02_icons/features/icon_02_inscripcion.png"
              title="Proceso de Admisión Claro"
              description="Conoce paso a paso cómo inscribirte, requisitos, fechas importantes y documentación necesaria para tu ingreso."
            />
            <FeatureCard
              iconSrc="/branding/02_icons/features/icon_03_becas.png"
              title="Opciones de Financiamiento"
              description="Explora becas, planes de pago, descuentos disponibles y opciones de financiamiento para hacer realidad tu educación."
            />
            <FeatureCard
              iconSrc="/branding/02_icons/features/icon_06_itse.png"
              title="Todo sobre el ITSE"
              description="Información completa sobre instalaciones, horarios, servicios estudiantiles, ubicación y todo lo que necesitas saber."
            />
            <FeatureCard
              iconSrc="/branding/02_icons/features/icon_08_speed.png"
              title="Respuestas Instantáneas"
              description="Sin esperas ni formularios complicados. Obtén respuestas precisas a tus preguntas en segundos, 24/7."
            />
            <FeatureCard
              iconSrc="/branding/02_icons/features/icon_09_accuracy.png"
              title="Confiable y Preciso"
              description="Entrenado con información oficial del ITSE. 98.93% de precisión en más de 4,358 consultas procesadas."
            />
          </div>
        </div>
      </section>

      {/* Demo Section */}
      <section className="bg-[#0e1117] py-[96px] px-[32px]">
        <div className="container mx-auto max-w-6xl text-center">
          <h2 
            className="text-[36px] text-[#FAFAFA] mb-[48px]"
            style={{ 
              fontFamily: 'Inter', 
              fontWeight: 700,
              lineHeight: 1.2
            }}
          >
            Pruébalo directamente aquí
          </h2>

          <div className="mx-auto flex justify-center">
            <Suspense fallback={
              <div className="flex items-center justify-center p-8">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-[#0066CC]"></div>
              </div>
            }>
              <TYRChat />
            </Suspense>
          </div>

          <p 
            className="text-[16px] text-[#B3B3B3] mt-[24px]"
            style={{ 
              fontFamily: 'IBM Plex Sans',
              fontWeight: 400
            }}
          >
            Mira cómo TYR responde a consultas reales
          </p>
        </div>
      </section>

      {/* Personas Section */}
      <section 
        className="py-[96px] px-[32px]"
        style={{
          background: 'linear-gradient(180deg, #0e1117 0%, #1a1d29 100%)'
        }}
      >
        <div className="container mx-auto max-w-6xl">
          <h2 
            className="text-[36px] text-[#FAFAFA] text-center mb-[64px]"
            style={{ 
              fontFamily: 'Inter', 
              fontWeight: 700,
              lineHeight: 1.2
            }}
          >
            ¿Quién puede usar TYR?
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-[32px]">
            <PersonaCard
              illustrationSrc="/branding/03_illustrations/personas/persona_maria_estudiante.png"
              title="Estudiante"
              metadata="18 años"
              quote="Necesito info rápida sobre carreras tech sin complicarme"
              name="María"
              location="Panamá"
            />
            <PersonaCard
              illustrationSrc="/branding/03_illustrations/personas/ersona_roberto_padre.png"
              title="Padre de Familia"
              metadata="45 años"
              quote="¿Cuánto cuesta la matrícula y qué becas hay disponibles?"
              name="Roberto"
              location="Panamá"
            />
            <PersonaCard 
              emoji="🧭"
              title="Orientador Vocacional"
              metadata="35 años"
              quote="Necesito datos actualizados para orientar mejor a mis estudiantes"
              name="Luis Rodríguez"
              location="Panamá"
            />
            <PersonaCard 
              emoji="👨‍🏫"
              title="Docente"
              metadata="40 años"
              quote="Consulto información sobre programas académicos constantemente"
              name="Ana Morales"
              location="Panamá"
            />
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="bg-[#0e1117] py-[96px] px-[32px]">
        <div className="container mx-auto max-w-[700px]">
          <h2 
            className="text-[36px] text-[#FAFAFA] text-center mb-[64px]"
            style={{ 
              fontFamily: 'Inter', 
              fontWeight: 700,
              lineHeight: 1.2
            }}
          >
            Preguntas Frecuentes
          </h2>
          
          <Accordion type="single" collapsible className="space-y-[12px]">
            <AccordionItem 
              value="item-1" 
              className="bg-[#262730] border border-[#31333F] rounded-[12px] px-[24px] data-[state=open]:border-[#0066CC]"
            >
              <AccordionTrigger 
                className="text-[#FAFAFA] hover:no-underline py-[20px]"
                style={{ 
                  fontFamily: 'Inter', 
                  fontWeight: 600,
                  fontSize: '18px'
                }}
              >
                ¿TYR es gratis?
              </AccordionTrigger>
              <AccordionContent 
                className="text-[#B3B3B3] pb-[20px]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  fontSize: '14px',
                  lineHeight: 1.6
                }}
              >
                Sí, TYR es completamente gratis. No necesitas pagar nada ni registrarte. Puedes hacer todas las preguntas que quieras sobre el ITSE, sus carreras, admisiones, becas y servicios sin ningún costo. Está disponible 24/7 para ayudarte.
              </AccordionContent>
            </AccordionItem>

            <AccordionItem 
              value="item-2" 
              className="bg-[#262730] border border-[#31333F] rounded-[12px] px-[24px] data-[state=open]:border-[#0066CC]"
            >
              <AccordionTrigger 
                className="text-[#FAFAFA] hover:no-underline py-[20px]"
                style={{ 
                  fontFamily: 'Inter', 
                  fontWeight: 600,
                  fontSize: '18px'
                }}
              >
                ¿Qué tan preciso es TYR?
              </AccordionTrigger>
              <AccordionContent 
                className="text-[#B3B3B3] pb-[20px]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  fontSize: '14px',
                  lineHeight: 1.6
                }}
              >
                TYR tiene una precisión del 98.93%, validada a través de más de 4,358 consultas de entrenamiento. Está construido con información oficial del ITSE y utiliza tecnología de inteligencia artificial avanzada para brindarte respuestas confiables y actualizadas. Si necesitas información específica o detallada, TYR te puede dirigir con el departamento correspondiente.
              </AccordionContent>
            </AccordionItem>

            <AccordionItem 
              value="item-3" 
              className="bg-[#262730] border border-[#31333F] rounded-[12px] px-[24px] data-[state=open]:border-[#0066CC]"
            >
              <AccordionTrigger 
                className="text-[#FAFAFA] hover:no-underline py-[20px]"
                style={{ 
                  fontFamily: 'Inter', 
                  fontWeight: 600,
                  fontSize: '18px'
                }}
              >
                ¿Puedo usar TYR desde móvil?
              </AccordionTrigger>
              <AccordionContent 
                className="text-[#B3B3B3] pb-[20px]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  fontSize: '14px',
                  lineHeight: 1.6
                }}
              >
                ¡Por supuesto! TYR está diseñado para funcionar perfectamente en cualquier dispositivo: celulares, tablets, laptops o computadoras de escritorio. La interfaz se adapta automáticamente a tu pantalla para brindarte la mejor experiencia, sin importar desde dónde te conectes.
              </AccordionContent>
            </AccordionItem>

            <AccordionItem 
              value="item-4" 
              className="bg-[#262730] border border-[#31333F] rounded-[12px] px-[24px] data-[state=open]:border-[#0066CC]"
            >
              <AccordionTrigger 
                className="text-[#FAFAFA] hover:no-underline py-[20px]"
                style={{ 
                  fontFamily: 'Inter', 
                  fontWeight: 600,
                  fontSize: '18px'
                }}
              >
                ¿TYR reemplaza a admisiones?
              </AccordionTrigger>
              <AccordionContent 
                className="text-[#B3B3B3] pb-[20px]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  fontSize: '14px',
                  lineHeight: 1.6
                }}
              >
                No, TYR es un asistente virtual que complementa los servicios del ITSE. Su función es brindarte información rápida y precisa sobre carreras, admisiones, becas y servicios. Para procesos formales como inscripciones, entrega de documentos o casos específicos, te dirigirá con el personal de admisiones correspondiente.
              </AccordionContent>
            </AccordionItem>

            <AccordionItem 
              value="item-5" 
              className="bg-[#262730] border border-[#31333F] rounded-[12px] px-[24px] data-[state=open]:border-[#0066CC]"
            >
              <AccordionTrigger 
                className="text-[#FAFAFA] hover:no-underline py-[20px]"
                style={{ 
                  fontFamily: 'Inter', 
                  fontWeight: 600,
                  fontSize: '18px'
                }}
              >
                ¿Mis conversaciones son privadas?
              </AccordionTrigger>
              <AccordionContent 
                className="text-[#B3B3B3] pb-[20px]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  fontSize: '14px',
                  lineHeight: 1.6
                }}
              >
                Sí, tus conversaciones con TYR son privadas. No compartimos tu información personal con terceros. Las conversaciones pueden ser utilizadas de forma anónima para mejorar el servicio y la precisión de las respuestas, pero siempre respetando tu privacidad.
              </AccordionContent>
            </AccordionItem>

            <AccordionItem 
              value="item-6" 
              className="bg-[#262730] border border-[#31333F] rounded-[12px] px-[24px] data-[state=open]:border-[#0066CC]"
            >
              <AccordionTrigger 
                className="text-[#FAFAFA] hover:no-underline py-[20px]"
                style={{ 
                  fontFamily: 'Inter', 
                  fontWeight: 600,
                  fontSize: '18px'
                }}
              >
                ¿Puedo descargar el historial?
              </AccordionTrigger>
              <AccordionContent 
                className="text-[#B3B3B3] pb-[20px]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  fontSize: '14px',
                  lineHeight: 1.6
                }}
              >
                Actualmente, TYR no requiere registro, por lo que las conversaciones no se guardan permanentemente. Te recomendamos tomar capturas de pantalla o copiar la información importante que necesites conservar. Estamos trabajando en futuras versiones que podrían incluir esta funcionalidad.
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
      </section>

      {/* Benefits Section */}
      <section id="features" className="container mx-auto px-4 py-16 bg-[#262730]/50">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl md:text-5xl text-[#FAFAFA] mb-4">
              ¿Por qué usar TYR?
            </h2>
            <p className="text-xl text-[#B3B3B3]">
              Tu compañero ideal en tu proceso educativo
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <FeatureCard 
              icon={<Clock className="size-8 text-[#0066CC]" />}
              title="Disponible 24/7"
              description="No importa la hora, TYR está siempre listo para resolver tus dudas sobre ITSE."
            />
            <FeatureCard 
              icon={<BookOpen className="size-8 text-[#3399FF]" />}
              title="Información Completa"
              description="Carreras, requisitos, costos, horarios, instalaciones y todo lo que necesitas saber."
            />
            <FeatureCard 
              icon={<MessageSquare className="size-8 text-[#0066CC]" />}
              title="Respuestas Claras"
              description="Conversaciones naturales y respuestas precisas que realmente te ayudan."
            />
          </div>
        </div>
      </section>

      {/* For Who Section */}
      <section id="demo" className="container mx-auto px-4 py-16">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl md:text-5xl text-[#FAFAFA] mb-4">
              TYR es para ti
            </h2>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            <div className="bg-gradient-to-br from-[#0066CC] to-[#004C99] rounded-2xl p-8 text-[#FAFAFA] space-y-4 border border-[#31333F]">
              <GraduationCap className="size-12" />
              <h3 className="text-2xl">Estudiantes</h3>
              <p className="text-[#FAFAFA]/80">
                Descubre carreras, conoce requisitos, resuelve dudas sobre inscripciones y horarios al instante.
              </p>
            </div>

            <div className="bg-gradient-to-br from-[#004C99] to-[#0066CC] rounded-2xl p-8 text-[#FAFAFA] space-y-4 border border-[#31333F]">
              <Users className="size-12" />
              <h3 className="text-2xl">Padres</h3>
              <p className="text-[#FAFAFA]/80">
                Obtén información clara sobre costos, becas, planes de estudio y todo para apoyar a tus hijos.
              </p>
            </div>

            <div className="bg-gradient-to-br from-[#3399FF] to-[#0066CC] rounded-2xl p-8 text-[#FAFAFA] space-y-4 border border-[#31333F]">
              <BookOpen className="size-12" />
              <h3 className="text-2xl">Orientadores</h3>
              <p className="text-[#FAFAFA]/80">
                Accede rápidamente a información actualizada para guiar mejor a tus estudiantes.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section id="contact" className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          <Card className="bg-gradient-to-r from-[#0066CC] via-[#004C99] to-[#0066CC] border-0 shadow-2xl">
            <CardContent className="pt-12 pb-12 text-center text-[#FAFAFA] space-y-6">
              <h2 className="text-4xl md:text-5xl">
                ¿Listo para comenzar?
              </h2>
              <p className="text-xl text-[#FAFAFA]/80 max-w-2xl mx-auto">
                Haz tu primera pregunta a TYR y descubre lo fácil que es obtener la información que necesitas sobre ITSE.
              </p>
              <Button onClick={() => setIsChatOpen(true)} size="lg" className="text-lg px-8 mt-6 bg-[#FAFAFA] text-[#0066CC] hover:bg-[#FAFAFA]/90">
                Chatear con TYR Ahora
                <MessageCircle className="size-5 ml-2" />
              </Button>
              <p className="text-sm text-[#FAFAFA]/70 pt-2">
                No requiere registro • Gratis • Respuestas instantáneas
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* CTA Final Section */}
      <section 
        className="py-[96px] px-[32px] text-center"
        style={{
          background: 'linear-gradient(135deg, #0066CC 0%, #004C99 100%)'
        }}
      >
        <div className="container mx-auto max-w-4xl">
          <h2 
            className="text-[36px] text-[#FFFFFF] mb-[12px]"
            style={{ 
              fontFamily: 'Inter', 
              fontWeight: 700,
              lineHeight: 1.2
            }}
          >
            ¿Listo para empezar?
          </h2>
          
          <p 
            className="text-[18px] text-[#FFFFFF] mb-[32px]"
            style={{ 
              fontFamily: 'IBM Plex Sans',
              fontWeight: 400,
              opacity: 0.95
            }}
          >
            Prueba TYR ahora, es completamente gratis
          </p>
          
          <button
            onClick={() => setIsChatOpen(true)}
            className="w-[200px] h-[60px] bg-[#FFFFFF] text-[#0066CC] rounded-[28px] cursor-pointer transition-all duration-300 hover:scale-105 hover:shadow-[0_20px_60px_rgba(0,0,0,0.3)] active:scale-95"
            style={{
              fontFamily: 'IBM Plex Sans',
              fontWeight: 600,
              fontSize: '18px'
            }}
          >
            Probar TYR
          </button>
          
          <p 
            className="text-[12px] text-[#FFFFFF] mt-[16px]"
            style={{ 
              fontFamily: 'IBM Plex Sans',
              fontWeight: 400,
              opacity: 0.8
            }}
          >
            Sin registro • Sin descargas • 24/7
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-[#0e1117] border-t border-[#31333F] py-[64px] px-[32px]">
        <div className="container mx-auto max-w-6xl">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-[48px]">
            {/* Columna 1 - Logo */}
            <div className="space-y-4">
              <div className="flex items-center gap-3 mb-4">
                <div className="size-[40px] rounded-full bg-gradient-to-br from-[#0066CC] to-[#004C99] flex items-center justify-center">
                  <MessageCircle className="size-5 text-[#FAFAFA]" />
                </div>
                <span 
                  className="text-[#FAFAFA]"
                  style={{ 
                    fontFamily: 'Inter',
                    fontWeight: 600,
                    fontSize: '18px'
                  }}
                >
                  ITSE
                </span>
              </div>
              <p 
                className="text-[14px] text-[#B3B3B3]"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 400,
                  lineHeight: 1.6
                }}
              >
                Técnico Superior en Inteligencia Artificial
              </p>
            </div>

            {/* Columna 2 - Producto */}
            <div>
              <h3 
                className="text-[14px] text-[#FAFAFA] mb-4"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 600
                }}
              >
                Producto
              </h3>
              <ul className="space-y-3">
                <li>
                  <a 
                    href="#hero" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    Inicio
                  </a>
                </li>
                <li>
                  <a 
                    href="#features" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    Características
                  </a>
                </li>
                <li>
                  <a 
                    href="#demo" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    Demo
                  </a>
                </li>
                <li>
                  <a 
                    href="#contact" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    Contacto
                  </a>
                </li>
              </ul>
            </div>

            {/* Columna 3 - Recursos */}
            <div>
              <h3 
                className="text-[14px] text-[#FAFAFA] mb-4"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 600
                }}
              >
                Recursos
              </h3>
              <ul className="space-y-3">
                <li>
                  <a 
                    href="#" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    Documentación
                  </a>
                </li>
                <li>
                  <a 
                    href="#" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    GitHub
                  </a>
                </li>
                <li>
                  <a 
                    href="#" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    API Docs
                  </a>
                </li>
                <li>
                  <a 
                    href="#" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    Blog
                  </a>
                </li>
              </ul>
            </div>

            {/* Columna 4 - Contacto */}
            <div>
              <h3 
                className="text-[14px] text-[#FAFAFA] mb-4"
                style={{ 
                  fontFamily: 'IBM Plex Sans',
                  fontWeight: 600
                }}
              >
                Contacto
              </h3>
              <ul className="space-y-[12px]">
                <li>
                  <a 
                    href="mailto:info@itse.ac.pa" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300 flex items-start gap-2"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    <span>📧</span>
                    <span>info@itse.ac.pa</span>
                  </a>
                </li>
                <li>
                  <a 
                    href="tel:+5075243333" 
                    className="text-[13px] text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300 flex items-start gap-2"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    <span>📞</span>
                    <span>+507 524-3333</span>
                  </a>
                </li>
                <li>
                  <div 
                    className="text-[13px] text-[#B3B3B3] flex items-start gap-2"
                    style={{ fontFamily: 'IBM Plex Sans', fontWeight: 400 }}
                  >
                    <span>📍</span>
                    <span>Tocumen, Panamá</span>
                  </div>
                </li>
              </ul>
            </div>
          </div>

          {/* Redes Sociales */}
          <div className="mt-[48px] flex justify-center items-center gap-[12px]">
            <a 
              href="#" 
              className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
              aria-label="Facebook"
            >
              <svg className="size-[24px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
            </a>
            <a 
              href="#" 
              className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
              aria-label="Instagram"
            >
              <svg className="size-[24px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
            <a 
              href="#" 
              className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
              aria-label="LinkedIn"
            >
              <svg className="size-[24px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
            </a>
            <a 
              href="#" 
              className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
              aria-label="YouTube"
            >
              <svg className="size-[24px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
              </svg>
            </a>
          </div>

          {/* Copyright */}
          <div className="mt-[24px] pt-[24px] border-t border-[#31333F] text-center">
            <p 
              className="text-[12px] text-[#808080]"
              style={{ 
                fontFamily: 'IBM Plex Sans',
                fontWeight: 400
              }}
            >
              © 2025 ITSE. Hecho con ❤️ en Panamá.
            </p>
            <p 
              className="text-[12px] text-[#808080] mt-[8px]"
              style={{ 
                fontFamily: 'IBM Plex Sans',
                fontWeight: 400
              }}
            >
              TYR v1.0.0 | MIT License | GitHub
            </p>
          </div>
        </div>
      </footer>

      {/* Modal de Chat */}
      <Dialog open={isChatOpen} onOpenChange={setIsChatOpen}>
        <DialogContent className="max-w-[95vw] w-[1000px] h-[95vh] p-0 bg-transparent border-0">
          <Suspense fallback={
            <div className="flex items-center justify-center h-full">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-[#0066CC]"></div>
            </div>
          }>
            <TYRChat />
          </Suspense>
        </DialogContent>
      </Dialog>
    </div>
  );
}