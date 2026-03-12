# Security Review Resources

Place one `.md` file per vulnerability type in this folder. The `security-review` skill will automatically load all files here during a review.

## File Naming

Use lowercase kebab-case: `sql-injection.md`, `xss.md`, `hardcoded-secrets.md`.

## Required Structure

Each file must follow this template:

```markdown
# <Vulnerability Name>

**Severity**: Critical | High | Medium | Low

## Description
What this vulnerability is and why it's dangerous.

## Detection
How to identify it — keywords, structural cues, code patterns to look for.

## Remediation
How to fix it, with a before/after example where helpful.
```
