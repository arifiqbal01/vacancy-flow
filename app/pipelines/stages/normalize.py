from __future__ import annotations

import logging

from app.models.raw import RawVacancy
from app.models.vacancy import Vacancy
from app.transform.normalizer import normalize

logger = logging.getLogger(__name__)


class NormalizeStage:
    """Normalize a single raw vacancy."""

    def __init__(self, source: str):
        self.source = source

    def run(self, raw: RawVacancy) -> Vacancy:
        """Normalize one vacancy."""

        try:
            return normalize(raw)

        except Exception:
            logger.exception(
                "[%s] Failed to normalize %s",
                self.source,
                raw.url,
            )
            raise