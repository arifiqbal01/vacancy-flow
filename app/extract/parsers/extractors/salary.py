"""
Extract salary information.

Responsibilities
----------------
- Salary minimum
- Salary maximum
- Salary scale
- Salary currency
- Salary period

Extraction only.
No normalization or inference.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup

from .utils import (
    definition_value,
    find_jobposting,
    parse_euro,
)


_RANGE = re.compile(
    r"€?\s*([\d.,]+)\s*-\s*€?\s*([\d.,]+)",
    re.I,
)

_SCALE = re.compile(
    r"schaal\s*([A-Za-z0-9]+)",
    re.I,
)


def parse_salary(soup: BeautifulSoup) -> dict[str, Any]:
    """
    Returns

    {
        "salary_min": float | None,
        "salary_max": float | None,
        "salary_currency": str | None,
        "salary_period": str | None,
        "salary_scale": str | None,
    }
    """

    salary = (
        definition_value(
            soup,
            "Salaris",
            "Salarisniveau",
        )
        or _salary_text(soup)
    )

    if salary:
        return _parse_salary(salary)

    return _salary_from_jsonld(soup)


# ---------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------


def _salary_text(soup: BeautifulSoup) -> str | None:
    """
    Fallback for pages that don't use definition lists.
    """

    text = soup.get_text("\n", strip=True)

    match = re.search(
        r"€\s*[\d.,]+\s*-\s*€?\s*[\d.,]+.*",
        text,
    )

    if match:
        return match.group(0)

    return None


def _parse_salary(text: str) -> dict[str, Any]:

    minimum = None
    maximum = None
    scale = None

    match = _RANGE.search(text)

    if match:

        minimum = parse_euro(match.group(1))
        maximum = parse_euro(match.group(2))

    scale_match = _SCALE.search(text)

    if scale_match:
        scale = scale_match.group(1)

    return {
        "salary_min": minimum,
        "salary_max": maximum,
        "salary_currency": "EUR",
        "salary_period": "month",
        "salary_scale": scale,
    }


# ---------------------------------------------------------------------
# JSON-LD fallback
# ---------------------------------------------------------------------


def _salary_from_jsonld(
    soup: BeautifulSoup,
) -> dict[str, Any]:

    job = find_jobposting(soup)

    if not job:
        return _empty()

    base = job.get("baseSalary")

    if not isinstance(base, dict):
        return _empty()

    value = base.get("value")

    if not isinstance(value, dict):
        return _empty()

    return {
        "salary_min": value.get("minValue"),
        "salary_max": value.get("maxValue"),
        "salary_currency": base.get(
            "currency",
            "EUR",
        ),
        "salary_period": value.get(
            "unitText",
            "MONTH",
        ).lower(),
        "salary_scale": None,
    }


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------


def _empty() -> dict[str, Any]:

    return {
        "salary_min": None,
        "salary_max": None,
        "salary_currency": None,
        "salary_period": None,
        "salary_scale": None,
    }