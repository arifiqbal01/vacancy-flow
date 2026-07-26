from dataclasses import dataclass

@dataclass(slots=True)
class Organization:
    """Normalized organization information."""

    name: str
    ministry: str | None = None
    department: str | None = None
    parent: str | None = None
