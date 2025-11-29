# 🚀 Guía de Deployment - TYR Landing Page + Chatbot

Esta guía te ayudará a desplegar TYR en producción con el frontend en Netlify y el backend en Render/Railway.

## 📋 Requisitos Previos

- [ ] Cuenta de GitHub
- [ ] Cuenta de Netlify
- [ ] Cuenta de Render.com o Railway (para backend)
- [ ] Git instalado localmente

## 🎯 Arquitectura de Deployment

```
┌─────────────────┐
│   Usuario Web   │
└────────┬────────┘
         │
         ↓
┌─────────────────────┐
│  Netlify (Frontend) │  ← Landing Page React
│  TYR/Figma/dist/    │
└────────┬────────────┘
         │
         │ API Calls
         ↓
┌──────────────────────┐
│  Render (Backend)    │  ← FastAPI + BERT Model
│  TYR/backend/        │
└──────────────────────┘
```

## 📦 Paso 1: Preparar el Código

### 1.1 Crear repositorio en GitHub

```bash
cd "TYR"
git init
git add .
git commit -m "Initial commit: TYR Landing Page + Chatbot"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/tyr-chatbot.git
git push -u origin main
```

### 1.2 Crear .gitignore

```bash
# En TYR/
cat > .gitignore << 'EOF'
# Node
node_modules/
dist/
*.log
.env
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF
```

## 🖥️ Paso 2: Deploy del Backend (Render.com)

### 2.1 Crear cuenta en Render

1. Ve a [render.com](https://render.com)
2. Regístrate con GitHub
3. Conecta tu repositorio

### 2.2 Crear Web Service

1. Click en "New +" → "Web Service"
2. Selecciona tu repositorio `tyr-chatbot`
3. Configuración:

```yaml
Name: tyr-backend
Region: Oregon (US West)
Branch: main
Root Directory: backend
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: python main.py
Instance Type: Free
```

### 2.3 Variables de Entorno (Render)

En Settings → Environment:

```
PYTHON_VERSION=3.11
PORT=8000
```

### 2.4 Esperar el Deploy

- Render instalará dependencias (~5 minutos)
- El modelo BERT se cargará en memoria (~500MB)
- Anota la URL: `https://tyr-backend-XXXX.onrender.com`

**⚠️ IMPORTANTE**: El plan gratuito de Render hiberna después de 15 minutos de inactividad. El primer request tomará ~30 segundos en "despertar" el servicio.

## 🌐 Paso 3: Deploy del Frontend (Netlify)

### 3.1 Build Local

```bash
cd TYR/Figma

# Actualizar .env con URL del backend
echo "VITE_API_URL=https://tyr-backend-XXXX.onrender.com" > .env

# Build
npm run build
```

### 3.2 Deploy a Netlify

**Opción A: Netlify CLI (Recomendado)**

```bash
# Instalar Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
cd TYR/Figma
netlify deploy --prod --dir=dist
```

**Opción B: Netlify Web UI**

1. Ve a [app.netlify.com](https://app.netlify.com)
2. Click "Add new site" → "Deploy manually"
3. Arrastra la carpeta `TYR/Figma/dist/`
4. Espera el deploy (~1 minuto)

### 3.3 Configurar Variables de Entorno (Netlify)

1. En tu site → Site Settings → Environment Variables
2. Añadir:

```
VITE_API_URL=https://tyr-backend-XXXX.onrender.com
```

3. Click "Save"
4. Trigger nuevo deploy: Deploys → Trigger deploy → Deploy site

### 3.4 Configurar Dominio (Opcional)

1. Site Settings → Domain Management
2. Click "Add custom domain"
3. Ejemplo: `tyr.tudominio.com`
4. Seguir instrucciones de DNS

## ✅ Paso 4: Verificación

### 4.1 Backend Health Check

```bash
curl https://tyr-backend-XXXX.onrender.com/health
```

Respuesta esperada:
```json
{
  "status": "healthy",
  "modelo_cargado": true,
  "version": "1.0.0"
}
```

### 4.2 Frontend

1. Abre tu URL de Netlify: `https://YOUR_SITE.netlify.app`
2. Navega a "Pruébalo directamente aquí"
3. Envía un mensaje de prueba: "¿Qué carreras hay?"
4. Verifica que recibas respuesta

## 🔧 Configuración Avanzada

### Auto-Deploy con GitHub (Netlify)

1. En Netlify: Site Settings → Build & deploy → Link repository
2. Conecta GitHub
3. Build settings:

```yaml
Base directory: Figma
Build command: npm run build
Publish directory: Figma/dist
```

4. Cada push a `main` desplegará automáticamente

### CORS en Producción

Si tienes problemas de CORS, actualiza `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://YOUR_SITE.netlify.app",
        "https://tyr.tudominio.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📊 Monitoreo

### Backend (Render)

- Logs: Dashboard → Logs
- Métricas: Dashboard → Metrics
- Alertas de health check automáticas

### Frontend (Netlify)

- Analytics: Site → Analytics
- Deploy logs: Deploys → Deploy log
- Real-time functions logs

## 🐛 Troubleshooting

### Error: Backend no responde

**Causa**: Render en plan gratuito hiberna después de 15 minutos.

**Solución**:
- El primer request tardará ~30 segundos
- Considera actualizar a plan pagado ($7/mes)
- O usar Railway (plan gratuito más generoso)

### Error: CORS blocked

**Solución**:
1. Verifica que `VITE_API_URL` en Netlify sea correcto
2. Actualiza `allow_origins` en `backend/main.py`
3. Redeploy backend

### Error: Build falla en Netlify

**Solución**:
1. Verifica `package.json` tiene todas las dependencias
2. Revisa build logs en Netlify
3. Prueba build local: `npm run build`

## 💰 Costos

| Servicio | Plan Gratuito | Límites |
|----------|---------------|---------|
| **Netlify** | ✅ Sí | 100GB bandwidth/mes, 300 build minutos/mes |
| **Render** | ✅ Sí | Hiberna después 15 min inactividad, 750hrs/mes |
| **Railway** | ✅ Sí | $5 crédito/mes, ~500hrs uptime |

**Recomendación para MVP**: Netlify (frontend) + Render (backend) = $0/mes

**Para producción**: Netlify Pro ($19/mes) + Render Starter ($7/mes) = $26/mes

## 🔐 Seguridad

### Variables de Entorno

- ❌ NUNCA comitees `.env` a Git
- ✅ Usa variables de entorno en Render/Netlify
- ✅ Usa `.env.example` para documentar

### API Rate Limiting (Opcional)

Considera añadir rate limiting en producción:

```python
# backend/main.py
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/chat")
@limiter.limit("10/minute")
async def chat(request: ChatRequest):
    ...
```

## 📝 Checklist Final

Antes de considerar el deployment completo:

- [ ] Backend desplegado y respondiendo en `/health`
- [ ] Frontend desplegado y accesible
- [ ] Chatbot funciona end-to-end
- [ ] CORS configurado correctamente
- [ ] Variables de entorno configuradas
- [ ] Dominio custom (opcional)
- [ ] SSL/HTTPS activo (auto en Netlify/Render)
- [ ] Git repository actualizado
- [ ] README con URLs de producción
- [ ] Monitoreo configurado

## 🎉 ¡Listo!

Tu aplicación TYR está en producción. Comparte tu URL:

```
Landing Page: https://YOUR_SITE.netlify.app
Backend API: https://tyr-backend-XXXX.onrender.com/docs
```

---

**Próximos pasos sugeridos**:

1. Añadir Google Analytics
2. Configurar SEO (meta tags, sitemap)
3. Implementar caché de respuestas
4. Añadir tests automatizados
5. Configurar CI/CD con GitHub Actions

**¿Necesitas ayuda?**
- Render Docs: https://render.com/docs
- Netlify Docs: https://docs.netlify.com
- Consulta `TYR/Figma/README.md` para troubleshooting local
