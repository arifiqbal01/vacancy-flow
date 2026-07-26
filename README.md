# VacancyFlow

VacancyFlow is a modular Python application that automates the collection, processing, and matching of software engineering vacancies.

The application periodically extracts vacancies, normalizes the data, removes duplicates, matches vacancies against configurable candidate profiles, and sends Slack notifications for relevant opportunities.

---

## Features

- Modular ETL pipeline
- Vacancy extraction from job boards
- Domain-driven vacancy model
- Vacancy normalization
- Duplicate detection
- Profile-based vacancy matching
- Weighted keyword matching
- Positive and negative keyword support
- Slack notifications
- Centralized configuration
- Structured logging
- Scheduled execution with GitHub Actions

---

## Pipeline

```
Extract
    ↓
Transform
    ↓
Deduplicate
    ↓
Export
    ↓
Match
    ↓
Notify
```

Each stage is independent and can be replaced or extended without affecting the rest of the application.

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── schedule.yml
│
├── app/
│   ├── core/
│   ├── extract/
│   │   └── parsers/
│   ├── intelligence/
│   │   ├── keywords/
│   │   └── profiles/
│   ├── load/
│   ├── models/
│   ├── notifications/
│   ├── pipelines/
│   │   └── stages/
│   ├── transform/
│   ├── tests/
│   └── main.py
│
├── exports/
├── knowledge/
├── logs/
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Matching Engine

VacancyFlow matches vacancies using configurable candidate profiles.

Each profile contains:

- Positive keywords
- Negative keywords
- Weighted scoring
- Minimum score threshold

Example:

```python
ArifProfile(
    min_score=10,
    keywords=[
        PYTHON,
        FASTAPI,
        DDD,
        POSTGRESQL,
    ],
    excluded_keywords=[
        JAVA_DEVELOPER,
        EMBEDDED,
    ],
)
```

A vacancy is considered a match only when:

- the minimum score is reached
- no excluded keywords are detected

---

## Configuration

Configuration is managed using **Pydantic Settings**.

Create a `.env` file from the provided example.

Example:

```env
APP_ENV=development

SLACK_ENABLED=true
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/arifiqbal01/vacancy-flow.git
cd vacancy-flow
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Usage

Run the complete pipeline.

```bash
python -m app.main
```

The pipeline performs:

1. Extract vacancies
2. Transform and normalize data
3. Remove duplicates
4. Export CSV and JSON
5. Match candidate profiles
6. Send Slack notifications

---

## GitHub Actions

The repository includes two workflows.

### Continuous Integration

Runs on every push and pull request to verify that the project builds successfully.

### Daily Vacancy Check

Runs automatically once per day and can also be started manually using **workflow_dispatch**.

---

## Output

Generated files are written to:

```
exports/
├── vacatures.csv
└── vacatures.json
```

Application logs are stored in:

```
logs/
└── vacancyflow.log
```

---

## Technologies

- Python 3.13
- Pydantic
- Pydantic Settings
- httpx
- BeautifulSoup
- Selectolax
- Pandas
- Slack Webhooks
- GitHub Actions

---

## Architecture Decision Records

Architectural decisions are documented in the `knowledge/` directory.

```
knowledge/
├── 001_addr.md
├── 002_addr.md
└── 003_addr.md
```

---

## Roadmap

- Additional vacancy sources
- Database persistence
- AI-assisted vacancy analysis
- Email notifications
- Web dashboard
- REST API
- Docker support
- Comprehensive test suite

---

## License

This project is licensed under the MIT License.