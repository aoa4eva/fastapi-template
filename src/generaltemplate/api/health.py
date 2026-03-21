"""
Health check endpoints.

Provides endpoints for monitoring application health and readiness.
"""

from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from generaltemplate.config import settings

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    environment: str
    timestamp: datetime
    app_name: str


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.

    Returns basic application health information.
    Use this for container health checks and monitoring.

    Returns:
        HealthResponse: Application health status
    """
    return HealthResponse(
        status="healthy",
        environment=settings.environment,
        timestamp=datetime.now(),
        app_name=settings.app_name,
    )


@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint.

    Returns whether the application is ready to serve traffic.
    Can be extended to check database connections, cache availability, etc.

    Returns:
        dict: Readiness status

    Example:
        {
            "ready": true,
            "checks": {
                "database": "connected",
                "cache": "connected"
            }
        }
    """
    # TODO: Add actual readiness checks for your dependencies
    # For example:
    # - Database connection: await db.check_connection()
    # - Redis connection: await redis.ping()
    # - External API availability: await external_api.health_check()

    checks = {
        # "database": "connected",  # Uncomment when using database
        # "cache": "connected",      # Uncomment when using Redis
    }

    return {
        "ready": True,
        "checks": checks if checks else {"status": "no dependencies configured"},
    }
