# Broken Authentication

**Severity**: Critical

## Description
Broken authentication encompasses weaknesses in how an application verifies user identity. This includes weak password policies, missing multi-factor authentication, improper session management, credential stuffing vulnerabilities, and flawed login logic. When authentication is broken, attackers can compromise user accounts, gain unauthorized access, and impersonate legitimate users.

## Detection
- Password comparison using plain text instead of hashed values
- Use of weak hashing algorithms for passwords: MD5, SHA1, SHA256 without key stretching
- Missing rate limiting or account lockout on login endpoints
- Session tokens that are predictable, short, or insufficiently random
- Session IDs exposed in URLs or logs
- Missing session invalidation on logout or password change
- Authentication bypass through parameter manipulation (e.g., `isAdmin=true` in request body)
- JWT tokens without signature verification, using `alg: none`, or with weak secrets
- Cookies missing `Secure`, `HttpOnly`, or `SameSite` attributes
- Keywords to look for: `md5`, `sha1`, `compare`, `==` with password variables, `session`, `token`, `jwt`, `alg`, `verify=false`

## Remediation
Use strong, industry-standard authentication mechanisms. Hash passwords with modern algorithms, implement proper session management, and validate all authentication tokens.

**Before:**
```
function login(username, password):
    user = db.findUser(username)
    if user.password == password:  # Plain text comparison
        session.token = generateSequentialId()  # Predictable token
        return session

function hashPassword(password):
    return md5(password)  # Weak hash
```

**After:**
```
function login(username, password):
    user = db.findUser(username)
    if not checkRateLimit(username):
        raise Error("Too many attempts")
    if not verifyHash(password, user.passwordHash):  # Constant-time comparison
        incrementFailedAttempts(username)
        raise Error("Invalid credentials")
    session.token = generateSecureRandom(32)  # Cryptographically random
    session.setFlag("HttpOnly", true)
    session.setFlag("Secure", true)
    return session

function hashPassword(password):
    return bcrypt.hash(password, rounds=12)  # Modern key-stretching hash
```
