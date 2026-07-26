"""
Extract vacancy title.

Responsibilities
----------------
- Vacancy title

Extraction only.
No normalization.
"""

from __future__ import annotations

from typing import Any

from bs4 import BeautifulSoup

from .utils import clean_text, find_jobposting


def parse_title(soup: BeautifulSoup) -> dict[str, Any]:
    """
    Returns

    {
        "title": str | None,
    }
    """

    title = _from_html(soup)

    if title:
        return {"title": title}

    return {
        "title": _from_jsonld(soup),
    }


# ---------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------


def _from_html(soup: BeautifulSoup) -> str | None:

    selectors = (
        "h1",
        ".vacancy-header h1",
        ".hero h1",
        "main h1",
    )

    for selector in selectors:

        node = soup.select_one(selector)

        if node:

            title = clean_text(
                node.get_text(" ", strip=True)
            )

            if title:
                return title

    return None


# ---------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------


def _from_jsonld(
    soup: BeautifulSoup,
) -> str | None:

    job = find_jobposting(soup)

    if not job:
        return None

    return clean_text(job.get("title"))