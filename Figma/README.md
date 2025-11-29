# TYR - Landing Page + Chatbot Nativo

Landing page profesional para TYR, el asistente virtual del ITSE, con chatbot integrado usando BERT.

## 🚀 Características

- ✅ Landing page moderna y responsive con React + TypeScript
- ✅ Chatbot nativo integrado (no iframe)
- ✅ Backend FastAPI con modelo BERT (98.93% precisión)
- ✅ Diseño basado en Figma con branding profesional
- ✅ Animaciones con Motion/Framer Motion
- ✅ Styled con Tailwind CSS + animaciones personalizadas
- ✅ Componentes UI reutilizables
- ⚡ Optimizado para performance (lazy loading, code splitting)
- ✨ UX mejorada (typing indicators, smooth scroll, feedback visual)

## 📁 Estructura del Proyecto

```
TYR/
├── Figma/                    # Frontend (Landing Page + Chat)
│   ├── components/           # Componentes React
│   │   ├── TYRChat.tsx      # Componente de chat nativo
│   │   ├── Header.tsx       # Header con navegación
│   │   ├── FeatureCard.tsx  # Cards de características
│   │   └── ui/              # Componentes UI base
│   ├── styles/              # Estilos globales
│   ├── App.tsx              # Componente principal
│   ├── main.tsx             # Entry point
│   ├── package.json         # Dependencias frontend
│   └── vite.config.ts       # Config de Vite
│
├── backend/                  # Backend API
│   ├── main.py              # FastAPI server
│   ├── requirements.txt     # Dependencias Python
│   └── README.md            # Docs del backend
│
├── modelo_bert_tyr_4358/    # Modelo BERT entrenado
├── branding/                # Assets de branding
└── tyr_chatbot.py          # Clase TYR (lógica del chatbot)
```

## 🛠️ Instalación

### 1. Backend (FastAPI + BERT)

```bash
# Ir al directorio backend
cd TYR/backend

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor
python main.py
```

El backend estará disponible en: `http://localhost:8000`

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 2. Frontend (React + Vite)

```bash
# Ir al directorio Figma
cd TYR/Figma

# Instalar dependencias
npm install

# Iniciar dev server
npm run dev
```

El frontend estará disponible en: `http://localhost:5173`

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` en `TYR/Figma/`:

```env
VITE_API_URL=http://localhost:8000
```

Para producción, cambia la URL a tu backend desplegado.

## 🧪 Desarrollo Local

### Terminal 1: Backend
```bash
cd TYR/backend
python main.py
```

### Terminal 2: Frontend
```bash
cd TYR/Figma
npm run dev
```

Ahora puedes:
1. Abrir `http://localhost:5173` en tu navegador
2. Navegar a la sección "Pruébalo directamente aquí"
3. Interactuar con el chatbot TYR en tiempo real

## 📦 Build para Producción

### Frontend

```bash
cd TYR/Figma
npm run build
```

Los archivos optimizados estarán en `TYR/Figma/dist/`

## 🚀 Deployment

### Netlify (Frontend)

1. **Configurar el proyecto:**
   ```bash
   cd TYR/Figma
   npm run build
   ```

2. **Subir a Netlify:**
   - Opción A: Conectar con GitHub y auto-deploy
   - Opción B: Deploy manual desde `dist/`

3. **Configurar variables de entorno en Netlify:**
   - `VITE_API_URL`: URL de tu backend en producción

### Backend (Render/Railway/Heroku)

El backend puede desplegarse en cualquier servicio que soporte Python:

**Render.com (Recomendado):**
1. Crear nuevo Web Service
2. Conectar repositorio
3. Build Command: `cd backend && pip install -r requirements.txt`
4. Start Command: `cd backend && python main.py`

**Railway:**
1. Crear nuevo proyecto
2. Subir código
3. Railway detectará automáticamente FastAPI

## 🎨 Branding

El proyecto incluye assets de branding en `TYR/branding/`:

- Logos (11 variaciones)
- Iconos (16+ íconos)
- Ilustraciones
- Backgrounds
- Social media templates

Para reemplazar placeholders con branding real, consulta:
`TYR/PROMPTS_BRANDING_TYR.md`

## 📋 Scripts Disponibles

### Frontend

- `npm run dev` - Iniciar servidor de desarrollo
- `npm run build` - Build para producción
- `npm run preview` - Preview del build
- `npm run lint` - Linter de código

### Backend

- `python main.py` - Iniciar servidor FastAPI

## 🧪 API Endpoints

### POST /chat
Procesar mensaje del usuario.

**Request:**
```json
{
  "mensaje": "¿Qué carreras hay en el ITSE?"
}
```

**Response:**
```json
{
  "respuesta": "El ITSE ofrece 16 carreras técnicas...",
  "intencion": "informacion_carreras",
  "confianza": 0.9893,
  "sentimiento": {
    "neg": 0.0,
    "neu": 0.8,
    "pos": 0.2,
    "compound": 0.5
  }
}
```

### GET /health
Health check del servidor.

### GET /stats
Estadísticas del modelo (precisión, consultas, etc.)

## 🐛 Troubleshooting

### Backend no inicia
- Verifica que tengas Python 3.8+
- Asegúrate de que todas las dependencias estén instaladas
- El modelo BERT requiere ~500MB de RAM

### Frontend no conecta con backend
- Verifica que el backend esté corriendo en `http://localhost:8000`
- Revisa el archivo `.env` y la variable `VITE_API_URL`
- Abre DevTools y revisa la consola para errores CORS

### Errores de CORS
- El backend ya incluye configuración CORS para desarrollo local
- Para producción, añade tu dominio en `backend/main.py` línea 32

## 📊 Métricas del Modelo

- **Precisión**: 98.93%
- **Consultas entrenadas**: 4,358
- **Carreras soportadas**: 16
- **Intenciones**: 10+
- **Análisis de sentimiento**: VADER

## 👥 Autor

**Martín Bundy**
Técnico Superior en Inteligencia Artificial - ITSE

## 📄 Licencia

Este proyecto es parte de un trabajo académico para el ITSE.

---

**¿Necesitas ayuda?**
Consulta la documentación completa en `TYR/PROJECT_OVERVIEW.md`
