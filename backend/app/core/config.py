"""Centralized application configuration, loaded from environment variables.

All settings are read via pydantic-settings so that no configuration value is
hardcoded in application code. Local development values live in `.env` (not
committed); `.env.example` documents the expected keys.
"""

from functools import lru_cache
from typing import Literal

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- Application ---
    app_name: str = "NutriPlan API"
    environment: Literal["development", "test", "production"] = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    # --- CORS ---
    # Comma-separated origins allowed to call the API from a browser. The Vite
    # dev server defaults to http://localhost:5173.
    cors_allowed_origins: str = "http://localhost:5173"

    # --- Database ---
    postgres_user: str = "nutriplan"
    postgres_password: str = "nutriplan_dev_only"
    postgres_host: str = "127.0.0.1"
    postgres_port: int = 5433
    postgres_db: str = "nutriplan"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def database_url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg",
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.postgres_host,
                port=self.postgres_port,
                path=self.postgres_db,
            )
        )

    @computed_field  # type: ignore[prop-decorator]
    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    """Cached settings accessor; use as a FastAPI dependency or direct import."""
    return Settings()
