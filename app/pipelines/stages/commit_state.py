from __future__ import annotations

from app.state import StateStore


class CommitStateStage:
    def __init__(self, store: StateStore):
        self.store = store

    def run(self, vacancies):
        for vacancy in vacancies:
            self.store.add(vacancy.source.source_url)

        self.store.save()