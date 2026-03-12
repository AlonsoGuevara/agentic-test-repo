# FastAPI Best Practices

## Project Structure
- Organize by feature/domain using routers, not by file type.
- Use a separate `schemas.py` (Pydantic models), `models.py` (ORM), and `routes.py` per domain.
- Keep the main `app.py` thin — register routers, middleware, and startup/shutdown events only.

## Routing
- Use `APIRouter` to group related endpoints into modules.
- Use meaningful route prefixes and tags for OpenAPI documentation.
- Keep path operations focused — delegate business logic to service functions.
- Use appropriate HTTP methods and status codes (`201` for creation, `204` for no content).

## Pydantic Models
- Define separate schemas for request, response, and database models.
- Use `Field()` for validation constraints and documentation.
- Leverage model inheritance to reduce duplication (e.g., `BaseUser`, `UserCreate`, `UserResponse`).
- Use `model_config` with `from_attributes = True` for ORM compatibility.

## Dependency Injection
- Use `Depends()` for shared logic: auth, database sessions, configuration.
- Keep dependencies small and composable — chain them when needed.
- Use `yield` dependencies for resource cleanup (e.g., database sessions).
- Define reusable dependencies in a dedicated `dependencies.py` module.

## Error Handling
- Raise `HTTPException` with appropriate status codes and detail messages.
- Use custom exception handlers for domain-specific errors.
- Return consistent error response shapes across the API.
- Never expose internal error details or stack traces to clients.

## Validation & Security
- Validate all input through Pydantic models — never trust raw request data.
- Use `OAuth2PasswordBearer` or JWT-based auth with proper token validation.
- Apply rate limiting and CORS middleware in production.
- Use `Security()` dependencies for permission checks.
- Sanitize any user input that will be reflected in responses.

## Database Integration
- Use async database drivers (`asyncpg`, `aiosqlite`) with async SQLAlchemy.
- Manage sessions via dependency injection with proper cleanup.
- Use Alembic for database migrations.
- Never execute raw SQL with string interpolation — use parameterized queries.

## Async
- Use `async def` for endpoints that perform I/O (database, HTTP calls, file access).
- Use regular `def` for CPU-bound endpoints — FastAPI runs them in a threadpool.
- Use `httpx.AsyncClient` for async HTTP requests to external services.
- Avoid blocking calls inside async endpoints.

## Testing
- Use `TestClient` (sync) or `httpx.AsyncClient` with `ASGITransport` (async) for API testing.
- Override dependencies in tests using `app.dependency_overrides`.
- Test validation errors, auth flows, and edge cases — not just happy paths.
- Use factories or fixtures for test data setup.

## Documentation
- Write clear docstrings on path operations — they appear in the OpenAPI docs.
- Use `response_model` to document and filter response shapes.
- Add `summary` and `description` to endpoints for richer Swagger UI.
- Use `tags` consistently for logical grouping in the API docs.

## Performance
- Use background tasks (`BackgroundTasks`) for non-blocking post-response work.
- Cache expensive computations or queries with `cachetools` or Redis.
- Use streaming responses (`StreamingResponse`) for large payloads.
- Profile with middleware or tools like `py-spy` before optimizing.
