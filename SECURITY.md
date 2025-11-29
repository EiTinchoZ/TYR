# 🔒 Security Policy

## Supported Versions

We currently support the following versions of TYR with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | ✅ Yes             |
| 1.x.x   | ❌ No              |
| < 1.0   | ❌ No              |

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in TYR, please **DO NOT** open a public issue.

### Reporting Process

1. **Send a private email** to: mbundy.deltawaves@gmail.com
   - Subject: "Security Vulnerability in TYR"
   - Include a detailed description of the vulnerability
   - If possible, include steps to reproduce it
   - Attach any proof of concept (PoC) code if applicable

2. **Response time**
   - We will acknowledge your report within **48 hours**
   - We will keep you informed about the progress
   - We will notify you when a patch is released

3. **Responsible disclosure**
   - Please give us **90 days** to resolve the vulnerability before making it public
   - We will coordinate with you on the public announcement if necessary
   - We will give you credit in the CHANGELOG if you wish

## 🛡️ Security Best Practices

### For Users

1. **Keep software updated**
   ```bash
   git pull origin main
   pip install -r requirements.txt --upgrade
   cd Figma && npm update
   ```

2. **Don't expose backend directly**
   - Use HTTPS in production
   - Configure CORS appropriately
   - Use a reverse proxy (nginx, Caddy)

3. **Environment variables**
   - NEVER upload `.env` files to GitHub
   - Use `.env.example` as a template
   - Rotate credentials regularly

4. **Limit access to history**
   - Conversation history may contain sensitive information
   - It's in `.gitignore` by default
   - Implement limited retention in production

### For Developers

1. **Dependencies**
   - Run `npm audit` and `safety check` regularly
   - Update dependencies with known vulnerabilities
   - Use specific versions in `requirements.txt`

2. **Input validation**
   ```python
   # ✅ GOOD
   def procesar_mensaje(mensaje: str) -> dict:
       if not mensaje or len(mensaje) > 1000:
           raise ValueError("Invalid message")
       clean_message = sanitize(mensaje)
       # ... process

   # ❌ BAD
   def procesar_mensaje(mensaje):
       # No validation
       return eval(mensaje)  # NEVER USE EVAL
   ```

3. **Authentication (if implemented)**
   - Use bcrypt/argon2 for passwords
   - Implement rate limiting
   - Use JWT tokens with expiration

4. **CORS**
   ```python
   # Backend - main.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://your-domain.com",  # Specific in production
           # DO NOT use "*" in production
       ],
       allow_credentials=True,
       allow_methods=["GET", "POST"],  # Only what's needed
       allow_headers=["*"],
   )
   ```

## 🔍 Known Security Audits

### Python Backend

```bash
# Install safety
pip install safety

# Run audit
safety check --json
```

### Frontend Node.js

```bash
# npm audit
cd Figma
npm audit

# Automatic fix (if possible)
npm audit fix
```

## 🚫 What is NOT a Vulnerability

To avoid unnecessary reports, the following are NOT considered security vulnerabilities:

1. **Usability issues** - Use normal GitHub Issues
2. **Bugs without security impact** - Use GitHub Issues
3. **Example configurations** - `.example` files are intentionally simple
4. **Outdated dependencies** - Unless they have critical CVE
5. **Missing security features** - Suggest in GitHub Issues

## 📋 Deployment Security Checklist

Before deploying to production:

- [ ] All dependencies are updated
- [ ] Environment variables configured (not hardcoded)
- [ ] HTTPS enabled
- [ ] CORS configured appropriately
- [ ] Rate limiting implemented
- [ ] Logs configured (without sensitive information)
- [ ] Firewall configured
- [ ] Automated backups
- [ ] Error monitoring enabled
- [ ] Incident response plan defined

## 🔐 Known Vulnerabilities

### CVE-XXXX-XXXX (Example)

**Status:** ✅ Resolved in v2.0.1
**Severity:** Medium
**Description:** [Brief description]
**Mitigation:** Update to v2.0.1+

---

There are currently no known vulnerabilities in version 2.0.x

## 📞 Contact

- **Security email:** mbundy.deltawaves@gmail.com
- **GitHub:** https://github.com/EiTinchoZ/TYR
- **GitHub Security Advisories:** https://github.com/EiTinchoZ/TYR/security/advisories

## 🙏 Acknowledgments

We thank the following security researchers for responsibly reporting vulnerabilities:

- [Pending - First list]

---

**Last updated:** November 2025
**Next review:** Every 3 months or as needed
