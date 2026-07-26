from __future__ import annotations

from dataclasses import dataclass

from app.core import get_logger
from app.intelligence import JobMatcher
from app.intelligence.results import ProfileMatch
from app.models.vacancy import Vacancy

logger = get_logger(__name__)


@dataclass(slots=True)
class MatchedVacancy:
    vacancy: Vacancy
    matches: list[ProfileMatch]


@dataclass(slots=True)
class MatchResult:
    vacancies: list[MatchedVacancy]


class MatchStage:

    def __init__(self, source: str, matcher: JobMatcher | None = None):
        self.source = source
        self.matcher = matcher or JobMatcher()

    def run(self, vacancies: list[Vacancy]) -> MatchResult:
        matched: list[MatchedVacancy] = []

        for vacancy in vacancies:
            profile_matches = self.matcher.match(vacancy)

            if not profile_matches:
                continue

            matched.append(
                MatchedVacancy(
                    vacancy=vacancy,
                    matches=profile_matches,
                )
            )

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

        logger.info(
            "[%s] %d/%d vacancies matched",
            self.source,
            len(matched),
            len(vacancies),
        )

        return MatchResult(vacancies=matched)