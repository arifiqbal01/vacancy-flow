"""
Parse structured vacancy sections.

Indexes all H2/H3 headings once
and exposes helper methods.
"""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from .utils import clean_text


class SectionParser:

    def __init__(self, soup: BeautifulSoup):

        self.sections = self._index(soup)

    # -------------------------------------------------------------

    def summary(self):

        return self._get(
            "Functieomschrijving",
            "Introductie",
            "Samenvatting",
        )

    def responsibilities(self):

        return self._get(
            "Dit ga je doen",
            "Werkzaamheden",
            "Taken",
        )

    def requirements(self):

        return self._get(
            "Dit vragen wij",
            "Functie-eisen",
            "Wie ben jij",
        )

    def competencies(self):

        return self._get(
            "Competenties",
        )

    def benefits(self):

        return self._get(
            "Arbeidsvoorwaarden",
            "Wat bieden wij",
        )

    def application(self):

        return self._get(
            "Bijzonderheden",
            "Sollicitatieprocedure",
        )

    # -------------------------------------------------------------

    def _get(self, *names):

        for name in names:

            if name in self.sections:
                return self.sections[name]

        return None

    # -------------------------------------------------------------

    def _index(
        self,
        soup: BeautifulSoup,
    ) -> dict[str, str]:

        sections = {}

        headings = soup.find_all(
            ["h2", "h3"]
        )

        for heading in headings:

            title = clean_text(
                heading.get_text(" ", strip=True)
            )

            if not title:
                continue

            content = []

            node = heading.next_sibling

            while node:

                if (
                    isinstance(node, Tag)
                    and node.name in ("h2", "h3")
                ):
                    break

                if isinstance(node, Tag):

                    text = clean_text(
                        node.get_text(
                            " ",
                            strip=True,
                        )
                    )

                    if text:
                        content.append(text)

                node = node.next_sibling

            sections[title] = "\n\n".join(content)

        return sections