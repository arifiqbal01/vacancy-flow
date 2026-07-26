from dataclasses import dataclass

@dataclass(slots=True)
class Location:
    """Normalized location."""

    city: str | None = None
    province: str | None = None
    state: str | None = None
    country: str | None = None

    address: str | None = None
    postal_code: str | None = None

    latitude: float | None = None
    longitude: float | None = None

    remote: bool = False
    hybrid: bool = False
