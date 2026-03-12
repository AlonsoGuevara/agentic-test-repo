# Error Hiding

**Severity**: High

## Description
Silently catching or ignoring errors without logging, handling, or propagating them. This makes debugging extremely difficult because failures are hidden, leaving no trace. Problems manifest differently downstream, making root cause analysis nearly impossible.

## Detection
- Empty except blocks: `except: pass`
- `try/except` catching errors and silently returning None
- Catching broad exceptions (Exception, Error) that should be more specific
- Error logs without re-raising
- Swallowing exceptions and returning default values silently
- Comments suggesting errors are being ignored intentionally

## Remediation
Handle errors explicitly. Log errors with context. Either recover from the specific error, or propagate it up with proper context. Use more specific exception types.

**Before:**
```
function parseUserData(jsonStr):
    try:
        return parse(jsonStr)
    catch:  // Silently hides all errors!
        pass   // Returns nothing with no indication of failure

function authenticate(username, password):
    try:
        user = findUser(username)
        if user.verifyPassword(password):
            return user
    catch Exception:  // Catches all, hides everything
        return null  // Caller doesn't know what failed

function writeToFile(filename, data):
    try:
        file = open(filename, "w")
        file.write(data)
    catch:  // File write failed? Network error? Unknown!
        print("Error")  // Doesn't indicate what was wrong
```

**After:**
```
function parseUserData(jsonStr):
    try:
        return parse(jsonStr)
    catch ParseError as e:
        log.error("Failed to parse JSON: " + jsonStr, exception: e)
        throw ValueError("Invalid JSON data: " + e)

function authenticate(username, password):
    try:
        user = findUser(username)
        if user == null:
            throw ValueError("User not found: " + username)
        if not user.verifyPassword(password):
            throw ValueError("Invalid password")
        return user
    catch ValueError as e:
        log.warning("Authentication failed for " + username + ": " + e)
        throw  // Let caller handle it
    catch Exception as e:
        log.error("Unexpected error during authentication for " + username, exception: e)
        throw

function writeToFile(filename, data):
    try:
        file = open(filename, "w")
        file.write(data)
    catch FileNotFoundError as e:
        log.error("File not found: " + filename)
        throw
    catch IOError as e:
        log.error("Failed to write to " + filename + ": " + e)
        throw
```
