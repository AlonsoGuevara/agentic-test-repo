# Python Best Practices

## Code Style
- Follow PEP 8 for formatting and naming conventions.
- Use `snake_case` for functions and variables, `PascalCase` for classes.
- Keep lines under 88 characters (Black formatter default).

## Type Hints
- Use type annotations for all function signatures.
- Use `from __future__ import annotations` for modern annotation syntax.
- Leverage `typing` module types: `Optional`, `Union`, `list`, `dict`, `tuple`.

## Project Structure
- Use `pyproject.toml` for project configuration and dependencies.
- Organize code into packages with clear `__init__.py` exports.
- Separate concerns: models, services, utilities, and entry points.

## Error Handling
- Use specific exception types — avoid bare `except:`.
- Create custom exception hierarchies for domain errors.
- Use context managers (`with` statements) for resource management.

## Testing
- Use `pytest` as the test framework.
- Follow the Arrange-Act-Assert pattern.
- Use fixtures for shared setup, parametrize for test variations.
- Aim for clear test names that describe the behavior being tested.

## Dependencies
- Pin dependencies with version constraints in `pyproject.toml`.
- Use virtual environments (`venv` or tools like `uv`, `poetry`).
- Separate production and development dependencies.

## Documentation
- Write docstrings for all public modules, classes, and functions.
- Use Google or NumPy docstring style consistently.
- Include usage examples in docstrings for complex functions.

## Security
- Never hardcode secrets — use environment variables or secret managers.
- Validate and sanitize all external input.
- Use parameterized queries for database operations.
- Keep dependencies updated to patch known vulnerabilities.

## Performance
- Prefer generators and iterators for large data processing.
- Use list/dict/set comprehensions over manual loops when readable.
- Profile before optimizing — use `cProfile` or `py-spy`.

## Async
- Use `asyncio` for I/O-bound concurrent operations.
- Prefer `async`/`await` over threads for network calls.
- Use `asyncio.gather` for concurrent task execution.
