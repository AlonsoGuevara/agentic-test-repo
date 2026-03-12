from fastapi import FastAPI

from agentic_test_repo.routers import health


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Agentic Test Repo API",
        version="0.1.0",
        description="FastAPI-based HTTP API for agentic-test-repo.",
    )
    app.include_router(health.router)
    return app
