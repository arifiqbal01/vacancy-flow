from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# Cloud Providers
# ==========================================================

AWS = Keyword(
    "aws",
    weight=4,
    synonyms=("amazon web services",),
)

AZURE = Keyword(
    "azure",
    weight=4,
    synonyms=("microsoft azure",),
)

GCP = Keyword(
    "gcp",
    weight=4,
    synonyms=("google cloud", "google cloud platform"),
)


# ==========================================================
# Platforms
# ==========================================================

RAILWAY = Keyword(
    "railway",
    weight=3,
)

VERCEL = Keyword(
    "vercel",
    weight=3,
)

NETLIFY = Keyword(
    "netlify",
    weight=2,
)

HEROKU = Keyword(
    "heroku",
    weight=2,
)


# ==========================================================
# Cloud Services
# ==========================================================

CLOUDFLARE = Keyword(
    "cloudflare",
    weight=3,
)

CLOUDFLARE_R2 = Keyword(
    "cloudflare r2",
    weight=3,
)

NEON = Keyword(
    "neon",
    weight=3,
)

SUPABASE = Keyword(
    "supabase",
    weight=3,
)

DIGITALOCEAN = Keyword(
    "digitalocean",
    weight=2,
)

TERRAFORM = Keyword(
    "terraform",
    weight=3,
)

ANSIBLE = Keyword(
    "ansible",
    weight=2,
)