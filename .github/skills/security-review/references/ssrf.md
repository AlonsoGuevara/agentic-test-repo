# Server-Side Request Forgery (SSRF)

**Severity**: High

## Description
Server-side request forgery occurs when an application fetches a remote resource using a user-supplied URL without proper validation. An attacker can abuse this to make the server send requests to internal services, cloud metadata endpoints, or other unintended destinations. SSRF can lead to internal network scanning, access to cloud instance metadata (credentials), data exfiltration from internal APIs, and in some cases remote code execution.

## Detection
- User-supplied URLs passed directly to HTTP client functions: `requests.get(url)`, `fetch(url)`, `urllib.urlopen(url)`, `http.get(url)`
- URL parameters used to proxy or redirect requests on the server side
- File fetching or import functionality that accepts URLs from users
- Webhook registration endpoints that don't validate callback URLs
- Image/document processing that fetches resources from user-provided URLs
- Absence of URL allowlisting or blocking of internal IP ranges
- Keywords to look for: `requests.get`, `fetch`, `urlopen`, `http.get`, `urllib`, `httpClient` combined with user-controlled URL values

## Remediation
Validate and restrict URLs before making server-side requests. Use allowlists for permitted domains/IPs. Block requests to internal networks and cloud metadata endpoints.

**Before:**
```
function fetchUrl(request):
    url = request.getParameter("url")
    response = httpClient.get(url)
    return response.body
```

**After:**
```
ALLOWED_HOSTS = ["api.example.com", "cdn.example.com"]

function fetchUrl(request):
    url = request.getParameter("url")
    parsed = parseUrl(url)

    # Validate scheme
    if parsed.scheme not in ["http", "https"]:
        raise Error("Invalid URL scheme")

    # Validate against allowlist
    if parsed.host not in ALLOWED_HOSTS:
        raise Error("Host not allowed")

    # Block internal IPs
    resolvedIp = dnsResolve(parsed.host)
    if isPrivateIp(resolvedIp):
        raise Error("Internal addresses not allowed")

    response = httpClient.get(url)
    return response.body
```
