from __future__ import annotations

from dataclasses import dataclass, field

from app.intelligence.keywords_matcher import Keyword


@dataclass(slots=True)
class BaseProfile:
    name: str
    min_score: int = 1

    keywords: list[str | Keyword] = field(default_factory=list)

    excluded_keywords: list[str | Keyword] = field(default_factory=list)