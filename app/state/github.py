from __future__ import annotations

from .base import StateStore


class GitHubStateStore(StateStore):
    """
    Future implementation.

    Intended for persisting state through:
    - GitHub API
    - Gists
    - Dedicated state branch
    """

    def contains(self, vacancy_id: str) -> bool:
        raise NotImplementedError

    def add(self, vacancy_id: str) -> None:
        raise NotImplementedError

    def save(self) -> None:
        raise NotImplementedError