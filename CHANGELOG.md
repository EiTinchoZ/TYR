# Changelog

Todos los cambios notables en el proyecto TYR serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.1.0] - 2025-11-28

### 🚀 Nuevas Características Mayores

#### PWA (Progressive Web App)
- ✨ Convertido a Progressive Web App instalable
- 📱 Funciona en Android e iOS como app nativa
- 🔄 Actualizaciones automáticas
- 💾 Funciona offline después de la primera visita
- 📲 manifest.json configurado con íconos y metadata
- 🎯 Meta tags PWA en index.html

#### Modo Demo Inteligente
- 🎯 **Fallback automático** cuando backend no está disponible
- 🧠 Respuestas mock inteligentes basadas en palabras clave
- 📚 6 categorías de respuestas predefinidas:
  - Información general sobre carreras
  - Proceso de admisión
  - Becas y financiamiento
  - Carrera de Inteligencia Artificial
  - Horarios y contacto
  - Saludo y bienvenida
- ⚡ Sin errores al usuario - cambio transparente
- 🔄 Permite deployment frontend-only (gratis en Vercel)

#### Chat Modal Integrado
- 💬 Botones "Prueba TYR" ahora abren modal con chat completo
- 📐 Chat más grande (850px altura vs 700px anterior)
- 🎨 Modal responsivo (95% viewport height)
- ✨ Animaciones de apertura/cierre fluidas
- 🚫 Backdrop blur effect
- ⌨️ Cerrar con ESC o click fuera

### 🔧 Mejoras

#### Frontend
- 🎨 Mejor experiencia de usuario con modal centralizado
- 📱 Optimizaciones para móviles
- 🔄 Lazy loading del componente TYRChat
- ⚡ Fallback loading spinner mejorado

#### Documentación
- 📚 [MVP_GUIDE.md](MVP_GUIDE.md) - Guía completa de MVP
- 🚀 [DEPLOYMENT.md](DEPLOYMENT.md) - Actualizado con opciones PWA
- 📖 README.md actualizado con nuevas características
- 🔧 .env.example para configuración
- 📝 Documentación del modo demo

### 🐛 Fixes

- ✅ Scroll automático al cargar página resuelto
- ✅ Instalado @radix-ui/react-dialog faltante
- ✅ Manejo de errores mejorado en TYRChat
- ✅ Prevención de múltiples scrolls al inicio

### 📦 Dependencias

- ➕ Agregado `@radix-ui/react-dialog@^1.1.15`
- 📝 Archivo mockResponses.ts para respuestas demo

### 🎯 Deployment

- ☁️ Listo para Vercel (frontend-only, gratis)
- ☁️ Preparado para Railway/Render (backend opcional)
- 📱 PWA instalable en producción
- 🔄 Modo demo funciona sin configuración adicional

---

## [1.0.0] - 2025-11-26

### 🎉 Release Inicial

Primera versión completa del asistente virtual TYR para el ITSE.

### ✨ Added (Añadido)

#### Backend & Modelo
- Modelo BERT (`dccuchile/bert-base-spanish-wwm-cased`) fine-tuned con 4,358 ejemplos
- Alcanzado **98.93% accuracy** (superando meta de 85% por +13.93%)
- Alcanzado **98.92% F1-Score** (superando meta de 82% por +16.92%)
- API REST con FastAPI con 3 endpoints principales
- Análisis de sentimientos con VADER-ES
- Base de conocimiento JSON externalizada (91 KB)
- 59 tests unitarios con 73.75% coverage
- Soporte para 9 intenciones diferentes y 48 patrones de pregunta

#### Frontend
- Landing page moderna con React 18 + TypeScript 5.6
- Chat integrado nativamente (sin iframe)
- Modo oscuro/claro toggle
- Animaciones con Motion 11 (scroll animations, transitions)
- Responsive design (móvil, tablet, desktop)
- Integración completa de branding ITSE
- Export de conversaciones a PDF con jsPDF

#### Documentación
- README.md completo con badges e instrucciones
- PROJECT_OVERVIEW.md con arquitectura detallada
- DEPLOYMENT_GUIDE.md para producción
- 6 diagramas Mermaid de arquitectura
- Visualizaciones de métricas (matriz de confusión, distribución)
- LICENSE MIT

---

## [1.0.1] - 2025-11-26

### ⚡ Optimización de Performance

### Added
- Lazy loading para todas las imágenes de branding
- Code splitting con React.lazy para componente TYRChat
- Separación manual de chunks por vendor (react, motion, icons, markdown)
- Animaciones personalizadas en Tailwind (`fade-in`, `pulse-subtle`)

### Changed
- Mejorada animación de "typing indicator" con 3 dots bouncing
- Agregado smooth scroll automático también en estado de loading
- Botón de enviar ahora tiene animación pulse sutil cuando hay texto
- Optimizado build de Vite con rollupOptions

### Performance
- **Tiempo de build reducido:** 14.66s → 4.17s (71% más rápido)
- **Bundle principal:** Modularizado en 6 chunks separados
- **TYRChat chunk:** 20.52 KB cargado on-demand
- **CSS optimizado:** 80.81 KB con animaciones custom
- **Mejor caching** del navegador con vendors separados

---

## [1.0.2] - 2025-11-25

### 🎨 Integración de Branding

### Added
- 150+ assets de branding profesional integrados
- Logos del ITSE en 11 variaciones
- 16 iconos personalizados para features
- Ilustraciones de avatares (bot, personas)
- Feature cards visuales (accuracy, 24/7, tests)
- Backgrounds y patterns

### Changed
- Reemplazados todos los emojis con iconos branded
- Logo de TYR en header del chat
- Avatar de bot en mensajes y typing indicator
- Hero background con neural network pattern
- Feature cards con visual branding
- Personas (María, Roberto) con ilustraciones custom

---

## [1.0.3] - 2025-11-24

### 🎤 Voice Input Feature

### Added
- Soporte para entrada por voz con Web Speech API
- Funciona en Chrome, Edge y Safari
- Indicador visual de grabación activa
- Detección automática de fin de speech
- Transcripción en tiempo real al input

### Fixed
- Manejo de navegadores sin soporte (Firefox)
- Mensajes informativos específicos por navegador
- Permisos de micrófono con manejo de errores

---

## [0.9.0] - 2025-11-23

### 🧪 Testing & Quality Assurance

### Added
- 59 tests unitarios con pytest
- Test suite completo para TYRChatbot
- Tests de integración backend
- Tests de preprocesamiento
- Tests de base de conocimiento
- Coverage report (73.75%)

### Changed
- Refactorizado código para mejor testabilidad
- Separada lógica de negocio de presentación
- Mejorada documentación de funciones

---

## [0.8.0] - 2025-11-22

### 📊 Dataset Expansion v3

### Changed
- Dataset expandido de 1,542 → 4,358 ejemplos (+183%)
- Mejorada distribución entre intenciones
- Agregados 48 patrones diferentes de preguntas
- Balance optimizado para información_carreras (65% del dataset)

### Performance
- Accuracy mejorada: 96.2% → 98.93%
- F1-Score mejorado: 95.8% → 98.92%
- Reducción de falsos positivos en 67%

---

## [0.7.0] - 2025-11-20

### 🎨 UI/UX Improvements

### Added
- Sidebar con historial de conversaciones
- Botones de ejemplo de preguntas frecuentes
- Contador de caracteres en input
- Timestamps en mensajes
- Indicador de estado del servidor

### Changed
- Mejorado diseño de burbujas de mensaje
- Agregado hover effects en cards
- Optimizado spacing y padding
- Mejorada legibilidad de texto

---

## [0.6.0] - 2025-11-18

### 🔧 Backend Optimization

### Added
- Caché de respuestas frecuentes
- Logging estructurado
- Health check endpoint
- Stats endpoint con métricas

### Changed
- Optimizado tiempo de respuesta de API
- Mejorado manejo de errores
- Agregado timeout handling

---

## [0.5.0] - 2025-11-15

### 📦 Initial Backend Implementation

### Added
- FastAPI backend con 3 endpoints
- Integración con modelo BERT
- CORS configuration
- Base de conocimiento JSON

---

## [0.4.0] - 2025-11-12

### 🤖 BERT Fine-tuning v1

### Added
- Modelo BERT fine-tuned primera versión
- 1,542 ejemplos de entrenamiento
- 9 intenciones clasificadas
- Accuracy inicial: 96.2%

---

## [0.3.0] - 2025-11-10

### 🎨 Frontend Foundation

### Added
- React + TypeScript setup
- Vite configuration
- Tailwind CSS integration
- Basic landing page structure

---

## [0.2.0] - 2025-11-08

### 📝 Dataset Creation

### Added
- Dataset inicial con 800 ejemplos
- 7 intenciones base
- Preprocesamiento pipeline
- Tokenización BERT

---

## [0.1.0] - 2025-11-05

### 🎬 Project Initialization

### Added
- Estructura inicial del proyecto
- README básico
- Requirements.txt
- .gitignore
- LICENSE MIT

---

## Roadmap Futuro

### En Consideración (Post v1.0)

- [ ] Despliegue en Netlify (frontend) + Render (backend)
- [ ] Integración con base de datos para logs
- [ ] Dashboard de analytics
- [ ] Soporte multiidioma (inglés)
- [ ] PWA con service workers
- [ ] Notificaciones push
- [ ] Chat history persistente con auth
- [ ] Fine-tuning continuo con feedback
- [ ] A/B testing de respuestas
- [ ] Métricas de satisfacción del usuario

---

## Tipos de Cambios

- **Added** - Para funcionalidades nuevas
- **Changed** - Para cambios en funcionalidades existentes
- **Deprecated** - Para funcionalidades que serán removidas
- **Removed** - Para funcionalidades removidas
- **Fixed** - Para corrección de bugs
- **Security** - Para cambios de seguridad
- **Performance** - Para mejoras de rendimiento

---

**Formato de Versiones:** MAJOR.MINOR.PATCH

- **MAJOR** - Cambios incompatibles con versiones anteriores
- **MINOR** - Funcionalidades nuevas compatibles
- **PATCH** - Correcciones de bugs compatibles
