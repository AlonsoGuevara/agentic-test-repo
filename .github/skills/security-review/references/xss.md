# Cross-Site Scripting (XSS)

**Severity**: High

## Description
Cross-site scripting occurs when untrusted data is included in web output without proper sanitization or encoding, allowing an attacker to inject malicious scripts that execute in other users' browsers. XSS can lead to session hijacking, credential theft, defacement, and malware distribution. Variants include reflected XSS, stored XSS, and DOM-based XSS.

## Detection
- User input rendered directly into HTML templates without escaping
- Use of dangerous rendering functions: `innerHTML`, `outerHTML`, `document.write()`, `insertAdjacentHTML`
- Template engines with auto-escaping disabled or bypassed (e.g., `|safe`, `{% autoescape off %}`, `markupsafe.Markup`, `dangerouslySetInnerHTML`)
- URL parameters reflected into page content without encoding
- Dynamic construction of HTML strings with user-controlled data
- Event handler attributes built from user input (`onclick`, `onerror`, etc.)
- JavaScript URLs: `href="javascript:..."` built with user data

## Remediation
Always encode or escape user input before rendering it in HTML. Use framework-provided auto-escaping and avoid bypassing it.

**Before:**
```
function renderComment(comment):
    element.innerHTML = comment.text
```

**After:**
```
function renderComment(comment):
    element.textContent = comment.text
```

For HTML contexts where markup is needed, use a sanitization library:
```
function renderComment(comment):
    sanitized = sanitize(comment.text, allowedTags=["b", "i", "a"])
    element.innerHTML = sanitized
```
