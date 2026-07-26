from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# AI
# ==========================================================

AI = Keyword(
    "artificial intelligence",
    weight=3,
    synonyms=("ai",),
)

GENERATIVE_AI = Keyword(
    "generative ai",
    weight=4,
)

LLM = Keyword(
    "llm",
    weight=4,
    synonyms=("large language model",),
)

AI_AGENT = Keyword(
    "ai agent",
    weight=5,
    synonyms=(
        "ai agents",
        "agentic ai",
        "agent",
    ),
)

RAG = Keyword(
    "rag",
    weight=4,
    synonyms=("retrieval augmented generation",),
)

EMBEDDINGS = Keyword(
    "embeddings",
    weight=3,
)

PROMPT_ENGINEERING = Keyword(
    "prompt engineering",
    weight=3,
)


# ==========================================================
# Providers
# ==========================================================

OPENAI = Keyword(
    "openai",
    weight=4,
)

ANTHROPIC = Keyword(
    "anthropic",
    weight=3,
)

CLAUDE = Keyword(
    "claude",
    weight=3,
)

GEMINI = Keyword(
    "gemini",
    weight=3,
)

OLLAMA = Keyword(
    "ollama",
    weight=3,
)

LANGCHAIN = Keyword(
    "langchain",
    weight=3,
)

LANGGRAPH = Keyword(
    "langgraph",
    weight=3,
)

MCP = Keyword(
    "model context protocol",
    weight=3,
    synonyms=("mcp",),
)


# ==========================================================
# AI / Machine Learning Job Titles
# ==========================================================

AI_ENGINEER = Keyword(
    "ai engineer",
    weight=8,
    synonyms=(
        "artificial intelligence engineer",
        "ai developer",
        "ai ontwikkelaar",
        "ai specialist",
        "artificial intelligence developer",
    ),
)

MACHINE_LEARNING_ENGINEER = Keyword(
    "machine learning engineer",
    weight=8,
    synonyms=(
        "ml engineer",
        "machine learning developer",
        "ml developer",
        "machine learning ontwikkelaar",
        "machine learning specialist",
    ),
)

GENAI_ENGINEER = Keyword(
    "generative ai engineer",
    weight=8,
    synonyms=(
        "genai engineer",
        "gen ai engineer",
        "generative ai developer",
        "genai developer",
        "llm engineer",
        "large language model engineer",
        "llm developer",
    ),
)

AI_SOFTWARE_ENGINEER = Keyword(
    "ai software engineer",
    weight=8,
    synonyms=(
        "ai software developer",
        "machine learning software engineer",
        "software engineer ai",
        "software developer ai",
    ),
)

DATA_SCIENTIST = Keyword(
    "data scientist",
    weight=7,
    synonyms=(
        "data science specialist",
        "data science engineer",
        "data scientist ai",
        "data scientist machine learning",
        "data scientist ml",
        "data scientist artificial intelligence",
        "data scientist kunstmatige intelligentie",
    ),
)

ML_RESEARCH_ENGINEER = Keyword(
    "machine learning research engineer",
    weight=7,
    synonyms=(
        "research engineer ai",
        "research engineer machine learning",
        "applied ai researcher",
        "applied machine learning engineer",
    ),
)

AI_RESEARCHER = Keyword(
    "ai researcher",
    weight=7,
    synonyms=(
        "artificial intelligence researcher",
        "machine learning researcher",
        "research scientist ai",
        "ai research scientist",
    ),
)

COMPUTER_VISION_ENGINEER = Keyword(
    "computer vision engineer",
    weight=7,
    synonyms=(
        "computer vision developer",
        "computer vision specialist",
        "vision engineer",
        "image processing engineer",
        "computer vision ontwikkelaar",
    ),
)

NLP_ENGINEER = Keyword(
    "nlp engineer",
    weight=7,
    synonyms=(
        "natural language processing engineer",
        "nlp developer",
        "natural language engineer",
        "language ai engineer",
    ),
)

AI_CONSULTANT = Keyword(
    "ai consultant",
    weight=5,
    synonyms=(
        "artificial intelligence consultant",
        "machine learning consultant",
        "ai adviseur",
        "ai specialist consultant",
    ),
)

AI_ARCHITECT = Keyword(
    "ai architect",
    weight=6,
    synonyms=(
        "artificial intelligence architect",
        "machine learning architect",
        "solution architect ai",
        "enterprise ai architect",
    ),
)

MLOPS_ENGINEER = Keyword(
    "mlops engineer",
    weight=7,
    synonyms=(
        "ml ops engineer",
        "machine learning operations engineer",
        "machine learning platform engineer",
        "ml platform engineer",
        "mlops developer",
    ),
)

PROMPT_ENGINEER = Keyword(
    "prompt engineer",
    weight=5,
    synonyms=(
        "prompt developer",
        "llm prompt engineer",
        "ai prompt engineer",
        "prompt specialist",
    ),
)

AI_PRODUCT_ENGINEER = Keyword(
    "ai product engineer",
    weight=6,
    synonyms=(
        "ai solutions engineer",
        "ai application engineer",
        "intelligent systems engineer",
    ),
)