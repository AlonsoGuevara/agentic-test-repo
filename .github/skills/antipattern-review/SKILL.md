---
name: antipattern-review
description: 'Review code for anti-patterns. Use when asked to check, audit, scan, or review code for bad practices, anti-patterns, code smells, or quality issues. Loads anti-pattern definitions from references/ and reports findings with file locations and remediation guidance.'
argument-hint: 'Optional: specific file or folder to review (defaults to changed/active files)'
---

# Anti-Pattern Review

Check code against a library of known anti-patterns and report findings with actionable remediation guidance.

## When to Use

- "Check this code for anti-patterns"
- "Review for bad practices / code smells"
- "Audit the codebase for quality issues"
- "Scan for anti-patterns before merging"
- "What's wrong with this code structurally?"

## Procedure

### 1. Identify Scope

Determine what to review:
- If the user specifies a file or folder, use that.
- If not, check which files are currently open or recently changed.
- For a full audit, traverse the relevant source directories.

### 2. Load Anti-Pattern Definitions

Read every `.md` file inside [`./references/`](./references/). Each file defines one anti-pattern:
- **Name** — short identifier
- **Description** — what it is and why it's harmful
- **Detection** — how to spot it (patterns, keywords, structural cues)
- **Remediation** — how to fix it

If no resource files exist yet, inform the user and stop.

### 3. Analyze the Code

For each anti-pattern definition:
1. Search the target files for the patterns described under **Detection**.
2. Record every match: file path, line range, and the anti-pattern name.

Work through all anti-patterns before moving to the next step.

### 4. Report Findings

Group findings by severity (if defined in the resource file) or by anti-pattern, then by file.

For each finding output:

```
## <Anti-Pattern Name>

**File**: `path/to/file.ts` (lines X–Y)
**Severity**: High / Medium / Low
**Issue**: One-sentence description of the specific violation.
**Remediation**: Concrete fix for this instance.
```

If no violations are found for an anti-pattern, skip it in the report.

### 5. Summary

End with a summary table:

| Anti-Pattern | Occurrences | Severity |
|---|---|---|
| Example Name | 3 | High |

If no violations are found at all, say so clearly.

## Resource File Convention

Anti-pattern definitions live in [`./references/`](./references/). Each file should follow this structure:

```markdown
# <Anti-Pattern Name>

**Severity**: High | Medium | Low

## Description
What this anti-pattern is and why it causes problems.

## Detection
How to identify it — keywords, structural cues, code patterns to grep for.

## Remediation
How to fix it, with a before/after example where helpful.
```

Add new anti-patterns simply by dropping a new `.md` file into `./references/`.
