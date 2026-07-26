from dataclasses import dataclass

@dataclass(slots=True)
class Contact:
    """Hiring contact information."""

    name: str | None = None
    role: str | None = None
    department: str | None = None

    email: str | None = None
    phone: str | None = None
