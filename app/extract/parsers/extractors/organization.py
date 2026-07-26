"""
Extract organisation metadata.

Responsibilities
----------------
- Organisation
- Ministry
- Department

Extraction only.
No normalization or inference.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup

from .utils import clean_text, find_jobposting


def parse_organization(soup: BeautifulSoup) -> dict[str, Any]:
    """
    Returns

    {
        "organization": str | None,
        "ministry": str | None,
        "department": str | None,
    }
    """

    header = _header_text(soup)

    html = {
        "organization": _organization(header),
        "ministry": _ministry(header),
        "department": _department(header),
    }

    jsonld = _from_jsonld(soup)

    return {
        "organization": html["organization"] or jsonld["organization"],
        "ministry": html["ministry"] or jsonld["ministry"],
        "department": html["department"],
    }


# ---------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------


def _header_text(soup: BeautifulSoup) -> str:
    """
    Search only the vacancy header.

    This avoids matching organisation names in the footer,
    contact section or application instructions.
    """

    selectors = (
        ".vacancy-header",
        ".hero",
        ".hero__content",
        "header",
        "main",
    )

    for selector in selectors:

        node = soup.select_one(selector)

        if node:
            return clean_text(node.get_text("\n", strip=True)) or ""

    return clean_text(soup.get_text("\n", strip=True)) or ""


# ---------------------------------------------------------------------
# HTML extraction
# ---------------------------------------------------------------------


def _organization(text: str) -> str | None:
    """
    Generic organisation detection.

    Examples

        Dienst Toeslagen
        Rijkswaterstaat
        Rijksvastgoedbedrijf
        IND
        CJIB
        SSC-ICT
    """

    patterns = [

        r"Ministerie van [A-ZÀ-ÿ][^\n,;]+",

        r"Dienst\s+[A-ZÀ-ÿ][^\n,;]+",

        r"Rijks[A-Za-zÀ-ÿ&\- ]+",

        r"\b[A-Z]{2,}(?:-[A-Z]+)?\b",

    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(0).strip()

    return None


def _ministry(text: str) -> str | None:

    match = re.search(
        r"Ministerie van [A-ZÀ-ÿ][^\n,;]+",
        text,
        flags=re.IGNORECASE,
    )

    if match:
        return match.group(0).strip()

    return None


def _department(text: str) -> str | None:

    keywords = (
        "Afdeling",
        "Team",
        "Cluster",
        "Programma",
        "Directie",
        "CIO",
        "Business Unit",
        "Divisie",
        "Sector",
    )

    for line in text.splitlines():

        line = clean_text(line)

        if not line:
            continue

        if any(
            line.startswith(keyword)
            for keyword in keywords
        ):
            return line

    return None


# ---------------------------------------------------------------------
# JSON-LD fallback
# ---------------------------------------------------------------------


def _from_jsonld(soup: BeautifulSoup) -> dict[str, str | None]:

    job = find_jobposting(soup)

    if not job:
        return {
            "organization": None,
            "ministry": None,
        }

    org = job.get("hiringOrganization")

    if not isinstance(org, dict):
        return {
            "organization": None,
            "ministry": None,
        }

    return {
        "organization": org.get("name"),
        "ministry": None,
    }