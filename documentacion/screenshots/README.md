# Screenshots de TYR

Esta carpeta contiene capturas de pantalla del proyecto TYR mostrando su interfaz y características principales.

## Estructura

```
screenshots/
├── landing/          # Landing page y vistas generales
├── chat/             # Chat modal y conversaciones
└── features/         # Características especiales (PWA, export, etc)
```

## Screenshots Incluidos

### Landing Page
1. **01_landing_hero.png** - Vista principal del hero section
2. **08_mobile_view.png** - Vista responsive en móvil

### Chat
3. **02_chat_modal_open.png** - Modal del chat abierto
4. **03_consulta_carreras.png** - Consulta sobre carreras del ITSE
5. **04_consulta_bigdata.png** - Consulta específica sobre Big Data
6. **05_modo_demo.png** - Chat en modo demo (sin backend)
7. **06_chat_features.png** - Botones y features del chat
8. **07_dark_mode.png** - Interfaz en modo oscuro

### Features
9. **09_pwa_install.png** - Instalación como PWA
10. **10_export_pdf.png** - Exportación de conversación a PDF

## Guía para Tomar Screenshots

### Requisitos
- **Resolución Desktop:** 1920x1080
- **Resolución Móvil:** 375x812 (iPhone) o 360x740 (Android)
- **Formato:** PNG
- **Calidad:** Alta (sin compresión)

### Herramientas Recomendadas
- Windows Snipping Tool (Win + Shift + S)
- Chrome DevTools (F12) para vistas móviles
- Awesome Screenshot (extensión de Chrome)

### Antes de Capturar
1. Ejecuta el frontend: `cd Figma && npm run dev`
2. Abre en navegador: http://localhost:5173
3. Opcional: Ejecuta backend para modo completo

### Consejos
- Usa datos de ejemplo realistas
- Evita información personal
- Asegúrate de que el texto sea legible
- Captura en modo claro Y oscuro
- Muestra estados activos (hover, focus)

## Uso en Documentación

Estos screenshots se usan en:
- README.md - Vista previa del proyecto
- docs/ - Guías de usuario
- GitHub - Descripción del repositorio
- Presentaciones y demos

## Actualización

Para actualizar screenshots:

1. Toma las nuevas capturas siguiendo la guía
2. Guárdalas en la carpeta correspondiente
3. Verifica con: .\verificar_screenshots.ps1
4. Commit y push a GitHub

---

**Última actualización:** Noviembre 2025
**Versión UI:** 1.1.0 (React + TypeScript)
