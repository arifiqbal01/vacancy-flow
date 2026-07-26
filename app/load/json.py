"""
JSON loader for VacancyFlow.

Writes normalized `Vacancy` records to JSON — either a single array
file, or JSON Lines (one object per line) for incremental/append and
streaming-friendly workflows.
"""

from __future__ import annotations

import json
from pathlib import Path

from app.load.serializers import json_default, vacancy_to_dict
from app.models.vacancy import Vacancy


def export_to_json(
    vacancies: list[Vacancy],
    path: str | Path,
    indent: int | None = 2,
) -> Path:
    """Write vacancies to a JSON file as a single array of objects.

    Full-fidelity, nested output — organization/location/salary/
    employment/source/contact/metadata stay as nested objects (unlike
    the flattened CSV export). This overwrites the target file each
    time; there's no meaningful "append" for a single JSON array, so
    use `export_to_jsonl` below for incremental runs.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [vacancy_to_dict(v) for v in vacancies]

    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, default=json_default, indent=indent, ensure_ascii=False)

    return path


def export_to_jsonl(
    vacancies: list[Vacancy],
    path: str | Path,
    mode: str = "w",
) -> Path:
    """Write vacancies as JSON Lines (one JSON object per line).

    Better suited than a single JSON array for incremental/append runs
    (`mode="a"`) and for streaming large datasets without loading the
    whole file into memory to read or write it.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open(mode, encoding="utf-8") as fh:
        for vacancy in vacancies:
            fh.write(json.dumps(vacancy_to_dict(vacancy), default=json_default, ensure_ascii=False))
            fh.write("\n")

    return path