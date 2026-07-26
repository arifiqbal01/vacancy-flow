"""
Normalization stage for VacancyFlow.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

from app.models.contact import Contact
from app.models.employment import Employment
from app.models.location import Location
from app.models.metadata import Metadata
from app.models.organization import Organization
from app.models.raw import RawVacancy
from app.models.salary import Salary
from app.models.source import SourceInfo
from app.models.vacancy import Vacancy
from app.transform.cleaner import clean_field


_DUTCH_MONTHS = {
    "jan": 1, "januari": 1,
    "feb": 2, "februari": 2,
    "mrt": 3, "maart": 3,
    "apr": 4, "april": 4,
    "mei": 5,
    "jun": 6, "juni": 6,
    "jul": 7, "juli": 7,
    "aug": 8, "augustus": 8,
    "sep": 9, "sept": 9, "september": 9,
    "okt": 10, "oktober": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}

_DUTCH_DATE_RE = re.compile(
    r"(?P<day>\d{1,2})\s+(?P<month>[a-zA-Z]+)\s+(?P<year>\d{4})"
)

_NUMBER_RE = re.compile(r"\d[\d.,]*")
_SCALE_RE = re.compile(r"schaal\s+(\d+)", re.IGNORECASE)
_HOURS_RANGE_RE = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(?:-|tot)\s*(\d+(?:[.,]\d+)?)"
)
_HOURS_SINGLE_RE = re.compile(r"(\d+(?:[.,]\d+)?)")

_REMOTE_KEYWORDS = ("remote", "thuiswerken", "vanuit huis")
_HYBRID_KEYWORDS = ("hybride",)


def parse_date(value: str | date | None) -> date | None:
    if value is None:
        return None

    if isinstance(value, date):
        return value

    value = value.strip()

    if not value:
        return None

    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass

    match = _DUTCH_DATE_RE.search(value.lower())

    if match:
        month = _DUTCH_MONTHS.get(match.group("month"))

        if month:
            return date(
                int(match.group("year")),
                month,
                int(match.group("day")),
            )

    return None


def _parse_decimal(text: str) -> Decimal | None:
    text = text.strip().replace(".", "").replace(",", ".")

    try:
        return Decimal(text)
    except InvalidOperation:
        return None


def _to_decimal(value) -> Decimal | None:
    if value in (None, ""):
        return None

    return _parse_decimal(str(value))


def parse_salary(raw: RawVacancy) -> Salary:
    minimum = _to_decimal(raw.metadata.get("salary_min"))
    maximum = _to_decimal(raw.metadata.get("salary_max"))
    scale = raw.metadata.get("salary_scale")
    period = "month"

    if raw.salary:
        if scale is None:
            match = _SCALE_RE.search(raw.salary)

            if match:
                scale = match.group(1)

        text = _SCALE_RE.sub("", raw.salary)

        numbers = [
            n
            for n in (
                _parse_decimal(x)
                for x in _NUMBER_RE.findall(text)
            )
            if n is not None
        ]

        if minimum is None and numbers:
            minimum = numbers[0]

        if maximum is None and len(numbers) > 1:
            maximum = numbers[-1]

        lowered = raw.salary.lower()

        if "jaar" in lowered:
            period = "year"
        elif "uur" in lowered:
            period = "hour"

    return Salary(
        minimum=minimum,
        maximum=maximum,
        scale=scale,
        period=period,
    )


def parse_location(city: str | None) -> Location:
    if not city:
        return Location()

    lowered = city.lower()

    return Location(
        city=city,
        country="Netherlands",
        remote=any(k in lowered for k in _REMOTE_KEYWORDS),
        hybrid=any(k in lowered for k in _HYBRID_KEYWORDS),
    )


def parse_working_hours(value: str | None):
    if not value:
        return None, None

    match = _HOURS_RANGE_RE.search(value)

    if match:
        return (
            float(match.group(1)),
            float(match.group(2)),
        )

    match = _HOURS_SINGLE_RE.search(value)

    if match:
        hours = float(match.group(1))
        return hours, hours

    return None, None


def build_organization(raw: RawVacancy) -> Organization:
    return Organization(
        name=raw.organization or "Unknown",
        ministry=raw.ministry,
        department=raw.department,
    )


def build_employment(raw: RawVacancy) -> Employment:
    working_hours = raw.metadata.get("working_hours")

    minimum, maximum = parse_working_hours(working_hours)

    return Employment(
        employment_type=raw.employment,
        contract_type=raw.metadata.get("contract_type"),
        contract_duration=raw.metadata.get("contract_duration"),
        working_hours=working_hours,
        working_hours_min=minimum,
        working_hours_max=maximum,
        education_level=raw.metadata.get("education_level"),
        experience_level=raw.metadata.get("experience_level"),
    )


def build_contact(raw: RawVacancy) -> Contact | None:
    if (
        raw.contact_name is None
        and raw.contact_email is None
        and raw.contact_phone is None
    ):
        return None

    return Contact(
        name=raw.contact_name,
        email=raw.contact_email,
        phone=raw.contact_phone,
    )


def build_source(raw: RawVacancy) -> SourceInfo:
    return SourceInfo(
        source=raw.source,
        source_url=raw.url,
    )


def normalize(raw: RawVacancy) -> Vacancy:
    return Vacancy(
        title=clean_field(raw.title) or "",

        organization=build_organization(raw),

        location=parse_location(raw.city),

        salary=parse_salary(raw),

        employment=build_employment(raw),

        source=build_source(raw),

        summary=clean_field(raw.summary),

        responsibilities=clean_field(
            raw.metadata.get("responsibilities")
        ),

        requirements=clean_field(
            raw.metadata.get("requirements")
        ),

        competencies=clean_field(
            raw.metadata.get("competencies")
        ),

        benefits=clean_field(
            raw.metadata.get("benefits")
        ),

        application_procedure=clean_field(
            raw.metadata.get("application_procedure")
        ),

        full_description=clean_field(raw.description),

        vacancy_number=raw.vacancy_number,

        published_date=parse_date(raw.published_date),

        closing_date=parse_date(raw.closing_date),

        contact=build_contact(raw),

        metadata=Metadata(normalized=True),
    )