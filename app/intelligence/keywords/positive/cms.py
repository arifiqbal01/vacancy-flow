from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# CMS
# ==========================================================

WORDPRESS = Keyword(
    "wordpress",
    weight=2,
)

SHOPIFY = Keyword(
    "shopify",
    weight=2,
)

WOOCOMMERCE = Keyword(
    "woocommerce",
    weight=2,
)

LIQUID = Keyword(
    "liquid",
    weight=2,
)

GUTENBERG = Keyword(
    "gutenberg",
    weight=2,
)

ELEMENTOR = Keyword(
    "elementor",
    weight=1,
)

ACF = Keyword(
    "advanced custom fields",
    weight=2,
    synonyms=("acf",),
)

WP_CLI = Keyword(
    "wp-cli",
    weight=2,
)

PHP = Keyword(
    "php",
    weight=2,
)

JAVASCRIPT = Keyword(
    "javascript",
    weight=1,
)