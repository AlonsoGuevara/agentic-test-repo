# Anti-Pattern Resources

Place one `.md` file per anti-pattern in this folder. The `antipattern-review` skill will automatically load all files here during a review.

## File Naming

Use lowercase kebab-case: `god-object.md`, `magic-numbers.md`, `long-parameter-list.md`.

## Required Structure

Each file must follow this template:

```markdown
# <Anti-Pattern Name>

**Severity**: High | Medium | Low

## Description
What this anti-pattern is and why it causes problems.

## Detection
How to identify it — keywords, structural cues, code patterns to look for.

## Remediation
How to fix it, with a before/after example where helpful.
```
