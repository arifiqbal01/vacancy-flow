from __future__ import annotations

from app.pipelines.stages.match import MatchedVacancy


def new_vacancy(matched: MatchedVacancy) -> str:
    vacancy = matched.vacancy

    organization = vacancy.organization.name

    location = (
        vacancy.location.city
        or vacancy.location.country
        or "Not specified"
    )

    if vacancy.salary.minimum or vacancy.salary.maximum:
        minimum = (
            f"€{vacancy.salary.minimum:,.0f}"
            if vacancy.salary.minimum
            else "?"
        )
        maximum = (
            f"€{vacancy.salary.maximum:,.0f}"
            if vacancy.salary.maximum
            else "?"
        )

        salary = f"{minimum} – {maximum} per {vacancy.salary.period}"

        if vacancy.salary.scale:
            salary += f" ({vacancy.salary.scale})"
    else:
        salary = "Not specified"

    profiles = ", ".join(
        match.profile.name
        for match in matched.matches
    )

    keywords = sorted({
        keyword
        for match in matched.matches
        for keyword in match.result.matched_keywords
    })

    closing = vacancy.closing_date or "Not specified"

    return f"""🆕 *New Vacancy*

*Title:* {vacancy.title}

*Matched Profiles:* {profiles}

*Matched Keywords:* {", ".join(keywords) if keywords else "None"}

*Organization:* {organization}

*Location:* {location}

*Salary:* {salary}

*Closing:* {closing}

<{vacancy.source.source_url}|View Vacancy>
"""