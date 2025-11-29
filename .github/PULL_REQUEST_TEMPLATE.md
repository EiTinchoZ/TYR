## 📝 Descripción

<!-- Describe claramente los cambios realizados en este PR -->

## 🎯 Tipo de Cambio

<!-- Marca con [x] lo que aplica -->

- [ ] 🐛 Bug fix (cambio que arregla un issue)
- [ ] ✨ Nueva característica (cambio que añade funcionalidad)
- [ ] 💥 Breaking change (cambio que rompe compatibilidad anterior)
- [ ] 📚 Documentación (mejoras o correcciones en docs)
- [ ] 🎨 Estilo (formato, puntos y comas, etc - sin cambios de código)
- [ ] ♻️ Refactoring (cambios de código que no arreglan bugs ni añaden features)
- [ ] ⚡ Performance (mejoras de rendimiento)
- [ ] ✅ Tests (añadir tests faltantes o corregir existentes)
- [ ] 🔧 Chore (cambios en build, CI, dependencias, etc)

## 🔗 Issues Relacionados

<!-- Referencia issues relacionados usando #numero -->

Fixes #
Closes #
Related to #

## 📋 Checklist

<!-- Marca con [x] cuando hayas completado cada ítem -->

### General

- [ ] Mi código sigue las guías de estilo del proyecto
- [ ] He realizado una auto-revisión de mi código
- [ ] He comentado mi código, especialmente en áreas difíciles de entender
- [ ] He actualizado la documentación según sea necesario
- [ ] Mis cambios no generan nuevos warnings

### Tests

- [ ] He añadido tests que prueban que mi fix es efectivo o que mi feature funciona
- [ ] Los tests nuevos y existentes pasan localmente con mis cambios
- [ ] He verificado que la cobertura de código no disminuye significativamente

### Backend (si aplica)

- [ ] He ejecutado `pytest tests/ -v` y todos los tests pasan
- [ ] He verificado que no hay vulnerabilidades con `safety check`
- [ ] He actualizado `requirements.txt` si añadí dependencias
- [ ] El código sigue PEP 8 (verificado con `black` y `flake8`)

### Frontend (si aplica)

- [ ] He ejecutado `npm run build:check` sin errores
- [ ] He ejecutado `npm run lint` y corregido los warnings
- [ ] He probado en diferentes navegadores (Chrome, Firefox, Safari)
- [ ] He verificado la responsividad en móvil/tablet
- [ ] He actualizado `package.json` si añadí dependencias

### Modelo/Dataset (si aplica)

- [ ] He documentado los cambios en el dataset
- [ ] He actualizado las métricas de performance si aplica
- [ ] He incluido instrucciones para re-entrenar el modelo si es necesario

## 🧪 Cómo Probar

<!-- Proporciona instrucciones claras para probar tus cambios -->

1.
2.
3.

## 📸 Screenshots (si aplica)

<!-- Añade screenshots para cambios visuales -->

### Antes
<!-- Screenshot del comportamiento anterior -->

### Después
<!-- Screenshot del nuevo comportamiento -->

## 📊 Impacto en Performance

<!-- Si aplica, describe el impacto en performance -->

- [ ] Sin impacto en performance
- [ ] Mejora en performance: <!-- describe la mejora -->
- [ ] Posible degradación en performance: <!-- describe y justifica -->

## 🚧 Notas Adicionales

<!-- Cualquier información adicional que los revisores deban saber -->

## 📚 Referencias

<!-- Links a documentación, artículos, o PRs relacionados -->

---

**Recordatorio para revisores:**
- [ ] El código es claro y mantenible
- [ ] Los tests cubren los casos edge
- [ ] La documentación está actualizada
- [ ] No hay código duplicado innecesariamente
- [ ] No hay secretos o credenciales hardcodeadas
