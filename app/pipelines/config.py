from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class PipelineConfig:
    """
    Configuration for a pipeline run.
    """

    output_dir: Path = field(default_factory=lambda: Path("exports"))

    csv_filename: str = "vacatures.csv"
    json_filename: str | None = "vacatures.json"

    # None = process every vacancy.
    max_vacancies: int | None = 10

    # Append instead of overwrite.
    incremental: bool = False

    def __post_init__(self) -> None:
        self.output_dir = Path(self.output_dir)

        if self.max_vacancies is not None:
            self.max_vacancies = int(self.max_vacancies)

            if self.max_vacancies <= 0:
                raise ValueError(
                    "max_vacancies must be greater than zero."
                )

    @property
    def csv_path(self) -> Path:
        return self.output_dir / self.csv_filename

    @property
    def json_path(self) -> Path | None:
        if self.json_filename is None:
            return None

        return self.output_dir / self.json_filename

    @property
    def write_mode(self) -> str:
        return "a" if self.incremental else "w"