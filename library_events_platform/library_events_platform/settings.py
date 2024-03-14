"""
Django settings for library_events_platform project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-gr3%y5tkfml)()y@b66q0^b$5h9vpn5r(xj(2h0wt_o_sq&^fl")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]

if os.environ.get('ALLOWED_HOSTS') is not None:
    try:
        ALLOWED_HOSTS += os.environ.get('ALLOWED_HOSTS').split(',')
    except Exception as e:
        print('Cant set ALLOWED_HOSTS, using default instead')


# Application definition

INSTALLED_APPS = [
    "channels",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # local
    "chat",
    "events",
    "organizations",
    "users",

    # 3-rd party
    "corsheaders",
    "django_filters",
    "phonenumber_field",
    "rangefilter",
    "rest_framework",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "library_events_platform.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "library_events_platform.wsgi.application"


# asgi
ASGI_APPLICATION = "library_events_platform.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_SQLITE = 'sqlite'
DB_POSTGRESQL = 'postgresql'

DATABASES_ALL = {
    DB_SQLITE: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    DB_POSTGRESQL: {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'NAME': os.environ.get('POSTGRES_NAME', 'library_postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'library_postgres_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'library_postgres_password'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432')),
    },
}

DATABASES = {'default': DATABASES_ALL[os.environ.get('DJANGO_DB', DB_SQLITE)]}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/django_static/"
STATIC_ROOT = BASE_DIR / "django_static"


# media
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "mediafiles")
MEDIA_URL = "/mediafiles/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# cors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# user model
AUTH_USER_MODEL = "users.User"


# celery config
CELERY_BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("RESULT_BACKEND", "redis://localhost:6379/0")
# CELERY_IMPORTS = ['events.tasks']
