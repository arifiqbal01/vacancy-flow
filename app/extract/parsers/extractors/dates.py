"""
Extract vacancy dates.

Responsibilities
----------------
- Published date
- Closing date
- Vacancy number

Extraction only.
No normalization or inference.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from bs4 import BeautifulSoup

from .utils import (
    definition_value,
    find_jobposting,
    parse_dutch_date,
)


def parse_dates(soup: BeautifulSoup) -> dict[str, Any]:
    """
    Returns

    {
        "published_date": date | None,
        "closing_date": date | None,
        "vacancy_number": str | None,
    }
    """

    published = (
        definition_value(
            soup,
            "Plaatsingsdatum",
            "Publicatiedatum",
            "Geplaatst",
        )
        or _published_from_jsonld(soup)
    )

    closing = (
        definition_value(
            soup,
            "Solliciteer voor",
            "Sluitingsdatum",
            "Reageer voor",
        )
        or _closing_from_jsonld(soup)
    )

    vacancy_number = definition_value(
        soup,
        "Vacaturenummer",
        "Referentienummer",
        "Kenmerk",
    )

    return {
        "published_date": _parse_date(published),
        "closing_date": _parse_date(closing),
        "vacancy_number": vacancy_number,
    }


# ---------------------------------------------------------------------
# JSON-LD fallback
# ---------------------------------------------------------------------


def _published_from_jsonld(
    soup: BeautifulSoup,
) -> str | None:

    job = find_jobposting(soup)

    if not job:
        return None

    return job.get("datePosted")


def _closing_from_jsonld(
    soup: BeautifulSoup,
) -> str | None:

    job = find_jobposting(soup)

    if not job:
        return None

    return job.get("validThrough")


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------


def _parse_date(
    value: str | None,
) -> date | None:

    if not value:
        return None

    return parse_dutch_date(value)