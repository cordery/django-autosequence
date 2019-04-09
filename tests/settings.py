import os

DEBUG = True
USE_TZ = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_autosequence"
    }
}
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "autosequence",
    "tests"
]
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(ROOT_DIR, 'tests')
SITE_ID = 1
MIDDLEWARE_CLASSES = ()
SECRET_KEY = 'test key'
ROOT_URLCONF = 'tests.urls'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
