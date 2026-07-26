"""
Shared helper functions for Werken voor Nederland extractors.
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from typing import Any

from bs4 import BeautifulSoup, NavigableString, Tag


# ---------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------


def clean_text(value: str | None) -> str | None:
    """
    Collapse whitespace and strip text.
    """

    if not value:
        return None

    value = re.sub(r"\s+", " ", value)

    return value.strip() or None


def text(node: Tag | None) -> str | None:

    if node is None:
        return None

    return clean_text(node.get_text(" ", strip=True))


# ---------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------


def find_jobposting(soup: BeautifulSoup) -> dict[str, Any] | None:
    """
    Return the JobPosting object from JSON-LD.

    Supports

        {}
        []
        @graph
    """

    for script in soup.find_all(
        "script",
        type="application/ld+json",
    ):

        try:
            payload = json.loads(
                script.string or script.get_text()
            )
        except Exception:
            continue

        job = _walk_jobposting(payload)

        if job:
            return job

    return None


def _walk_jobposting(data):

    if isinstance(data, dict):

        if data.get("@type") == "JobPosting":
            return data

        graph = data.get("@graph")

        if isinstance(graph, list):

            for item in graph:

                result = _walk_jobposting(item)

                if result:
                    return result

    elif isinstance(data, list):

        for item in data:

            result = _walk_jobposting(item)

            if result:
                return result

    return None


# ---------------------------------------------------------------------
# Definition list helpers
# ---------------------------------------------------------------------


def definition_value(
    soup: BeautifulSoup,
    *labels: str,
) -> str | None:
    """
    Lookup a value from a definition list.

    Example

        <dt>Plaats</dt>
        <dd>Den Haag</dd>

    or

        <dt>Salaris</dt>
        <dd>€4.500 - €6.000</dd>
    """

    wanted = {label.lower() for label in labels}

    for dt in soup.find_all("dt"):

        label = clean_text(dt.get_text())

        if not label:
            continue

        if label.lower() not in wanted:
            continue

        dd = dt.find_next_sibling("dd")

        if dd:
            return clean_text(dd.get_text(" ", strip=True))

    return None


# ---------------------------------------------------------------------
# Generic label lookup
# ---------------------------------------------------------------------


def labelled_value(
    soup: BeautifulSoup,
    *labels: str,
) -> str |None:
    """
    Finds

        Salaris
        €4.500

    even when no <dl> exists.
    """

    pattern = "|".join(
        re.escape(label)
        for label in labels
    )

    node = soup.find(
        string=re.compile(
            rf"^(?:{pattern})$",
            re.I,
        )
    )

    if node is None:
        return None

    parent = node.parent

    if parent is None:
        return None

    sibling = parent.find_next()

    if sibling is None:
        return None

    return clean_text(
        sibling.get_text(" ", strip=True)
    )


# ---------------------------------------------------------------------
# Money
# ---------------------------------------------------------------------


def parse_euro(value: str | None) -> float | None:

    if not value:
        return None

    match = re.search(
        r"([\d\.,]+)",
        value,
    )

    if not match:
        return None

    number = (
        match.group(1)
        .replace(".", "")
        .replace(",", ".")
    )

    try:
        return float(number)
    except ValueError:
        return None


# ---------------------------------------------------------------------
# Hour ranges
# ---------------------------------------------------------------------


def parse_hour_range(
    value: str | None,
) -> tuple[int | None, int | None]:

    if not value:
        return None, None

    match = re.search(
        r"(\d+)\s*-\s*(\d+)",
        value,
    )

    if not match:
        return None, None

    return (
        int(match.group(1)),
        int(match.group(2)),
    )


# ---------------------------------------------------------------------
# Dates
# ---------------------------------------------------------------------


_MONTHS = {
    "januari": 1,
    "februari": 2,
    "maart": 3,
    "april": 4,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "augustus": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "december": 12,
}


def parse_dutch_date(
    value: str | None,
) -> date | None:

    if not value:
        return None

    value = value.strip()

    # ISO
    try:
        return datetime.fromisoformat(
            value.replace("Z", "")
        ).date()
    except Exception:
        pass

    # 5 juni 2025
    match = re.search(
        r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})",
        value,
    )

    if not match:
        return None

    month = _MONTHS.get(
        match.group(2).lower()
    )

    if month is None:
        return None

    return date(
        int(match.group(3)),
        month,
        int(match.group(1)),
    )


# ---------------------------------------------------------------------
# Email
# ---------------------------------------------------------------------


_EMAIL = re.compile(
    r"[\w.\-+%]+@[\w.\-]+\.[A-Za-z]{2,}"
)


def extract_email(text: str | None):

    if not text:
        return None

    match = _EMAIL.search(text)

    if match:
        return match.group(0)

    return None


# ---------------------------------------------------------------------
# Phone
# ---------------------------------------------------------------------


_PHONE = re.compile(
    r"(?:\+31|0)[\d\s\-()]{8,}"
)


def extract_phone(text: str | None):

    if not text:
        return None

    match = _PHONE.search(text)

    if match:
        return clean_text(match.group(0))

    return None