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