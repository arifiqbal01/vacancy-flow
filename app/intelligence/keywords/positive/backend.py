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
# Backend Job Titles
# ==========================================================

PYTHON_DEVELOPER = Keyword(
    "python developer",
    weight=8,
    synonyms=(
        "python engineer",
        "python ontwikkelaar",
        "python programmeur",
        "python software engineer",
        "python software developer",
    ),
)

BACKEND_DEVELOPER = Keyword(
    "backend developer",
    weight=8,
    synonyms=(
        "backend engineer",
        "backend ontwikkelaar",
        "back-end developer",
        "back-end engineer",
        "back-end ontwikkelaar",
        "backend programmeur",
        "backend software engineer",
        "backend software developer",
    ),
)

SOFTWARE_DEVELOPER = Keyword(
    "software developer",
    weight=6,
    synonyms=(
        "software engineer",
        "software ontwikkelaar",
        "software programmeur",
        "ontwikkelaar software",
        "developer software",
        "software developer .net",
    ),
)

APPLICATION_DEVELOPER = Keyword(
    "application developer",
    weight=6,
    synonyms=(
        "application engineer",
        "applicatieontwikkelaar",
        "applicatie ontwikkelaar",
        "ontwikkelaar applicaties",
        "software applicatieontwikkelaar",
    ),
)

API_DEVELOPER = Keyword(
    "api developer",
    weight=7,
    synonyms=(
        "api engineer",
        "api ontwikkelaar",
        "rest api developer",
        "rest api engineer",
        "rest ontwikkelaar",
        "integration api developer",
    ),
)

FULLSTACK_DEVELOPER = Keyword(
    "full stack developer",
    weight=5,
    synonyms=(
        "full-stack developer",
        "fullstack developer",
        "full stack engineer",
        "full-stack engineer",
        "fullstack engineer",
        "full stack ontwikkelaar",
        "full-stack ontwikkelaar",
        "fullstack ontwikkelaar",
    ),
)

WEB_DEVELOPER = Keyword(
    "web developer",
    weight=4,
    synonyms=(
        "web engineer",
        "webontwikkelaar",
        "web ontwikkelaar",
        "webdeveloper",
        "internet developer",
    ),
)

SYSTEMS_DEVELOPER = Keyword(
    "systems developer",
    weight=5,
    synonyms=(
        "system developer",
        "system engineer",
        "systeemontwikkelaar",
        "systeem ontwikkelaar",
    ),
)

INTEGRATION_DEVELOPER = Keyword(
    "integration developer",
    weight=6,
    synonyms=(
        "integration engineer",
        "integratie ontwikkelaar",
        "integratieontwikkelaar",
        "middleware developer",
        "middleware engineer",
        "esb developer",
        "koppelingen ontwikkelaar",
    ),
)

PLATFORM_ENGINEER = Keyword(
    "platform engineer",
    weight=5,
    synonyms=(
        "platform developer",
        "platform ontwikkelaar",
        "platform engineer cloud",
        "cloud platform engineer",
    ),
)

MICROSERVICES_ENGINEER = Keyword(
    "microservices engineer",
    weight=6,
    synonyms=(
        "microservices developer",
        "microservices ontwikkelaar",
        "backend microservices",
        "microservice developer",
    ),
)

CLOUD_ENGINEER = Keyword(
    "cloud engineer",
    weight=5,
    synonyms=(
        "cloud developer",
        "cloud architect",
        "azure engineer",
        "azure developer",
        "aws engineer",
        "gcp engineer",
        "cloud ontwikkelaar",
    ),
)

DEVOPS_ENGINEER = Keyword(
    "devops engineer",
    weight=4,
    synonyms=(
        "devops developer",
        "devops ontwikkelaar",
        "site reliability engineer",
        "sre",
        "platform devops engineer",
    ),
)

TECHNICAL_SOFTWARE_ENGINEER = Keyword(
    "technical software engineer",
    weight=6,
    synonyms=(
        "technical software developer",
        "technisch software engineer",
        "technisch software ontwikkelaar",
    ),
)

TECHNICAL_APPLICATION_MANAGER = Keyword(
    "technical application manager",
    weight=3,
    synonyms=(
        "technisch applicatiebeheerder",
        "applicatiebeheerder",
        "application administrator",
        "technical application administrator",
        "technisch beheerder",
    ),
)

SOFTWARE_ARCHITECT = Keyword(
    "software architect",
    weight=6,
    synonyms=(
        "solution architect",
        "technical architect",
        "applicatie architect",
        "software architectuur",
        "solution engineer",
    ),
)