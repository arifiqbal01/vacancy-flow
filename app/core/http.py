"""
Shared HTTP client for VacancyFlow.
"""

from __future__ import annotations

import httpx

from app.core.logging import get_logger
from app.core.rate_limiter import RateLimiter
from app.core.retry import retry_request

logger = get_logger(__name__)


class HttpClient:
    """
    Shared HTTP client.

    Features
    --------
    - Connection pooling
    - Automatic retries
    - Rate limiting
    - Shared headers
    - Logging
    """

    DEFAULT_HEADERS = {
        "User-Agent": (
            "VacancyFlow/1.0 "
            "(https://github.com/your-org/vacancyflow)"
        ),
        "Accept": (
            "text/html,"
            "application/xhtml+xml,"
            "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        requests_per_period: int = 2,
        period: float = 4.0,
        headers: dict[str, str] | None = None,
        http2: bool = False,
    ) -> None:
        self._limiter = RateLimiter(
            requests=requests_per_period,
            period=period,
        )

        self._client = httpx.Client(
            timeout=timeout,
            headers=headers or self.DEFAULT_HEADERS,
            follow_redirects=True,
            http2=http2,
        )

    @retry_request()
    def get(self, url: str, **kwargs) -> httpx.Response:
        self._limiter.wait()

        logger.debug("GET %s", url)

        response = self._client.get(url, **kwargs)
        response.raise_for_status()
        return response

    @retry_request()
    def post(self, url: str, **kwargs) -> httpx.Response:
        self._limiter.wait()

        logger.debug("POST %s", url)

        response = self._client.post(url, **kwargs)
        response.raise_for_status()
        return response

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
