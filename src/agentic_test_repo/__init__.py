import uvicorn


def main() -> None:
    """Start the Uvicorn server with the FastAPI application."""
    from agentic_test_repo.app import create_app

    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
