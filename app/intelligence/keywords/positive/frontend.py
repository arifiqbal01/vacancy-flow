from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# Frameworks
# ==========================================================

REACT = Keyword(
    "react",
    weight=3,
)

NEXTJS = Keyword(
    "next.js",
    weight=3,
    synonyms=(
        "nextjs",
        "next js",
    ),
)

VUE = Keyword(
    "vue",
    weight=2,
)

ANGULAR = Keyword(
    "angular",
    weight=2,
)


# ==========================================================
# Languages
# ==========================================================

TYPESCRIPT = Keyword(
    "typescript",
    weight=3,
)

JAVASCRIPT = Keyword(
    "javascript",
    weight=3,
)

HTML = Keyword(
    "html",
    weight=1,
)

CSS = Keyword(
    "css",
    weight=1,
)


# ==========================================================
# Styling
# ==========================================================

TAILWIND = Keyword(
    "tailwind",
    weight=2,
)

BOOTSTRAP = Keyword(
    "bootstrap",
    weight=1,
)