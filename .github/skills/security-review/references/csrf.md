# Cross-Site Request Forgery (CSRF)

**Severity**: High

## Description
Cross-site request forgery occurs when an attacker tricks a user's browser into making an unintended request to a web application where the user is authenticated. Because the browser automatically includes session cookies, the application cannot distinguish between legitimate and forged requests. CSRF can lead to unauthorized state changes — such as changing email addresses, transferring funds, or modifying account settings — without the user's knowledge.

## Detection
- State-changing operations (POST, PUT, DELETE) that lack CSRF token validation
- Forms that don't include CSRF tokens in hidden fields
- Missing CSRF middleware in web framework configuration
- SameSite cookie attribute not set or set to `None` without justification
- API endpoints that accept both cookie-based and token-based authentication but only check cookies
- CORS configuration that allows credentials from any origin (`Access-Control-Allow-Origin: *` with `Access-Control-Allow-Credentials: true`)
- CSRF protection explicitly disabled in configuration
- Keywords to look for: `csrf_exempt`, `@csrf_exempt`, `csrfProtection=false`, `SameSite=None`, `credentials: true` with wildcard origin

## Remediation
Implement CSRF tokens for all state-changing requests. Use SameSite cookie attributes and validate the origin of requests.

**Before:**
```
# Missing CSRF protection
@route("/transfer", methods=["POST"])
function transferFunds(request):
    amount = request.getParameter("amount")
    recipient = request.getParameter("recipient")
    performTransfer(request.user, recipient, amount)
    return success()

# CSRF explicitly disabled
@csrf_exempt
@route("/settings", methods=["POST"])
function updateSettings(request):
    # ...
```

**After:**
```
# CSRF token validated by middleware
@route("/transfer", methods=["POST"])
@requireCsrfToken
function transferFunds(request):
    amount = request.getParameter("amount")
    recipient = request.getParameter("recipient")
    performTransfer(request.user, recipient, amount)
    return success()

# Cookie configuration
function configureSession():
    session.setCookie("SameSite", "Strict")
    session.setCookie("Secure", true)
    session.setCookie("HttpOnly", true)
```
