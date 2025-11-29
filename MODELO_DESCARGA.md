# 📦 Descarga del Modelo BERT TYR

El modelo BERT entrenado (`modelo_bert_tyr_10_clases_COMPLETO/`) pesa aproximadamente **420MB** y no está incluido en el repositorio de GitHub por razones de tamaño.

## 🚀 Opciones para Obtener el Modelo

### Opción 1: Descargar Modelo Pre-entrenado (Recomendado)

#### Google Drive

1. Descarga el modelo desde: [**Link de Google Drive**](https://drive.google.com/drive/folders/1EyCCO7cv14ubufmvhDyGc_Jv02YPTBSO?usp=sharing)
2. Extrae el archivo ZIP
3. Coloca la carpeta `modelo_bert_tyr_10_clases_COMPLETO/` en la raíz del proyecto TYR

```bash
TYR/
├── modelo_bert_tyr_10_clases_COMPLETO/  # <- Aquí
│   ├── config.json
│   ├── model.safetensors (420MB)
│   ├── tokenizer.json
│   └── ...
├── tyr_chatbot.py
└── ...
```

#### Hugging Face Hub (Alternativo)

```bash
# Instalar huggingface-hub
pip install huggingface-hub

# Descargar modelo (próximamente)
# huggingface-cli download martin-bundy/tyr-bert-itse
```

### Opción 2: Entrenar el Modelo Desde Cero

Si prefieres entrenar tu propio modelo:

#### En Google Colab (Recomendado - GPU gratis)

1. Abre el notebook: [TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb](TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb)
2. Súbelo a Google Colab
3. Ejecuta todas las celdas (toma ~15-20 minutos)
4. Descarga la carpeta del modelo generada
5. Colócala en la raíz del proyecto

#### Localmente (requiere GPU)

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar entrenamiento
jupyter notebook TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb

# O usar el script de Python:
python scripts_desarrollo/entrenar_modelo.py
```

**Requisitos para entrenamiento local:**
- GPU NVIDIA con CUDA (recomendado: 6GB+ VRAM)
- 8GB RAM mínimo
- ~2GB espacio en disco
- Tiempo estimado: 15-30 minutos

## 📊 Especificaciones del Modelo

| Característica | Valor |
|----------------|-------|
| **Modelo base** | `dccuchile/bert-base-spanish-wwm-cased` |
| **Tamaño** | ~420MB |
| **Accuracy** | 98.93% |
| **F1-Score** | 98.92% |
| **Ejemplos entrenamiento** | 4,358 |
| **Clases (intenciones)** | 10 |
| **Formato** | SafeTensors + PyTorch |

## 🔍 Verificación de la Instalación

Una vez descargado/entrenado el modelo, verifica que esté correctamente instalado:

```bash
# Debe existir el directorio y archivos
ls modelo_bert_tyr_10_clases_COMPLETO/

# Deberías ver:
# - config.json
# - model.safetensors (420MB)
# - tokenizer.json
# - vocab.txt
# - label_map.json
```

### Test Rápido

```python
# test_modelo.py
from tyr_chatbot import TYRChatbot

# Cargar chatbot
chatbot = TYRChatbot()

# Prueba
resultado = chatbot.procesar_mensaje("¿Qué carreras hay en el ITSE?")
print(f"Intención: {resultado['intencion']}")
print(f"Confianza: {resultado['confianza']:.2%}")
print(f"Respuesta: {resultado['respuesta'][:100]}...")
```

Si ves la respuesta correcta, ¡el modelo está funcionando! ✅

## ⚠️ Troubleshooting

### Error: "No such file or directory: modelo_bert_tyr_10_clases_COMPLETO"

**Solución:** El modelo no está descargado. Sigue la Opción 1 o 2 arriba.

### Error: "CUDA out of memory"

**Solución:** Si estás entrenando localmente, reduce el batch size en el notebook o usa CPU:

```python
# En el notebook, cambiar:
device = torch.device("cpu")  # En vez de "cuda"
```

### Error: "ValueError: Invalid file: model.safetensors"

**Solución:** El modelo está corrupto. Vuelve a descargar el ZIP completo.

## 📝 Notas Importantes

- **No subas el modelo a GitHub** - Está en `.gitignore` por su tamaño
- **Usa Git LFS** si trabajas en un fork y quieres versionar el modelo
- **Actualiza el modelo** siguiendo [GUIA_REENTRENAMIENTO.md](GUIA_REENTRENAMIENTO.md) si añades nuevos datos

## 🆘 Ayuda

Si tienes problemas:

1. Revisa [DEPLOYMENT_GUIDE.md](docs/guides/DEPLOYMENT_GUIDE.md)
2. Abre un [issue en GitHub](https://github.com/EiTinchoZ/TYR/issues)
3. Contacta al mantenedor: mbundy.deltawaves@gmail.com

---

**Última actualización:** Noviembre 2025
**Versión del modelo:** v3 (4,358 ejemplos, 10 clases)
