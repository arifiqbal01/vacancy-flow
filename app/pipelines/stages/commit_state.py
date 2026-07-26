from __future__ import annotations

from app.models.vacancy import Vacancy
from app.state import StateStore


class CommitStateStage:
    """Commit successfully processed vacancies to state."""

    def __init__(self, store: StateStore):
        self.store = store

    def run(self, vacancy: Vacancy) -> None:
        self.store.add(vacancy.source.source_url)

    def finish(self) -> None:
        self.store.save()