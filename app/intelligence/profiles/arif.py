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

                # Backend
                PYTHON_DEVELOPER,
                BACKEND_DEVELOPER,
                SOFTWARE_DEVELOPER,
                APPLICATION_DEVELOPER,
                API_DEVELOPER,
                FULLSTACK_DEVELOPER,
                WEB_DEVELOPER,
                SYSTEMS_DEVELOPER,
                INTEGRATION_DEVELOPER,
                MICROSERVICES_ENGINEER,
                TECHNICAL_SOFTWARE_ENGINEER,
                SOFTWARE_ARCHITECT,
                PRODUCT_ENGINEER,

                # Frontend
                FRONTEND_DEVELOPER,
                UI_DEVELOPER,
                WEB_APPLICATION_DEVELOPER,
                JAVASCRIPT_DEVELOPER,
                TYPESCRIPT_DEVELOPER,
                REACT_DEVELOPER,
                ANGULAR_DEVELOPER,
                VUE_DEVELOPER,

                # AI
                AI_ENGINEER,
                MACHINE_LEARNING_ENGINEER,
                GENAI_ENGINEER,
                AI_SOFTWARE_ENGINEER,
                MLOPS_ENGINEER,
                NLP_ENGINEER,
                COMPUTER_VISION_ENGINEER,
                AI_ARCHITECT,
                AI_RESEARCHER,
                ML_RESEARCH_ENGINEER,
                DATA_SCIENTIST,
                FORWARD_DEPLOYED_ENGINEER,

                # AgriTech
                AGRITECH_ENGINEER,
                AGRITECH_DEVELOPER,
                AGRICULTURAL_DATA_SCIENTIST,
                GIS_DEVELOPER,
                REMOTE_SENSING_ENGINEER,

                # Agriculture
                AGRICULTURE,
                PRECISION_AGRICULTURE,
                AGRONOMY,

                # Entomology
                ENTOMOLOGY,
                PEST_MANAGEMENT,
                PEST_FORECASTING,
                INSECT_MONITORING,
                BIOLOGICAL_CONTROL,
                IPM,
                PHEROMONE,
                INSECT_TRAP,

                # Plant Science
                PLANT_HEALTH,
                PLANT_PROTECTION,

                # GIS / Smart Farming
                GIS,
                REMOTE_SENSING,
                COMPUTER_VISION,
                IOT,

                # Agricultural Data
                AGRICULTURAL_DATA,
                CROP_MODELLING,
                DECISION_SUPPORT,
                YIELD_PREDICTION,

                # Agriculture Domain
                SOIL,
                IRRIGATION,
                GREENHOUSE,

                # CMS Job Titles
                WORDPRESS_DEVELOPER,
                SHOPIFY_DEVELOPER,
                WOOCOMMERCE_DEVELOPER,
                CMS_DEVELOPER,
                ECOMMERCE_DEVELOPER,
                WEB_CONTENT_ENGINEER,
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