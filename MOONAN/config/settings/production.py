# 운영환경

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #운영하는 서버에서는 debug false

ALLOWED_HOSTS = ['15.165.203.13']

DJANGO_APPS += [
]

PROJECT_APPS += [
]

THIRD_PARTY_APPS += [
    
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
