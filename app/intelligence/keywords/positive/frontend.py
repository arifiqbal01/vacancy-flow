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



# ==========================================================
# Frontend Job Titles
# ==========================================================

FRONTEND_DEVELOPER = Keyword(
    "frontend developer",
    weight=8,
    synonyms=(
        "front-end developer",
        "frontend engineer",
        "front-end engineer",
        "frontend ontwikkelaar",
        "front-end ontwikkelaar",
        "frontend programmeur",
        "frontend software engineer",
        "frontend software developer",
    ),
)

FRONTEND_ENGINEER = Keyword(
    "frontend engineer",
    weight=8,
    synonyms=(
        "front-end engineer",
        "frontend developer",
        "front-end developer",
        "frontend ontwikkelaar",
    ),
)

UI_DEVELOPER = Keyword(
    "ui developer",
    weight=7,
    synonyms=(
        "ui engineer",
        "user interface developer",
        "interface developer",
        "ui ontwikkelaar",
    ),
)

WEB_DEVELOPER = Keyword(
    "web developer",
    weight=6,
    synonyms=(
        "web engineer",
        "webontwikkelaar",
        "web ontwikkelaar",
        "webdeveloper",
        "internet developer",
    ),
)

JAVASCRIPT_DEVELOPER = Keyword(
    "javascript developer",
    weight=7,
    synonyms=(
        "javascript engineer",
        "javascript ontwikkelaar",
        "javascript programmeur",
        "js developer",
        "js engineer",
    ),
)

TYPESCRIPT_DEVELOPER = Keyword(
    "typescript developer",
    weight=7,
    synonyms=(
        "typescript engineer",
        "typescript ontwikkelaar",
        "typescript programmeur",
        "ts developer",
    ),
)

REACT_DEVELOPER = Keyword(
    "react developer",
    weight=8,
    synonyms=(
        "react engineer",
        "react ontwikkelaar",
        "react programmeur",
        "react.js developer",
        "reactjs developer",
        "react js developer",
    ),
)

ANGULAR_DEVELOPER = Keyword(
    "angular developer",
    weight=8,
    synonyms=(
        "angular engineer",
        "angular ontwikkelaar",
        "angular programmeur",
    ),
)

VUE_DEVELOPER = Keyword(
    "vue developer",
    weight=8,
    synonyms=(
        "vue engineer",
        "vue ontwikkelaar",
        "vue.js developer",
        "vuejs developer",
    ),
)

FRONTEND_ARCHITECT = Keyword(
    "frontend architect",
    weight=7,
    synonyms=(
        "front-end architect",
        "ui architect",
        "frontend solution architect",
        "frontend architectuur",
    ),
)

WEB_APPLICATION_DEVELOPER = Keyword(
    "web application developer",
    weight=6,
    synonyms=(
        "web application engineer",
        "webapp developer",
        "webapp ontwikkelaar",
        "web applicatie ontwikkelaar",
        "webapplicatieontwikkelaar",
    ),
)

UI_ENGINEER = Keyword(
    "ui engineer",
    weight=7,
    synonyms=(
        "ui developer",
        "user interface engineer",
        "interface engineer",
        "ui ontwikkelaar",
    ),
)

UX_ENGINEER = Keyword(
    "ux engineer",
    weight=6,
    synonyms=(
        "ux developer",
        "ux ontwikkelaar",
        "frontend ux engineer",
    ),
)

FRONTEND_CONSULTANT = Keyword(
    "frontend consultant",
    weight=5,
    synonyms=(
        "frontend specialist",
        "frontend expert",
        "frontend adviseur",
        "frontend consultant ict",
    ),
)