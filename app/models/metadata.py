from dataclasses import dataclass, field
from datetime import datetime

@dataclass(slots=True)
class Metadata:
    """Pipeline metadata."""
    language: str = "nl"
    scraped_at: datetime = field(default_factory=datetime.utcnow)
    last_updated: datetime | None = None
    normalized: bool = False
    deduplicated: bool = False
    checksum: str | None = None
    pipeline_version: str = "1.0"
    notes: str | None = None
