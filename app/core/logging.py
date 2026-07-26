"""
Shared logging configuration for VacancyFlow.

Provides centralized logging configuration for the entire application.

All modules should import get_logger() instead of configuring logging
individually.

Example:
    from app.core.logging import get_logger

    logger = get_logger(__name__)
    logger.info("Starting extractor...")
"""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "vacancyflow.log"

CONSOLE_LEVEL = "INFO"
FILE_LEVEL = "DEBUG"
ROOT_LEVEL = "INFO"

LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": (
                "%(asctime)s | %(levelname)-8s | "
                "%(name)s | %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "detailed": {
            "format": (
                "%(asctime)s | %(levelname)-8s | "
                "%(name)s | %(filename)s:%(lineno)d | "
                "%(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": CONSOLE_LEVEL,
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": FILE_LEVEL,
            "formatter": "detailed",
            "filename": str(LOG_FILE),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },
    "root": {
        "level": ROOT_LEVEL,
        "handlers": [
            "console",
            "file",
        ],
    },
}


_configured = False


def configure_logging() -> None:
    """
    Configure application logging.

    Safe to call multiple times.
    """
    global _configured

    if _configured:
        return

    logging.config.dictConfig(LOGGING_CONFIG)

    #
    # Silence verbose third-party libraries.
    #

    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    #
    # Keep parser libraries quiet unless debugging.
    #

    logging.getLogger("selectolax").setLevel(logging.WARNING)
    logging.getLogger("bs4").setLevel(logging.WARNING)

    _configured = True


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name:
            Logger name, typically ``__name__``.

    Returns:
        Configured logger.
    """
    configure_logging()
    return logging.getLogger(name)