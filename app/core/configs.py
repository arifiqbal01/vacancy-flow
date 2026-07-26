"""
Centralized application configuration.

This module is responsible for loading environment variables and exposing
application settings through a single configuration object.

All modules should import configuration from here rather than accessing
environment variables directly.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    APP_NAME: str = "VacancyFlow"
    APP_ENV: str = "development"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str | None = None

    # Slack
    SLACK_WEBHOOK_URL: str | None = None
    SLACK_ENABLED: bool = False

    # Crawling
    REQUEST_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    USER_AGENT: str = Field(
        default="VacancyFlow/1.0 (+https://github.com/arifiqbal01/vacancyflow)"
    )

    # Logging
    LOG_LEVEL: str = "INFO"

    # Parser
    DEFAULT_LANGUAGE: str = "nl"
    PARSER_VERSION: str = "2.0"


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.

    The settings are loaded only once during the application's lifetime.
    """
    return Settings()


# Global settings instance
settings = get_settings()