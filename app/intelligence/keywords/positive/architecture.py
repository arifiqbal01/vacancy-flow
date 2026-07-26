from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# Domain-Driven Design
# ==========================================================

DDD = Keyword(
    "domain driven design",
    weight=5,
    synonyms=(
        "ddd",
        "domain-driven design",
    ),
)

BOUNDED_CONTEXT = Keyword(
    "bounded context",
    weight=4,
)

DOMAIN_MODEL = Keyword(
    "domain model",
    weight=4,
)

AGGREGATE = Keyword(
    "aggregate",
    weight=4,
    synonyms=("aggregate root",),
)

VALUE_OBJECT = Keyword(
    "value object",
    weight=4,
)

ENTITY = Keyword(
    "entity",
    weight=3,
)

REPOSITORY_PATTERN = Keyword(
    "repository pattern",
    weight=4,
)

UNIT_OF_WORK = Keyword(
    "unit of work",
    weight=4,
)


# ==========================================================
# Architecture
# ==========================================================

HEXAGONAL = Keyword(
    "hexagonal architecture",
    weight=5,
    synonyms=(
        "ports and adapters",
        "ports & adapters",
    ),
)

CLEAN_ARCHITECTURE = Keyword(
    "clean architecture",
    weight=5,
)

LAYERED_ARCHITECTURE = Keyword(
    "layered architecture",
    weight=3,
)

MODULAR_MONOLITH = Keyword(
    "modular monolith",
    weight=4,
)

MICROSERVICES = Keyword(
    "microservices",
    weight=4,
    synonyms=("microservice",),
)


# ==========================================================
# Event-Driven
# ==========================================================

EVENT_DRIVEN = Keyword(
    "event driven architecture",
    weight=5,
    synonyms=(
        "event-driven architecture",
        "event driven",
    ),
)

EVENT_SOURCING = Keyword(
    "event sourcing",
    weight=4,
)

CQRS = Keyword(
    "cqrs",
    weight=5,
)

OUTBOX_PATTERN = Keyword(
    "outbox pattern",
    weight=4,
)

MESSAGE_BUS = Keyword(
    "message bus",
    weight=3,
)

EVENT_BUS = Keyword(
    "event bus",
    weight=3,
)


# ==========================================================
# API & Design
# ==========================================================

API_DESIGN = Keyword(
    "api design",
    weight=3,
)

SYSTEM_DESIGN = Keyword(
    "system design",
    weight=4,
)

SOFTWARE_ARCHITECTURE = Keyword(
    "software architecture",
    weight=4,
)

DESIGN_PATTERNS = Keyword(
    "design patterns",
    weight=3,
)

DEPENDENCY_INJECTION = Keyword(
    "dependency injection",
    weight=3,
)

SOLID = Keyword(
    "solid",
    weight=3,
)