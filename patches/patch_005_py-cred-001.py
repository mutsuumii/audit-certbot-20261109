# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: certbot-dns-cloudflare/src/certbot_dns_cloudflare/_internal/tests/dns_cloudflare_test.py line 37

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
