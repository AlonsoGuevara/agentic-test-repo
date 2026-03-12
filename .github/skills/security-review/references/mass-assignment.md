# Mass Assignment

**Severity**: High

## Description
Mass assignment (also called over-posting or autobinding) occurs when an application automatically binds user-supplied input to model properties without restricting which fields can be set. An attacker can exploit this by including extra fields in a request — such as `isAdmin`, `role`, `price`, or `verified` — to modify properties that should only be set internally. This is especially prevalent in web frameworks that support model binding from request bodies.

## Detection
- Request body parsed and passed directly to model creation or update functions without field filtering
- ORM or model methods that accept dictionaries/objects without allowlisting fields: `Model.create(**request.body)`, `Object.assign(model, request.body)`, `model.update(request.data)`
- Missing use of serializers, DTOs, or form classes that restrict assignable fields
- Models with sensitive fields (role, permissions, balance, verified) that are also used for user-facing input
- Keywords to look for: `**request`, `**kwargs` with model operations, `Object.assign`, `spread operator (...)` into model, `update_attributes`, `mass_assign`, `from_dict`

## Remediation
Explicitly define which fields are allowed for user input. Use allowlists (not blocklists) to control what can be set. Use dedicated input schemas or DTOs separate from internal models.

**Before:**
```
function createUser(request):
    data = request.getBody()
    # Attacker can add { "role": "admin", "verified": true }
    user = User.create(data)
    return user

function updateProfile(request):
    data = request.getBody()
    user = getCurrentUser(request)
    user.updateFromDict(data)  # Overwrites any field including role, permissions
    user.save()
```

**After:**
```
ALLOWED_FIELDS = ["name", "email", "bio", "avatar"]

function createUser(request):
    data = request.getBody()
    # Only pick allowed fields
    safeData = pickFields(data, ALLOWED_FIELDS)
    safeData["role"] = "user"       # Set defaults server-side
    safeData["verified"] = false
    user = User.create(safeData)
    return user

function updateProfile(request):
    data = request.getBody()
    user = getCurrentUser(request)
    safeData = pickFields(data, ["name", "email", "bio", "avatar"])
    user.updateFromDict(safeData)
    user.save()
```
