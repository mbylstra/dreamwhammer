"""
Django settings for dreamwhammer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from local_settings import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9x%ebbi7l=tjbg@7i+036s@87aztnx16a3)ur7b6&%1miwwq4v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wham',
    'wham.apis.lastfm',
    'beat_gigs',
    'django_docs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dreamwhammer.urls'

WSGI_APPLICATION = 'dreamwhammer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


LASTFM_API_KEY='a04961fe4330211ff149a949dfabef51'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_cache',
    },
    'wham_web_request': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'wham_web_request_cache',
        # 'TIMEOUT': 60 * 60 * 24 #one day
        'TIMEOUT': None, #cache forever
        'OPTIONS': {
            'MAX_ENTRIES': 1000000  #we don't want any deleted at all!
        }
    }
}
