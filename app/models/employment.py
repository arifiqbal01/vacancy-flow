from dataclasses import dataclass


@dataclass(slots=True)
class Employment:
    """Normalized employment / contract details."""

    employment_type: str | None = None  # e.g. "vast", "tijdelijk"
    contract_type: str | None = None
    contract_duration: str | None = None

    working_hours: str | None = None  # raw text, e.g. "32-36 uur"
    working_hours_min: float | None = None
    working_hours_max: float | None = None

    education_level: str | None = None
    experience_level: str | None = None