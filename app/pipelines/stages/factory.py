from __future__ import annotations

from dataclasses import dataclass

from app.extract.base import BaseExtractor
from app.intelligence import JobMatcher
from app.notifications import SlackFormatter, SlackNotifier
from app.pipelines.config import PipelineConfig
from app.pipelines.stages.deduplicate import DeduplicateStage
from app.pipelines.stages.extract import ExtractStage
from app.pipelines.stages.load import LoadStage
from app.pipelines.stages.match import MatchStage
from app.pipelines.stages.normalize import NormalizeStage
from app.pipelines.stages.notify import NotifyStage
from app.transform.deduplicator import Deduplicator
from app.pipelines.stages.state import StateStage
from app.state import FileStateStore


@dataclass(slots=True)
class PipelineStages:
    extract: ExtractStage
    normalize: NormalizeStage
    deduplicate: DeduplicateStage
    state: StateStage
    load: LoadStage
    match: MatchStage
    notify: NotifyStage

    @classmethod
    def create(
        cls,
        extractor: BaseExtractor,
        config: PipelineConfig,
    ) -> "PipelineStages":
        source = extractor.source_name

        return cls(
            extract=ExtractStage(extractor),
            normalize=NormalizeStage(source),
            deduplicate=DeduplicateStage(
                source=source,
                deduplicator=Deduplicator(),
            ),
            state=StateStage(
                source=source,
                store=FileStateStore(),
            ),
            load=LoadStage(
                source=source,
                config=config,
            ),
            match=MatchStage(
                source=source,
                matcher=JobMatcher(),
            ),
            notify=NotifyStage(
                source=source,
                notifier=SlackNotifier(),
                formatter=SlackFormatter(),
            ),
        )