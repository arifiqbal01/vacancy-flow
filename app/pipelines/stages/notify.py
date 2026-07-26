from __future__ import annotations

from app.core import get_logger
from app.notifications import SlackFormatter, SlackNotifier
from app.pipelines.stages.match import MatchedVacancy

logger = get_logger(__name__)


class NotifyStage:
    """Send a notification for a matched vacancy."""

    def __init__(
        self,
        source: str,
        notifier: SlackNotifier | None = None,
        formatter: SlackFormatter | None = None,
    ):
        self.source = source
        self.notifier = notifier or SlackNotifier()
        self.formatter = formatter or SlackFormatter()

    def run(
        self,
        matched: MatchedVacancy,
    ) -> bool:
        """Send a notification for one matched vacancy."""

        if not self.notifier.enabled():
            logger.info("[%s] Slack disabled", self.source)
            return False

        message = self.formatter.new_vacancy(matched)

        sent = self.notifier.send(message)

        if sent:
            logger.info(
                "[%s] Sent notification for '%s'",
                self.source,
                matched.vacancy.title,
            )

        return sent