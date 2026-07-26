"""
Extract employment metadata.

Responsibilities
----------------
- Employment type
- Contract type
- Working hours
- Education level
- Hybrid / remote

Extraction only.
No normalization or inference.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup

from .utils import (
    clean_text,
    definition_value,
    parse_hour_range,
)


def parse_employment(soup: BeautifulSoup) -> dict[str, Any]:
    """
    Returns

    {
        "employment_type": str | None,
        "contract_type": str | None,
        "working_hours": str | None,
        "working_hours_min": int | None,
        "working_hours_max": int | None,
        "education_level": str | None,
        "hybrid": bool,
    }
    """

    text = clean_text(soup.get_text("\n", strip=True)) or ""

    hours = (
        definition_value(
            soup,
            "Arbeidsduur",
            "Werkweek",
            "Uren",
        )
        or _working_hours_text(text)
    )

    minimum, maximum = parse_hour_range(hours)

    return {
        "employment_type": _employment_type(soup, text),
        "contract_type": _contract_type(soup, text),
        "working_hours": hours,
        "working_hours_min": minimum,
        "working_hours_max": maximum,
        "education_level": _education(soup, text),
        "hybrid": _hybrid(text),
    }


# ---------------------------------------------------------------------
# Employment type
# ---------------------------------------------------------------------


def _employment_type(
    soup: BeautifulSoup,
    text: str,
) -> str | None:

    value = definition_value(
        soup,
        "Dienstverband",
        "Soort dienstverband",
        "Arbeidsovereenkomst",
    )

    if value:
        lower = value.lower()

        if "fulltime" in lower:
            return "Fulltime"

        if "parttime" in lower:
            return "Parttime"

        return value

    patterns = (
        "Fulltime",
        "Parttime",
        "Stage",
        "Traineeship",
    )

    for pattern in patterns:

        if re.search(rf"\b{pattern}\b", text, re.I):
            return pattern

    return None


# ---------------------------------------------------------------------
# Contract type
# ---------------------------------------------------------------------


def _contract_type(
    soup: BeautifulSoup,
    text: str,
) -> str | None:

    value = definition_value(
        soup,
        "Contractduur",
        "Dienstverband",
    )

    if value:

        lower = value.lower()

        if "vast" in lower:
            return "Permanent"

        if "tijdelijk" in lower:
            return "Temporary"

        if "jaar" in lower:
            return value

        return value

    patterns = (
        "Vast dienstverband",
        "Tijdelijk",
        "Jaarcontract",
        "Detachering",
        "Oproep",
    )

    lower = text.lower()

    for pattern in patterns:

        if pattern.lower() in lower:
            return pattern

    return None


# ---------------------------------------------------------------------
# Working hours
# ---------------------------------------------------------------------


def _working_hours_text(
    text: str,
) -> str | None:

    match = re.search(
        r"\d+\s*-\s*\d+\s*uur",
        text,
        re.I,
    )

    if match:
        return match.group(0)

    match = re.search(
        r"\d+\s*uur",
        text,
        re.I,
    )

    if match:
        return match.group(0)

    return None


# ---------------------------------------------------------------------
# Education
# ---------------------------------------------------------------------


def _education(
    soup: BeautifulSoup,
    text: str,
) -> str | None:

    value = definition_value(
        soup,
        "Opleidingsniveau",
        "Opleiding",
    )

    if value:

        for level in (
            "WO",
            "HBO",
            "MBO",
            "VMBO",
        ):

            if level.lower() in value.lower():
                return level

    for level in (
        "WO",
        "HBO",
        "MBO",
        "VMBO",
    ):

        if re.search(
            rf"\b{level}\b",
            text,
            re.I,
        ):
            return level

    return None


# ---------------------------------------------------------------------
# Hybrid
# ---------------------------------------------------------------------


def _hybrid(text: str) -> bool:

    keywords = (
        "hybride",
        "hybride werken",
        "thuiswerken",
        "thuiswerk",
        "remote",
        "vanuit huis",
        "werken vanuit huis",
    )

    lower = text.lower()

    return any(
        keyword in lower
        for keyword in keywords
    )