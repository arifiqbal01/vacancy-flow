"""
Retry utilities for VacancyFlow.

Provides a shared retry decorator for transient HTTP failures using
exponential backoff.

Example:
    from app.core.retry import retry_request

    @retry_request()
    def fetch(url: str):
        return client.get(url)
"""

from __future__ import annotations

import logging

import httpx
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from app.core.logging import get_logger

logger = get_logger(__name__)


def retry_request(
    attempts: int = 3,
    multiplier: float = 1.0,
    minimum: float = 1.0,
    maximum: float = 10.0,
):
    """
    Retry decorator for HTTP requests.

    Retries transient network failures with exponential backoff.

    Args:
        attempts:
            Maximum number of attempts.

        multiplier:
            Exponential backoff multiplier.

        minimum:
            Minimum wait between retries.

        maximum:
            Maximum wait between retries.

    Returns:
        A configured tenacity retry decorator.
    """

    retry_exceptions = (
        httpx.ConnectError,
        httpx.ConnectTimeout,
        httpx.ReadTimeout,
        httpx.WriteTimeout,
        httpx.PoolTimeout,
        httpx.NetworkError,
        httpx.RemoteProtocolError,
        httpx.HTTPStatusError,
    )

    return retry(
        reraise=True,
        stop=stop_after_attempt(attempts),
        wait=wait_exponential(
            multiplier=multiplier,
            min=minimum,
            max=maximum,
        ),
        retry=retry_if_exception_type(retry_exceptions),
        before_sleep=before_sleep_log(
            logger,
            logging.WARNING,
        ),
    )