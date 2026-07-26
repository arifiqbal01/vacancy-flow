from __future__ import annotations

import logging

from app.extract.base import BaseExtractor

logger = logging.getLogger(__name__)


class ExtractStage:
    """Extract raw vacancies from a source."""

    def __init__(self, extractor: BaseExtractor):
        self.extractor = extractor

    def run(self):
        source = self.extractor.source_name

        logger.info("[%s] Starting extraction", source)

        return self.extractor.extract()