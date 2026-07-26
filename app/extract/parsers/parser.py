from bs4 import BeautifulSoup

from app.models import RawVacancy

from app.extract.parsers.extractors import (
    parse_contact,
    parse_dates,
    parse_employment,
    parse_location,
    parse_metadata,
    parse_organization,
    parse_salary,
    parse_title,
)
from .sections import SectionParser


class WerkenVoorNederlandParser:

    def parse(
        self,
        html: str,
        *,
        source: str,
        url: str,
    ) -> RawVacancy:

        soup = BeautifulSoup(html, "lxml")

        title = parse_title(soup)
        organization = parse_organization(soup)
        location = parse_location(soup)
        employment = parse_employment(soup)
        salary = parse_salary(soup)
        dates = parse_dates(soup)
        contact = parse_contact(soup)

        sections = SectionParser(soup)

        description = "\n\n".join(
            filter(
                None,
                [
                    sections.summary(),
                    sections.responsibilities(),
                    sections.requirements(),
                    sections.competencies(),
                    sections.benefits(),
                    sections.application(),
                ],
            )
        )

        #
        # Backwards-compatible formatting
        #

        salary_text = None

        if (
            salary["salary_min"] is not None
            and salary["salary_max"] is not None
        ):
            salary_text = (
                f"€{salary['salary_min']:,.0f} - "
                f"€{salary['salary_max']:,.0f}"
            ).replace(",", ".")

            if salary.get("salary_scale"):
                salary_text += (
                    f" (schaal {salary['salary_scale']})"
                )

        employment_text = employment.get("employment_type")

        if employment.get("working_hours"):

            if employment_text:
                employment_text = (
                    f"{employment_text} "
                    f"({employment['working_hours']})"
                )
            else:
                employment_text = employment["working_hours"]

        #
        # Metadata
        #

        metadata = {
            **parse_metadata(soup),
            "salary": salary,
            "employment": employment,
            "location": location,
            "organization": organization,
            "contact": contact,
        }

        return RawVacancy(
            source=source,
            url=url,

            title=title.get("title"),

            organization=organization.get("organization"),
            ministry=organization.get("ministry"),
            department=organization.get("department"),

            city=location.get("city"),

            salary=salary_text,
            employment=employment_text,

            summary=sections.summary(),
            description=description,

            published_date=dates.get("published_date"),
            closing_date=dates.get("closing_date"),

            vacancy_number=dates.get("vacancy_number"),

            contact_name=contact.get("contact_name"),
            contact_email=contact.get("contact_email"),
            contact_phone=contact.get("contact_phone"),

            metadata=metadata,

            html=html,
        )