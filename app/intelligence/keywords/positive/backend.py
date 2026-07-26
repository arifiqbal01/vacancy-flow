from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# Languages
# ==========================================================

PYTHON = Keyword("python", weight=5)

PHP = Keyword("php", weight=2)


# ==========================================================
# Frameworks
# ==========================================================

FASTAPI = Keyword("fastapi", weight=5)

DJANGO = Keyword("django", weight=4)

FLASK = Keyword("flask", weight=3)


# ==========================================================
# ORM / Validation
# ==========================================================

SQLALCHEMY = Keyword("sqlalchemy", weight=4)

ALEMBIC = Keyword("alembic", weight=3)

PYDANTIC = Keyword("pydantic", weight=4)


# ==========================================================
# Async Python
# ==========================================================

ASYNCIO = Keyword(
    "asyncio",
    weight=4,
)

ASYNC = Keyword(
    "async",
    weight=2,
)

AIOHTTP = Keyword(
    "aiohttp",
    weight=3,
)

HTTPX = Keyword(
    "httpx",
    weight=3,
)


# ==========================================================
# APIs
# ==========================================================

REST_API = Keyword(
    "rest api",
    weight=4,
    synonyms=(
        "restful api",
        "api development",
        "web api",
    ),
)

GRAPHQL = Keyword(
    "graphql",
    weight=3,
)

OPENAPI = Keyword(
    "openapi",
    weight=3,
)

SWAGGER = Keyword(
    "swagger",
    weight=2,
)


# ==========================================================
# Databases
# ==========================================================

POSTGRESQL = Keyword(
    "postgresql",
    weight=4,
    synonyms=("postgres",),
)

SQL = Keyword(
    "sql",
    weight=2,
)

REDIS = Keyword(
    "redis",
    weight=3,
)

MONGODB = Keyword(
    "mongodb",
    weight=2,
)


# ==========================================================
# Messaging
# ==========================================================

RABBITMQ = Keyword(
    "rabbitmq",
    weight=3,
)

KAFKA = Keyword(
    "kafka",
    weight=3,
)

CELERY = Keyword(
    "celery",
    weight=3,
)


# ==========================================================
# Testing
# ==========================================================

PYTEST = Keyword(
    "pytest",
    weight=3,
)

UNIT_TESTING = Keyword(
    "unit testing",
    weight=3,
)

INTEGRATION_TESTING = Keyword(
    "integration testing",
    weight=2,
)


# ==========================================================
# Backend Job Titles (English)
# ==========================================================

PYTHON_DEVELOPER = Keyword(
    "python developer",
    weight=8,
)

PYTHON_ENGINEER = Keyword(
    "python engineer",
    weight=8,
)

BACKEND_DEVELOPER = Keyword(
    "backend developer",
    weight=8,
)

BACKEND_ENGINEER = Keyword(
    "backend engineer",
    weight=8,
)

SOFTWARE_ENGINEER = Keyword(
    "software engineer",
    weight=6,
)

SOFTWARE_DEVELOPER = Keyword(
    "software developer",
    weight=6,
)

APPLICATION_DEVELOPER = Keyword(
    "application developer",
    weight=6,
)

API_DEVELOPER = Keyword(
    "api developer",
    weight=7,
)

FULLSTACK_DEVELOPER = Keyword(
    "full stack developer",
    weight=4,
    synonyms=(
        "full-stack developer",
        "fullstack developer",
    ),
)


# ==========================================================
# Backend Job Titles (Dutch)
# ==========================================================

PYTHON_ONTWIKKELAAR = Keyword(
    "python ontwikkelaar",
    weight=8,
)

BACKEND_ONTWIKKELAAR = Keyword(
    "backend ontwikkelaar",
    weight=8,
)

SOFTWARE_ONTWIKKELAAR = Keyword(
    "software ontwikkelaar",
    weight=6,
)

APPLICATIEONTWIKKELAAR = Keyword(
    "applicatieontwikkelaar",
    weight=6,
)

FULLSTACK_ONTWIKKELAAR = Keyword(
    "fullstack ontwikkelaar",
    weight=4,
)

PYTHON_ENGINEER_NL = Keyword(
    "python engineer",
    weight=8,
)

BACKEND_ENGINEER_NL = Keyword(
    "backend engineer",
    weight=8,
)