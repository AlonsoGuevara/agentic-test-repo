# Broken Access Control

**Severity**: Critical

## Description
Broken access control occurs when an application fails to properly enforce restrictions on what authenticated users are allowed to do. Attackers can exploit these flaws to access unauthorized functionality or data — such as viewing other users' accounts, modifying data, or accessing admin functions. Common manifestations include insecure direct object references (IDOR), missing function-level access control, privilege escalation, and metadata manipulation.

## Detection
- Endpoints that use user-supplied IDs to fetch resources without ownership verification (IDOR)
- Missing authorization checks on controller methods or API endpoints
- Role checks only performed on the client side (UI), not enforced server-side
- Admin functionality accessible without role verification
- API endpoints that rely solely on authentication (logged in) without authorization (permitted)
- Direct database queries using user-supplied IDs without scoping to the current user
- CORS misconfiguration allowing requests from untrusted origins
- Missing `@authorize`, `@login_required`, `@permission_required` decorators or middleware
- Keywords to look for: `getById`, `findById`, `request.params.id` without ownership check, `isAdmin` client-side only

## Remediation
Implement server-side access control checks for every protected resource and action. Deny by default and verify ownership/permissions before granting access.

**Before:**
```
function getDocument(request):
    docId = request.getParameter("id")
    document = db.documents.findById(docId)  # No ownership check
    return document

function deleteUser(request):
    userId = request.getParameter("userId")
    db.users.delete(userId)  # No admin check
    return success()
```

**After:**
```
function getDocument(request):
    docId = request.getParameter("id")
    currentUser = request.getAuthenticatedUser()
    document = db.documents.findById(docId)

    if document.ownerId != currentUser.id:
        raise Error("Forbidden")

    return document

@requireRole("admin")
function deleteUser(request):
    userId = request.getParameter("userId")
    db.users.delete(userId)
    auditLog("User deleted", userId, request.getAuthenticatedUser().id)
    return success()
```
