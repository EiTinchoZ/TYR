# 🤝 Contribuir a TYR

¡Gracias por tu interés en contribuir a TYR! Este documento proporciona guías para contribuir al proyecto.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Cómo Contribuir](#cómo-contribuir)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Guía de Estilo](#guía-de-estilo)
- [Reporte de Bugs](#reporte-de-bugs)
- [Sugerencias de Mejoras](#sugerencias-de-mejoras)

## 📜 Código de Conducta

Este proyecto se adhiere a un código de conducta profesional y respetuoso. Al participar, se espera que mantengas este código.

### Nuestros Estándares

- **Ser respetuoso** con otros contribuyentes
- **Aceptar críticas constructivas** con gracia
- **Enfocarse en lo que es mejor** para la comunidad
- **Mostrar empatía** hacia otros miembros de la comunidad

## 🚀 Cómo Contribuir

Hay muchas formas de contribuir a TYR:

1. **Reportar bugs** - Si encuentras un error, abre un issue
2. **Sugerir mejoras** - Propón nuevas características o mejoras
3. **Mejorar documentación** - Ayuda a hacer la documentación más clara
4. **Contribuir código** - Implementa nuevas características o arregla bugs
5. **Mejorar el dataset** - Contribuye con nuevos ejemplos de entrenamiento

## 🛠️ Configuración del Entorno de Desarrollo

### Prerrequisitos

- Python 3.8 o superior
- Node.js 16+ y npm (para el frontend)
- Git
- 4GB RAM mínimo (8GB recomendado para entrenar el modelo)

### Instalación

1. **Fork el repositorio**

```bash
# Clona tu fork
git clone https://github.com/TU_USUARIO/TYR.git
cd TYR
```

2. **Configura el backend**

```bash
# Crea entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Instala dependencias de desarrollo
pip install -r backend/requirements.txt
```

3. **Configura el frontend**

```bash
cd Figma
npm install
cp .env.example .env
```

4. **Descarga el modelo (o entrena uno nuevo)**

El modelo BERT no está en el repositorio por su tamaño. Opciones:

- **Opción A:** Descarga el modelo pre-entrenado desde [link a compartir]
- **Opción B:** Entrena tu propio modelo siguiendo [GUIA_REENTRENAMIENTO.md](GUIA_REENTRENAMIENTO.md)

5. **Ejecuta los tests**

```bash
# Backend
pytest tests/ -v

# Frontend (si aplica)
cd Figma
npm test
```

### Estructura del Proyecto

```
TYR/
├── backend/           # API FastAPI
├── Figma/            # Frontend React + TypeScript
├── data/             # Base de conocimiento JSON
├── tests/            # Suite de tests
├── documentacion/    # Documentación del proyecto
└── tyr_chatbot.py   # Clase principal del chatbot
```

## 🔄 Proceso de Pull Request

1. **Crea una rama** desde `main`

```bash
git checkout -b feature/mi-nueva-caracteristica
# o
git checkout -b fix/mi-bug-fix
```

2. **Haz tus cambios**

- Escribe código limpio y bien documentado
- Sigue la guía de estilo del proyecto
- Añade tests para nuevas características
- Actualiza la documentación si es necesario

3. **Commit tus cambios**

```bash
git add .
git commit -m "feat: descripción clara de los cambios"
```

Usa commits semánticos:
- `feat:` Nueva característica
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formato, puntos y comas faltantes, etc
- `refactor:` Refactorización de código
- `test:` Añadir tests
- `chore:` Mantenimiento

4. **Push a tu fork**

```bash
git push origin feature/mi-nueva-caracteristica
```

5. **Abre un Pull Request**

- Describe claramente qué cambios hiciste y por qué
- Referencia cualquier issue relacionado
- Asegúrate de que todos los tests pasen
- Solicita revisión de código

### Criterios de Aceptación

Tu PR será aceptado si:

- ✅ Todos los tests pasan
- ✅ El código sigue las guías de estilo
- ✅ Está bien documentado
- ✅ No introduce bugs conocidos
- ✅ La documentación está actualizada

## 🎨 Guía de Estilo

### Python

- Sigue [PEP 8](https://pep8.org/)
- Usa type hints cuando sea posible
- Documenta funciones con docstrings
- Máximo 88 caracteres por línea (Black formatter)

```python
def procesar_mensaje(mensaje: str, confianza_minima: float = 0.8) -> dict:
    """
    Procesa un mensaje del usuario y retorna la respuesta del chatbot.

    Args:
        mensaje: Texto del usuario
        confianza_minima: Umbral de confianza mínimo

    Returns:
        Dict con respuesta, intención, confianza y sentimiento
    """
    # Tu código aquí
    pass
```

### TypeScript / React

- Usa TypeScript estricto
- Componentes funcionales con hooks
- Nombres de componentes en PascalCase
- Props tipadas con interfaces

```typescript
interface ChatMessageProps {
  mensaje: string;
  esUsuario: boolean;
  timestamp: Date;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ mensaje, esUsuario, timestamp }) => {
  // Tu código aquí
}
```

### Commits

Usa [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(chat): añadir soporte para voz
fix(bert): corregir clasificación de intención
docs(readme): actualizar instrucciones de instalación
```

## 🐛 Reporte de Bugs

Si encuentras un bug, por favor abre un [issue](https://github.com/USUARIO/TYR/issues) con:

### Template de Bug Report

```markdown
**Descripción del bug**
Descripción clara y concisa del bug.

**Pasos para reproducir**
1. Ir a '...'
2. Hacer click en '...'
3. Scroll hasta '...'
4. Ver error

**Comportamiento esperado**
Qué esperabas que sucediera.

**Screenshots**
Si aplica, añade screenshots.

**Entorno:**
- OS: [ej. Windows 10, macOS 14.1, Ubuntu 22.04]
- Python: [ej. 3.10.5]
- Node.js: [ej. 18.16.0]
- Navegador: [ej. Chrome 120, Firefox 121]

**Contexto adicional**
Cualquier otra información relevante.
```

## 💡 Sugerencias de Mejoras

Si tienes una idea para mejorar TYR, abre un [issue](https://github.com/USUARIO/TYR/issues) con:

### Template de Feature Request

```markdown
**¿Tu feature request está relacionado con un problema?**
Descripción clara del problema. Ej: "Me frustra que..."

**Describe la solución que te gustaría**
Descripción clara de lo que quieres que suceda.

**Describe alternativas que hayas considerado**
Otras soluciones o características que consideraste.

**Contexto adicional**
Screenshots, mockups, o cualquier contexto adicional.
```

## 🧪 Tests

Todos los cambios deben incluir tests apropiados:

### Backend Tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar con coverage
pytest tests/ --cov=. --cov-report=html

# Ejecutar tests específicos
pytest tests/test_tyr_chatbot.py -v
```

### Frontend Tests (si aplica)

```bash
cd Figma
npm test
npm run test:coverage
```

### Escribir Tests

```python
# tests/test_mi_funcionalidad.py
import pytest
from tyr_chatbot import TYRChatbot

def test_clasificacion_intencion():
    """Test que verifica clasificación correcta de intención"""
    chatbot = TYRChatbot()
    resultado = chatbot.procesar_mensaje("¿Qué carreras hay?")

    assert resultado['intencion'] == 'informacion_carreras'
    assert resultado['confianza'] > 0.8
```

## 📝 Documentación

Si añades una nueva característica, actualiza:

- README.md principal
- Documentación técnica en `documentacion/`
- Docstrings en el código
- Ejemplos de uso si aplica

## 🎯 Áreas para Contribuir

Algunas áreas donde puedes contribuir:

### Backend
- Mejorar precisión del modelo BERT
- Optimizar tiempos de respuesta
- Añadir nuevas intenciones
- Mejorar análisis de sentimiento

### Frontend
- Mejorar UX/UI
- Añadir modo oscuro/claro toggle
- Implementar chat por voz
- Optimizar performance

### Dataset
- Añadir más ejemplos de entrenamiento
- Mejorar variedad de patrones de pregunta
- Corregir errores en respuestas

### Documentación
- Mejorar guías de instalación
- Añadir tutoriales
- Traducir documentación
- Crear videos demostrativos

## ❓ Preguntas

Si tienes preguntas, puedes:

1. Revisar la [documentación](documentacion/)
2. Abrir un [issue](https://github.com/EiTinchoZ/TYR/issues)
3. Contactar al mantenedor: mbundy.deltawaves@gmail.com

## 📄 Licencia

Al contribuir a TYR, aceptas que tus contribuciones serán licenciadas bajo la [Licencia MIT](LICENSE).

---

**¡Gracias por contribuir a TYR! 🚀**

Tu ayuda hace que este proyecto sea mejor para toda la comunidad del ITSE.
