"""
Vacancies pipeline: orchestrates the full ETL workflow.

Extract
    ↓
Normalize
    ↓
Deduplicate
    ↓
Load
    ↓
Match
    ↓
Notify

Each stage is intentionally independent and swappable.
"""

from __future__ import annotations

import logging

from app.extract.base import BaseExtractor
from app.extract.werkenvoornederland import WerkenVoorNederlandExtractor
from app.pipelines.config import PipelineConfig
from app.pipelines.result import PipelineResult
from app.pipelines.stages.factory import PipelineStages

logger = logging.getLogger(__name__)


class VacaturesPipeline:
    """Coordinates the ETL pipeline."""

    def __init__(
        self,
        extractor: BaseExtractor,
        config: PipelineConfig | None = None,
    ):
        self.extractor = extractor
        self.config = config or PipelineConfig()

        self.stages = PipelineStages.create(
            extractor=extractor,
            config=self.config,
        )

    def run(self) -> PipelineResult:
        # Extract
        raw = self.stages.extract.run()

        # Normalize
        normalized = self.stages.normalize.run(raw)

        # Deduplicate
        dedupe = self.stages.deduplicate.run(
            normalized.vacancies
        )

        # State
        new_vacancies = self.stages.state.run(
            dedupe.unique
        )

        # Load
        self.stages.load.run(
            new_vacancies
        )

        # Match
        matched = self.stages.match.run(
            new_vacancies
        )

        # Notify
        notified = self.stages.notify.run(
            matched.vacancies
        )

        return PipelineResult(
            source=self.extractor.source_name,
            extracted=normalized.extracted,
            normalized=len(normalized.vacancies),
            failed=normalized.failed,
            unique=len(new_vacancies),
            duplicates=len(dedupe.duplicates),
            matched=len(matched.vacancies),
            notified=notified,
            vacancies=new_vacancies,
        )


def run_werkenvoornederland(
    config: PipelineConfig | None = None,
) -> PipelineResult:
    """Run the Werken voor Nederland pipeline."""

    config = config or PipelineConfig()

    extractor = WerkenVoorNederlandExtractor(
        limit=config.max_vacancies,
    )

    try:
        pipeline = VacaturesPipeline(
            extractor=extractor,
            config=config,
        )

        return pipeline.run()

    finally:
        extractor.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    result = run_werkenvoornederland()

    print(result)