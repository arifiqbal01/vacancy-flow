# VacancyFlow Handover – Werken voor Nederland Extractor

## Current Status

The pipeline is now separated into clear stages:

```
Source
   │
   ▼
Extractor
   │
   ▼
Parser
   │
   ▼
RawVacancy
   │
   ▼
Normalizer
   │
   ▼
Vacancy
   │
   ▼
Deduplicator
```

### Responsibilities

#### Extractor

`app/extract/werkenvoornederland.py`

Responsible only for:

- downloading sitemap
- downloading vacancy HTML
- retry logic
- HTTP client
- passing HTML to parser

It **must not** parse HTML.

---

#### Parser

`app/extract/parsers/werkenvoornederland.py`

Responsible for converting

```
HTML
        ↓
RawVacancy
```

All HTML parsing belongs here.

---

#### Normalizer

Responsible for converting

```
RawVacancy
        ↓
Vacancy
```

No HTML parsing should happen here.

---

# Current Extraction Coverage

## Working

✔ title

✔ organization

✔ city

✔ salary text

✔ salary min

✔ salary max

✔ employment type

✔ summary

✔ full description

✔ vacancy number

✔ published date

✔ closing date

✔ phone number

---

## Missing

Current parser does **not** extract:

```
department

contract_type

contract_duration

working_hours

education_level

experience_level

responsibilities

requirements

competencies

benefits

application_procedure

contact_name

contact_email

role

hybrid

remote
```

---

# Important

Do NOT parse information using huge regexes over the entire page.

The Werken voor Nederland pages have a very consistent HTML structure.

Always extract from the relevant section.

---

# JSON-LD

Every vacancy contains JobPosting JSON-LD.

Always use JSON-LD first.

Currently extracted:

```
title

description

organization

city

employmentType

datePosted

validThrough

salary min

salary max
```

Future additions may appear automatically.

Always inspect JSON-LD before writing HTML parsers.

---

# HTML Sections

The vacancy page is divided into logical sections.

Instead of one giant description, parse every section separately.

---

## Dit ga je doen

Store as

```
responsibilities
```

---

## Dit vragen wij

Store as

```
requirements
```

This section usually contains

- hard requirements
- preferred requirements
- competencies

Competencies can optionally be separated later.

---

## Dit bieden we nog meer

Store as

```
benefits
```

---

## Bijzonderheden

Store as

```
application_procedure
```

Contains

- interview process
- assessments
- VOG
- references
- hybrid work
- application instructions

---

## Hier kom je te werken

Can remain inside

```
full_description
```

or become

```
organization_description
```

in the future.

---

# Employment Block

Every vacancy has a block similar to

```
Dit krijg je

Schaal 11

€4.132 - €6.275

Arbeidsovereenkomst ...

12 maanden

32 - 36 uur
```

Extract

```
salary_scale

contract_type

contract_duration

working_hours

working_hours_min

working_hours_max
```

Do NOT parse these from the entire document.

Only parse inside this block.

---

# Contact Section

Near the bottom exists

```
Stel gerust je vraag
```

Usually contains

```
Name

Role

Email

Phone
```

Current parser only extracts phone.

Improve to capture

```
contact_name

contact_role

contact_email

contact_phone
```

The section is highly structured.

Avoid global regex.

---

# Hybrid Detection

Many vacancies mention

```
hybride werken

thuiswerken

vanuit huis
```

Usually inside

```
Bijzonderheden
```

or

```
Dit bieden we nog meer
```

Set

```
Location.hybrid = True
```

when found.

---

# Education

Many vacancies contain

```
Hbo

Wo

Mbo
```

inside the employment block.

Extract

```
education_level
```

Possible values

```
MBO

HBO

WO
```

---

# Experience

Search requirement section for

```
3 jaar

5 jaar

minimaal X jaar

ervaring
```

Store as

```
experience_level
```

or

```
metadata["years_experience"]
```

until a proper model exists.

---

# Better HTML Parsing

Current parser often does

```
soup.get_text(...)
```

This loses structure.

Instead

```
find heading

↓

find next sibling

↓

read until next heading
```

This preserves section boundaries.

Pseudo code

```
find "Dit ga je doen"

↓

collect all siblings

↓

stop when next H2 encountered
```

Repeat for every heading.

---

# Avoid

Avoid parsing the entire document with regex.

Example (bad)

```
re.search(...)
```

over

```
soup.get_text()
```

Prefer

```
section.find(...)
```

or

```
CSS selectors
```

---

# Future Improvements

The parser can eventually expose

```
_parse_salary()

_parse_contact()

_parse_employment()

_parse_sections()

_parse_requirements()

_parse_benefits()

_parse_application()

_parse_location()

_parse_jsonld()
```

instead of one large parser.

---

# Testing

Whenever parser changes

Run

```
python -m app.main
```

Check that

```
Extracted

↓

Normalized

↓

Deduplicated
```

all succeed.

Then inspect output JSON.

Verify

```
null
```

fields are decreasing.

---

# Long-Term Goal

The target normalized vacancy should contain

```
title

organization

department

city

salary

employment

summary

responsibilities

requirements

benefits

application_procedure

contact

dates

vacancy_number
```

while

```
full_description
```

should only be a fallback containing the complete page text.

The parser should produce the richest possible `RawVacancy`, leaving the normalizer to perform only data cleaning, type conversion, and mapping—not HTML extraction.