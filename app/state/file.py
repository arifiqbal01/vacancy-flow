from __future__ import annotations

import json
from pathlib import Path

from .base import StateStore


class FileStateStore(StateStore):
    """Stores processed vacancy IDs in a JSON file."""

    def __init__(self, path: str | Path = "state/seen.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self._seen: set[str] = set()

        if self.path.exists():
            try:
                data = json.loads(self.path.read_text())

                self._seen = set(
                    data.get("vacancies", [])
                )

            except Exception:
                self._seen = set()

    def contains(self, vacancy_id: str) -> bool:
        return vacancy_id in self._seen

    def add(self, vacancy_id: str) -> None:
        self._seen.add(vacancy_id)

    def save(self) -> None:
        self.path.write_text(
            json.dumps(
                {
                    "vacancies": sorted(self._seen),
                },
                indent=2,
            )
        )