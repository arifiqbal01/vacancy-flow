from __future__ import annotations

from app.core import get_logger

from app.intelligence.keywords_matcher import KeywordMatcher
from app.intelligence.profiles import (
    DEFAULT_PROFILES,
    BaseProfile,
)
from app.intelligence.results import ProfileMatch
from app.models.vacancy import Vacancy

logger = get_logger(__name__)


class JobMatcher:
    """
    Main intelligence entry point.

    Every configured profile is evaluated against a vacancy.
    """

    def __init__(self, profiles: list[BaseProfile] | None = None):
        self.profiles = profiles or DEFAULT_PROFILES

        logger.info(
            "JobMatcher initialized with %d profile(s): %s",
            len(self.profiles),
            ", ".join(profile.name for profile in self.profiles),
        )

    def match(self, vacancy: Vacancy) -> list[ProfileMatch]:
        matches: list[ProfileMatch] = []

        for profile in self.profiles:
            matcher = KeywordMatcher(
                keywords=profile.keywords,
                excluded_keywords=profile.excluded_keywords,
                min_score=profile.min_score,
            )

            result = matcher.match(vacancy)

            logger.info(
                (
                    "Profile='%s' | Vacancy='%s' | matched=%s | "
                    "score=%d | matched_keywords=%s | excluded_keywords=%s"
                ),
                profile.name,
                vacancy.title,
                result.matched,
                result.score,
                result.matched_keywords,
                result.excluded_keywords,
            )

            if result.matched:
                matches.append(
                    ProfileMatch(
                        profile=profile,
                        result=result,
                    )
                )

        return matches