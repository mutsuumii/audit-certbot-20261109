# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: certbot-dns-gehirn/src/certbot_dns_gehirn/_internal/tests/dns_gehirn_test.py line 16

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
