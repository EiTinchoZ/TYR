# 🚀 Guía MVP - Deploy TYR en 10 Minutos

Esta guía te llevará paso a paso para tener tu MVP de TYR funcionando en la nube.

---

## 🎯 ¿Qué es un MVP?

**MVP = Minimum Viable Product** (Producto Mínimo Viable)

Es una versión funcional de tu app con las características esenciales para validar la idea con usuarios reales.

---

## ✅ TU MVP INCLUYE:

- ✅ Landing page profesional
- ✅ Chat funcional con TYR
- ✅ **Modo Demo** (funciona sin backend)
- ✅ PWA instalable en celulares
- ✅ Respuestas inteligentes sobre ITSE
- ✅ Diseño responsivo
- ✅ Historial de conversaciones
- ✅ Exportar conversaciones a PDF

---

## 🚀 OPCIÓN 1: MVP Solo Frontend (MÁS RÁPIDO - 10 MIN)

Esta opción despliega solo el frontend con **modo demo** (respuestas predefinidas inteligentes).

### Paso 1: Preparar el Proyecto

```bash
cd Figma
npm run build
```

Verifica que compile sin errores.

### Paso 2: Subir a GitHub

```bash
# Desde la raíz del proyecto
git add .
git commit -m "feat: MVP ready - demo mode enabled"
git push origin main
```

### Paso 3: Deploy en Vercel (GRATIS)

1. **Ve a [vercel.com](https://vercel.com)**
2. **Inicia sesión** con tu cuenta de GitHub
3. **New Project** → Selecciona tu repositorio TYR
4. **Configuración:**
   - Framework Preset: **Vite**
   - Root Directory: **`Figma`**
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. **Environment Variables:**
   - NO necesitas agregar ninguna (el modo demo funciona sin backend)
6. **Deploy** → Espera 2-3 minutos

### Paso 4: ¡Listo!

Tu MVP estará en: `https://tyr-tu-usuario.vercel.app`

**¿Cómo funciona?**
- Si el backend NO está disponible → Usa respuestas mock inteligentes
- Si el backend SÍ está disponible → Usa el modelo BERT real

---

## 🚀 OPCIÓN 2: MVP Completo (Frontend + Backend)

Si quieres usar el modelo BERT real, necesitas desplegar también el backend.

### Problema: Modelo muy pesado (420MB)

**Servicios gratuitos tienen límites:**
- Render Free: ❌ Muy lento + se duerme
- Railway Free: ⚠️ Solo $5 crédito/mes
- Heroku: ❌ Ya no es gratis

### Solución Recomendada: Railway

Railway es la mejor opción para modelos pesados.

#### Paso 1: Crear requirements.txt

```bash
cd backend
pip freeze > requirements.txt
```

#### Paso 2: Deploy en Railway

1. **Ve a [railway.app](https://railway.app)**
2. **New Project** → Deploy from GitHub repo
3. **Selecciona** tu repositorio TYR
4. **Settings:**
   - Root Directory: `/backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Variables:**
   - `PYTHON_VERSION` = `3.11`
6. **Deploy**

#### Paso 3: Conectar Frontend con Backend

1. **Copia la URL** del backend Railway (ej: `https://tyr-backend.railway.app`)
2. **En Vercel:**
   - Settings → Environment Variables
   - Agrega: `VITE_API_URL` = `https://tyr-backend.railway.app`
3. **Redeploy** el frontend

---

## 📱 INSTALAR COMO APP (PWA)

Una vez deployed, los usuarios pueden instalar TYR como app:

### Android (Chrome):

1. Abre `https://tyr-tu-usuario.vercel.app`
2. Aparece banner "Agregar a pantalla de inicio"
3. O menú (⋮) → "Instalar aplicación"
4. ¡Listo! TYR ahora es una app nativa

### iOS (Safari):

1. Abre la URL en Safari
2. Botón compartir (⬆️)
3. "Agregar a pantalla de inicio"
4. ¡Instalado!

### Características PWA:

✅ Funciona offline
✅ Ícono en pantalla de inicio
✅ Sin barra del navegador
✅ Actualizaciones automáticas
✅ Notificaciones (futuro)

---

## 🎨 MODO DEMO - Cómo Funciona

El modo demo usa respuestas inteligentes predefinidas:

**Responde a preguntas sobre:**
- 📚 Carreras (16 programas técnicos)
- 📝 Admisión e inscripción
- 💰 Becas y financiamiento
- 🏫 Información del ITSE
- ⏰ Horarios y contacto
- 🤖 Carrera de IA específicamente

**Ejemplo:**
```
Usuario: "¿Qué carreras hay?"
TYR: [Respuesta detallada sobre las 16 carreras]
```

El sistema detecta palabras clave y responde de forma contextual.

---

## 📊 Comparación de Opciones

| Aspecto | Solo Frontend | Frontend + Backend |
|---------|--------------|-------------------|
| **Tiempo deploy** | 10 minutos | 30-60 minutos |
| **Costo** | $0 | $0-$10/mes |
| **Respuestas** | Predefinidas inteligentes | IA real con BERT |
| **Precisión** | ~85% | 98.93% |
| **Escalabilidad** | ✅ Ilimitada | ⚠️ Limitada en plan free |
| **Recomendado para** | Demos, validación | Producción real |

---

## 🔄 Migrar de Demo a Producción

Cuando quieras pasar de modo demo a producción real:

1. Deploy el backend en Railway
2. Agrega `VITE_API_URL` en Vercel
3. Redeploy
4. ¡Automáticamente usa el backend real!

---

## ✅ Checklist MVP

- [ ] Código en GitHub
- [ ] Frontend deployed en Vercel
- [ ] URL funcional y accesible
- [ ] Chat funciona (modo demo o real)
- [ ] Probado en móvil
- [ ] PWA instalable
- [ ] Compartido con 5 personas para feedback

---

## 🎯 Siguientes Pasos Después del MVP

1. **Recolectar Feedback:**
   - Comparte con amigos/familia
   - Pide opiniones honestas
   - Anota bugs y sugerencias

2. **Mejorar basado en feedback:**
   - Agregar más respuestas mock
   - Mejorar UI/UX
   - Agregar analytics

3. **Escalar:**
   - Deploy backend cuando tengas usuarios
   - Upgrade a plan pago si es necesario
   - Agregar features avanzadas

---

## 📞 ¿Problemas?

**Error: Build Failed**
- Verifica que `npm run build` funcione localmente
- Revisa los logs en Vercel

**Error: PWA no se puede instalar**
- Verifica que uses HTTPS (Vercel lo da automático)
- Revisa manifest.json esté accesible

**Error: Chat no responde**
- Abre consola del navegador (F12)
- Revisa errores en Network tab
- Verifica que mockResponses.ts esté importado

---

## 🎉 ¡Felicidades!

Ahora tienes un **MVP funcional** de TYR que puedes:

- ✅ Compartir con usuarios
- ✅ Demostrar a inversores/profesores
- ✅ Instalar como app en celulares
- ✅ Iterar y mejorar

**Tu URL será:** `https://tyr-[tu-usuario].vercel.app`

---

**¿Dudas?** Abre un [issue en GitHub](https://github.com/EiTinchoZ/TYR/issues)

*Última actualización: 28 de Noviembre 2025*
