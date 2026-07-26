"""
Extract location information.

Responsibilities
----------------
- City
- Province
- Country

Extraction only.
No normalization.
"""

from __future__ import annotations

from typing import Any

from bs4 import BeautifulSoup

from .utils import (
    clean_text,
    definition_value,
    find_jobposting,
)


def parse_location(
    soup: BeautifulSoup,
) -> dict[str, Any]:

    city = (
        definition_value(
            soup,
            "Plaats",
            "Locatie",
            "Standplaats",
        )
        or _city_from_jsonld(soup)
    )

    return {
        "city": city,
        "province": None,
        "country": "Nederland" if city else None,
    }


# ---------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------


def _city_from_jsonld(
    soup: BeautifulSoup,
) -> str | None:

    job = find_jobposting(soup)

    if not job:
        return None

    location = job.get("jobLocation")

    if isinstance(location, list):

        if location:
            location = location[0]

    if not isinstance(location, dict):
        return None

    address = location.get("address")

    if not isinstance(address, dict):
        return None

    return clean_text(
        address.get("addressLocality")
    )