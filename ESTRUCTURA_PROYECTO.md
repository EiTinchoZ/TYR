# 📁 Estructura del Proyecto TYR

Organización final y limpia del proyecto preparado para GitHub.

## 🌳 Árbol de Directorios

```
TYR/
│
├── 📄 README.md                    # ⭐ Documentación principal
├── 📄 LICENSE                      # Licencia MIT
├── 📄 CONTRIBUTING.md              # Guía de contribución
├── 📄 SECURITY.md                  # Política de seguridad
├── 📄 CHANGELOG.md                 # Historial de cambios
├── 📄 MODELO_DESCARGA.md           # Instrucciones para obtener el modelo
│
├── 📄 requirements.txt             # Dependencias Python
├── 📄 pytest.ini                   # Configuración de tests
├── 📄 .coveragerc                  # Configuración de coverage
├── 📄 .gitignore                   # Archivos ignorados
├── 📄 .gitattributes               # Git LFS config
│
├── 📄 tyr_chatbot.py               # ⚙️ Clase principal del chatbot
├── 📄 Dataset_TYR_3000_FINAL.json  # Dataset de entrenamiento (4,358 ejemplos)
├── 📄 TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb  # Notebook para Colab
├── 📄 label_map.json               # Mapeo de etiquetas
│
├── 📜 run_backend.sh               # Script para ejecutar backend (cross-platform)
├── 📜 run_frontend.sh              # Script para ejecutar frontend
├── 📜 run_streamlit.sh             # Script para ejecutar Streamlit
├── 📜 run_backend.bat              # Script Windows (legacy)
├── 📜 run_frontend.bat             # Script Windows (legacy)
│
├── 🗂️ .github/                    # Configuración de GitHub
│   ├── workflows/
│   │   └── ci.yml                  # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── config.yml
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 🗂️ backend/                    # Backend FastAPI
│   ├── main.py                     # Servidor FastAPI
│   ├── tyr_simple.py               # Wrapper simplificado
│   ├── requirements.txt            # Dependencias backend
│   ├── .env.example                # Template de variables de entorno
│   └── README.md
│
├── 🗂️ Figma/                      # Frontend React + TypeScript
│   ├── App.tsx                     # Componente principal
│   ├── main.tsx                    # Entry point
│   ├── index.html
│   ├── package.json                # Dependencias Node.js
│   ├── tsconfig.json               # Config TypeScript
│   ├── vite.config.ts              # Config Vite
│   ├── tailwind.config.js          # Config Tailwind
│   ├── .env.example                # Template variables frontend
│   ├── components/                 # Componentes React
│   ├── styles/                     # Estilos CSS
│   ├── hooks/                      # Custom hooks
│   ├── public/                     # Assets públicos
│   └── README.md
│
├── 🗂️ data/                       # Base de conocimiento
│   ├── carreras_itse.json          # 16 carreras del ITSE
│   ├── ITSE_Base_Datos_Definitiva_v3.md
│   ├── ITSE_JSON_Definitivo_v3.md
│   └── README.md
│
├── 🗂️ tests/                      # Suite de tests (59 tests)
│   ├── conftest.py                 # Fixtures compartidas
│   ├── test_normalizacion.py
│   ├── test_respuestas.py
│   ├── test_tyr_chatbot.py
│   └── README.md
│
├── 🗂️ docs/                       # 📚 Documentación organizada
│   ├── README.md                   # Índice de documentación
│   │
│   ├── guides/                     # Guías de usuario
│   │   ├── GUIA_REENTRENAMIENTO.md
│   │   └── DEPLOYMENT_GUIDE.md
│   │
│   ├── dev/                        # Documentación de desarrollo
│   │   ├── CHECKLIST_PRE_GITHUB.md
│   │   ├── TAREAS_FINALES_ANTES_DE_GITHUB.md
│   │   └── RESUMEN_MEJORAS_GITHUB.md
│   │
│   ├── archive/                    # Archivos históricos
│   │   ├── PLAN_PRE_GITHUB.md
│   │   ├── INFORME_LIMPIEZA_PROYECTO.md
│   │   ├── RESUMEN_SESION_INTEGRACION.md
│   │   ├── SESION_FINAL_COMPLETA.md
│   │   └── VOICE_INPUT_FEATURE.md
│   │
│   ├── PROJECT_OVERVIEW.md         # Visión general del proyecto
│   ├── INDEX_DOCUMENTACION.md      # Índice antiguo (para referencia)
│   ├── ITSE-informacion-completa.md
│   └── PROMPTS_BRANDING_TYR.md
│
├── 🗂️ documentacion/               # Documentación técnica detallada
│   ├── ARQUITECTURA_SISTEMA.md     # Diagramas de arquitectura
│   ├── PROYECTO_TYR_LOG_COMPLETO.md
│   ├── README.md
│   │
│   ├── guias/
│   │   ├── GUIA_EJECUCION.md
│   │   └── INSTRUCCIONES_REENTRENAMIENTO.md
│   │
│   ├── reportes/                   # Reportes de sesiones
│   │   ├── REPORTE_SESION1_TESTS.md
│   │   ├── REPORTE_SESION2_JSON.md
│   │   ├── REPORTE_SESION3_VISUALIZACIONES.md
│   │   ├── REPORTE_SESION4_ARQUITECTURA.md
│   │   └── REPORTE_SESION5_DEMO_FINAL.md
│   │
│   ├── visualizaciones/            # Gráficas y métricas
│   │   ├── matriz_confusion_4358.png
│   │   ├── distribucion_intenciones.png
│   │   ├── evolucion_modelos.png
│   │   └── metricas_clasificacion.txt
│   │
│   └── screenshots/                # Capturas de pantalla
│       ├── 01_pantalla_inicial.png
│       ├── 02_consulta_bigdata.png
│       ├── 03_consulta_caipi.png
│       └── ...
│
├── 🗂️ branding/                   # Assets de branding
│   ├── README.md
│   ├── 01_logos/                   # Logos (11 variaciones)
│   ├── 02_icons/                   # Iconos (16+)
│   ├── 03_illustrations/
│   ├── 04_backgrounds/
│   ├── 05_social_media/
│   └── 06_misc/
│
├── 🗂️ scripts_desarrollo/         # Scripts de desarrollo
│   ├── expandir_dataset_v3_completo.py
│   ├── preprocesar_dataset_4358.py
│   ├── test_chatbot_4358.py
│   └── generar_visualizaciones.py
│
├── 🗂️ entregables_profesor/       # ⚠️ NO SE SUBE A GITHUB
│   ├── README.md                   # (excluido en .gitignore)
│   ├── INFORME_FINAL_TYR.md
│   ├── Dataset_TYR_3000_FINAL.json
│   ├── TYR_REENTRENAMIENTO_4358_Colab.ipynb
│   └── ...
│
└── 🗂️ modelo_bert_tyr_10_clases_COMPLETO/  # ⚠️ NO SE SUBE (420MB)
    ├── config.json                 # (excluido en .gitignore)
    ├── model.safetensors            # 420MB
    ├── tokenizer.json
    ├── vocab.txt
    └── label_map.json
```

## 📌 Archivos en la Raíz (Visibles en GitHub)

Solo archivos esenciales que se ven profesionales:

### Documentación Principal
- ✅ `README.md` - Primera impresión, quick start
- ✅ `LICENSE` - Licencia MIT
- ✅ `CONTRIBUTING.md` - Cómo contribuir
- ✅ `SECURITY.md` - Políticas de seguridad
- ✅ `CHANGELOG.md` - Historial de versiones
- ✅ `MODELO_DESCARGA.md` - Obtener el modelo BERT

### Configuración
- ✅ `requirements.txt` - Dependencias Python
- ✅ `pytest.ini` - Config de tests
- ✅ `.coveragerc` - Config de coverage
- ✅ `.gitignore` - Archivos ignorados
- ✅ `.gitattributes` - Git LFS

### Código Principal
- ✅ `tyr_chatbot.py` - Clase del chatbot
- ✅ `Dataset_TYR_3000_FINAL.json` - Dataset
- ✅ `TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb` - Notebook
- ✅ `label_map.json` - Etiquetas

### Scripts
- ✅ `run_*.sh` - Scripts cross-platform
- ✅ `run_*.bat` - Scripts Windows (legacy)

## 🗂️ Documentación Organizada en `/docs/`

### `/docs/guides/` - Guías de Usuario
- Guía de reentrenamiento
- Guía de deployment

### `/docs/dev/` - Para Desarrolladores
- Checklist pre-GitHub
- Tareas finales
- Resumen de mejoras

### `/docs/archive/` - Históricos
- Documentos antiguos archivados
- Para referencia interna

### `/docs/` (raíz)
- Visión general del proyecto
- Información ITSE
- Prompts de branding

## ⚠️ NO se Suben a GitHub

### Archivos Grandes (en `.gitignore`)
```
modelo_bert_tyr_10_clases_COMPLETO/  # 420MB
Figma/node_modules/                  # ~300MB
Figma/dist/                          # Build generado
historial_conversaciones/            # Datos privados
*.env                                # Variables sensibles
entregables_profesor/                # Solo para el profesor
```

### Carpeta `entregables_profesor/`

**Estado:** ✅ Actualizada y lista para uso local
**GitHub:** ❌ Excluida del repositorio (en `.gitignore`)
**Contiene:**
- INFORME_FINAL_TYR.md
- Dataset original (3,000 ejemplos)
- Notebook de Colab
- LOG completo de desarrollo
- README explicativo

**Uso:** Solo para entregar al profesor. No se necesita en GitHub.

## 📊 Comparación Antes/Después

### ANTES (Desorganizado)
```
TYR/
├── 19 archivos .md en la raíz ❌
├── Documentos duplicados ❌
├── Archivos de desarrollo mezclados ❌
├── Sin estructura clara ❌
```

### DESPUÉS (Organizado)
```
TYR/
├── 5 archivos .md esenciales en raíz ✅
├── Documentación en /docs/ ✅
├── Archivos de dev en /docs/dev/ ✅
├── Estructura profesional y clara ✅
```

## 🎯 Ventajas de la Nueva Estructura

### Para Usuarios de GitHub
- ✅ README limpio y profesional
- ✅ Documentación fácil de encontrar
- ✅ Archivos esenciales visibles
- ✅ No hay desorden

### Para Contribuyentes
- ✅ Guías claras en `/docs/guides/`
- ✅ CONTRIBUTING.md accesible
- ✅ Templates de Issues/PRs
- ✅ CI/CD automático

### Para Ti (Desarrollador)
- ✅ Archivos del profesor separados
- ✅ Documentación histórica archivada
- ✅ Estructura escalable
- ✅ Fácil mantenimiento

## 📝 Notas Importantes

1. **entregables_profesor/** está en `.gitignore` - NO se subirá
2. **modelo_bert_tyr_10_clases_COMPLETO/** está en `.gitignore` - NO se subirá
3. Todos los documentos tienen referencias actualizadas
4. Usuario GitHub: `EiTinchoZ`
5. Email de contacto: `mbundy.deltawaves@gmail.com`

## ✅ Lista de Verificación Final

- [x] Usuario GitHub actualizado (EiTinchoZ)
- [x] Email actualizado en todos los docs
- [x] Archivos MD organizados en carpetas
- [x] Solo 5 MD esenciales en raíz
- [x] entregables_profesor/ en .gitignore
- [x] modelo_bert/ en .gitignore
- [x] node_modules/ en .gitignore
- [x] Referencias actualizadas en documentación
- [x] Estructura profesional y limpia

## 🚀 Listo para GitHub

El proyecto está completamente organizado y listo para:

```bash
git init
git add .
git commit -m "feat: initial commit - TYR chatbot v1.0.0"
git remote add origin https://github.com/EiTinchoZ/TYR.git
git branch -M main
git push -u origin main
```

---

*Última actualización: Noviembre 27, 2025*
*Autor: Martín Bundy*
*GitHub: @EiTinchoZ*
