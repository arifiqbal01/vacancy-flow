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
from app.state import FileStateStore
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
        state_store: FileStateStore,
        config: PipelineConfig | None = None,
    ):
        self.extractor = extractor
        self.config = config or PipelineConfig()

        self.stages = PipelineStages.create(
            extractor=extractor,
            config=self.config,
            state_store=state_store,
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
        # Load
        self.stages.load.run(
            dedupe.unique
        )

        # Match
        matched = self.stages.match.run(
            dedupe.unique
        )

        # Notify
        notified = self.stages.notify.run(
            matched.vacancies
        )

        # Commit processed vacancies to state
        self.stages.commit_state.run(
            dedupe.unique
        )

        return PipelineResult(
            source=self.extractor.source_name,
            extracted=normalized.extracted,
            normalized=len(normalized.vacancies),
            failed=normalized.failed,
            unique=len(dedupe.unique),
            duplicates=len(dedupe.duplicates),
            matched=len(matched.vacancies),
            notified=notified,
            vacancies=dedupe.unique,
        )


def run_werkenvoornederland(
    config: PipelineConfig | None = None,
) -> PipelineResult:
    """Run the Werken voor Nederland pipeline."""

    config = config or PipelineConfig()

    store = FileStateStore()

    extractor = WerkenVoorNederlandExtractor(
        state_store=store,
        limit=config.max_vacancies,
    )

    try:
        pipeline = VacaturesPipeline(
            extractor=extractor,
            state_store=store,
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