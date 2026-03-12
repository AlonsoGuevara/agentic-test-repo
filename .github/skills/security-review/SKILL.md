---
name: security-review
description: 'Review code for security vulnerabilities. Use when asked to check, audit, scan, or review code for security issues, vulnerabilities, or unsafe practices. Loads vulnerability definitions from references/ and reports findings with file locations and remediation guidance.'
argument-hint: 'Optional: specific file or folder to review (defaults to changed/active files)'
---

# Security Review

Check code against a library of known security vulnerabilities and report findings with actionable remediation guidance.

## When to Use

- "Check this code for security issues"
- "Review for vulnerabilities"
- "Audit the codebase for security"
- "Scan for security problems before merging"
- "Is this code safe?"
- "Check for OWASP Top 10 issues"

## Procedure

### 1. Identify Scope

Determine what to review:
- If the user specifies a file or folder, use that.
- If not, check which files are currently open or recently changed.
- For a full audit, traverse the relevant source directories.

### 2. Load Vulnerability Definitions

Read every `.md` file inside [`./references/`](./references/). Each file defines one vulnerability category:
- **Name** — short identifier
- **Description** — what it is and why it's dangerous
- **Detection** — how to spot it (patterns, keywords, structural cues)
- **Remediation** — how to fix it

If no resource files exist yet, inform the user and stop.

### 3. Analyze the Code

For each vulnerability definition:
1. Search the target files for the patterns described under **Detection**.
2. Record every match: file path, line range, and the vulnerability name.

Work through all vulnerability types before moving to the next step.

### 4. Report Findings

Group findings by severity (if defined in the resource file) or by vulnerability type, then by file.

For each finding output:

```
## <Vulnerability Name>

**File**: `path/to/file.ts` (lines X–Y)
**Severity**: Critical / High / Medium / Low
**Issue**: One-sentence description of the specific vulnerability.
**Impact**: What an attacker could achieve by exploiting this.
**Remediation**: Concrete fix for this instance.
```

If no violations are found for a vulnerability type, skip it in the report.

### 5. Summary

End with a summary table:

| Vulnerability | Occurrences | Severity |
|---|---|---|
| Example Name | 3 | Critical |

If no vulnerabilities are found at all, say so clearly.

## Resource File Convention

Vulnerability definitions live in [`./references/`](./references/). Each file should follow this structure:

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

Add new vulnerability types simply by dropping a new `.md` file into `./references/`.
