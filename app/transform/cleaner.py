"""
HTML cleaning utilities for the transform stage.

Takes raw HTML captured during extraction and produces clean,
whitespace-normalized text suitable for storing in the canonical
Vacancy content fields.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup


_DROP_TAGS = (
    "script",
    "style",
    "noscript",
    "svg",
    "iframe",
    "form",
)

_BLOCK_TAGS = (
    "p",
    "div",
    "br",
    "li",
    "tr",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "section",
    "article",
    "header",
    "footer",
    "ul",
    "ol",
)

_WHITESPACE_RE = re.compile(r"[ \t\f\v]+")
_BLANK_LINES_RE = re.compile(r"\n{3,}")


def clean_html(html: str | None) -> str | None:
    """Convert HTML into normalized plain text."""

    if not html:
        return None

    soup = BeautifulSoup(html, "lxml")

    for tag in soup.find_all(_DROP_TAGS):
        tag.decompose()

    for li in soup.find_all("li"):
        li.insert(0, "- ")

    for tag in soup.find_all(_BLOCK_TAGS):
        tag.append("\n")

    return normalize_whitespace(soup.get_text())


def normalize_whitespace(text: str | None) -> str | None:
    """Normalize whitespace."""

    if text is None:
        return None

    text = text.replace("\xa0", " ")

    lines = [
        _WHITESPACE_RE.sub(" ", line).strip()
        for line in text.splitlines()
    ]

    text = "\n".join(lines)
    text = _BLANK_LINES_RE.sub("\n\n", text)

    return text.strip() or None


def clean_field(value: str | None) -> str | None:
    """Clean a single field."""

    if not value:
        return None

    if "<" in value and ">" in value:
        return clean_html(value)

    return normalize_whitespace(value)


def clean_fields(
    data: dict[str, Any],
    keys: list[str],
) -> dict[str, str | None]:
    """Clean multiple fields from a mapping."""

    return {
        key: clean_field(data.get(key))
        for key in keys
    }