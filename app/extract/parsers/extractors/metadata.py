"""
Parser metadata.

This is metadata ABOUT the scrape,
not about the vacancy itself.
"""

from __future__ import annotations

from datetime import datetime, UTC
from typing import Any

from bs4 import BeautifulSoup

from .utils import find_jobposting


PARSER_NAME = "werkenvoornederland"
PARSER_VERSION = "2.0"


def parse_metadata(
    soup: BeautifulSoup,
) -> dict[str, Any]:

    return {
        "language": "nl",
        "parser": PARSER_NAME,
        "parser_version": PARSER_VERSION,
        "jsonld": find_jobposting(soup) is not None,
        "scraped_at": datetime.now(
            UTC
        ).isoformat(),
    }