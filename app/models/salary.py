from dataclasses import dataclass
from decimal import Decimal

@dataclass(slots=True)
class Salary:
    """Normalized salary."""

    minimum: Decimal | None = None
    maximum: Decimal | None = None

    currency: str = "EUR"
    period: str = "month"

    scale: str | None = None
