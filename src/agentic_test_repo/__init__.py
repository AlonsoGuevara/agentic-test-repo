import os


def main() -> None:
    """Start the Uvicorn server with the FastAPI application."""
    import uvicorn

    from agentic_test_repo.app import create_app

    host = os.environ.get("HOST", "127.0.0.1")
    try:
        port = int(os.environ.get("PORT", "8000"))
    except ValueError:
        port = 8000
    uvicorn.run(create_app(), host=host, port=port)
