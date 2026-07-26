from __future__ import annotations

from bs4 import BeautifulSoup, Tag


class SectionParser:
    """
    Parses the content sections of a Werken voor Nederland vacancy.

    This class is responsible ONLY for extracting section text from HTML.
    It performs no normalization or business logic.
    """

    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    # ---------------------------------------------------------------------
    # Generic helpers
    # ---------------------------------------------------------------------

    def _find_section(self, heading: str) -> Tag | None:
        """
        Find a <section> containing an <h2> matching the given heading.
        """

        heading = heading.lower().strip()

        for section in self.soup.find_all("section"):

            h2 = section.find("h2")

            if not h2:
                continue

            title = h2.get_text(" ", strip=True).lower()

            if heading == title or heading in title:
                return section

        return None

    def _extract_text(self, section: Tag | None) -> str | None:
        """
        Extract clean text from a section.
        """

        if section is None:
            return None

        content = section.select_one(".s-article-content")

        if content:
            return content.get_text("\n", strip=True)

        return section.get_text("\n", strip=True)

    def _text(self, heading: str) -> str | None:
        """
        Convenience wrapper.
        """

        return self._extract_text(self._find_section(heading))

    # ---------------------------------------------------------------------
    # Vacancy sections
    # ---------------------------------------------------------------------

    def summary(self) -> str | None:
        """
        Functieomschrijving
        """
        return self._text("Functieomschrijving")

    def responsibilities(self) -> str | None:
        """
        Dit ga je doen
        """
        return self._text("Dit ga je doen")

    def requirements(self) -> str | None:
        """
        Dit vragen wij
        """
        return self._text("Dit vragen wij")

    def competencies(self) -> str | None:
        """
        Competenties
        """
        return self._text("Competenties")

    def benefits(self) -> str | None:
        """
        Dit bieden we nog meer
        """
        return self._text("Dit bieden we nog meer")

    def application(self) -> str | None:
        """
        Bijzonderheden
        """
        return self._text("Bijzonderheden")

    def organization(self) -> str | None:
        """
        Over de organisatie
        """
        return self._text("Over de organisatie")

    def department(self) -> str | None:
        """
        Over de afdeling
        """
        return self._text("Over de afdeling")

    # ---------------------------------------------------------------------
    # Utility
    # ---------------------------------------------------------------------

    def all_sections(self) -> dict[str, str]:
        """
        Return all detected H2 sections.

        Useful for debugging and future parser improvements.
        """

        sections = {}

        for section in self.soup.find_all("section"):

            h2 = section.find("h2")

            if not h2:
                continue

            title = h2.get_text(" ", strip=True)

            text = self._extract_text(section)

            if text:
                sections[title] = text

        return sections