# Sensitive Data Exposure

**Severity**: High

## Description
Sensitive data exposure occurs when an application fails to adequately protect sensitive information — such as credentials, personal data, financial information, or health records — during storage, transit, or processing. This includes transmitting data over unencrypted channels, storing data without encryption, logging sensitive values, using weak cryptographic algorithms, or exposing sensitive data in error messages and API responses.

## Detection
- HTTP URLs used instead of HTTPS for sensitive operations
- Sensitive data (passwords, tokens, PII) written to log files
- API responses that return more fields than necessary (over-fetching), including internal IDs, password hashes, or tokens
- Error messages that reveal stack traces, database schemas, or internal paths to end users
- Sensitive data stored in local storage, cookies without encryption, or client-side state
- Use of weak or obsolete cryptographic algorithms: DES, RC4, MD5, SHA1 for sensitive data
- Missing TLS certificate validation (`verify=false`, `rejectUnauthorized=false`)
- Sensitive data in URL query parameters (visible in logs and browser history)
- Keywords to look for: `log`, `print`, `console.log` with password/token/key variables, `verify=False`, `http://` for API calls, `DES`, `RC4`

## Remediation
Classify data by sensitivity level. Encrypt sensitive data at rest and in transit. Minimize exposure in logs, error messages, and API responses.

**Before:**
```
function loginUser(username, password):
    log("Login attempt: user=" + username + " password=" + password)
    response = httpClient.post("http://api.example.com/auth",
        data={username: username, password: password},
        verifySSL=false)
    return response

function getUser(userId):
    user = db.users.findById(userId)
    return user  # Returns all fields including passwordHash, ssn, etc.
```

**After:**
```
function loginUser(username, password):
    log("Login attempt: user=" + username)  # Never log passwords
    response = httpClient.post("https://api.example.com/auth",
        data={username: username, password: password},
        verifySSL=true)
    return response

function getUser(userId):
    user = db.users.findById(userId)
    return {
        id: user.id,
        name: user.name,
        email: user.email
        # Exclude sensitive fields
    }
```
