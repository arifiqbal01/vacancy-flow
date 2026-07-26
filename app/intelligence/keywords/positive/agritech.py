from app.intelligence.keywords_matcher import Keyword

# ==========================================================
# Agriculture
# ==========================================================

AGRICULTURE = Keyword(
    "agriculture",
    weight=4,
    synonyms=(
        "agricultural",
        "agri",
        "agro",
        "agrifood",
        "farming",
        "farm",
        "crop production",
        "crop management",
        "landbouw",
        "agrarisch",
        "akkerbouw",
        "tuinbouw",
        "land- en tuinbouw",
        "veehouderij",
    ),
)

PRECISION_AGRICULTURE = Keyword(
    "precision agriculture",
    weight=6,
    synonyms=(
        "precision farming",
        "digital agriculture",
        "digital farming",
        "smart farming",
        "smart agriculture",
        "precision landbouw",
        "precisielandbouw",
        "digitale landbouw",
        "slimme landbouw",
    ),
)

AGRONOMY = Keyword(
    "agronomy",
    weight=6,
    synonyms=(
        "agronomist",
        "crop science",
        "crop production",
        "agronoom",
        "teeltkunde",
        "gewasteelt",
    ),
)

# ==========================================================
# Entomology
# ==========================================================

ENTOMOLOGY = Keyword(
    "entomology",
    weight=8,
    synonyms=(
        "entomologist",
        "agricultural entomology",
        "economic entomology",
        "insect science",
        "entomoloog",
        "insectenkunde",
    ),
)

PEST_MANAGEMENT = Keyword(
    "integrated pest management",
    weight=8,
    synonyms=(
        "ipm",
        "pest management",
        "pest control",
        "crop protection",
        "plant protection",
        "integrated crop protection",
        "gewasbescherming",
        "plaagbeheer",
        "plaagbestrijding",
        "geïntegreerde gewasbescherming",
        "geintegreerde gewasbescherming",
    ),
)

PEST_FORECASTING = Keyword(
    "pest forecasting",
    weight=9,
    synonyms=(
        "pest prediction",
        "pest modelling",
        "pest modeling",
        "insect forecasting",
        "insect prediction",
        "disease forecasting",
        "crop disease forecasting",
        "early warning system",
        "plaagvoorspelling",
        "ziektevoorspelling",
        "voorspellingsmodel",
        "waarschuwingssysteem",
    ),
)

INSECT_MONITORING = Keyword(
    "insect monitoring",
    weight=6,
    synonyms=(
        "pest monitoring",
        "crop monitoring",
        "insect surveillance",
        "trap monitoring",
        "insectenmonitoring",
        "plaagmonitoring",
        "monitoring gewassen",
    ),
)

# ==========================================================
# Plant Science
# ==========================================================

PLANT_HEALTH = Keyword(
    "plant health",
    weight=6,
    synonyms=(
        "plant pathology",
        "crop health",
        "plant disease",
        "crop disease",
        "plantgezondheid",
        "plantenziekten",
        "fytopathologie",
    ),
)

PLANT_PROTECTION = Keyword(
    "plant protection",
    weight=6,
    synonyms=(
        "crop protection",
        "gewasbescherming",
        "plant protection products",
        "gewasverzorging",
    ),
)

# ==========================================================
# GIS / Remote Sensing
# ==========================================================

GIS = Keyword(
    "gis",
    weight=5,
    synonyms=(
        "geographic information system",
        "geospatial",
        "geospatial analysis",
        "spatial analysis",
        "geo information",
        "geografisch informatiesysteem",
        "geo-informatie",
        "ruimtelijke analyse",
    ),
)

REMOTE_SENSING = Keyword(
    "remote sensing",
    weight=6,
    synonyms=(
        "earth observation",
        "satellite imagery",
        "satellite monitoring",
        "satellite data",
        "uav",
        "drone mapping",
        "aardobservatie",
        "satellietbeelden",
        "satellietdata",
        "teledetectie",
    ),
)

# ==========================================================
# Smart Farming
# ==========================================================

COMPUTER_VISION = Keyword(
    "computer vision",
    weight=5,
    synonyms=(
        "image recognition",
        "crop detection",
        "weed detection",
        "plant detection",
        "fruit detection",
        "leaf detection",
        "disease detection",
        "beeldherkenning",
        "gewasdetectie",
        "plantdetectie",
        "onkruiddetectie",
        "ziektedetectie",
    ),
)

IOT = Keyword(
    "iot",
    weight=4,
    synonyms=(
        "internet of things",
        "smart sensors",
        "field sensors",
        "soil sensors",
        "weather station",
        "internet der dingen",
        "slimme sensoren",
        "bodemsensoren",
        "weerstation",
    ),
)

DECISION_SUPPORT = Keyword(
    "decision support system",
    weight=5,
    synonyms=(
        "decision support",
        "dss",
        "beslissingsondersteuning",
        "beslissingsondersteunend systeem",
    ),
)

YIELD_PREDICTION = Keyword(
    "yield prediction",
    weight=6,
    synonyms=(
        "yield forecasting",
        "crop yield",
        "yield modelling",
        "yield modeling",
        "opbrengstvoorspelling",
        "opbrengstprognose",
        "oogstvoorspelling",
    ),
)

# ==========================================================
# Agricultural Data
# ==========================================================

AGRICULTURAL_DATA = Keyword(
    "agricultural data",
    weight=5,
    synonyms=(
        "agri data",
        "farm data",
        "crop data",
        "field data",
        "agricultural analytics",
        "landbouwdata",
        "agrarische data",
        "gewasdata",
    ),
)

CROP_MODELLING = Keyword(
    "crop modelling",
    weight=6,
    synonyms=(
        "crop modeling",
        "crop model",
        "crop simulation",
        "crop growth model",
        "yield modelling",
        "yield modeling",
        "gewasmodellering",
        "gewasmodel",
        "groeimodel",
    ),
)

# ==========================================================
# Biological Control
# ==========================================================

BIOLOGICAL_CONTROL = Keyword(
    "biological control",
    weight=7,
    synonyms=(
        "biocontrol",
        "biological pest control",
        "natural enemies",
        "beneficial insects",
        "parasitoids",
        "predatory insects",
        "biologische bestrijding",
        "natuurlijke vijanden",
        "nuttige insecten",
    ),
)

IPM = Keyword(
    "ipm",
    weight=8,
    synonyms=(
        "integrated pest management",
        "integrated crop protection",
        "geïntegreerde gewasbescherming",
        "geintegreerde gewasbescherming",
    ),
)

PHEROMONE = Keyword(
    "pheromone",
    weight=6,
    synonyms=(
        "pheromones",
        "pheromone trap",
        "sex pheromone",
        "feromoon",
        "feromonen",
        "feromoonval",
    ),
)

INSECT_TRAP = Keyword(
    "insect trap",
    weight=6,
    synonyms=(
        "sticky trap",
        "yellow trap",
        "delta trap",
        "pheromone trap",
        "smart trap",
        "insectenval",
        "feromoonval",
        "vangplaat",
        "plakval",
    ),
)

# ==========================================================
# Agriculture Domain
# ==========================================================

SOIL = Keyword(
    "soil",
    weight=4,
    synonyms=(
        "soil science",
        "soil health",
        "soil management",
        "bodem",
        "bodemkunde",
        "bodemgezondheid",
        "bodembeheer",
    ),
)

IRRIGATION = Keyword(
    "irrigation",
    weight=4,
    synonyms=(
        "watering",
        "smart irrigation",
        "drip irrigation",
        "irrigatie",
        "beregening",
        "druppelirrigatie",
        "slimme irrigatie",
    ),
)

GREENHOUSE = Keyword(
    "greenhouse",
    weight=4,
    synonyms=(
        "greenhouse technology",
        "glasshouse",
        "greenhouse horticulture",
        "kas",
        "kassen",
        "glastuinbouw",
        "kasbouw",
    ),
)

# ==========================================================
# AgriTech Job Titles
# ==========================================================

AGRITECH_ENGINEER = Keyword(
    "agritech engineer",
    weight=8,
    synonyms=(
        "agri tech engineer",
        "agriculture engineer",
        "agricultural engineer",
        "digital agriculture engineer",
        "precision agriculture engineer",
        "smart farming engineer",
        "landbouwingenieur",
        "agrarisch ingenieur",
    ),
)

AGRITECH_DEVELOPER = Keyword(
    "agritech developer",
    weight=8,
    synonyms=(
        "agri tech developer",
        "agriculture software developer",
        "agricultural software developer",
        "agri software developer",
        "digital agriculture developer",
        "precision agriculture developer",
        "landbouw software ontwikkelaar",
        "agritech ontwikkelaar",
    ),
)

AGRICULTURAL_DATA_SCIENTIST = Keyword(
    "agricultural data scientist",
    weight=7,
    synonyms=(
        "agriculture data scientist",
        "agri data scientist",
        "crop data scientist",
        "precision agriculture data scientist",
        "landbouw data scientist",
        "agrarisch data scientist",
    ),
)

GIS_DEVELOPER = Keyword(
    "gis developer",
    weight=7,
    synonyms=(
        "gis engineer",
        "geospatial developer",
        "geospatial engineer",
        "geo developer",
        "geo engineer",
        "gis ontwikkelaar",
        "geo ontwikkelaar",
    ),
)

REMOTE_SENSING_ENGINEER = Keyword(
    "remote sensing engineer",
    weight=7,
    synonyms=(
        "remote sensing specialist",
        "earth observation engineer",
        "satellite data engineer",
        "teledetectie specialist",
        "teledetectie engineer",
        "aardobservatie engineer",
    ),
)