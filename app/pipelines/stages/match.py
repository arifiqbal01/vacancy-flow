from __future__ import annotations

from app.core import get_logger
from app.intelligence import JobMatcher
from app.intelligence.results import ProfileMatch
from app.models.vacancy import Vacancy
from dataclasses import dataclass

logger = get_logger(__name__)


@dataclass(slots=True)
class MatchedVacancy:
    vacancy: Vacancy
    matches: list[ProfileMatch]


class MatchStage:
    """Match a single vacancy against all profiles."""

    def __init__(
        self,
        source: str,
        matcher: JobMatcher | None = None,
    ):
        self.source = source
        self.matcher = matcher or JobMatcher()

    def run(
        self,
        vacancy: Vacancy,
    ) -> MatchedVacancy | None:

        profile_matches = self.matcher.match(vacancy)

        if not profile_matches:
            return None

        profiles = ", ".join(
            match.profile.name
            for match in profile_matches
        )

        keywords = sorted({
            keyword
            for match in profile_matches
            for keyword in match.result.matched_keywords
        })

        logger.info(
            "[%s] Matched '%s' for profile(s): %s (%s)",
            self.source,
            vacancy.title,
            profiles,
            ", ".join(keywords) if keywords else "no keywords",
        )

        return MatchedVacancy(
            vacancy=vacancy,
            matches=profile_matches,
        )