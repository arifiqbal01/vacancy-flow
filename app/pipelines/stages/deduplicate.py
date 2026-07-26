from __future__ import annotations

import logging

from app.models.vacancy import Vacancy
from app.transform.deduplicator import Deduplicator

logger = logging.getLogger(__name__)


class DeduplicateStage:
    """Filter duplicate vacancies."""

    def __init__(
        self,
        source: str,
        deduplicator: Deduplicator | None = None,
    ):
        self.source = source
        self.deduplicator = deduplicator or Deduplicator()

    def run(
        self,
        vacancy: Vacancy,
    ) -> Vacancy | None:
        """
        Return the vacancy if it is unique, otherwise None.
        """

        if self.deduplicator.is_duplicate(vacancy):
            logger.debug(
                "[%s] Duplicate vacancy skipped: %s",
                self.source,
                vacancy.source.source_url,
            )
            return None

        self.deduplicator.add(vacancy)

        return vacancy