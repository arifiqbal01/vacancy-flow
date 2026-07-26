"""
Base extractor interface for VacancyFlow.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from app.core.logging import get_logger
from app.models.raw import RawVacancy


logger = get_logger(__name__)


class BaseExtractor(ABC):
    """
    Abstract base class for all VacancyFlow extractors.

    Every extractor is responsible for:

    1. Discovering vacancy URLs.
    2. Extracting each vacancy.
    3. Cleaning up any resources.

    URL discovery may use:

    - XML sitemap
    - HTML pagination
    - REST API
    - GraphQL
    - RSS
    - Search endpoint
    """

    source_name: str

    def __enter__(self):
        """Allow usage with a context manager."""
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    @abstractmethod
    def fetch_listing_urls(self) -> list[str]:
        """
        Discover vacancy detail URLs.

        Returns
        -------
        list[str]
            Unique vacancy URLs.
        """
        raise NotImplementedError

    @abstractmethod
    def extract_vacancy(self, url: str) -> RawVacancy:
        """
        Extract a single vacancy.

        Parameters
        ----------
        url
            Vacancy detail page.

        Returns
        -------
        RawVacancy
        """
        raise NotImplementedError

    def extract(self) -> Iterable[RawVacancy]:
        """
        Yield extracted vacancies.

        Individual vacancy failures are logged and skipped so the
        extractor continues processing the remaining URLs.
        """
        urls = self.fetch_listing_urls()

        logger.info(
            "[%s] Discovered %d vacancies.",
            self.source_name,
            len(urls),
        )

        for url in urls:
            try:
                vacancy = self.extract_vacancy(url)
                logger.debug("[%s] Extracted %s", self.source_name, url)
                yield vacancy

            except Exception:
                logger.exception(
                    "[%s] Failed to extract %s",
                    self.source_name,
                    url,
                )

    def close(self) -> None:
        """
        Release resources.

        Subclasses may override if they manage HTTP clients,
        browser instances, or database connections.
        """
        return None