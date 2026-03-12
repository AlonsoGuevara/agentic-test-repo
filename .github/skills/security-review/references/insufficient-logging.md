# Insufficient Logging and Monitoring

**Severity**: Medium

## Description
Insufficient logging and monitoring occurs when an application fails to record security-relevant events or lacks mechanisms to detect and respond to suspicious activity. Without adequate logging, breaches can go undetected for extended periods, forensic investigation is hampered, and attackers can operate freely without triggering alerts. Key events that must be logged include authentication attempts, access control failures, input validation failures, and administrative actions.

## Detection
- Authentication endpoints (login, logout, password reset) without logging of success/failure
- Access control denials that are silently ignored without logging
- Missing logging of administrative or privileged operations
- Sensitive operations (data export, bulk delete, configuration changes) without audit trails
- Log entries that lack enough context: missing timestamp, user ID, IP address, or action details
- Sensitive data (passwords, tokens, full credit card numbers) included in log output
- Logs written only to local files without centralized collection or rotation
- No alerting configured for repeated authentication failures or anomalous patterns
- Exception handlers that swallow errors silently: `except: pass`, `catch (e) {}`
- Keywords to look for: `except: pass`, `catch {}` (empty), absence of `log`, `audit`, `logger` calls in security-critical code paths

## Remediation
Log all security-relevant events with sufficient context. Centralize logs, set up alerts for suspicious patterns, and ensure logs are tamper-resistant. Never log sensitive data.

**Before:**
```
function login(username, password):
    user = db.findUser(username)
    if not verifyPassword(password, user.passwordHash):
        return error("Invalid credentials")  # No logging
    return createSession(user)

function deleteAccount(request):
    try:
        db.users.delete(request.userId)
    except Exception:
        pass  # Silent failure, no logging

function accessResource(request, resourceId):
    resource = db.find(resourceId)
    if resource.ownerId != request.userId:
        return error("Forbidden")  # No record of unauthorized attempt
```

**After:**
```
function login(username, password):
    user = db.findUser(username)
    if not verifyPassword(password, user.passwordHash):
        securityLog.warn("Failed login attempt",
            user=username,
            ip=request.remoteAddr,
            timestamp=now())
        return error("Invalid credentials")
    securityLog.info("Successful login",
        user=username,
        ip=request.remoteAddr,
        timestamp=now())
    return createSession(user)

function deleteAccount(request):
    try:
        auditLog.info("Account deletion",
            targetUser=request.userId,
            performedBy=request.authenticatedUser,
            timestamp=now())
        db.users.delete(request.userId)
    except Exception as e:
        errorLog.error("Account deletion failed",
            targetUser=request.userId,
            error=str(e))
        raise

function accessResource(request, resourceId):
    resource = db.find(resourceId)
    if resource.ownerId != request.userId:
        securityLog.warn("Unauthorized access attempt",
            user=request.userId,
            resource=resourceId,
            ip=request.remoteAddr,
            timestamp=now())
        return error("Forbidden")
```
