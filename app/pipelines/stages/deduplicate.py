from __future__ import annotations

import logging

from app.transform.deduplicator import Deduplicator

logger = logging.getLogger(__name__)


class DeduplicateStage:

    def __init__(self, source: str, deduplicator=None):
        self.source = source
        self.deduplicator = deduplicator or Deduplicator()

    def run(self, vacancies):
        result = self.deduplicator.process(vacancies)

        logger.info(
            "[%s] %d unique, %d duplicates",
            self.source,
            len(result.unique),
            len(result.duplicates),
        )

        return result