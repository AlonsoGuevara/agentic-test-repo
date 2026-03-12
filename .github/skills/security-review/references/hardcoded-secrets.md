# Hardcoded Secrets

**Severity**: Critical

## Description
Hardcoded secrets — such as passwords, API keys, tokens, and cryptographic keys — embedded directly in source code are a severe security risk. Once code is committed to version control, these secrets become permanently exposed in the repository history. Attackers who gain access to the codebase (via public repos, leaked backups, or compromised developer machines) can use these credentials to access production systems, APIs, and databases.

## Detection
- Variables named `password`, `secret`, `api_key`, `token`, `private_key`, `auth`, `credential` assigned string literals
- Connection strings with embedded passwords: `postgresql://user:password@host/db`
- Hardcoded JWT secrets, encryption keys, or signing keys
- API keys in configuration files committed to version control (especially `.env` files without `.gitignore`)
- Cloud provider credentials: AWS access keys (`AKIA...`), Azure connection strings, GCP service account keys
- Base64-encoded strings that decode to credentials
- Comments like `# TODO: move to env vars` near hardcoded values

## Remediation
Store secrets in environment variables, secret managers, or encrypted configuration systems. Never commit secrets to source code.

**Before:**
```
DATABASE_URL = "postgresql://admin:s3cretP@ss@db.example.com/production"
API_KEY = "sk-abc123def456ghi789"
JWT_SECRET = "my-super-secret-key"
```

**After:**
```
DATABASE_URL = getEnvironmentVariable("DATABASE_URL")
API_KEY = getEnvironmentVariable("API_KEY")
JWT_SECRET = getEnvironmentVariable("JWT_SECRET")
```

For more sensitive environments, use a secret manager:
```
function getDatabaseUrl():
    secret = secretManager.getSecret("production/database-url")
    return secret.value
```
