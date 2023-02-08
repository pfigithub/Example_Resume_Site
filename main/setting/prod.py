from main.settings import *
from django.core.management.utils import get_random_secret_key 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY_orginal = 'django-insecure-6omfoa4(^up)z$*hyn=*a__a0_zm+jwn*^&oebs(n=vwalx9&4'

SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['pfilife.ir', 'www.pfilife.ir']

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

COMPRESS_ENABLED = not DEBUG

STATIC_ROOT = '/home/testpfic1/public_html/static'
MEDIA_ROOT = '/home/testpfic1/public_html/media'


## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

## X-Frame-Options
X_FRAME_OPTIONS = 'DENY'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

CSRF_COOKIE_SECURE = True
