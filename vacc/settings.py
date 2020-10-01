
import os
from dotenv import load_dotenv
# Heroku Stuff
import django_heroku
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'secret-key-of-at-least-50-characters-to-pass-check-deploy')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 'comp.veio.in', 'competitionhunter.herokuapp.com']

website_name = 'Competiton Hunter'
# Application definition

INSTALLED_APPS = [
    # Core Applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',

    # Users Config
    'users.apps.UsersConfig',
    'comp.apps.CompConfig',
    'appl.apps.ApplConfig',
    'issuerep.apps.IssuerepConfig',

    # External Applications
    'rest_framework',
    'phone_field',
    'markdownx',
    'crispy_forms',
    'bulma',
    'imagekit',
    'pwa',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vacc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'vacc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


IN_DOCKER = bool(os.environ.get('IN_DOCKER'))


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", default="usap"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", default="usap"),
        "HOST": os.environ.get("SQL_HOST", default="db"),
        "PORT": os.environ.get("SQL_PORT", default="5432"),
    }
}

if not bool(os.environ.get('LOCAL_DEVELOPMENT_SYSTEM')):
    DATABASES = {
        "default": {
            "ENGINE": os.environ['SQL_ENGINE'],
            "NAME": os.environ['SQL_DATABASE'],
            "USER": os.environ['SQL_USER'],
            "PASSWORD": os.environ['SQL_PASSWORD'],
            "HOST": os.environ['SQL_HOST'],
            "PORT": os.environ['SQL_PORT'],
            "CONN": 600,
            "OPTIONS": {'sslmode': 'require'},
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Admin Emails
ADMINS = [
    ('Shreshth-Arora', 'arorashreshth1@gmail.com'),
    ('Shreshth-Arora-System', 'shreshtharora@icloud.com'),
    ('Shreshth-Arora-Uni', 'sarora_be18@thapar.edu')
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
# Login Stuff
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard-home'
LOGOUT_REDIRECT_URL = 'home'
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Django Toolbar
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel', ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

INTERNAL_IPS = ['127.0.0.1', 'localhost']

# Django Extensions
INSTALLED_APPS += ['django_extensions', ]

# Captcha System
INSTALLED_APPS += ['captcha', ]
RECAPTCHA_PUBLIC_KEY = '6LczbcwZAAAAAM0xlmQzIErz9fE5-z6V1tCD_Gx2'
RECAPTCHA_PRIVATE_KEY = '6LczbcwZAAAAAJvY4Hr6moDw6n05neq0jyXE0KQ3'


# Email Setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "competitionhunternoreply@gmail.com"
EMAIL_HOST_PASSWORD = "Ysm3'U;?B"

# PWA SETUP
PWA_APP_NAME = website_name
PWA_APP_DESCRIPTION = "Organize and Participate in Comeptitions"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/icon/android-chrome-512x512.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/icon/apple-touch-icon-180x180.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/icons/android-chrome-maskable-512x512.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_DEBUG_MODE = False

# Github workflow File
if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'test_database',
            'USER': 'test_user',
            'PASSWORD': 'test_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# if not bool(os.environ.get('LOCAL_DEVELOPMENT_SYSTEM')):
#     django_heroku.settings(locals())  # Heroku Sucks Big Time
