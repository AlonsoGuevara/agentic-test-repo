# Copy and Paste Programming (DRY Violation)

**Severity**: High

## Description
Duplicating code instead of extracting it into reusable functions or modules. This violates the DRY (Don't Repeat Yourself) principle and creates maintenance headaches: when bugs are fixed or logic changes, the fix must be applied to every copy. It also increases codebase size unnecessarily.

## Detection
- Identical or nearly-identical code blocks in multiple locations
- Similar logic with minor variations (variable names, values)
- Functions/methods with identical implementations in different classes
- Copy-pasted error handling or validation logic
- Repeated initialization sequences

## Remediation
Extract common logic into shared functions or modules. Use inheritance, composition, or higher-order functions depending on context.

**Before:**
```
// In userService module
function validateEmail(email):
    regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(email)

function trimAndLower(str):
    return str.trim().toLowerCase()

email = trimAndLower(userInput)
if validateEmail(email):
    # process user

// In subscriptionService module
function validateEmail(email):
    regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(email)

function trimAndLower(str):
    return str.trim().toLowerCase()

email = trimAndLower(subscriberInput)
if validateEmail(email):
    # process subscription
```

**After:**
```
// In utils/validators module
function validateEmail(email):
    regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(email)

function normalizeString(str):
    return str.trim().toLowerCase()

// In userService module
import validateEmail, normalizeString from 'validators'
email = normalizeString(userInput)
if validateEmail(email):
    # process user

// In subscriptionService module
import validateEmail, normalizeString from 'validators'
email = normalizeString(subscriberInput)
if validateEmail(email):
    # process subscription
```
