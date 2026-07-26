"""
VacancyFlow entry point.

Run the complete ETL pipeline.

Usage:
    python main.py
"""

from __future__ import annotations

import sys

from app.core.logging import configure_logging, get_logger
from app.pipelines.vacancies import (
    PipelineConfig,
    run_werkenvoornederland,
)

logger = get_logger(__name__)


def main() -> int:
    """Application entry point."""

    configure_logging()

    logger.info("Starting VacancyFlow...")

    config = PipelineConfig()

    try:
        result = run_werkenvoornederland(config)

    except KeyboardInterrupt:
        logger.warning("Pipeline interrupted by user.")
        return 1

    except Exception:
        logger.exception("Pipeline failed.")
        return 1

    logger.info("Pipeline completed successfully.")

    print("\nVacancyFlow Summary")
    print("-" * 40)
    print(f"Source       : {result.source}")
    print(f"Extracted    : {result.extracted}")
    print(f"Normalized   : {result.normalized}")
    print(f"Unique       : {result.unique}")
    print(f"Duplicates   : {result.duplicates}")
    print(f"Failed       : {result.failed}")
    print("-" * 40)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())