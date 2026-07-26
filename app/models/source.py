from dataclasses import dataclass


@dataclass(slots=True)
class SourceInfo:
    """Where a vacancy came from."""

    source: str
    source_url: str