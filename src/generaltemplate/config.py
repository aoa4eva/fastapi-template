"""
Configuration management using Pydantic Settings.

This module provides type-safe configuration loaded from environment variables
and .env files. All settings are validated at startup.

Usage:
    from generaltemplate.config import settings

    database_url = settings.database_url
    debug = settings.debug
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    # Application settings
    app_name: str = Field(default="generaltemplate", description="Application name")
    environment: Literal["development", "staging", "production"] = Field(
        default="development", description="Runtime environment"
    )
    debug: bool = Field(default=False, description="Enable debug mode")

    # Server settings
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")

    # API settings
    api_prefix: str = Field(default="/api", description="API route prefix")
    api_version: str = Field(default="v1", description="API version")

    # Security settings
    secret_key: str = Field(
        default="change-this-in-production-use-openssl-rand-hex-32",
        description="Secret key for signing tokens (change in production!)",
    )
    allowed_hosts: list[str] = Field(
        default=["*"], description="Allowed hosts for CORS"
    )

    # Database settings (uncomment when using database)
    # database_url: str = Field(
    #     default="sqlite:///./generaltemplate.db",
    #     description="Database connection URL"
    # )
    # database_echo: bool = Field(
    #     default=False,
    #     description="Echo SQL queries (for debugging)"
    # )

    # Redis settings (uncomment when using Redis)
    # redis_url: str = Field(
    #     default="redis://localhost:6379/0",
    #     description="Redis connection URL"
    # )

    # External API settings (example)
    # external_api_key: str = Field(default="", description="External API key")
    # external_api_url: str = Field(
    #     default="https://api.example.com",
    #     description="External API base URL"
    # )

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Ensure environment is a valid value."""
        if v not in ["development", "staging", "production"]:
            raise ValueError(
                f"Invalid environment: {v}. Must be development, staging, or production."
            )
        return v

    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.environment == "production"

    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.environment == "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # Ignore extra fields in .env
    )


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Using lru_cache ensures we only create one settings instance,
    which is important for performance and consistency.

    Returns:
        Settings: The application settings instance
    """
    return Settings()


# Global settings instance
settings = get_settings()
