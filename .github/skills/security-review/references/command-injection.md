# Command Injection

**Severity**: Critical

## Description
Command injection occurs when untrusted input is passed to system shell commands, allowing an attacker to execute arbitrary operating system commands on the host. This can lead to full system compromise, data exfiltration, lateral movement, and denial of service. It is especially dangerous because it grants the attacker the same privileges as the application process.

## Detection
- Functions that invoke shell commands with user-controlled arguments: `os.system()`, `subprocess.call()` with `shell=True`, `exec()`, `popen()`, `child_process.exec()`
- String concatenation or interpolation used to build shell command strings
- User input passed to shell interpreters without sanitization
- Backtick execution or system call wrappers with dynamic arguments
- Keywords to look for: `system`, `exec`, `popen`, `spawn`, `shell=True`, `subprocess`, `child_process`, combined with user-controlled variables

## Remediation
Avoid shell invocation when possible. Use direct process execution with argument arrays instead of shell strings. Never concatenate user input into shell commands.

**Before:**
```
function convertFile(filename):
    command = "convert " + filename + " output.pdf"
    system(command)
```

**After:**
```
function convertFile(filename):
    # Use argument list instead of shell string
    result = execute(["convert", filename, "output.pdf"], shell=false)
    return result
```

If shell features are truly needed, use allowlists to validate input:
```
function convertFile(filename):
    if not matches(filename, "^[a-zA-Z0-9._-]+$"):
        raise Error("Invalid filename")
    result = execute(["convert", filename, "output.pdf"], shell=false)
    return result
```
