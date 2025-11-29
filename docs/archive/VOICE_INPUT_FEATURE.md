# 🎤 Feature: Reconocimiento de Voz (Speech-to-Text)

**Fecha de implementación**: 25 de noviembre de 2025
**Estado**: ✅ Completado con mejoras de compatibilidad

---

## 📋 Descripción

Sistema de entrada de voz integrado en el chatbot TYR que permite a los usuarios dictar mensajes usando la **Web Speech API**. El sistema detecta automáticamente la disponibilidad del navegador y proporciona retroalimentación clara al usuario.

---

## ✅ Características Implementadas

### 1. **Detección Multi-Navegador**
```typescript
const SpeechRecognition =
  (window as any).SpeechRecognition ||
  (window as any).webkitSpeechRecognition ||
  (window as any).mozSpeechRecognition ||
  (window as any).msSpeechRecognition;
```

Detecta múltiples prefijos de vendors:
- ✅ Chrome: `webkitSpeechRecognition`
- ✅ Edge: `webkitSpeechRecognition`
- ✅ Safari: `webkitSpeechRecognition`
- ❌ Firefox: No soportado nativamente (ver alternativas)

### 2. **Configuración Optimizada**
```typescript
recognition.continuous = false;      // No grabar continuamente
recognition.interimResults = false;  // Solo resultados finales
recognition.lang = "es-ES";         // Español de España
recognition.maxAlternatives = 1;    // Una sola alternativa
```

### 3. **UI/UX Intuitiva**

**Botón de Micrófono:**
- 🎤 **Estado inactivo**: Icono `Mic` azul con fondo translúcido
- 🔴 **Grabando**: Icono `MicOff` rojo con animación `pulse`
- El botón solo aparece si el navegador lo soporta
- Placeholder cambia a "Escuchando..." mientras graba

**Visual States:**
```css
/* Inactivo */
bg-[#3399FF]/20 hover:bg-[#3399FF]/40

/* Grabando */
bg-red-500 hover:bg-red-600 animate-pulse
```

### 4. **Manejo de Errores Robusto**

El sistema detecta y maneja múltiples tipos de errores:

| Error | Mensaje al Usuario |
|-------|-------------------|
| `not-allowed` / `permission-denied` | "🎤 Permiso denegado. Permite el acceso al micrófono..." |
| `no-speech` | "No se detectó voz. Intenta de nuevo." |
| `network` | "Error de red. Verifica tu conexión." |
| `aborted` | (Sin mensaje - cancelación del usuario) |
| `InvalidStateError` | Auto-detiene y resetea |

### 5. **Mensajes Específicos por Navegador**

**Firefox:**
```
❌ Firefox no soporta Web Speech API actualmente.

📱 Alternativas:
• Usa Google Chrome, Microsoft Edge o Safari
• Instala la extensión 'Voice Control for ChatGPT' en Firefox
• Usa un servicio de transcripción externo
```

**Safari:**
```
❌ Safari requiere permisos especiales.
Verifica la configuración de privacidad.
```

**Otros navegadores:**
```
❌ Reconocimiento de voz no disponible.

✅ Navegadores compatibles:
• Google Chrome
• Microsoft Edge
• Safari (iOS/macOS)
```

### 6. **Banner Informativo (Firefox)**

Cuando se detecta Firefox, se muestra un banner naranja visible:

```tsx
{!isVoiceAvailable && navigator.userAgent.toLowerCase().includes("firefox") && (
  <div className="mb-3 p-3 bg-orange-500/10 border border-orange-500/30 rounded-lg">
    <p className="text-[12px] text-orange-400">
      ℹ️ <strong>Firefox no soporta entrada de voz.</strong>
      Usa Chrome, Edge o Safari para esta función.
    </p>
  </div>
)}
```

---

## 🌐 Compatibilidad de Navegadores

| Navegador | Versión | Soporte | Notas |
|-----------|---------|---------|-------|
| **Google Chrome** | 33+ | ✅ Full | Mejor soporte, recomendado |
| **Microsoft Edge** | 79+ | ✅ Full | Chromium-based, excelente |
| **Safari** | 14.1+ | ✅ Parcial | Requiere permisos explícitos |
| **Opera** | 20+ | ✅ Full | Chromium-based |
| **Firefox** | Todas | ❌ No | No soporta Web Speech API |
| **Brave** | Todas | ✅ Full | Chromium-based |

---

## 🔧 Código Principal

### Estado y Refs
```typescript
const [isListening, setIsListening] = useState(false);
const [isVoiceAvailable, setIsVoiceAvailable] = useState(false);
const recognitionRef = useRef<any>(null);
```

### Inicialización (useEffect)
```typescript
useEffect(() => {
  const SpeechRecognition =
    (window as any).SpeechRecognition ||
    (window as any).webkitSpeechRecognition ||
    (window as any).mozSpeechRecognition ||
    (window as any).msSpeechRecognition;

  if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    // ... configuración
    recognitionRef.current = recognition;
    setIsVoiceAvailable(true);
  } else {
    setIsVoiceAvailable(false);
  }
}, []);
```

### Toggle Function
```typescript
const toggleVoiceInput = () => {
  if (!recognitionRef.current) {
    // Mostrar mensaje específico por navegador
    return;
  }

  if (isListening) {
    recognitionRef.current.stop();
  } else {
    recognitionRef.current.start();
  }
};
```

### Event Handlers
```typescript
recognition.onresult = (event) => {
  const transcript = event.results[0][0].transcript;
  setInputValue(transcript);
  setIsListening(false);
};

recognition.onerror = (event) => {
  // Manejo específico de errores
  setIsListening(false);
};

recognition.onspeechend = () => {
  recognition.stop();
};
```

---

## 🚀 Uso

1. **Hacer clic en el botón del micrófono** 🎤 (si está visible)
2. **Permitir acceso al micrófono** (primera vez)
3. **Hablar claramente** en español
4. **El texto aparece automáticamente** en el input
5. **Presionar Enter o botón Send** para enviar

---

## ⚠️ Limitaciones Conocidas

### Firefox
- **Problema**: No soporta Web Speech API nativamente
- **Solución**: Usar Chrome, Edge, Safari o extensiones de terceros

### Safari (iOS)
- **Problema**: Requiere permisos muy específicos
- **Solución**: Verificar Settings → Safari → Camera/Microphone

### Conexión a Internet
- **Problema**: Web Speech API requiere internet (usa servidores de Google)
- **Solución**: Verificar conexión activa

### Privacidad
- **Problema**: El audio se envía a servidores de Google para transcripción
- **Solución**: Informar a usuarios sobre política de privacidad

---

## 🔮 Mejoras Futuras Sugeridas

1. **Soporte Offline**: Implementar `pocketsphinx.js` o similar
2. **Multi-idioma**: Botón para cambiar entre `es-ES`, `en-US`, etc.
3. **Resultados Intermedios**: Mostrar transcripción en tiempo real
4. **Corrección de Texto**: Sugerencias de corrección post-transcripción
5. **Atajos de Teclado**: `Ctrl+Shift+V` para activar voz
6. **Animación de Onda**: Visualización de audio mientras graba

---

## 📚 Referencias

- [MDN: Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [Can I Use: Speech Recognition](https://caniuse.com/speech-recognition)
- [Chrome Speech Recognition](https://developer.chrome.com/blog/voice-driven-web-apps-introduction-to-the-web-speech-api/)

---

## ✅ Testing Checklist

- [x] Funciona en Chrome Desktop
- [x] Funciona en Edge Desktop
- [ ] Funciona en Safari Desktop
- [ ] Funciona en Chrome Mobile
- [ ] Funciona en Safari iOS
- [x] Muestra mensaje correcto en Firefox
- [x] Maneja permisos denegados correctamente
- [x] Maneja errores de red
- [x] Botón se oculta en navegadores no compatibles
- [x] Banner informativo aparece en Firefox
- [x] Animación pulse funciona al grabar
- [x] Placeholder cambia a "Escuchando..."

---

**Autor**: Claude Code
**Última actualización**: 25 de noviembre de 2025
