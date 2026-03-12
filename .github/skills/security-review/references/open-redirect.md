# Open Redirect

**Severity**: Medium

## Description
Open redirect occurs when an application accepts a user-controlled URL parameter and redirects the user to that URL without validation. Attackers use this to craft phishing links that appear to originate from a trusted domain but redirect victims to malicious sites. This erodes user trust, enables credential theft through convincing phishing pages, and can be chained with other vulnerabilities like OAuth token theft.

## Detection
- Redirect functions that use user-supplied URLs: `redirect(request.getParameter("url"))`, `response.redirect(req.query.next)`
- URL parameters named `redirect`, `next`, `url`, `return`, `returnUrl`, `goto`, `target`, `destination` used in redirect logic
- Missing validation that the redirect target is a relative path or belongs to an allowed domain
- Client-side redirects using `window.location = userInput` or `location.href = userInput`
- OAuth callback URLs that accept arbitrary redirect targets
- Keywords to look for: `redirect`, `302`, `Location header`, `window.location`, `next=`, `returnUrl=`

## Remediation
Validate redirect targets against an allowlist of trusted domains. Prefer relative paths for redirects. Never redirect to user-supplied absolute URLs without validation.

**Before:**
```
function handleLogin(request):
    user = authenticate(request)
    redirectUrl = request.getParameter("next")
    return redirect(redirectUrl)  # Attacker: ?next=https://evil.com
```

**After:**
```
ALLOWED_HOSTS = ["example.com", "app.example.com"]

function handleLogin(request):
    user = authenticate(request)
    redirectUrl = request.getParameter("next")

    if redirectUrl:
        parsed = parseUrl(redirectUrl)
        # Allow only relative paths or trusted hosts
        if parsed.host and parsed.host not in ALLOWED_HOSTS:
            redirectUrl = "/dashboard"
    else:
        redirectUrl = "/dashboard"

    return redirect(redirectUrl)
```
