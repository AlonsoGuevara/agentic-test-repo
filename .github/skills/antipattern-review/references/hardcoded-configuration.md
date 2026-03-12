# Hardcoded Configuration Values

**Severity**: High

## Description
Configuration values, credentials, API endpoints, file paths, or other deployment-specific settings embedded directly in source code. This makes code inflexible, insecure (credentials in repos), and requires code changes for different environments (dev, staging, production).

## Detection
- Database connection strings in code
- API endpoints, URLs, or hostnames in code
- Credentials (API keys, passwords, tokens) in source
- File system paths hard-coded for specific machines
- Environment-specific settings without conditional logic
- Port numbers, server addresses, or URLs in function calls
- Email addresses, phone numbers, or other contact info embedded

## Remediation
Extract configuration to environment variables, config files, or a configuration management system. Use separate configs for different environments.

**Before:**
```
function connectDatabase():
    conn = connect(
        dbname: "production_db",
        user: "admin",
        password: "secretPassword123",  // NEVER in code!
        host: "192.168.1.100",
        port: 5432
    )
    return conn

function fetchUserData(userId):
    response = httpGet(
        url: "https://api.example.com/v1/users/" + userId,
        headers: {"Authorization": "Bearer sk_live_abcd1234"}  // NEVER in code!
    )
    return response.json()
```

**After:**
```
function connectDatabase():
    conn = connect(
        dbname: getEnv("DB_NAME", "dev_db"),
        user: getEnv("DB_USER"),
        password: getEnv("DB_PASSWORD"),
        host: getEnv("DB_HOST", "localhost"),
        port: getEnv("DB_PORT", 5432)
    )
    return conn

function fetchUserData(userId):
    apiBase = getEnv("API_BASE_URL", "https://api.dev.example.com")
    apiKey = getEnv("API_KEY")
    response = httpGet(
        url: apiBase + "/v1/users/" + userId,
        headers: {"Authorization": "Bearer " + apiKey}
    )
    return response.json()
```

**Configuration file (not committed to repo):**
```
DB_NAME=production_db
DB_USER=admin
DB_PASSWORD=secretPassword123
DB_HOST=db.internal.example.com
API_BASE_URL=https://api.example.com
API_KEY=sk_live_abcd1234
```
