"""
Production extractor for Werken voor Nederland.

Vacancy discovery uses the official XML sitemap instead of the
JavaScript-rendered listing page.
"""

from __future__ import annotations

from urllib.parse import urlparse
from xml.etree import ElementTree

from app.core import HttpClient
from app.core import get_logger
from app.core import retry_request
from app.extract.base import BaseExtractor
from app.extract.parsers.parser import (
    WerkenVoorNederlandParser,
)
from app.models.raw import RawVacancy


logger = get_logger(__name__)


class WerkenVoorNederlandExtractor(BaseExtractor):
    """Extractor for Werken voor Nederland."""

    source_name = "Werken voor Nederland"

    BASE_URL = "https://www.werkenvoornederland.nl"

    SITEMAP_URL = (
        "https://www.werkenvoornederland.nl/sitemap-vacatures.xml"
    )

    def __init__(self, limit: int | None = None) -> None:
        self.client = HttpClient()

        if limit is not None:
            limit = int(limit)

            if limit <= 0:
                raise ValueError(
                    "limit must be greater than zero."
                )

        self.limit = limit

    @retry_request()
    def fetch_listing_urls(self) -> list[str]:
        """Fetch vacancy URLs from the sitemap."""

        response = self.client.get(self.SITEMAP_URL)

        root = ElementTree.fromstring(response.text)

        namespace = {
            "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
        }

        urls: list[str] = []
        seen: set[str] = set()

        for node in root.findall(
            "sm:url/sm:loc",
            namespace,
        ):
            if not node.text:
                continue

            url = node.text.strip()

            if (
                self._is_valid_url(url)
                and url not in seen
            ):
                seen.add(url)
                urls.append(url)

        if self.limit is not None:
            urls = urls[: self.limit]

        logger.info(
            "[%s] Found %d vacancy URLs%s.",
            self.source_name,
            len(urls),
            (
                f" (limited to {self.limit})"
                if self.limit is not None
                else ""
            ),
        )

        return urls

    @retry_request()
    def extract_vacancy(
            self,
            url: str,
    ) -> RawVacancy:

        response = self.client.get(url)

        parser = WerkenVoorNederlandParser()

        return parser.parse(
            response.text,
            source=self.source_name,
            url=url,
        )

    @classmethod
    def _is_valid_url(
        cls,
        url: str,
    ) -> bool:
        """Validate vacancy URL."""

        parsed = urlparse(url)

        return (
            parsed.scheme in {"http", "https"}
            and parsed.netloc
            == "www.werkenvoornederland.nl"
            and "/vacatures/" in parsed.path
        )

    def close(self) -> None:
        """Close the HTTP client."""

        self.client.close()