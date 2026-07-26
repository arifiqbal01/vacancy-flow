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
    ↓
CommitState

Each stage is intentionally independent and swappable.
"""

from __future__ import annotations

import logging

from app.extract.base import BaseExtractor
from app.extract.werkenvoornederland import WerkenVoorNederlandExtractor
from app.pipelines.config import PipelineConfig
from app.pipelines.result import PipelineResult
from app.pipelines.stages.factory import PipelineStages
from app.state import FileStateStore

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
        result = PipelineResult(
            source=self.extractor.source_name,
        )

        for raw in self.stages.extract.run():
            result.extracted += 1

            # Normalize
            try:
                vacancy = self.stages.normalize.run(raw)
                result.normalized += 1
            except Exception:
                result.failed += 1
                continue

            # Deduplicate
            vacancy = self.stages.deduplicate.run(vacancy)

            if vacancy is None:
                result.duplicates += 1
                continue

            result.unique += 1
            result.vacancies.append(vacancy)

            # Load
            self.stages.load.run(vacancy)

            # Match
            matched = self.stages.match.run(vacancy)

            if matched is not None:
                result.matched += 1

                # Notify
                if self.stages.notify.run(matched):
                    result.notified += 1

            # Commit processed vacancy
            self.stages.commit_state.run(vacancy)

        # Persist state once
        self.stages.commit_state.finish()

        return result


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