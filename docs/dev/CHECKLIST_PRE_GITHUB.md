# ✅ Checklist Pre-GitHub - TYR

Esta lista te ayudará a verificar que todo está listo antes de subir TYR a GitHub.

## 📦 Archivos y Configuración

### Archivos Esenciales (Verificar que existen)

- [x] `README.md` - Completo y actualizado
- [x] `LICENSE` - Licencia MIT
- [x] `.gitignore` - Con Node.js, Python, y archivos grandes
- [x] `.gitattributes` - Para Git LFS
- [x] `CONTRIBUTING.md` - Guía de contribución
- [x] `SECURITY.md` - Política de seguridad
- [x] `MODELO_DESCARGA.md` - Instrucciones para descargar el modelo
- [x] `requirements.txt` - Dependencias Python actualizadas
- [x] `backend/requirements.txt` - Dependencias del backend
- [x] `Figma/package.json` - Dependencias frontend
- [x] `.github/workflows/ci.yml` - GitHub Actions CI
- [x] `.github/ISSUE_TEMPLATE/` - Templates de issues
- [x] `.github/PULL_REQUEST_TEMPLATE.md` - Template de PRs

### Archivos a NO Subir (Verificar .gitignore)

- [ ] `modelo_bert_tyr_10_clases_COMPLETO/` - ¡MUY IMPORTANTE! (~420MB)
- [ ] `Figma/node_modules/` - Dependencias de Node.js
- [ ] `Figma/dist/` - Build del frontend
- [ ] `Figma/.env` - Variables de entorno
- [ ] `backend/.env` - Variables de entorno del backend
- [ ] `historial_conversaciones/` - Conversaciones guardadas
- [ ] `*.code-workspace` - Archivos de VSCode
- [ ] `__pycache__/` - Cache de Python
- [ ] `.pytest_cache/` - Cache de tests
- [ ] Archivos con credenciales o API keys

## 🧹 Limpieza del Proyecto

### Archivos Temporales a Eliminar

```bash
# Ejecuta estos comandos para limpiar:

# Eliminar cache de Python
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete

# Eliminar archivos de workspace
rm -f "GladOS Chatbot PLN.code-workspace"

# Eliminar historiales de conversaciones (opcional)
# rm -rf historial_conversaciones/
```

### Revisar y Limpiar (Opcional)

- [ ] Carpeta `entregables_profesor/` - ¿Es necesaria en GitHub público?
- [ ] Archivos `.bat` - Son específicos de Windows, considera añadir scripts cross-platform
- [ ] Documentos de desarrollo temporal - Revisa `documentacion/` y limpia lo innecesario

## 🔍 Verificaciones de Seguridad

### Variables de Entorno

- [ ] No hay API keys hardcodeadas en el código
- [ ] Archivos `.env` están en `.gitignore`
- [ ] Existe `.env.example` como template
- [ ] README explica cómo configurar variables de entorno

### Datos Sensibles

- [ ] No hay contraseñas en el código
- [ ] No hay tokens o credenciales en commits anteriores
- [ ] Historial de conversaciones no contiene información personal
- [ ] Logs no contienen información sensible

### Auditoría de Dependencias

```bash
# Backend - Verificar vulnerabilidades
pip install safety
safety check

# Frontend - Verificar vulnerabilidades
cd Figma
npm audit
```

## 📝 Documentación

### README Principal

- [ ] Badges actualizados (reemplazar "USUARIO" con tu usuario de GitHub)
- [ ] Screenshots funcionan (rutas correctas)
- [ ] Links a documentación funcionan
- [ ] Instrucciones de instalación son claras
- [ ] Hay ejemplos de uso

### Documentación Adicional

- [ ] `CONTRIBUTING.md` tiene tu email/contacto actualizado
- [ ] `SECURITY.md` tiene un email de contacto válido
- [ ] `MODELO_DESCARGA.md` tiene el link de descarga del modelo
- [ ] Todas las referencias a rutas locales están corregidas

## 🧪 Tests

### Ejecutar Suite de Tests

```bash
# Backend Tests
pytest tests/ -v
# Resultado esperado: 59 tests passing

# Verificar coverage
pytest tests/ --cov=. --cov-report=html
# Resultado esperado: ~73.75% coverage
```

### Frontend (si aplica)

```bash
cd Figma
npm run build:check  # Verificar TypeScript
npm run lint         # Verificar ESLint
npm run build        # Verificar build exitoso
```

## 📦 Modelo BERT

### Preparar Modelo para Distribución

Opciones:

#### Opción A: Google Drive (Recomendado para inicio)

1. [ ] Comprimir el modelo:
   ```bash
   zip -r modelo_bert_tyr_10_clases_COMPLETO.zip modelo_bert_tyr_10_clases_COMPLETO/
   ```

2. [ ] Subir a Google Drive
3. [ ] Obtener link público de descarga
4. [ ] Actualizar link en `MODELO_DESCARGA.md`
5. [ ] Probar que el link funciona desde navegador incógnito

#### Opción B: Hugging Face Hub (Profesional)

1. [ ] Crear cuenta en Hugging Face: https://huggingface.co/join
2. [ ] Crear nuevo modelo: https://huggingface.co/new
3. [ ] Subir modelo con `huggingface-cli`:
   ```bash
   pip install huggingface-hub
   huggingface-cli login
   huggingface-cli upload martin-bundy/tyr-bert-itse modelo_bert_tyr_10_clases_COMPLETO/
   ```
4. [ ] Actualizar `MODELO_DESCARGA.md` con instrucciones

#### Opción C: Git LFS (Para repositorio privado)

1. [ ] Instalar Git LFS: https://git-lfs.github.com/
2. [ ] Inicializar Git LFS:
   ```bash
   git lfs install
   git lfs track "*.safetensors"
   git lfs track "*.pth"
   ```
3. [ ] Nota: GitHub LFS tiene límites (1GB gratis)

## 🌐 Configuración de GitHub

### Antes del Primer Push

1. [ ] Crear repositorio en GitHub
   - Nombre: `TYR` o `TYR-Chatbot-ITSE`
   - Descripción: "🤖 TYR - Asistente Virtual Inteligente para ITSE | BERT NLP Chatbot"
   - Visibilidad: Público / Privado (según prefieras)
   - NO inicialices con README (ya tienes uno)

2. [ ] Configurar Git localmente:
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit - TYR chatbot completo"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TYR.git
   ```

3. [ ] Verificar qué se va a subir:
   ```bash
   git status
   # Revisar que no aparezcan archivos grandes o sensibles
   ```

4. [ ] Primer push:
   ```bash
   git push -u origin main
   ```

### Después del Primer Push

1. [ ] Configurar GitHub Pages (si quieres documentación web)
2. [ ] Habilitar GitHub Discussions
3. [ ] Configurar rama protegida `main`:
   - Settings → Branches → Add rule
   - Require pull request reviews before merging
   - Require status checks to pass (CI)
4. [ ] Añadir Topics al repositorio:
   - `chatbot`, `bert`, `nlp`, `fastapi`, `react`, `typescript`, `spanish`, `education`
5. [ ] Configurar GitHub Secrets para CI (si necesitas):
   - Settings → Secrets and variables → Actions

## 📊 Verificación Final

### Prueba de Clone Fresco

```bash
# En otro directorio, simula que eres un usuario nuevo:
cd /tmp
git clone https://github.com/TU_USUARIO/TYR.git
cd TYR

# 1. Verifica README
cat README.md  # ¿Se ve bien?

# 2. Instala backend
pip install -r requirements.txt
# ¿Funciona sin errores?

# 3. Descarga modelo siguiendo MODELO_DESCARGA.md
# ¿Las instrucciones son claras?

# 4. Instala frontend
cd Figma
npm install
# ¿Funciona sin errores?

# 5. Ejecuta tests
cd ..
pytest tests/ -v
# ¿Pasan todos?
```

### Checklist Visual en GitHub

Después de subir, verifica en GitHub.com:

- [ ] README se renderiza correctamente
- [ ] Screenshots se muestran
- [ ] Badges funcionan
- [ ] Links a documentación funcionan
- [ ] Issue templates aparecen
- [ ] PR template funciona
- [ ] CI workflow se ejecuta (Actions tab)
- [ ] Licencia se detecta correctamente
- [ ] .gitignore está funcionando (no hay archivos grandes)

## 🎯 Tareas Post-GitHub

### Promover el Proyecto

1. [ ] Crear una release v1.0.0:
   - GitHub → Releases → Create a new release
   - Tag: `v1.0.0`
   - Title: "TYR v1.0.0 - Primer Release Oficial"
   - Descripción: Resumen del proyecto y logros

2. [ ] Añadir al perfil de GitHub:
   - Pin repository en tu perfil

3. [ ] Compartir (opcional):
   - LinkedIn
   - Twitter
   - Reddit (r/MachineLearning, r/LanguageTechnology)
   - Dev.to blog post

### Mejoras Continuas

1. [ ] Configurar Codecov para coverage reports
2. [ ] Añadir más tests para llegar a 80%+ coverage
3. [ ] Crear GitHub Project para roadmap
4. [ ] Escribir Wiki con guías detalladas
5. [ ] Crear ejemplos en notebooks interactivos

## ⚠️ Errores Comunes a Evitar

❌ **NO HAGAS ESTO:**

1. ❌ Subir el modelo BERT (420MB) al repositorio
2. ❌ Subir `node_modules/` (puede ser varios GB)
3. ❌ Subir archivos `.env` con credenciales
4. ❌ Hacer commit de archivos binarios grandes
5. ❌ Pushear código con API keys hardcodeadas
6. ❌ Subir historiales de conversaciones con datos reales

✅ **SÍ HAZ ESTO:**

1. ✅ Usa `.gitignore` correctamente
2. ✅ Documenta cómo descargar el modelo por separado
3. ✅ Usa `.env.example` como template
4. ✅ Revisa `git status` antes de cada commit
5. ✅ Ejecuta tests antes de pushear
6. ✅ Escribe commits descriptivos

## 🆘 Troubleshooting

### "Mi primer push está tardando mucho"

- Probablemente estás subiendo archivos grandes
- Cancela con `Ctrl+C`
- Ejecuta `git status` y `git ls-files --cached`
- Añade archivos grandes a `.gitignore`
- Ejecuta `git rm --cached <archivo-grande>`
- Vuelve a hacer commit

### "GitHub dice que mi repositorio es muy grande"

- Límite de GitHub: 1GB (recomendado), 5GB (máximo)
- Usa `git lfs` para archivos grandes
- O distribuye el modelo por separado (Google Drive, Hugging Face)

### "Los badges en README no funcionan"

- Reemplaza `USUARIO` con tu usuario real de GitHub
- Espera unos minutos después del primer push
- Algunos badges requieren configuración adicional

## 📝 Notas Finales

- **Backup:** Antes de hacer cambios grandes, haz backup del proyecto
- **Branches:** Considera usar `develop` para desarrollo y `main` para releases
- **Commits:** Usa commits semánticos: `feat:`, `fix:`, `docs:`, etc.
- **Versioning:** Sigue Semantic Versioning (v1.0.0, v1.1.0, v2.0.0)

---

## ✨ ¡Listo para GitHub!

Una vez completadas todas las tareas de este checklist, tu proyecto TYR estará listo para brillar en GitHub de manera profesional.

**Última revisión:** Noviembre 2025
**Proyecto:** TYR - Asistente Virtual ITSE
**Autor:** Martín Bundy
