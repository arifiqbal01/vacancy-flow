from dataclasses import dataclass, field
from datetime import date

from .contact import Contact
from .employment import Employment
from .location import Location
from .metadata import Metadata
from .organization import Organization
from .salary import Salary
from .source import SourceInfo

@dataclass(slots=True)
class Vacancy:
    """Canonical vacancy model."""

    title: str

    organization: Organization
    location: Location
    salary: Salary
    employment: Employment
    source: SourceInfo

    summary: str | None = None
    responsibilities: str | None = None
    requirements: str | None = None
    competencies: str | None = None
    benefits: str | None = None

    application_procedure: str | None = None
    full_description: str | None = None

    vacancy_number: str | None = None

    published_date: date | None = None
    closing_date: date | None = None

    contact: Contact | None = None

    metadata: Metadata = field(default_factory=Metadata)
