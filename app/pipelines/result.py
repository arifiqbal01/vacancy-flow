from __future__ import annotations

from dataclasses import dataclass, field

from app.models.vacancy import Vacancy


@dataclass(slots=True)
class PipelineResult:
    """
    Summary of a pipeline execution.
    """

    source: str

    extracted: int = 0
    normalized: int = 0
    failed: int = 0

    unique: int = 0
    duplicates: int = 0

    matched: int = 0
    notified: int = 0

    vacancies: list[Vacancy] = field(default_factory=list)

    @property
    def success_rate(self) -> float:
        if self.extracted == 0:
            return 0.0

        return round((self.normalized / self.extracted) * 100, 2)

    def __str__(self) -> str:
        return (
            f"{self.source}: "
            f"extracted={self.extracted}, "
            f"normalized={self.normalized}, "
            f"unique={self.unique}, "
            f"duplicates={self.duplicates}, "
            f"matched={self.matched}, "
            f"notified={self.notified}, "
            f"failed={self.failed}"
        )