VacancyFlow – Project Handover
Project Overview

VacancyFlow is a modular vacancy aggregation system. The current focus has been building a robust parser for Werken voor Nederland that extracts structured vacancy data into a RawVacancy model.

The parser has now been refactored from a monolithic implementation into a collection of single-responsibility extractors.

The next milestone is Slack notifications. The parser architecture is considered complete enough for an MVP.

Current Architecture
app/
├── extract/
│   └── parsers/
│       ├── parser.py
│       ├── sections.py
│       └── extractors/
│           ├── __init__.py
│           ├── utils.py
│           ├── jsonld.py
│           ├── title.py
│           ├── location.py
│           ├── organization.py
│           ├── employment.py
│           ├── salary.py
│           ├── dates.py
│           ├── contact.py
│           ├── metadata.py
│           └── sections.py

Each extractor has exactly one responsibility.

Extractors
title.py

Responsible for

Vacancy title

Extraction order

HTML (<h1>)
JSON-LD fallback

Returns

{
    "title": str | None
}
location.py

Responsible for

city
province
country

Extraction order

Definition list
JSON-LD fallback

Returns

{
    "city": ...,
    "province": ...,
    "country": ...
}
organization.py

Responsible for

organization
ministry
department

Extraction order

HTML
JSON-LD fallback

Returns

{
    "organization": ...,
    "ministry": ...,
    "department": ...
}
employment.py

Responsible for

employment type
contract type
working hours
education
hybrid

Returns

{
    "employment_type": ...,
    "contract_type": ...,
    "working_hours": ...,
    "working_hours_min": ...,
    "working_hours_max": ...,
    "education_level": ...,
    "hybrid": ...
}
salary.py

Responsible for

salary min
salary max
salary scale
salary currency
salary period

Returns

{
    "salary_min": ...,
    "salary_max": ...,
    "salary_currency": ...,
    "salary_period": ...,
    "salary_scale": ...
}
dates.py

Responsible for

published date
closing date
vacancy number

Returns

{
    "published_date": ...,
    "closing_date": ...,
    "vacancy_number": ...
}
contact.py

Responsible for

contact name
contact role
email
phone

Returns

{
    "contact_name": ...,
    "contact_role": ...,
    "contact_phone": ...,
    "contact_email": ...
}
metadata.py

Returns parser metadata.

{
    "language": "nl",
    "parser": "werkenvoornederland",
    "parser_version": "2.0",
    "jsonld": True,
    "scraped_at": ...
}
jsonld.py

Shared JSON-LD helper.

Finds

JobPosting

recursively and exposes structured values.

utils.py

Contains reusable helpers.

Examples

clean_text()

text()

find_jobposting()

definition_value()

labelled_value()

parse_euro()

parse_hour_range()

parse_dutch_date()

extract_email()

extract_phone()
sections.py

Contains

SectionParser

Indexes headings once and exposes

summary()

responsibilities()

requirements()

competencies()

benefits()

application()

instead of repeatedly traversing the DOM.

Parser

Current parser flow

HTML

↓

BeautifulSoup

↓

Extractors

↓

RawVacancy

↓

Database

Current extractors

parse_title()

parse_location()

parse_organization()

parse_employment()

parse_salary()

parse_dates()

parse_contact()

SectionParser()

parse_metadata()

The parser also builds

salary_text

employment_text

for backward compatibility while preserving structured metadata.

Metadata stores the raw extractor outputs.

Example

metadata = {
    **parse_metadata(soup),
    "salary": salary,
    "employment": employment,
    "location": location,
    "organization": organization,
    "contact": contact,
}
Design Principles

HTML always has priority over JSON-LD.

JSON-LD is only a fallback.

Every extractor should do one thing.

No normalization inside extractors.

No database logic inside extractors.

No Slack logic inside parser.

No duplicated helper functions.

Shared parsing belongs inside

utils.py
Current State

Architecture completeness

Component	Status
Parser	✅
Extractors	✅
JSON-LD fallback	✅
Utilities	✅
Metadata	✅
Sections	✅

Overall architecture

~90–95% complete

Remaining improvements are quality improvements rather than architectural work.

Examples

better organization detection
better hybrid detection
improved section recognition
better contact parsing

These can be added incrementally.

Output Fields

The parser currently supports

title
organization
ministry
department
city
salary
employment
summary
description
published_date
closing_date
vacancy_number
contact_name
contact_email
contact_phone
metadata
html

Metadata additionally stores

salary_min
salary_max
salary_scale
salary_currency
salary_period

employment_type
contract_type
working_hours
education_level

organization

location
Next Milestone
Slack Notifications

This is the next feature to implement.

Recommended structure

app/
└── notifications/
    ├── __init__.py
    ├── slack.py
    ├── formatter.py
    └── templates.py

Flow

Crawler

↓

Parser

↓

RawVacancy

↓

Normalizer

↓

Database

↓

Slack Notification

Slack should never be called directly from extractors.

The notification layer should consume normalized vacancy objects.

Example notification

🆕 New Vacancy

Title
Kubernetes Software Platform Engineer

Organization
CJIB

Location
Leeuwarden

Salary
€4.132 – €6.275

Closing
2 September 2026

View Vacancy
https://...

Future enhancements

Block Kit formatting
Organization logos
Duplicate suppression
Multiple Slack channels
Daily summary digest
Interactive buttons
Severity/priority indicators
Future Roadmap
Phase 1 (Current)
✅ Crawler
✅ Parser
✅ Structured extractors
✅ Database
Phase 2
Slack notifications
Notification formatting
Duplicate detection improvements
Phase 3
Additional vacancy sources
Parser framework reuse
Shared extractors where applicable
Phase 4
Vacancy normalization
Classification
AI enrichment
Search
Analytics dashboard
Overall Assessment

The parser has evolved from a monolithic scraper into a clean, modular extraction framework. Responsibilities are clearly separated, HTML is preferred over JSON-LD, and shared parsing logic has been centralized. The current implementation is a strong foundation for an MVP.

The recommended next step is to shift focus away from parser architecture and toward user-facing capabilities—starting with Slack notifications—while continuing to refine extractor accuracy over time as new vacancy formats and edge cases are encountered.