---
description: "Use when: running Python code, managing Python dependencies, creating virtual environments, installing packages, or executing Python scripts and commands."
applyTo: "**/*.py"
---

# Python: Use `uv` for All Operations

All Python dependency management and execution MUST use [`uv`](https://docs.astral.sh/uv/).

## Rules

- **Never** use `pip`, `pip install`, `pip freeze`, `python -m pip`, or `pipx` — use `uv` equivalents instead.
- **Never** use `python` or `python3` directly to run scripts — use `uv run` instead.
- **Never** use `venv`, `virtualenv`, or `python -m venv` — use `uv venv` instead.
- **Never** use `poetry`, `pipenv`, or `conda` for dependency management.

## Command Mapping

| Instead of | Use |
|---|---|
| `pip install <pkg>` | `uv add <pkg>` |
| `pip install -r requirements.txt` | `uv pip install -r requirements.txt` or migrate to `pyproject.toml` |
| `python script.py` | `uv run script.py` |
| `python -m pytest` | `uv run pytest` |
| `python -m venv .venv` | `uv venv` |
| `pip freeze` | `uv pip freeze` |

## Project Setup

- Use `uv init` to initialize new Python projects.
- Use `pyproject.toml` for declaring dependencies (not `requirements.txt`).
- Use `uv lock` to generate/update the lockfile.
- Use `uv sync` to install dependencies from the lockfile.
