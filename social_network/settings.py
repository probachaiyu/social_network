import os
from datetime import timedelta

from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):
    DEBUG = False
    SECRET_KEY = '-asdghthc--5=5m6rqpsi6v$kjtr^t@%7l8oxf(hmp@)t6g7+r&@%1a'
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", ]

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'admin_reorder',
        'social',
        'rest_framework',
        'rest_framework.authtoken',
        'allauth',
        'allauth.account',
        'dj_rest_auth',
        'dj_rest_auth.registration',
    ]

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    SITE_ID = 1
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'admin_reorder.middleware.ModelAdminReorder',
        "django.contrib.sessions.middleware.SessionMiddleware",
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'social.middleware.UpdateLastActivityMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'request_logging.middleware.LoggingMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "social_network.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    # Default
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                ]
            },
        }
    ]

    AUTH_USER_MODEL = "social.User"

    WSGI_APPLICATION = "social_network.wsgi.application"

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = False

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = "/static/"

    MEDIA_URL = "/media/"

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    ACCOUNT_EMAIL_VERIFICATION = "none"

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=55),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': 'velname)s %(message)s'
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'WARNING',
            },
            'error': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    ADMIN_REORDER = (
        {'app': 'social_network', 'label': 'Social', 'models': (
            {'model': 'social_network.User', 'label': 'User'},
            {'model': 'social_network.Blog', 'label': 'Blog'},
        )},
    )

    STATICFILES_LOCATION = 'static'

    FILE_UPLOAD_PERMISSIONS = 0o644
    FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 20
    }

    REST_USE_JWT = True
    JWT_AUTH_COOKIE = 'social_network'


class Development(Base):
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]
    BASE_URL = 'https://dev.djooky.fun/'
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get("POSTGRES_DB", ""),
            'USER': os.environ.get("POSTGRES_USER", ""),
            'PASSWORD': os.environ.get("POSTGRES_PASSWORD", ""),
            'HOST': os.environ.get("POSTGRES_HOST", ""),
            'PORT': os.environ.get("POSTGRES_PORT", "5432"),
            'OPTIONS': {
            }
        }
    }


class Local(Development):
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
