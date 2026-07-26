from __future__ import annotations

from abc import ABC, abstractmethod


class StateStore(ABC):
    """Persistence for processed vacancies."""

    @abstractmethod
    def contains(self, vacancy_id: str) -> bool:
        """Return True if the vacancy has already been processed."""

    @abstractmethod
    def add(self, vacancy_id: str) -> None:
        """Mark a vacancy as processed."""

    @abstractmethod
    def save(self) -> None:
        """Persist the current state."""