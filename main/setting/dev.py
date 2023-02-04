from main.settings import *
from django.core.management.utils import get_random_secret_key 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-6omfoa4(^up)z$*hyn=*a__a0_zm+jwn*^&oebs(n=vwalx9&4'

SECRET_KEY = get_random_secret_key()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#INSTALLED_APPS = []

# sites framework

SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


X_FRAME_OPTIONS = 'SAMEORIGIN'
