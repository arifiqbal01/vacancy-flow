from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

@dataclass(slots=True)
class RawVacancy:
    source: str
    url: str

    title: str | None = None

    organization: str | None = None
    ministry: str | None = None
    department: str | None = None

    city: str | None = None

    salary: str | None = None
    employment: str | None = None

    summary: str | None = None
    description: str | None = None

    published_date: str | None = None
    closing_date: str | None = None

    vacancy_number: str | None = None

    contact_name: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

    html: str | None = None

    extracted_at: datetime = field(default_factory=datetime.utcnow)
