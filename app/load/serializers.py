"""
Shared serialization helpers for the load stage.

Converts the nested `Vacancy` dataclass tree into the two shapes the
loaders need: a flat dict (CSV, one row per vacancy) and a nested dict
(JSON, full fidelity — organization/location/salary/etc. stay as
nested objects).
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from app.models.vacancy import Vacancy

CONTENT_FIELDS = [
    "summary",
    "responsibilities",
    "requirements",
    "competencies",
    "benefits",
    "application_procedure",
    "full_description",
]

# Column order for CSV output — keys match what `flatten_vacancy` produces.
CSV_FIELDNAMES = [
    "title",
    "organization_name", "ministry", "department",
    "location_city", "location_province", "location_country",
    "remote", "hybrid",
    "salary_min", "salary_max", "salary_currency", "salary_period", "salary_scale",
    "employment_type", "contract_type", "contract_duration",
    "working_hours", "working_hours_min", "working_hours_max",
    "education_level", "experience_level",
    "published_date", "closing_date", "vacancy_number",
    "source", "source_url",
    "contact_name", "contact_email", "contact_phone",
    *CONTENT_FIELDS,
    "scraped_at", "last_updated", "language",
    "normalized", "deduplicated", "checksum",
]


def json_default(value: Any) -> Any:
    """`default=` handler for `json.dump`, for types it can't serialize natively."""
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return float(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def vacancy_to_dict(vacancy: Vacancy) -> dict[str, Any]:
    """Nested dict representation of a vacancy, for JSON output."""
    return asdict(vacancy)


def flatten_vacancy(vacancy: Vacancy) -> dict[str, Any]:
    """Flat dict representation of a vacancy, for CSV output.

    Nested sub-objects are flattened into prefixed columns (e.g.
    `organization.name` -> `organization_name`, `salary.minimum` ->
    `salary_min`) per `CSV_FIELDNAMES`. Dates/Decimals are converted to
    plain str/float so `csv.DictWriter` can write them directly.
    """
    contact = vacancy.contact

    row: dict[str, Any] = {
        "title": vacancy.title,
        "organization_name": vacancy.organization.name,
        "ministry": vacancy.organization.ministry,
        "department": vacancy.organization.department,
        "location_city": vacancy.location.city,
        "location_province": vacancy.location.province,
        "location_country": vacancy.location.country,
        "remote": vacancy.location.remote,
        "hybrid": vacancy.location.hybrid,
        "salary_min": vacancy.salary.minimum,
        "salary_max": vacancy.salary.maximum,
        "salary_currency": vacancy.salary.currency,
        "salary_period": vacancy.salary.period,
        "salary_scale": vacancy.salary.scale,
        "employment_type": vacancy.employment.employment_type,
        "contract_type": vacancy.employment.contract_type,
        "contract_duration": vacancy.employment.contract_duration,
        "working_hours": vacancy.employment.working_hours,
        "working_hours_min": vacancy.employment.working_hours_min,
        "working_hours_max": vacancy.employment.working_hours_max,
        "education_level": vacancy.employment.education_level,
        "experience_level": vacancy.employment.experience_level,
        "published_date": vacancy.published_date,
        "closing_date": vacancy.closing_date,
        "vacancy_number": vacancy.vacancy_number,
        "source": vacancy.source.source,
        "source_url": vacancy.source.source_url,
        "contact_name": contact.name if contact else None,
        "contact_email": contact.email if contact else None,
        "contact_phone": contact.phone if contact else None,
        "scraped_at": vacancy.metadata.scraped_at,
        "last_updated": vacancy.metadata.last_updated,
        "language": vacancy.metadata.language,
        "normalized": vacancy.metadata.normalized,
        "deduplicated": vacancy.metadata.deduplicated,
        "checksum": vacancy.metadata.checksum,
    }

    for field_name in CONTENT_FIELDS:
        row[field_name] = getattr(vacancy, field_name)

    for key, value in row.items():
        if isinstance(value, (date, datetime)):
            row[key] = value.isoformat()
        elif isinstance(value, Decimal):
            row[key] = float(value)

    return row