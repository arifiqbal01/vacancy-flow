from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# CMS
# ==========================================================

WORDPRESS = Keyword(
    "wordpress",
    weight=5,
    synonyms=(
        "wordpress development",
        "wordpress developer",
        "wordpress engineer",
        "wordpress theme development",
        "wordpress plugin development",
        "custom wordpress",
        "headless wordpress",
        "wordpress cms",
        "wordpress ontwikkelaar",
    ),
)

SHOPIFY = Keyword(
    "shopify",
    weight=5,
    synonyms=(
        "shopify development",
        "shopify developer",
        "shopify engineer",
        "shopify theme development",
        "shopify app development",
        "shopify plus",
        "headless shopify",
        "shopify cms",
        "shopify ontwikkelaar",
    ),
)

WOOCOMMERCE = Keyword(
    "woocommerce",
    weight=4,
    synonyms=(
        "woo commerce",
        "woocommerce development",
        "woocommerce developer",
        "woocommerce plugin",
        "woocommerce customization",
        "woocommerce webshop",
    ),
)

LIQUID = Keyword(
    "liquid",
    weight=4,
    synonyms=(
        "shopify liquid",
        "liquid template",
        "liquid templating",
        "liquid theme",
    ),
)

GUTENBERG = Keyword(
    "gutenberg",
    weight=3,
    synonyms=(
        "gutenberg blocks",
        "block editor",
        "wordpress block editor",
        "custom blocks",
    ),
)

ELEMENTOR = Keyword(
    "elementor",
    weight=3,
    synonyms=(
        "elementor pro",
        "elementor builder",
        "page builder",
    ),
)

ACF = Keyword(
    "advanced custom fields",
    weight=4,
    synonyms=(
        "acf",
        "acf pro",
        "custom fields",
    ),
)

WP_CLI = Keyword(
    "wp-cli",
    weight=3,
    synonyms=(
        "wp cli",
        "wordpress cli",
    ),
)

PHP = Keyword(
    "php",
    weight=4,
    synonyms=(
        "php8",
        "php 8",
        "php development",
        "core php",
    ),
)

JAVASCRIPT = Keyword(
    "javascript",
    weight=3,
    synonyms=(
        "js",
        "es6",
        "ecmascript",
        "vanilla javascript",
    ),
)


# ==========================================================
# CMS Job Titles
# ==========================================================

WORDPRESS_DEVELOPER = Keyword(
    "wordpress developer",
    weight=8,
    synonyms=(
        "wordpress engineer",
        "wordpress specialist",
        "wordpress consultant",
        "wordpress programmer",
        "wordpress web developer",
        "wordpress full stack developer",
        "wordpress backend developer",
        "wordpress frontend developer",
        "wordpress ontwikkelaar",
    ),
)

SHOPIFY_DEVELOPER = Keyword(
    "shopify developer",
    weight=8,
    synonyms=(
        "shopify engineer",
        "shopify specialist",
        "shopify consultant",
        "shopify programmer",
        "shopify web developer",
        "shopify theme developer",
        "shopify app developer",
        "shopify frontend developer",
        "shopify backend developer",
        "shopify plus developer",
        "shopify ontwikkelaar",
    ),
)

WOOCOMMERCE_DEVELOPER = Keyword(
    "woocommerce developer",
    weight=7,
    synonyms=(
        "woocommerce engineer",
        "woocommerce specialist",
        "woocommerce consultant",
        "woocommerce programmer",
        "woo developer",
        "woocommerce ontwikkelaar",
    ),
)

CMS_DEVELOPER = Keyword(
    "cms developer",
    weight=7,
    synonyms=(
        "content management system developer",
        "cms engineer",
        "cms specialist",
        "cms consultant",
        "cms ontwikkelaar",
    ),
)

ECOMMERCE_DEVELOPER = Keyword(
    "ecommerce developer",
    weight=7,
    synonyms=(
        "e-commerce developer",
        "ecommerce engineer",
        "e-commerce engineer",
        "webshop developer",
        "online store developer",
        "commerce developer",
        "e-commerce ontwikkelaar",
        "webshop ontwikkelaar",
    ),
)

WEB_CONTENT_ENGINEER = Keyword(
    "web content engineer",
    weight=5,
    synonyms=(
        "content engineer",
        "content platform engineer",
        "cms engineer",
    ),
)