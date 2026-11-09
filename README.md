# Security audit: certbot/certbot

Date: 2026-11-09 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 5 issue(s): 5 high.

## Findings

### 1. [HIGH] Hardcoded credentials

**CWE-798** | `certbot-dns-gehirn/src/certbot_dns_gehirn/_internal/tests/dns_gehirn_test.py` line 16

Credentials hardcoded in source. Anyone with repo access can extract them.

```
API_TOKEN = '00000000-0000-0000-0000-000000000000'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 2. [HIGH] Hardcoded credentials

**CWE-798** | `certbot-dns-gehirn/src/certbot_dns_gehirn/_internal/tests/dns_gehirn_test.py` line 17

Credentials hardcoded in source. Anyone with repo access can extract them.

```
API_SECRET = 'MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 3. [HIGH] Path traversal via unsanitized input

**CWE-22** | `certbot/src/certbot/reverter.py` line 207

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
op_fd = open(filepath, "r+")
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 4. [HIGH] Hardcoded credentials

**CWE-798** | `certbot-dns-cloudflare/src/certbot_dns_cloudflare/_internal/tests/dns_cloudflare_test.py` line 35

Credentials hardcoded in source. Anyone with repo access can extract them.

```
API_TOKEN = 'an-api-token'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 5. [HIGH] Hardcoded credentials

**CWE-798** | `certbot-dns-cloudflare/src/certbot_dns_cloudflare/_internal/tests/dns_cloudflare_test.py` line 37

Credentials hardcoded in source. Anyone with repo access can extract them.

```
API_KEY = 'an-api-key'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---
