from __future__ import annotations

import re

from dataclasses import dataclass
from typing import Iterable

from app.core.logging import get_logger
from app.models.vacancy import Vacancy

logger = get_logger(__name__)


@dataclass(slots=True, frozen=True)
class Keyword:
    text: str
    weight: int = 1
    synonyms: tuple[str, ...] = ()


@dataclass(slots=True)
class MatchResult:
    matched: bool
    score: int
    matched_keywords: list[str]
    excluded_keywords: list[str]


class KeywordMatcher:
    """
    Weighted keyword matcher with synonym support and excluded keywords.
    """

    SEARCH_FIELDS = (
        "title",
        "summary",
        "description",
        "responsibilities",
        "requirements",
        "competencies",
    )

    def __init__(
        self,
        keywords: Iterable[str | Keyword],
        min_score: int = 1,
        excluded_keywords: Iterable[str | Keyword] = (),
    ):
        self.min_score = min_score

        self.keywords = [
            self._normalize_keyword(k)
            for k in keywords
        ]

        self.excluded_keywords = [
            self._normalize_keyword(k)
            for k in excluded_keywords
        ]

    def match(self, vacancy: Vacancy) -> MatchResult:
        text = self._build_text(vacancy)

        # Check excluded keywords first
        excluded = [
            keyword.text
            for keyword in self.excluded_keywords
            if self._matches(keyword, text)
        ]

        if excluded:
            logger.debug(
                "Vacancy excluded by keywords: %s",
                excluded,
            )

            return MatchResult(
                matched=False,
                score=0,
                matched_keywords=[],
                excluded_keywords=sorted(excluded),
            )

        score = 0
        matched_keywords: list[str] = []

        for keyword in self.keywords:
            if self._matches(keyword, text):
                score += keyword.weight
                matched_keywords.append(keyword.text)

        logger.debug(
            "KeywordMatcher score=%d matched=%d excluded=%d",
            score,
            len(matched_keywords),
            len(excluded),
        )

        return MatchResult(
            matched=score >= self.min_score,
            score=score,
            matched_keywords=sorted(matched_keywords),
            excluded_keywords=[],
        )

    @staticmethod
    def _normalize_keyword(keyword: str | Keyword) -> Keyword:
        if isinstance(keyword, Keyword):
            return Keyword(
                text=keyword.text.strip().lower(),
                weight=keyword.weight,
                synonyms=tuple(
                    synonym.strip().lower()
                    for synonym in keyword.synonyms
                ),
            )

        return Keyword(
            text=keyword.strip().lower(),
        )

    def _matches(self, keyword: Keyword, text: str) -> bool:
        candidates = (
            keyword.text,
            *keyword.synonyms,
        )

        return any(
            self._contains(candidate, text)
            for candidate in candidates
        )

    @staticmethod
    def _contains(phrase: str, text: str) -> bool:
        pattern = rf"\b{re.escape(phrase)}\b"
        return re.search(pattern, text) is not None

    def _build_text(self, vacancy: Vacancy) -> str:
        parts: list[str] = []

        for field in self.SEARCH_FIELDS:
            value = getattr(vacancy, field, None)

            if value:
                parts.append(str(value))

        return "\n".join(parts).lower()