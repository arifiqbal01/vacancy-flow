from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# Containers
# ==========================================================

DOCKER = Keyword(
    "docker",
    weight=4,
)

DOCKER_COMPOSE = Keyword(
    "docker compose",
    weight=3,
)

KUBERNETES = Keyword(
    "kubernetes",
    weight=4,
    synonyms=("k8s",),
)


# ==========================================================
# Operating Systems
# ==========================================================

LINUX = Keyword(
    "linux",
    weight=3,
)

BASH = Keyword(
    "bash",
    weight=2,
)

SHELL_SCRIPTING = Keyword(
    "shell scripting",
    weight=2,
)


# ==========================================================
# Version Control
# ==========================================================

GIT = Keyword(
    "git",
    weight=3,
)

GITHUB = Keyword(
    "github",
    weight=3,
)

GITLAB = Keyword(
    "gitlab",
    weight=2,
)


# ==========================================================
# CI/CD
# ==========================================================

CI_CD = Keyword(
    "ci/cd",
    weight=3,
    synonyms=(
        "ci cd",
        "continuous integration",
        "continuous delivery",
        "continuous deployment",
    ),
)

GITHUB_ACTIONS = Keyword(
    "github actions",
    weight=3,
)

GITLAB_CI = Keyword(
    "gitlab ci",
    weight=3,
)

JENKINS = Keyword(
    "jenkins",
    weight=2,
)