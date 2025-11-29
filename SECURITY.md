# 🔒 Política de Seguridad

## Versiones Soportadas

Actualmente soportamos las siguientes versiones de TYR con actualizaciones de seguridad:

| Versión | Soportada          |
| ------- | ------------------ |
| 2.0.x   | ✅ Sí              |
| 1.x.x   | ❌ No              |
| < 1.0   | ❌ No              |

## 🚨 Reportar una Vulnerabilidad

Si descubres una vulnerabilidad de seguridad en TYR, por favor **NO** abras un issue público.

### Proceso de Reporte

1. **Envía un email privado** a: mbundy.deltawaves@gmail.com
   - Asunto: "Security Vulnerability in TYR"
   - Incluye una descripción detallada de la vulnerabilidad
   - Si es posible, incluye pasos para reproducirla
   - Adjunta cualquier código de prueba (PoC) si aplica

2. **Tiempo de respuesta**
   - Reconoceremos tu reporte dentro de **48 horas**
   - Te mantendremos informado sobre el progreso
   - Te notificaremos cuando se lance un parche

3. **Divulgación responsable**
   - Por favor, danos **90 días** para resolver la vulnerabilidad antes de hacer divulgación pública
   - Coordinaremos contigo el anuncio público si es necesario
   - Te daremos crédito en el CHANGELOG si lo deseas

## 🛡️ Mejores Prácticas de Seguridad

### Para Usuarios

1. **Mantén actualizado el software**
   ```bash
   git pull origin main
   pip install -r requirements.txt --upgrade
   cd Figma && npm update
   ```

2. **No expongas el backend directamente**
   - Usa HTTPS en producción
   - Configura CORS apropiadamente
   - Usa un reverse proxy (nginx, Caddy)

3. **Variables de entorno**
   - NUNCA subas archivos `.env` a GitHub
   - Usa `.env.example` como plantilla
   - Rota credenciales regularmente

4. **Limita acceso al historial**
   - El historial de conversaciones puede contener información sensible
   - Está en `.gitignore` por defecto
   - Implementa retención limitada en producción

### Para Desarrolladores

1. **Dependencias**
   - Ejecuta `npm audit` y `safety check` regularmente
   - Actualiza dependencias con vulnerabilidades conocidas
   - Usa versiones específicas en `requirements.txt`

2. **Validación de entrada**
   ```python
   # ✅ BUENO
   def procesar_mensaje(mensaje: str) -> dict:
       if not mensaje or len(mensaje) > 1000:
           raise ValueError("Mensaje inválido")
       mensaje_limpio = sanitizar(mensaje)
       # ... procesar

   # ❌ MALO
   def procesar_mensaje(mensaje):
       # Sin validación
       return eval(mensaje)  # NUNCA USES EVAL
   ```

3. **Autenticación (si implementas)**
   - Usa bcrypt/argon2 para passwords
   - Implementa rate limiting
   - Usa tokens JWT con expiración

4. **CORS**
   ```python
   # Backend - main.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://tu-dominio.com",  # Específico en producción
           # NO uses "*" en producción
       ],
       allow_credentials=True,
       allow_methods=["GET", "POST"],  # Solo los necesarios
       allow_headers=["*"],
   )
   ```

## 🔍 Auditorías de Seguridad Conocidas

### Python Backend

```bash
# Instalar safety
pip install safety

# Ejecutar audit
safety check --json
```

### Frontend Node.js

```bash
# Audit de npm
cd Figma
npm audit

# Fix automático (si es posible)
npm audit fix
```

## 🚫 Qué NO es una vulnerabilidad

Para evitar reportes innecesarios, los siguientes NO son considerados vulnerabilidades de seguridad:

1. **Problemas de usabilidad** - Usa GitHub Issues normal
2. **Bugs sin impacto de seguridad** - Usa GitHub Issues
3. **Configuraciones de ejemplo** - Los archivos `.example` son intencionalmente simples
4. **Dependencias sin actualizar** - A menos que tengan CVE crítico
5. **Falta de características de seguridad** - Sugiere en GitHub Issues

## 📋 Checklist de Seguridad para Deployment

Antes de desplegar a producción:

- [ ] Todas las dependencias están actualizadas
- [ ] Variables de entorno configuradas (no hardcoded)
- [ ] HTTPS habilitado
- [ ] CORS configurado apropiadamente
- [ ] Rate limiting implementado
- [ ] Logs configurados (sin información sensible)
- [ ] Firewall configurado
- [ ] Backups automatizados
- [ ] Monitoreo de errores habilitado
- [ ] Plan de respuesta a incidentes definido

## 🔐 Vulnerabilidades Conocidas

### CVE-XXXX-XXXX (Ejemplo)

**Estado:** ✅ Resuelto en v2.0.1
**Severidad:** Media
**Descripción:** [Descripción breve]
**Mitigación:** Actualizar a v2.0.1+

---

Actualmente no hay vulnerabilidades conocidas en la versión 2.0.x

## 📞 Contacto

- **Email de seguridad:** mbundy.deltawaves@gmail.com
- **GitHub:** https://github.com/EiTinchoZ/TYR
- **GitHub Security Advisories:** https://github.com/EiTinchoZ/TYR/security/advisories

## 🙏 Agradecimientos

Agradecemos a los siguientes investigadores de seguridad por reportar vulnerabilidades de manera responsable:

- [Pendiente - Primera lista]

---

**Última actualización:** Noviembre 2025
**Próxima revisión:** Cada 3 meses o cuando sea necesario
