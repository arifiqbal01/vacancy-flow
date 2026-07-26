"""
Deduplication stage for VacancyFlow.

Duplicate vacancies can arise from:
* re-crawling the same listing across pipeline runs (incremental
  updates should update, not duplicate, an existing record), and
* the same underlying vacancy being posted more than once, or across
  multiple sources once VacancyFlow supports several job boards.

Two fingerprints are used:
* `identity_key` — a strict key (source + source_url, or source +
  vacancy_number when available) used to recognize "the same posting
  seen again", e.g. on a repeat crawl.
* `content_checksum` — a hash of normalized content (title,
  organization, location, salary) used to catch near-duplicates that
  don't share a URL/vacancy_number, e.g. the same role re-posted under
  a new URL, or (in future) the same role cross-posted to another
  source.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

from app.models.vacancy import Vacancy


def identity_key(vacancy: Vacancy) -> str:
    """Strict key for "the same posting", stable across re-crawls."""
    if vacancy.vacancy_number:
        return f"{vacancy.source.source}:{vacancy.vacancy_number}"
    return f"{vacancy.source.source}:{vacancy.source.source_url}"


def content_checksum(vacancy: Vacancy) -> str:
    """Hash of normalized core content, for cross-URL near-duplicates."""
    parts = [
        (vacancy.title or "").strip().lower(),
        (vacancy.organization.name or "").strip().lower(),
        (vacancy.location.city or "").strip().lower(),
        (vacancy.employment.employment_type or "").strip().lower(),
        str(vacancy.salary.minimum or ""),
        str(vacancy.salary.maximum or ""),
    ]
    digest_input = "|".join(parts).encode("utf-8")
    return hashlib.sha256(digest_input).hexdigest()


@dataclass
class DedupeResult:
    unique: list[Vacancy]
    duplicates: list[Vacancy]


class Deduplicator:
    """Stateful deduplicator for a batch (or an incremental run).

    Usage:
        dedupe = Deduplicator()
        result = dedupe.process(vacancies)
        # result.unique -> vacancies to load
        # result.duplicates -> vacancies skipped/merged

    For incremental crawls, seed `seen_identity_keys` from previously
    loaded records (e.g. existing source_urls / vacancy_numbers in the
    database) before calling `process`, so re-crawled postings are
    recognized as duplicates on the very first pass.
    """

    def __init__(
        self,
        seen_identity_keys: set[str] | None = None,
        seen_checksums: set[str] | None = None,
    ):
        self.seen_identity_keys: set[str] = seen_identity_keys or set()
        self.seen_checksums: set[str] = seen_checksums or set()

    def is_duplicate(self, vacancy: Vacancy) -> bool:
        return (
            identity_key(vacancy) in self.seen_identity_keys
            or content_checksum(vacancy) in self.seen_checksums
        )

    def add(self, vacancy: Vacancy) -> None:
        self.seen_identity_keys.add(identity_key(vacancy))
        self.seen_checksums.add(content_checksum(vacancy))

    def process(self, vacancies: list[Vacancy]) -> DedupeResult:
        """Split a batch into unique vacancies and duplicates.

        Marks each unique vacancy's `metadata.deduplicated = True` and
        stamps `metadata.checksum` with its content checksum before
        returning it.
        """
        unique: list[Vacancy] = []
        duplicates: list[Vacancy] = []

        for vacancy in vacancies:
            if self.is_duplicate(vacancy):
                duplicates.append(vacancy)
                continue

            vacancy.metadata.deduplicated = True
            vacancy.metadata.checksum = content_checksum(vacancy)

            self.add(vacancy)
            unique.append(vacancy)

        return DedupeResult(unique=unique, duplicates=duplicates)