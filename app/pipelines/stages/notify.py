from __future__ import annotations

from app.core import get_logger
from app.notifications import SlackFormatter, SlackNotifier
from app.pipelines.stages.match import MatchedVacancy

logger = get_logger(__name__)


class NotifyStage:

    def __init__(
        self,
        source: str,
        notifier: SlackNotifier | None = None,
        formatter: SlackFormatter | None = None,
    ):
        self.source = source
        self.notifier = notifier or SlackNotifier()
        self.formatter = formatter or SlackFormatter()

    def run(self, vacancies: list[MatchedVacancy]) -> int:
        if not vacancies:
            logger.info("[%s] Nothing to notify", self.source)
            return 0

        if not self.notifier.enabled():
            logger.info("[%s] Slack disabled", self.source)
            return 0

        sent = 0

        for matched in vacancies:
            message = self.formatter.new_vacancy(matched)

            if self.notifier.send(message):
                sent += 1

        logger.info(
            "[%s] Sent %d notification(s)",
            self.source,
            sent,
        )

        return sent