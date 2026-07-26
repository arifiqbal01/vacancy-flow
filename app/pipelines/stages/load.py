from __future__ import annotations

import logging

from app.load.csv import export_to_csv
from app.load.json import export_to_json

logger = logging.getLogger(__name__)


class LoadStage:

    def __init__(self, source: str, config):
        self.source = source
        self.config = config

    def run(self, vacancies):
        if not vacancies:
            logger.info("[%s] Nothing to load", self.source)
            return

        export_to_csv(
            vacancies,
            self.config.csv_path,
            mode=self.config.write_mode,
        )

        logger.info(
            "[%s] Wrote %d rows to %s",
            self.source,
            len(vacancies),
            self.config.csv_path,
        )

        if self.config.json_path:
            export_to_json(
                vacancies,
                self.config.json_path,
            )

            logger.info(
                "[%s] Wrote %d records to %s",
                self.source,
                len(vacancies),
                self.config.json_path,
            )