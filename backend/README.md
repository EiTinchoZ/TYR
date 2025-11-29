# TYR Backend API

Backend FastAPI para el chatbot TYR con modelo BERT.

## Instalación

```bash
cd backend
pip install -r requirements.txt
```

## Ejecutar Servidor

```bash
python main.py
```

El servidor estará disponible en `http://localhost:8000`

## Endpoints

### POST /chat
Procesar mensaje del usuario y obtener respuesta.

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
Estadísticas del modelo TYR.

## Documentación Interactiva

Una vez ejecutado el servidor, visita:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
