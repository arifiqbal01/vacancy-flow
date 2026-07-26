from .base import BaseProfile

from app.intelligence.keywords.positive import *
from app.intelligence.keywords.negative import *


class ArifProfile(BaseProfile):

    def __init__(self):
        super().__init__(
            name="Arif",
            min_score=10,
            keywords=[
                # Backend
                PYTHON,
                FASTAPI,
                DJANGO,
                FLASK,
                SQLALCHEMY,
                ALEMBIC,
                PYDANTIC,
                ASYNCIO,
                HTTPX,
                REST_API,
                POSTGRESQL,
                REDIS,

                # Architecture
                DDD,
                HEXAGONAL,
                CLEAN_ARCHITECTURE,
                CQRS,
                EVENT_DRIVEN,
                UNIT_OF_WORK,
                OUTBOX_PATTERN,
                BOUNDED_CONTEXT,
                MODULAR_MONOLITH,
                MICROSERVICES,

                # Infrastructure
                DOCKER,
                DOCKER_COMPOSE,
                KUBERNETES,
                LINUX,
                GIT,
                GITHUB,
                CI_CD,
                GITHUB_ACTIONS,

                # Cloud
                AWS,
                AZURE,
                GCP,
                RAILWAY,
                VERCEL,
                CLOUDFLARE,
                CLOUDFLARE_R2,
                NEON,

                # AI
                AI,
                GENERATIVE_AI,
                LLM,
                RAG,
                AI_AGENT,
                OPENAI,
                LANGCHAIN,
                LANGGRAPH,
                MCP,

                # Frontend
                REACT,
                NEXTJS,
                TYPESCRIPT,
                JAVASCRIPT,

                # CMS
                WORDPRESS,
                SHOPIFY,
                WOOCOMMERCE,
                LIQUID,
                GUTENBERG,

                # High-value job titles
                PYTHON_DEVELOPER,
                PYTHON_ENGINEER,
                BACKEND_DEVELOPER,
                BACKEND_ENGINEER,
                SOFTWARE_ENGINEER,
                SOFTWARE_DEVELOPER,
                API_DEVELOPER,
                FULLSTACK_DEVELOPER,

                # Dutch job titles
                PYTHON_ONTWIKKELAAR,
                BACKEND_ONTWIKKELAAR,
                SOFTWARE_ONTWIKKELAAR,
                APPLICATIEONTWIKKELAAR,
                FULLSTACK_ONTWIKKELAAR,
            ],
            excluded_keywords=[
                # Java ecosystem
                JAVA_DEVELOPER,
                JAVA_ENGINEER,
                SPRING_BOOT,
                SPRING_FRAMEWORK,

                # .NET ecosystem
                DOTNET,
                ASP_NET,

                # Embedded / Hardware
                EMBEDDED,
                EMBEDDED_SYSTEMS,
                FIRMWARE,
                HARDWARE,
                PLC,
                SCADA,
                RTOS,
                MICROCONTROLLER,
                BARE_METAL,

                # Enterprise platforms
                SAP,
                ABAP,
                SALESFORCE,
                SERVICENOW,
                COBOL,
                MAINFRAME,

                # DevOps / Infrastructure focused roles
                DEVOPS_ENGINEER,
                SITE_RELIABILITY_ENGINEER,
                SRE,
                PLATFORM_ENGINEER,
                INFRASTRUCTURE_ENGINEER,
                CLOUD_ENGINEER,
                CLOUD_ARCHITECT,
                CLOUD_CONSULTANT,

                # Technician roles
                TECHNICIAN,
                INSTALLATION,
                ASSEMBLY,
                FIELD_SERVICE,
            ],
        )