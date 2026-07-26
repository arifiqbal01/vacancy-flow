"""
Extract vacancy contact information.

Responsibilities
----------------
- Contact name
- Contact role
- Contact phone
- Contact email

Extraction only.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup

from .utils import clean_text, extract_email, extract_phone


def parse_contact(soup: BeautifulSoup) -> dict[str, Any]:

    text = clean_text(soup.get_text("\n", strip=True)) or ""

    name, role = _contact_person(text)

    return {
        "contact_name": name,
        "contact_role": role,
        "contact_phone": extract_phone(text),
        "contact_email": extract_email(text),
    }


def _contact_person(text: str) -> tuple[str | None, str | None]:
    """
    Examples

        Myanneke Vermeer, Plaatsvervangend hoofd CIO office

        Aalderik Reilink (Operationeel Manager)

        Jan Jansen
    """

    patterns = [

        r"([A-Z][A-Za-zÀ-ÿ' -]+),\s*([^\n]+)",

        r"([A-Z][A-Za-zÀ-ÿ' -]+)\s*\(([^)]+)\)",

    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            return (
                clean_text(match.group(1)),
                clean_text(match.group(2)),
            )

    return None, None