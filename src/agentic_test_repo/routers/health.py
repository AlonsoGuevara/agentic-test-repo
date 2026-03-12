from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: str


@router.get("/health", summary="Health check", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return the service health status."""
    return HealthResponse(status="ok")
