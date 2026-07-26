from __future__ import annotations

import logging

from app.models.vacancy import Vacancy
from app.load.csv import export_to_csv
from app.load.json import export_to_json

logger = logging.getLogger(__name__)


class LoadStage:
    """Persist a single vacancy."""

    def __init__(self, source: str, config):
        self.source = source
        self.config = config

    def run(self, vacancy: Vacancy) -> None:
        export_to_csv(
            [vacancy],
            self.config.csv_path,
            mode=self.config.write_mode,
        )

        logger.debug(
            "[%s] Wrote vacancy to %s",
            self.source,
            self.config.csv_path,
        )

        if self.config.json_path:
            export_to_json(
                [vacancy],
                self.config.json_path,
            )

            logger.debug(
                "[%s] Wrote vacancy to %s",
                self.source,
                self.config.json_path,
            )