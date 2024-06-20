"""Routes for system state."""

from fastapi import APIRouter
from pydantic import BaseModel

system_state_router = APIRouter(tags=["System State"])


class HealthCheckDTO(BaseModel):
    """Data transfer object for the health check endpoint."""

    status: str


@system_state_router.get(
    "/health_check",
    response_model=HealthCheckDTO,
    summary="Check if the API is running.",
)
async def health_check() -> HealthCheckDTO:
    """Check if the API is running."""
    return HealthCheckDTO(status="OK")
