from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config
import dj_database_url
import os

# ============================================================
# BASE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 Clé secrète (local ou Render via .env)
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-ezho_*p@*1$5!c7e^rgv#94jple&^3rjvga7tv=stz+5h(3r+z"
)
# ⚙️ Mode DEBUG
DEBUG = config("DEBUG", default=False, cast=bool)  # False par défaut en prod

# 🌐 Hôtes autorisés — supporte tous les sous-domaines Render
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="*",  # Permet tous les hôtes dynamiques Render
    cast=lambda v: [s.strip() for s in v.split(",")]
)

# 🔒 CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com"  # Permet tous les sous-domaines Render dynamiques
]

# 🔑 Exemple pour les autres variables sensibles
SECRET_KEY = config("SECRET_KEY")
ORANGE_MONEY_RECEIVER = config("ORANGE_MONEY_RECEIVER")
ORANGE_MONEY_MIN_MONTANT = config("ORANGE_MONEY_MIN_MONTANT", cast=int)
ORANGE_MONEY_API_KEY = config("ORANGE_MONEY_API_KEY", default="")


# ============================================================
# APPLICATIONS
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'eglise.apps.EgliseConfig',
    'channels',         # WebSockets
    'django_extensions'
]


# ============================================================
# MIDDLEWARE
# ============================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise pour Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URLS, WSGI, ASGI
# ============================================================
ROOT_URLCONF = 'ModApp.urls'

WSGI_APPLICATION = 'ModApp.wsgi.application'
ASGI_APPLICATION = 'ModApp.asgi.application'


# ============================================================
# TEMPLATES
# ============================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'eglise' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================================================
# BASE DE DONNÉES : SQLite local + PostgreSQL Render
# ============================================================
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# ============================================================
# VALIDATION MOT DE PASSE
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================================
# INTERNATIONALISATION
# ============================================================
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Kinshasa'
USE_I18N = True
USE_TZ = True


# ============================================================
# STATIC & MEDIA
# ============================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    
    BASE_DIR / "eglise" / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# === MEDIA ===
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Permet d'afficher les médias en local
if DEBUG:
    print("⚠️ DEBUG actif — MEDIA servis en local")


# ============================================================
# AUTHENTIFICATION
# ============================================================
AUTH_USER_MODEL = 'eglise.CustomUser'
LOGIN_URL = 'eglise:connexion'
LOGIN_REDIRECT_URL = 'eglise:accueil'
LOGOUT_REDIRECT_URL = '/'


# ============================================================
# MESSAGES
# ============================================================
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}


# ============================================================
# CHANNELS
# ============================================================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


# ============================================================
# HTTPS
# ============================================================
SECURE_SSL_REDIRECT = False  # SSL géré par Render


# ============================================================
# CORS
# ============================================================
CORS_ALLOW_ALL_ORIGINS = True
