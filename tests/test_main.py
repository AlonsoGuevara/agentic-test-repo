import os
from unittest.mock import patch

from agentic_test_repo import main


def test_main_defaults(monkeypatch) -> None:
    """main() should default to 127.0.0.1:8000 when env vars are unset."""
    monkeypatch.delenv("HOST", raising=False)
    monkeypatch.delenv("PORT", raising=False)

    with patch("uvicorn.run") as mock_run:
        main()
        mock_run.assert_called_once()
        _, kwargs = mock_run.call_args
        assert kwargs["host"] == "127.0.0.1"
        assert kwargs["port"] == 8000


def test_main_env_override(monkeypatch) -> None:
    """main() should read HOST and PORT from environment variables."""
    monkeypatch.setenv("HOST", "0.0.0.0")
    monkeypatch.setenv("PORT", "9090")

    with patch("uvicorn.run") as mock_run:
        main()
        mock_run.assert_called_once()
        _, kwargs = mock_run.call_args
        assert kwargs["host"] == "0.0.0.0"
        assert kwargs["port"] == 9090
