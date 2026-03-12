# Feature: FastAPI Project Scaffolding

**Created**: 2026-03-12  
**Status**: Implemented

## Summary

Scaffold a FastAPI-based HTTP API inside the existing `agentic-test-repo` Python project. The project already uses `uv` with `uv_build` backend and the `src/agentic_test_repo/` package layout. This plan adds FastAPI and Uvicorn as dependencies, creates a router-based project structure, and exposes a `GET /health` endpoint.

## Goals

- Add `fastapi` and `uvicorn[standard]` as project dependencies via `uv add`.
- Create a well-organized FastAPI application with router-based module separation.
- Provide a working `GET /health` endpoint.
- Wire the existing `main()` entry point to start the Uvicorn server.
- Follow FastAPI best practices for project layout.

## Non-Goals / Out of Scope

- Database integration or ORM setup.
- Authentication / authorization.
- Docker / containerization.
- CI/CD pipeline changes.
- Frontend or static file serving.
- Custom middleware or CORS configuration (can be added later).

## Architecture & Design Decisions

1. **Router-based layout**: Each logical domain gets its own router module under `src/agentic_test_repo/routers/`. This keeps the main application factory thin and makes it easy to add new route groups later.

2. **Application factory pattern**: A `create_app()` function in `src/agentic_test_repo/app.py` builds and returns the `FastAPI` instance. This separates app construction from server startup and makes testing easier.

3. **Entry point wiring**: The existing `[project.scripts]` entry point (`agentic_test_repo:main`) will be updated to import and run Uvicorn programmatically, so `uv run agentic-test-repo` starts the server.

4. **Keep `__init__.py` minimal**: The package init will re-export `main` but won't contain application logic.

## Relevant Existing Code

| File | Relevance |
|---|---|
| `pyproject.toml` | Needs `fastapi` and `uvicorn[standard]` added to `dependencies`. Entry point already defined. |
| `src/agentic_test_repo/__init__.py` | Contains `main()` — must be updated to start the server. |

## Implementation Steps

### Step 1 — Add dependencies

- **What**: Add `fastapi` and `uvicorn[standard]` to the project.
- **How**: Run `uv add fastapi "uvicorn[standard]"` from the workspace root.
- **Why**: These are the core runtime dependencies for serving the API.

### Step 2 — Create the application factory

- **What**: Create `src/agentic_test_repo/app.py` with a `create_app()` function that:
  - Instantiates `FastAPI` with a title, version, and description.
  - Includes all routers (see Step 3).
  - Returns the configured app instance.
- **Where**: `src/agentic_test_repo/app.py` (new file).
- **Why**: Separates app construction from startup; enables easy testing and reuse.

### Step 3 — Create the routers package and health router

- **What**: Create `src/agentic_test_repo/routers/` package with:
  - `__init__.py` — empty or re-exports.
  - `health.py` — defines an `APIRouter` with a `GET /health` endpoint that returns `{"status": "ok"}`.
- **Where**: `src/agentic_test_repo/routers/` (new directory and files).
- **Why**: Router-based separation keeps the codebase modular. The health endpoint is the first concrete route and serves as a readiness/liveness check.

### Step 4 — Update the entry point

- **What**: Modify `src/agentic_test_repo/__init__.py` so that `main()` imports `create_app` from `app.py` and starts Uvicorn programmatically (e.g., `uvicorn.run(create_app(), host="0.0.0.0", port=8000)`).
- **Where**: `src/agentic_test_repo/__init__.py`.
- **Why**: Lets `uv run agentic-test-repo` launch the server directly.

### Step 5 — Verify the setup

- **What**: Run the server with `uv run agentic-test-repo` and confirm:
  - The server starts without errors.
  - `GET /health` returns `{"status": "ok"}` with HTTP 200.
  - The auto-generated OpenAPI docs are accessible at `/docs`.
- **Why**: Validates the entire scaffolding end to end.

## Final Project Structure

```
src/agentic_test_repo/
├── __init__.py          # main() entry point — starts Uvicorn
├── app.py               # create_app() factory
└── routers/
    ├── __init__.py
    └── health.py         # GET /health
```

## Dependencies

| Package | Purpose |
|---|---|
| `fastapi` | Web framework |
| `uvicorn[standard]` | ASGI server (with performance extras) |

## Risks & Open Questions

- **Port conflicts**: The default port `8000` may already be in use on a developer's machine. This can be addressed later by making the port configurable via environment variables.
- **Reload mode**: During development, `uvicorn.run(..., reload=True)` is convenient but should not be used in production. Consider adding a `--reload` flag or a separate dev entry point in the future.
- **CORS**: If a frontend will consume this API, CORS middleware will need to be added — intentionally out of scope for this initial scaffold.

## Testing Strategy

- **Manual smoke test**: Start the server with `uv run agentic-test-repo`, then `curl http://localhost:8000/health` and verify the JSON response.
- **Automated tests (future)**: Add `pytest` and `httpx` as dev dependencies, use FastAPI's `TestClient` to write integration tests for each router. This is not part of the current scaffolding scope but the architecture supports it cleanly.
