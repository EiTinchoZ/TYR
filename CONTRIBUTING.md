# 🤝 Contributing to TYR

Thank you for your interest in contributing to TYR! This document provides guidelines for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Environment Setup](#development-environment-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [Bug Reports](#bug-reports)
- [Feature Suggestions](#feature-suggestions)

## 📜 Code of Conduct

This project adheres to a professional and respectful code of conduct. By participating, you are expected to uphold this code.

### Our Standards

- **Be respectful** to other contributors
- **Accept constructive criticism** gracefully
- **Focus on what is best** for the community
- **Show empathy** towards other community members

## 🚀 How to Contribute

There are many ways to contribute to TYR:

1. **Report bugs** - If you find an error, open an issue
2. **Suggest improvements** - Propose new features or enhancements
3. **Improve documentation** - Help make the documentation clearer
4. **Contribute code** - Implement new features or fix bugs
5. **Improve the dataset** - Contribute new training examples

## 🛠️ Development Environment Setup

### Prerequisites

- Python 3.8 or higher
- Node.js 16+ and npm (for frontend)
- Git
- 4GB RAM minimum (8GB recommended for training the model)

### Installation

1. **Fork the repository**

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/TYR.git
cd TYR
```

2. **Set up the backend**

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r backend/requirements.txt
```

3. **Set up the frontend**

```bash
cd Figma
npm install
cp .env.example .env
```

4. **Download the model (or train a new one)**

The BERT model is not in the repository due to its size. Options:

- **Option A:** Download the pre-trained model from [Google Drive](https://drive.google.com/drive/folders/1EyCCO7cv14ubufmvhDyGc_Jv02YPTBSO)
- **Option B:** Train your own model following the retraining guide

5. **Run the tests**

```bash
# Backend
pytest tests/ -v

# Frontend (if applicable)
cd Figma
npm test
```

### Project Structure

```
TYR/
├── backend/           # FastAPI API
├── Figma/            # React + TypeScript frontend
├── data/             # JSON knowledge base
├── tests/            # Test suite
├── documentacion/    # Project documentation
└── tyr_chatbot.py   # Main chatbot class
```

## 🔄 Pull Request Process

1. **Create a branch** from `main`

```bash
git checkout -b feature/my-new-feature
# or
git checkout -b fix/my-bug-fix
```

2. **Make your changes**

- Write clean and well-documented code
- Follow the project's style guide
- Add tests for new features
- Update documentation if necessary

3. **Commit your changes**

```bash
git add .
git commit -m "feat: clear description of changes"
```

Use semantic commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Formatting, missing semicolons, etc
- `refactor:` Code refactoring
- `test:` Add tests
- `chore:` Maintenance

4. **Push to your fork**

```bash
git push origin feature/my-new-feature
```

5. **Open a Pull Request**

- Clearly describe what changes you made and why
- Reference any related issues
- Ensure all tests pass
- Request code review

### Acceptance Criteria

Your PR will be accepted if:

- ✅ All tests pass
- ✅ Code follows style guidelines
- ✅ It is well documented
- ✅ Doesn't introduce known bugs
- ✅ Documentation is updated

## 🎨 Style Guide

### Python

- Follow [PEP 8](https://pep8.org/)
- Use type hints when possible
- Document functions with docstrings
- Maximum 88 characters per line (Black formatter)

```python
def procesar_mensaje(mensaje: str, confianza_minima: float = 0.8) -> dict:
    """
    Process a user message and return the chatbot response.

    Args:
        mensaje: User text
        confianza_minima: Minimum confidence threshold

    Returns:
        Dict with response, intent, confidence, and sentiment
    """
    # Your code here
    pass
```

### TypeScript / React

- Use strict TypeScript
- Functional components with hooks
- Component names in PascalCase
- Props typed with interfaces

```typescript
interface ChatMessageProps {
  mensaje: string;
  esUsuario: boolean;
  timestamp: Date;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ mensaje, esUsuario, timestamp }) => {
  // Your code here
}
```

### Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(chat): add voice support
fix(bert): correct intent classification
docs(readme): update installation instructions
```

## 🐛 Bug Reports

If you find a bug, please open an [issue](https://github.com/EiTinchoZ/TYR/issues) with:

### Bug Report Template

```markdown
**Bug Description**
Clear and concise description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. Scroll to '...'
4. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. Windows 10, macOS 14.1, Ubuntu 22.04]
- Python: [e.g. 3.10.5]
- Node.js: [e.g. 18.16.0]
- Browser: [e.g. Chrome 120, Firefox 121]

**Additional Context**
Any other relevant information.
```

## 💡 Feature Suggestions

If you have an idea to improve TYR, open an [issue](https://github.com/EiTinchoZ/TYR/issues) with:

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
Clear description of the problem. E.g., "I'm frustrated that..."

**Describe the solution you'd like**
Clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions or features you've considered.

**Additional Context**
Screenshots, mockups, or any additional context.
```

## 🧪 Tests

All changes must include appropriate tests:

### Backend Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific tests
pytest tests/test_tyr_chatbot.py -v
```

### Frontend Tests (if applicable)

```bash
cd Figma
npm test
npm run test:coverage
```

### Writing Tests

```python
# tests/test_my_functionality.py
import pytest
from tyr_chatbot import TYRChatbot

def test_intent_classification():
    """Test that verifies correct intent classification"""
    chatbot = TYRChatbot()
    result = chatbot.procesar_mensaje("What programs are available?")

    assert result['intencion'] == 'informacion_carreras'
    assert result['confianza'] > 0.8
```

## 📝 Documentation

If you add a new feature, update:

- Main README.md
- Technical documentation in `documentacion/`
- Code docstrings
- Usage examples if applicable

## 🎯 Areas to Contribute

Some areas where you can contribute:

### Backend
- Improve BERT model accuracy
- Optimize response times
- Add new intents
- Improve sentiment analysis

### Frontend
- Improve UX/UI
- Add dark/light mode toggle
- Implement voice chat
- Optimize performance

### Dataset
- Add more training examples
- Improve variety of question patterns
- Fix errors in responses

### Documentation
- Improve installation guides
- Add tutorials
- Translate documentation
- Create demo videos

## ❓ Questions

If you have questions, you can:

1. Review the [documentation](documentacion/)
2. Open an [issue](https://github.com/EiTinchoZ/TYR/issues)
3. Contact the maintainer: mbundy.deltawaves@gmail.com

## 📄 License

By contributing to TYR, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**Thank you for contributing to TYR! 🚀**

Your help makes this project better for the entire ITSE community.
