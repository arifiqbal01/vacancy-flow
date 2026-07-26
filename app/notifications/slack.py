from __future__ import annotations

import httpx

from app.core import get_logger
from app.core.configs import settings

logger = get_logger(__name__)


class SlackNotifier:
    """
    Sends messages to Slack using Incoming Webhooks.
    """

    def __init__(self) -> None:
        self.webhook = settings.SLACK_WEBHOOK_URL

    def enabled(self) -> bool:
        return bool(settings.SLACK_ENABLED and self.webhook)

    def send(self, message: str) -> bool:
        """
        Send a message to Slack.

        Returns
        -------
        bool
            True if the message was sent successfully.
        """

        if not self.enabled():
            logger.debug("Slack notifications disabled.")
            return False

        try:
            response = httpx.post(
                self.webhook,
                json={"text": message},
                timeout=settings.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            logger.info("Slack notification sent.")

            return True

        except Exception:
            logger.exception("Failed to send Slack notification.")
            return False