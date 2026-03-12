# SQL Injection

**Severity**: Critical

## Description
SQL injection occurs when untrusted input is concatenated directly into SQL queries, allowing an attacker to manipulate the query logic. This can lead to unauthorized data access, data modification, data deletion, or even full system compromise. It is consistently ranked as one of the most dangerous web application vulnerabilities.

## Detection
- String concatenation or interpolation used to build SQL queries with user-supplied values
- Use of format strings, f-strings, or template literals to embed variables in SQL
- Raw SQL execution functions called with dynamically constructed query strings
- Absence of parameterized queries or prepared statements
- Keywords to look for: `execute`, `query`, `raw`, `cursor`, `sql`, combined with `+`, `%`, `f"`, `.format(`
- ORM methods that accept raw SQL strings (e.g., `raw()`, `extra()`, `RawSQL`)

## Remediation
Always use parameterized queries or prepared statements. Never concatenate user input into SQL strings.

**Before:**
```
function getUser(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    result = db.execute(query)
    return result
```

**After:**
```
function getUser(username):
    query = "SELECT * FROM users WHERE name = ?"
    result = db.execute(query, [username])
    return result
```

For ORMs, use the query builder or model methods rather than raw SQL:
```
function getUser(username):
    return User.objects.filter(name=username).first()
```
