from __future__ import annotations

from app.pipelines.stages.match import MatchedVacancy
from app.notifications import templates


class SlackFormatter:
    """
    Converts matched vacancies into Slack messages.
    """

    @staticmethod
    def new_vacancy(matched: MatchedVacancy) -> str:
        return templates.new_vacancy(matched)