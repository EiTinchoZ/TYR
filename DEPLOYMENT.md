# 🚀 Guía de Deployment - TYR Chatbot

Esta guía te ayudará a desplegar TYR en producción con frontend y backend separados.

---

## 📋 Tabla de Contenidos

1. [Frontend (Vercel/Netlify)](#frontend)
2. [Backend (Render/Railway)](#backend)
3. [Variables de Entorno](#variables-de-entorno)
4. [PWA - App Instalable](#pwa)
5. [Troubleshooting](#troubleshooting)

---

## 🎨 Frontend - Desplegar en Vercel

### Opción 1: Deploy Automático desde GitHub

1. **Sube tu código a GitHub** (si aún no lo has hecho):
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit"
   git remote add origin https://github.com/EiTinchoZ/TYR.git
   git push -u origin main
   ```

2. **Ve a [Vercel](https://vercel.com)** y crea una cuenta (puedes usar tu cuenta de GitHub)

3. **Importa tu proyecto**:
   - Click en "New Project"
   - Selecciona tu repositorio TYR
   - Framework Preset: **Vite**
   - Root Directory: `Figma`
   - Build Command: `npm run build`
   - Output Directory: `dist`

4. **Variables de Entorno**:
   - Agrega: `VITE_API_URL` = `https://tu-backend.onrender.com` (la URL del backend)

5. **Deploy** - ¡Click en Deploy y espera 2 minutos!

### Opción 2: Deploy Manual desde CLI

```bash
cd Figma
npm install -g vercel
vercel login
vercel --prod
```

---

## ⚙️ Backend - Desplegar en Render

### Paso 1: Preparar el Backend

1. Crea un archivo `requirements.txt` en `/backend/`:
   ```bash
   cd backend
   pip freeze > requirements.txt
   ```

2. Crea `render.yaml` en la raíz del proyecto:
   ```yaml
   services:
     - type: web
       name: tyr-backend
       env: python
       buildCommand: pip install -r backend/requirements.txt
       startCommand: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
       envVars:
         - key: PYTHON_VERSION
           value: 3.11.0
   ```

### Paso 2: Deploy en Render

1. **Ve a [Render](https://render.com)** y crea una cuenta

2. **New Web Service**:
   - Conecta tu repositorio de GitHub
   - Branch: `main`
   - Root Directory: `.` (raíz)
   - Environment: **Python 3**
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

3. **Variables de Entorno**:
   - `PYTHON_VERSION` = `3.11.0`

4. **Deploy** - Render comenzará a construir automáticamente

5. **Importante**:
   - Copia la URL del backend (ej: `https://tyr-backend.onrender.com`)
   - Actualiza `VITE_API_URL` en Vercel con esta URL

---

## 🌐 Variables de Entorno

### Frontend (`Figma/.env.production`)

```bash
VITE_API_URL=https://tu-backend.onrender.com
```

### Backend (`backend/.env`)

```bash
# No necesitas variables especiales por ahora
# El modelo se carga automáticamente desde /modelo_bert_tyr_10_clases_COMPLETO
```

---

## 📱 PWA - Progressive Web App

Tu app YA ES UNA PWA y se puede instalar en celulares. Para probarla:

### En Android (Chrome):

1. Abre tu app en Chrome: `https://tyr.vercel.app`
2. Toca el menú (⋮) → "Agregar a pantalla de inicio"
3. ¡Listo! Ahora tienes TYR como una app nativa

### En iOS (Safari):

1. Abre tu app en Safari
2. Toca el botón de compartir (⬆️)
3. Selecciona "Agregar a pantalla de inicio"
4. ¡Instalado!

### Características PWA:

✅ Se instala como app nativa
✅ Funciona offline (después de la primera visita)
✅ Ícono en la pantalla de inicio
✅ Modo standalone (sin barra del navegador)
✅ Actualizaciones automáticas

---

## 🐛 Troubleshooting

### Problema: CORS Error en producción

**Solución**: Actualiza `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://tyr.vercel.app",  # Tu dominio de Vercel
        "https://tu-dominio-custom.com",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Problema: Backend muy lento en Render (plan gratuito)

**Causa**: Render free tier "duerme" después de 15 minutos de inactividad.

**Soluciones**:
1. **Upgrade a plan pago** ($7/mes) - Recomendado para producción
2. **Keep-alive service** - Usa un servicio como [UptimeRobot](https://uptimerobot.com) para hacer ping cada 5 minutos
3. **Railway** - Alternativa a Render con mejor plan gratuito

### Problema: Modelo BERT muy pesado para deployment

**Solución**: El modelo (420MB) es demasiado grande para algunos servicios gratis.

**Alternativas**:
1. **Usar Railway** - Permite modelos grandes en plan gratuito
2. **Almacenar en S3/Cloud Storage** y descargar al iniciar
3. **Usar Hugging Face Model Hub** para hospedar el modelo

---

## 📊 Resumen de Costos

| Servicio | Plan Gratuito | Plan Pago | Recomendado |
|----------|--------------|-----------|-------------|
| **Vercel** (Frontend) | ✅ Ilimitado | $20/mes | ✅ Gratis es suficiente |
| **Render** (Backend) | ⚠️ Duerme después 15min | $7/mes | Considerar pago |
| **Railway** (Backend Alt) | ✅ $5 crédito/mes | $10/mes | ✅ Mejor opción gratuita |
| **Netlify** (Frontend Alt) | ✅ 100GB ancho banda | $19/mes | ✅ Gratis OK |

---

## ✅ Checklist Final

Antes de ir a producción:

- [ ] Backend deployed y funcionando
- [ ] Frontend deployed
- [ ] CORS configurado correctamente
- [ ] Variables de entorno configuradas
- [ ] `VITE_API_URL` apunta al backend correcto
- [ ] Modelo BERT cargado correctamente en backend
- [ ] PWA manifest.json configurado
- [ ] Probado en móvil
- [ ] Tests pasando (`pytest`)

---

## 🎯 Próximos Pasos

1. **Monitoreo**: Configura [Sentry](https://sentry.io) para error tracking
2. **Analytics**: Agrega Google Analytics o Plausible
3. **Custom Domain**: Conecta tu propio dominio en Vercel
4. **SSL**: Vercel y Render proveen SSL automático (HTTPS)

---

**¿Necesitas ayuda?** Abre un [issue en GitHub](https://github.com/EiTinchoZ/TYR/issues)

---

*Última actualización: 28 de Noviembre 2025*
