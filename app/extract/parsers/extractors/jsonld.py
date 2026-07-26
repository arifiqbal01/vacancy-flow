"""
Extract structured JobPosting data from JSON-LD.

The Werken voor Nederland vacancy pages expose a JobPosting schema that
contains useful structured information such as title, hiring organization,
location and publication dates.

This module only extracts raw values. It does not normalize or enrich them.
"""

from __future__ import annotations

import json
from typing import Any

from bs4 import BeautifulSoup


def parse_jsonld(soup: BeautifulSoup) -> dict[str, Any]:
    """
    Parse the JobPosting JSON-LD block.

    Returns only fields that are explicitly present.
    Missing or malformed JSON-LD simply returns {}.
    """

    script = _find_jobposting_script(soup)

    if script is None:
        return {}

    try:
        payload = json.loads(script.string or script.get_text())
    except (json.JSONDecodeError, TypeError):
        return {}

    job = _find_jobposting(payload)

    if not job:
        return {}

    return {
        "title": job.get("title"),
        "organization": _organization(job),
        "city": _city(job),
        "published_date": job.get("datePosted"),
        "closing_date": job.get("validThrough"),
        "employment": _employment_type(job),
        "salary": _salary(job),
    }


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------


def _find_jobposting_script(
    soup: BeautifulSoup,
):
    """
    Locate the JSON-LD script that contains a JobPosting.
    """

    for script in soup.find_all("script", type="application/ld+json"):
        text = script.string or script.get_text()

        if text and "JobPosting" in text:
            return script

    return None


def _find_jobposting(data: Any) -> dict[str, Any] | None:
    """
    JSON-LD can be

        {}
        []
        {"@graph": [...]}

    Search recursively for the JobPosting object.
    """

    if isinstance(data, dict):

        if data.get("@type") == "JobPosting":
            return data

        graph = data.get("@graph")

        if isinstance(graph, list):
            for item in graph:
                result = _find_jobposting(item)

                if result:
                    return result

    elif isinstance(data, list):

        for item in data:
            result = _find_jobposting(item)

            if result:
                return result

    return None


def _organization(job: dict[str, Any]) -> str | None:

    org = job.get("hiringOrganization")

    if isinstance(org, dict):
        return org.get("name")

    return None


def _city(job: dict[str, Any]) -> str | None:

    location = job.get("jobLocation")

    if isinstance(location, list):
        location = location[0]

    if not isinstance(location, dict):
        return None

    place = location.get("address")

    if isinstance(place, dict):
        return place.get("addressLocality")

    return None


def _employment_type(job: dict[str, Any]) -> str | None:

    employment = job.get("employmentType")

    if isinstance(employment, list):
        return ", ".join(employment)

    return employment


def _salary(job: dict[str, Any]) -> str | None:
    """
    Return the raw salary representation.

    Salary normalization belongs in salary.py.
    """

    salary = job.get("baseSalary")

    if salary is None:
        return None

    return json.dumps(salary, ensure_ascii=False)