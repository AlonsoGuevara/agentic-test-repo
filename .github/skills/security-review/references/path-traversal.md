# Path Traversal

**Severity**: High

## Description
Path traversal (also called directory traversal) occurs when user-supplied input is used to construct file paths without proper validation, allowing an attacker to access files and directories outside the intended scope. By using sequences like `../` or absolute paths, attackers can read sensitive system files, application configuration, or even overwrite critical files. This can lead to information disclosure, configuration theft, or arbitrary file write.

## Detection
- User input used directly in file path construction: `open(userInput)`, `readFile(userInput)`, `path.join(base, userInput)`
- Path operations that don't validate against a base directory
- Absence of checks for `..`, `./`, or absolute paths in user-supplied file names
- File download or upload endpoints where the filename comes from user input
- Keywords to look for: `open`, `readFile`, `writeFile`, `path.join`, `os.path.join`, combined with request parameters or user input
- Static file serving with user-controlled path segments

## Remediation
Validate and sanitize file paths. Resolve the canonical path and verify it stays within the intended base directory. Never use raw user input in file paths.

**Before:**
```
function downloadFile(request):
    filename = request.getParameter("file")
    path = "/var/data/uploads/" + filename
    return readFile(path)
```

**After:**
```
function downloadFile(request):
    filename = request.getParameter("file")
    basePath = resolve("/var/data/uploads/")
    fullPath = resolve(join(basePath, filename))

    # Ensure resolved path is within the base directory
    if not startsWith(fullPath, basePath):
        raise Error("Access denied")

    return readFile(fullPath)
```
