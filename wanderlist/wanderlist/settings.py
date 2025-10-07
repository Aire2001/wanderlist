import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# ==========================================
# 🌍 LOAD ENVIRONMENT VARIABLES
# ==========================================
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# 🔐 SECURITY
# ==========================================
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-demo-key")
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,lhcupvxctvtdhobilzix.supabase.co"
).split(",")

# ==========================================
# 🧠 CSRF & SECURITY
# ==========================================
CSRF_TRUSTED_ORIGINS = os.getenv(
    "CSRF_TRUSTED_ORIGINS",
    "http://127.0.0.1:8000,http://localhost:8000,"
    "https://127.0.0.1:8000,https://localhost:8000,"
    "https://lhcupvxctvtdhobilzix.supabase.co"
).split(",")

# ✅ For development only — adjust for production later
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False
SESSION_COOKIE_SECURE = False

# ==========================================
# 🧩 INSTALLED APPS
# ==========================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",  # for natural time filters

    # Custom app
    "accounts",

    # Third-party
    "django_countries",
]

# ==========================================
# ⚙️ MIDDLEWARE
# ==========================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==========================================
# 🌐 URL & WSGI
# ==========================================
ROOT_URLCONF = "wanderlist.urls"
WSGI_APPLICATION = "wanderlist.wsgi.application"

# ==========================================
# 🧱 TEMPLATES
# ==========================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==========================================
# 🗄 DATABASE (Supabase PostgreSQL)
# ==========================================
DATABASES = {
    "default": dj_database_url.config(
        default=(
            "postgresql://postgres.lhcupvxctvtdhobilzix:"
            "Airetan.123@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres"
        ),
        conn_max_age=600,
        ssl_require=True,
    )
}

# ==========================================
# 🔑 PASSWORD VALIDATION
# ==========================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==========================================
# 🌏 INTERNATIONALIZATION & TIMEZONE
# ==========================================
LANGUAGE_CODE = "en-us"

# ✅ Use exact Philippine time (localtime, not UTC)
TIME_ZONE = "Asia/Manila"
USE_I18N = True
USE_L10N = True
USE_TZ = False  # ⚠️ Disable UTC — shows correct local time in templates

# ==========================================
# 🖼 STATIC & MEDIA FILES
# ==========================================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"  # ✅ for deployment (collectstatic)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==========================================
# 🚪 LOGIN / LOGOUT REDIRECTS
# ==========================================
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/destinations/"
LOGOUT_REDIRECT_URL = "/login/"

# ==========================================
# 🧱 DEFAULT FIELD TYPE
# ==========================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
