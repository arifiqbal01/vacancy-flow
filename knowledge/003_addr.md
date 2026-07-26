VacancyFlow Handover

Version: Intelligence & Multi-Profile Notifications

Project Overview

VacancyFlow is a modular vacancy extraction and intelligence platform.

Current pipeline:

Extract
    ↓
Normalize
    ↓
Deduplicate
    ↓
Load
    ↓
Match
    ↓
Notify

The project intentionally separates responsibilities into independent stages so new extractors, matching strategies, or notification channels can be added without affecting the rest of the system.

Current Architecture
app/
├── core/
│   ├── configs.py
│   └── logging.py
│
├── extract/
│   ├── base.py
│   ├── werkenvoornederland.py
│   └── parsers/
│
├── intelligence/
│   ├── matcher.py
│   ├── keywords.py
│   ├── results.py
│   └── profiles/
│       ├── __init__.py
│       ├── base.py
│       ├── arif.py
│       └── stub.py
│
├── models/
│
├── notifications/
│   ├── formatter.py
│   ├── slack.py
│   └── templates.py
│
├── pipelines/
│   ├── vacancies.py
│   ├── config.py
│   ├── result.py
│   └── stages/
│       ├── extract.py
│       ├── normalize.py
│       ├── deduplicate.py
│       ├── load.py
│       ├── match.py
│       ├── notify.py
│       └── factory.py
│
└── transform/
Pipeline
1. Extract

Responsible only for scraping raw vacancies.

Output:

list[RawVacancy]

No normalization.

No database logic.

No notifications.

2. Normalize

Converts RawVacancy into the canonical Vacancy model.

Output:

list[Vacancy]

The canonical model contains nested value objects.

Vacancy
├── Organization
├── Location
├── Salary
├── Employment
├── Contact
├── SourceInfo
└── Metadata

Everything downstream uses this model.

3. Deduplicate

Responsible for duplicate detection.

Output:

unique_vacancies
duplicates
4. Load

Writes normalized vacancies to

CSV
JSON

Current persistence is export files only.

Database persistence can later replace or complement this stage.

5. Intelligence

This is the largest architectural improvement.

Instead of notifying every vacancy, every vacancy is evaluated against one or more profiles.

Pipeline:

Vacancy
    ↓
JobMatcher
    ↓
Profiles
    ↓
MatchedVacancy
Intelligence Module

Structure:

intelligence/
├── matcher.py
├── keywords.py
├── results.py
└── profiles/
BaseProfile

Every profile inherits from

BaseProfile

Contains

name
keywords
min_score

Example

ArifProfile()
StubProfile()
DEFAULT_PROFILES

Profiles are registered centrally.

DEFAULT_PROFILES = [
    ArifProfile(),
    StubProfile(),
]

JobMatcher automatically evaluates every configured profile.

Adding another profile only requires:

class JohnProfile(BaseProfile):
    ...

and

DEFAULT_PROFILES.append(
    JohnProfile()
)

No other code changes.

KeywordMatcher

Responsible only for keyword matching.

Searches

title
summary
description
responsibilities
requirements
competencies

Returns

MatchResult(
    matched=True,
    score=3,
    matched_keywords=[
        "python",
        "docker",
        "aws",
    ],
)

It knows nothing about Slack or profiles.

JobMatcher

Acts as the intelligence orchestrator.

Responsibilities

iterate over every configured profile
create KeywordMatcher
collect successful matches

Returns

list[ProfileMatch]

instead of a single MatchResult.

ProfileMatch
ProfileMatch
├── profile
└── result

Example

Profile:
    Arif

Matched keywords:
    python
    docker
    aws

Score:
    3
MatchStage

Produces

MatchedVacancy

instead of Vacancy.

MatchedVacancy
├── vacancy
└── matches

Example

Vacancy
└── Kubernetes Engineer

Matches

├── Arif
│   ├── kubernetes
│   └── docker
│
└── DevOps
    ├── kubernetes
    ├── linux
    └── terraform

This information is preserved for later stages.

Notify Stage

NotifyStage now receives

list[MatchedVacancy]

instead of

list[Vacancy]

This allows notifications to include intelligence information.

Slack Notifications

Current flow

MatchedVacancy
      ↓
SlackFormatter
      ↓
Template
      ↓
SlackNotifier
      ↓
Slack Incoming Webhook
SlackFormatter

Responsible only for converting domain objects into text.

No HTTP logic.

SlackNotifier

Responsible only for

send(message)

Uses

httpx

and Incoming Webhooks.

Slack Template

Now uses the canonical Vacancy model.

Instead of old flat properties

salary_text
organization_name
location
url

it now reads

vacancy.organization.name
vacancy.location.city
vacancy.salary.minimum
vacancy.salary.maximum
vacancy.source.source_url

Notifications also include the profile(s) and matched keywords.

Logging

Centralized.

Every module uses

from app.core import get_logger

logger = get_logger(__name__)

instead of configuring logging independently.

Pipeline Stages
ExtractStage

Only extraction.

NormalizeStage

Only normalization.

DeduplicateStage

Only duplicate detection.

LoadStage

Only exports.

MatchStage

Only intelligence.

NotifyStage

Only delivery.

Each stage has a single responsibility.

Configuration

Centralized in

app/core/configs.py

Includes

parser
crawler
database
Slack
logging
exports
Domain Models

Canonical model

Vacancy
├── Organization
├── Location
├── Salary
├── Employment
├── Contact
├── Metadata
└── SourceInfo

The notification system, intelligence layer, exports, and future database all depend on this model.

Design Principles

The project follows these principles:

Single Responsibility Principle
Dependency Injection
Stage-based pipeline
Canonical domain model
Separation of extraction, intelligence, and delivery
No cross-layer coupling
Profiles are extensible without modifying the matcher
Current Workflow
Extract
      ↓
Normalize
      ↓
Deduplicate
      ↓
Export
      ↓
Match
      │
      ├── ArifProfile
      ├── StubProfile
      └── Future Profiles
      ↓
MatchedVacancy
      ↓
Slack Formatter
      ↓
Slack Webhook
Current Status

Completed:

✅ Modular parser architecture
✅ Canonical vacancy model
✅ Stage-based pipeline
✅ CSV export
✅ JSON export
✅ Centralized configuration
✅ Centralized logging
✅ Deduplication
✅ Intelligence layer
✅ Keyword matching
✅ Multi-profile matching
✅ ProfileMatch
✅ MatchedVacancy
✅ Slack notifications
✅ Notifications using the canonical domain model
✅ Dependency injection throughout the pipeline
Recommended Next Milestones
1. Database persistence

Replace or augment CSV/JSON exports with persistent storage.

2. Profile configuration

Load enabled profiles from configuration rather than hardcoding DEFAULT_PROFILES.

3. Profile-specific notifications

Allow each profile to target a different Slack webhook, channel, or recipient.

4. AI-powered matching

Introduce additional matchers (e.g. embeddings or LLM-based relevance scoring) while keeping JobMatcher as the orchestration layer.

5. Notification history

Persist notification state to prevent sending the same vacancy to the same profile across pipeline runs.

6. Additional extractors

Add new vacancy sources by implementing new extractors that output RawVacancy; the existing normalization, intelligence, and notification pipeline can be reused without modification.

The current architecture provides a clean separation between data acquisition, data transformation, intelligence, and delivery, making VacancyFlow straightforward to extend with additional sources, matching strategies, storage backends, and notification channels.