from __future__ import annotations

import logging
from dataclasses import dataclass

from app.models.vacancy import Vacancy
from app.transform.normalizer import normalize

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class NormalizeResult:
    vacancies: list[Vacancy]
    extracted: int
    failed: int


class NormalizeStage:

    def __init__(self, source: str):
        self.source = source

    def run(self, raw_vacancies) -> NormalizeResult:
        normalized = []
        extracted = 0
        failed = 0

        for raw in raw_vacancies:
            extracted += 1

            try:
                normalized.append(normalize(raw))

            except Exception:
                failed += 1
                logger.exception(
                    "[%s] Failed to normalize %s",
                    self.source,
                    raw.url,
                )

        logger.info(
            "[%s] Extracted %d, normalized %d, failed %d",
            self.source,
            extracted,
            len(normalized),
            failed,
        )

        return NormalizeResult(
            vacancies=normalized,
            extracted=extracted,
            failed=failed,
        )