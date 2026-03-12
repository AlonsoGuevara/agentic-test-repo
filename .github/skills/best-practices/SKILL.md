---
name: best-practices
description: "Load language-specific and framework-specific coding best practices. Use when: writing code in a specific language or framework, reviewing code quality, enforcing coding standards, or needing language/framework conventions and idioms."
argument-hint: "Language and optional frameworks (e.g., python fastapi pandas, typescript react)"
---

# Best Practices Loader

## When to Use
- When writing or reviewing code in a specific programming language
- When working with a specific framework (React, Pandas, Django, etc.)
- When you need language-specific conventions, patterns, and idioms
- When enforcing coding standards for a project

## Procedure

1. Identify the programming language and optionally the framework the user is working with.
2. Run the loader script to fetch best practices:
   ```
   bash ./scripts/load_best_practices <language> [framework ...]
   ```
   - Language only: `bash ./scripts/load_best_practices python`
   - Language + frameworks: `bash ./scripts/load_best_practices python fastapi pandas`
3. If the language or framework is not available, the script will list all supported options.
4. Apply the loaded best practices as guidance when generating or reviewing code.

## Available references

### Languages
- [Python](./references/python.md)
- [TypeScript](./references/typescript.md)

### Frameworks
- [FastAPI](./references/frameworks/fastapi.md)
- [Pandas](./references/frameworks/pandas.md)
- [React](./references/frameworks/react.md)

## Adding New references
- **Language**: Create `./references/<language>.md` using lowercase.
- **Framework**: Create `./references/frameworks/<framework>.md` using lowercase.
