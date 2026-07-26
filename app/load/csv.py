"""
CSV loader for VacancyFlow.

Writes normalized `Vacancy` records to a flat CSV file.
"""

from __future__ import annotations

import csv
from pathlib import Path

from app.load.serializers import CSV_FIELDNAMES, flatten_vacancy
from app.models.vacancy import Vacancy


def export_to_csv(
    vacancies: list[Vacancy],
    path: str | Path,
    mode: str = "w",
) -> Path:
    """Write vacancies to a CSV file, one row per vacancy.

    `mode="w"` (default) overwrites the file and writes the header.
    `mode="a"` appends rows without re-writing the header — use this
    for incremental runs against an existing export. The header is
    still written if the target file doesn't exist yet, even in
    append mode.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    write_header = mode == "w" or not path.exists()

    with path.open(mode, newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDNAMES, extrasaction="ignore")
        if write_header:
            writer.writeheader()
        for vacancy in vacancies:
            writer.writerow(flatten_vacancy(vacancy))

    return path