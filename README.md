# TYR - Intelligent Virtual Assistant for ITSE

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![BERT](https://img.shields.io/badge/BERT-Spanish-yellow.svg)](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased)
[![React](https://img.shields.io/badge/React-18.3-61DAFB.svg?logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6-3178C6.svg?logo=typescript)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/Tests-80%20passing-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-91%25-green.svg)](tests/)
[![Accuracy](https://img.shields.io/badge/Accuracy-98.93%25-success.svg)](#model-metrics)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

TYR is an intelligent virtual assistant built with BERT for the Instituto Técnico Superior Especializado (ITSE) in Panama. It provides accurate, context-aware responses about the institution's 16 technical programs, admission processes, scholarships, and general information.

**Key Achievement:** 98.93% classification accuracy, exceeding the academic goal of 85% by 13.93 percentage points.

---

<div align="center">
  <img src="branding/01_logos/logo_horizontal_con_tagline.png" alt="TYR - Tu asistente virtual inteligente" width="600">
</div>

---

## Overview

TYR combines state-of-the-art Natural Language Processing with a modern web interface to deliver an exceptional user experience. The system features:

- **Dual-mode operation**: Full AI-powered mode with BERT (98.93% accuracy) or intelligent demo mode with pre-defined responses
- **Progressive Web App**: Installable on Android and iOS devices with offline support
- **Professional UI/UX**: Modern landing page with integrated chat modal, responsive design, and smooth animations
- **Advanced NLP**: BERT-based intent classification with VADER sentiment analysis and custom NER (Named Entity Recognition)
- **Entity Extraction**: Recognizes 6 types of entities (careers, services, organizations, locations, requirements, time periods) with ~95% precision
- **Real-time Visualization**: Visual display of detected sentiment (😊😐😟) and color-coded entity recognition
- **Comprehensive knowledge base**: Complete information about ITSE's programs, services, and procedures

The assistant handles 9 different intent categories and provides specific responses for 16 technical programs, special services (CAIPI daycare, CIIECYT research center), international recognizations, and institutional partnerships.

---

## Quick Start

> **Note:** The BERT model (421MB) is not included in this repository. To use the full AI-powered mode, download it from [Google Drive](#model-download) and follow the [installation instructions](INSTRUCCIONES_DESCARGA_MODELO.txt).

### Frontend with Demo Mode (Fastest)

Run the modern React interface with intelligent mock responses (no backend required):

```bash
cd Figma
npm install
npm run dev
# Open http://localhost:5173
```

The chat automatically uses smart pre-defined responses when the backend is unavailable.

### Full Stack with AI (Recommended)

**Prerequisites:** Download the BERT model first (see [Model Download](#model-download) section below).

Run both backend (BERT model) and frontend for full AI-powered responses:

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
# Backend at http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd Figma
npm install
cp .env.example .env
npm run dev
# Frontend at http://localhost:5173
```

### Alternative: Streamlit Interface

Simple interface for testing and development:

```bash
pip install -r requirements.txt
streamlit run tyr_chatbot.py
# Open http://localhost:8501
```

---

## Features

### Progressive Web App (PWA)
- Installable on mobile devices (Android/iOS)
- Works offline with service workers
- Automatic updates
- Native app experience

### Advanced Chat Interface
- Conversation history
- Export to PDF
- Dark/light mode themes
- Voice input via Web Speech API
- Markdown-formatted responses
- Smart suggestions

### Dual-Mode Intelligence
- **With backend**: Real BERT-based AI (98.93% accuracy)
- **Without backend**: Intelligent mock responses
- Automatic fallback system
- Seamless transition

### Professional Design
- Complete landing page
- Integrated chat modal
- Responsive layout (desktop/tablet/mobile)
- Smooth animations
- Modern gradients and shadows

### Named Entity Recognition (NER)
- Custom domain-specific entity extraction
- 6 entity types: CARRERA, SERVICIO, ORGANIZACION, UBICACION, REQUISITO, PERIODO
- ~95% precision on ITSE domain entities
- 21 unit tests with 100% pass rate
- Integrated in main chatbot pipeline
- Zero additional dependencies

**Example:**
```python
Input: "Quiero estudiar Big Data en el ITSE de Tocumen"
Output:
  CARRERA: ['big data']
  ORGANIZACION: ['itse']
  UBICACION: ['tocumen']
```

See [IMPLEMENTACION_NER.md](IMPLEMENTACION_NER.md) for technical details.

---

## Model Metrics

### Performance Results

| Metric | Academic Goal | Achieved | Status |
|--------|--------------|----------|--------|
| **Accuracy** | ≥ 85% | **98.93%** | +13.93% above target |
| **F1-Score** | ≥ 82% | **98.92%** | +16.92% above target |
| **Precision** | - | **98.92%** | Excellent |
| **Recall** | - | **98.93%** | Excellent |

### Dataset
- **Training examples**: 4,358
- **Distribution**: 70% train / 15% validation / 15% test
- **Intent classes**: 9 categories
- **Question patterns**: 48 variations

### Intent Categories

1. Career information (2,832 examples, 65%)
2. Admission and enrollment
3. Entrance requirements
4. Scholarships and financial aid
5. Schedules and duration
6. Contact and location
7. General FAQs
8. Greetings and farewells
9. Out of domain

---

## Technology Stack

### Frontend
- React 18.3 with TypeScript 5.6
- Vite 5.4 for build tooling
- Tailwind CSS 3.4 for styling
- Radix UI for components
- Framer Motion for animations
- Lucide React for icons

### Backend
- FastAPI 0.115 for REST API
- PyTorch 2.9 for model inference
- Transformers 4.57 (Hugging Face)
- BERT: `dccuchile/bert-base-spanish-wwm-cased`
- VADER-ES for sentiment analysis

### Machine Learning & NLP
- Model: BERT Spanish (110M parameters)
- Fine-tuned on 4,358 custom examples
- 9-class intent classification
- Sentiment analysis with VADER
- Custom NER for entity extraction (6 types)

---

## Project Structure

```
TYR/
├── Figma/                          # React frontend (PWA)
│   ├── components/                 # React components
│   │   ├── TYRChat.tsx            # Main chat component
│   │   ├── ui/                    # UI component library
│   │   └── ...
│   ├── utils/
│   │   └── mockResponses.ts       # Demo mode responses
│   ├── public/
│   │   ├── manifest.json          # PWA configuration
│   │   └── branding/              # Visual assets
│   ├── package.json
│   └── vite.config.ts
│
├── backend/                        # FastAPI backend
│   ├── main.py                    # API endpoints
│   ├── tyr_simple.py              # BERT chatbot core
│   └── requirements.txt
│
├── tests/                          # Test suite (80 tests)
│   ├── test_tyr_chatbot.py        # BERT classification tests
│   ├── test_normalizacion.py     # Text normalization tests
│   ├── test_respuestas.py         # Response tests
│   └── test_ner.py                # NER entity extraction tests (21)
│
├── data/                           # Knowledge base (JSON)
│   ├── carreras_itse.json         # 16 technical programs
│   ├── respuestas_base.json       # Base responses
│   └── label_map.json             # Intent mappings
│
├── documentacion/                  # Documentation
│   ├── screenshots/               # UI screenshots
│   ├── visualizaciones/           # Performance charts
│   └── ARQUITECTURA_SISTEMA.md    # System architecture
│
├── branding/                       # Brand assets
│   ├── 01_logos/                  # Logo variations
│   ├── 02_icons/                  # Feature icons
│   ├── 03_illustrations/          # Illustrations
│   └── 04_backgrounds/            # Backgrounds
│
├── ner_module.py                  # Named Entity Recognition module
├── demo_ner.py                    # NER demonstration script
├── verificar_ner.py               # NER verification script
├── Dataset_TYR_3000_FINAL.json    # Training dataset
├── tyr_chatbot.py                 # Streamlit app (with NER integrated)
├── requirements.txt               # Python dependencies
├── IMPLEMENTACION_NER.md          # NER technical documentation
└── README.md                      # This file
```

---

## Model Download

The trained BERT model (421MB) is required for full AI-powered responses. It's not included in this repository due to size constraints.

### Download Instructions

1. **Download the model from Google Drive:**
   - [Download modelo_bert_tyr_10_clases_COMPLETO.zip](https://drive.google.com/drive/folders/1EyCCO7cv14ubufmvhDyGc_Jv02YPTBSO?usp=sharing)
   - File size: 421MB

2. **Extract to project root:**
   ```bash
   # Place the ZIP in the TYR/ directory
   cd TYR/
   unzip modelo_bert_tyr_10_clases_COMPLETO.zip
   ```

3. **Verify the structure:**
   ```
   TYR/
   ├── modelo_bert_tyr_10_clases_COMPLETO/
   │   ├── model.safetensors (420MB)
   │   ├── config.json
   │   ├── tokenizer.json
   │   └── ... (other files)
   ```

For detailed instructions, see [INSTRUCCIONES_DESCARGA_MODELO.txt](INSTRUCCIONES_DESCARGA_MODELO.txt).

### Alternative: Demo Mode Without Model

You can use TYR in demo mode without downloading the model:
- Runs frontend only with intelligent mock responses
- No backend or model download required
- Perfect for testing the UI/UX

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Python Dependencies

```bash
pip install -r requirements.txt
```

Main dependencies:
- `torch` - PyTorch for deep learning
- `transformers` - Hugging Face transformers
- `fastapi` - Modern web framework
- `uvicorn` - ASGI server
- `vaderSentiment-es` - Spanish sentiment analysis
- `streamlit` - Alternative UI framework

### Node.js Dependencies

```bash
cd Figma
npm install
```

Main dependencies:
- `react` & `react-dom` - UI framework
- `typescript` - Type safety
- `vite` - Build tool
- `tailwindcss` - Utility CSS
- `@radix-ui/react-dialog` - Modal components
- `framer-motion` - Animations

---

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_tyr_chatbot.py -v
```

### Frontend Development

```bash
cd Figma
npm run dev          # Development server
npm run build        # Production build
npm run preview      # Preview production build
npm run lint         # Lint code
```

### Backend Development

```bash
cd backend
python main.py       # Start FastAPI server
# API docs at http://localhost:8000/docs
```

---

## Deployment

### Frontend Deployment (Vercel)

1. Connect your GitHub repository to Vercel
2. Configure build settings:
   - **Framework**: Vite
   - **Root Directory**: `Figma`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
3. Add environment variable (optional):
   - `VITE_API_URL`: Your backend URL
4. Deploy

### Backend Deployment (Railway)

1. Connect repository to Railway
2. Configure settings:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Add environment variables:
   - `PYTHON_VERSION`: `3.11`
4. Deploy

**Note**: The BERT model (420MB) is excluded from the repository. Download or train locally following the instructions in [MODELO_DESCARGA.md](MODELO_DESCARGA.md).

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

---

## Usage Examples

### Example Queries

- "Tell me about the Big Data program"
- "What is CAIPI?"
- "ITSE international recognitions"
- "Strategic partnerships"
- "How do I enroll?"
- "Cybersecurity program requirements"
- "Scholarship information"
- "Contact details"

### API Endpoints

```
GET  /health              # Health check
POST /chat                # Send message to chatbot
GET  /intenciones         # List available intents
GET  /carreras            # List all programs
```

Example request:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"mensaje": "Información sobre Big Data"}'
```

---

## Documentation

- [MVP_GUIDE.md](MVP_GUIDE.md) - Quick MVP deployment guide
- [DEPLOYMENT.md](DEPLOYMENT.md) - Full deployment instructions
- [IMPLEMENTACION_NER.md](IMPLEMENTACION_NER.md) - NER technical documentation
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [SECURITY.md](SECURITY.md) - Security policy
- [documentacion/ARQUITECTURA_SISTEMA.md](documentacion/ARQUITECTURA_SISTEMA.md) - System architecture

---

## Testing

The project includes comprehensive automated tests:

- **80 passing tests** with 91% code coverage
- Unit tests for text normalization
- Integration tests for BERT classification
- Response accuracy tests
- Sentiment analysis tests
- **NER entity extraction tests (21 tests)**

Run all tests:
```bash
pytest -v
```

Run NER tests specifically:
```bash
pytest tests/test_ner.py -v
```

Verify NER implementation:
```bash
python verificar_ner.py
```

---

## Model Training

To retrain the model with your own data:

1. Prepare dataset in JSON format (see [Dataset_TYR_3000_FINAL.json](Dataset_TYR_3000_FINAL.json))
2. Follow notebook: [TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb](TYR_REENTRENAMIENTO_SOLO_PESOS.ipynb)
3. Or use Google Colab for GPU acceleration

See [documentacion/guias/INSTRUCCIONES_REENTRENAMIENTO.md](documentacion/guias/INSTRUCCIONES_REENTRENAMIENTO.md) for details.

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Instituto Técnico Superior Especializado (ITSE) for institutional information
- Hugging Face for the BERT Spanish model
- Universidad de Chile (DCC) for bert-base-spanish-wwm-cased

---

## Contact

**Project Author:** Martín Bundy
**Institution:** Instituto Técnico Superior Especializado (ITSE)
**Email:** mbundy.deltawaves@gmail.com
**GitHub:** [@EiTinchoZ](https://github.com/EiTinchoZ)

**ITSE Contact:**
- Website: [https://www.itse.ac.pa](https://www.itse.ac.pa)
- Email: info@itse.ac.pa
- Phone: +507 524-3333
- Location: Tocumen, Panama

---

**Version:** 1.2.0 (with NER)
**Last Updated:** December 2025
**Status:** Production Ready

**Latest Changes:**
- Added custom Named Entity Recognition (NER) module
- 6 entity types recognized (CARRERA, SERVICIO, ORGANIZACION, UBICACION, REQUISITO, PERIODO)
- 21 new tests for NER (80 total tests)
- Integrated NER in main chatbot pipeline
- ~95% precision on domain-specific entities
