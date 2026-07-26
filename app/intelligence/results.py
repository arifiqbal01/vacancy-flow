from __future__ import annotations

from dataclasses import dataclass

from app.intelligence.keywords_matcher import MatchResult
from app.intelligence.profiles import BaseProfile


@dataclass(slots=True)
class ProfileMatch:
    profile: BaseProfile
    result: MatchResult