"""
Django settings for DjangoFRCS project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'soyccfn)r&ad^9*k(v64%_it=0d7qqsv04$%0=!xc#yrek)8sp'

try:
    None
    #SECRET_KEY = os.environ['FRCS_SECRET']
except KeyError:
    print("Put the secret key in your environment as 'FRCS_SECRET' then restart your computer")
    print("This is for security issues")

# SECURITY WARNING: don't run with debug tuned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ["localhost", "*", "192.168.86.37"]
else:
    ALLOWED_HOSTS = [
        "*",
        "104.248.235.19",
        "frcscouting.systems",
        "www.frcscouting.systems",
        ".frcscouting.systems",
        "127.0.0.1",
    ]
# ALLOWED_HOSTS = ['localhost']
#'192.168.86.60'
AUTH_USER_MODEL = "users.CustomUser"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
    "feedback.apps.FeedbackConfig",
    "teams.apps.TeamsConfig",
    "stats.apps.StatsConfig",
    "api.apps.ApiConfig",
    "widget_tweaks",  # ngl i have no idea what this does ask aaquib
    "six",  # number parsing for phonetic team code
    "crispy_forms",  # makes native forms look better
    "rest_framework",  # api backend
    "django_cleanup",  # removes old profile pics
    "rest_framework.authtoken",
]

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}

MIDDLEWARE = [
    
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- Specify the authentication backends 

# AUTHENTICATION_BACKENDS = ('users.backends.CustomUserAuth',)

# API Authentication settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  
    ],
}

# crisy looks good with this - uses bootstrap framework
CRISPY_TEMPLATE_PACK = "bootstrap4"

ROOT_URLCONF = "DjangoFRCS.urls"

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

WSGI_APPLICATION = "DjangoFRCS.wsgi.application"

# mutes profile picture warning on server startup
SILENCED_SYSTEM_CHECKS = ["fields.W161"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# if DEBUG:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# DATABASES = {

#     'default': {

#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': 'FRCS',

#         'USER': 'postgres',

#         'PASSWORD': 'Jacktyler03',

#         'HOST': 'localhost',

#         'PORT': '5432',

#     }

# }

# else:
#    DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'frcs',
#        'USER': 'team810',
#        'PASSWORD': '@Team810',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
# }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC FILE DIRS
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGIN_URL = "login-view"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.google.com'
EMAIL_HOST_USER = 'frcsassistant@gmail.com'
EMAIL_HOST_PASSWORD = 'bbqdjfcccrjagkyu'
EMAIL_PORT = 587

# MEDIA FILE DIRS
MEDIA_ROOT = os.path.join(BASE_DIR, "profile-pics")
MEDIA_URL = "/profile-pics/"