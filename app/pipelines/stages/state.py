from __future__ import annotations

import logging

from app.state import StateStore

logger = logging.getLogger(__name__)


class StateStage:
    """Filters already processed vacancies and persists new ones."""

    def __init__(self, source: str, store: StateStore):
        self.source = source
        self.store = store

    def run(self, vacancies):
        unseen = []

        for vacancy in vacancies:
            identifier = vacancy.identifier

            if self.store.contains(identifier):
                continue

            unseen.append(vacancy)
            self.store.add(identifier)

        self.store.save()

        logger.info(
            "[%s] %d new vacancies (%d skipped)",
            self.source,
            len(unseen),
            len(vacancies) - len(unseen),
        )

        return unseen