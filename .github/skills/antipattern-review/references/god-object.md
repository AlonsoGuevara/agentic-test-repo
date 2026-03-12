# God Object

**Severity**: High

## Description
A class or object that knows too much or does too much. It centralizes excessive functionality, violates the Single Responsibility Principle, and becomes difficult to test, modify, and maintain. God objects often grow over time as developers add features without refactoring.

## Detection
- Classes/objects with many fields (>10-15)
- Classes with many methods (>15-20)
- Methods that reference many properties or handle multiple concerns
- Classes used throughout the codebase (overly coupled dependencies)
- Class name is vague or generic (e.g., `Manager`, `Handler`, `Service` without specificity)
- Mixed concerns (e.g., database access + business logic + API handling in one class)
- Difficulty testing the class in isolation

## Remediation
Break the god object into smaller, focused classes following the Single Responsibility Principle. Each class should have one reason to change.

**Before:**
```
class User:
    id: string
    name: string
    email: string
    password: string
    avatar: string
    role: string
    settings: object
    
    constructor(data):
        # ...
    
    function validate():
        # ...
    
    function save():
        # ...
    
    function delete():
        # ...
    
    function sendEmail(template):
        # ...
    
    function generateToken():
        # ...
    
    function hashPassword():
        # ...
    
    function checkPermission(action):
        # ...
    
    function logActivity(action):
        # ...
    
    function calculateStats():
        # ...
```

**After:**
```
// Focused domain object
class User:
    id: string
    name: string
    email: string
    role: string
    
    constructor(data):
        # ...

// Separate concerns
class UserValidator:
    function validate(user):
        # ...

class UserRepository:
    function save(user):
        # ...
    
    function delete(user):
        # ...

class UserAuthenticator:
    function hashPassword(pwd):
        # ...
    
    function generateToken(user):
        # ...

class UserPermissions:
    function checkPermission(user, action):
        # ...

class UserNotifier:
    function sendEmail(user, template):
        # ...
```
