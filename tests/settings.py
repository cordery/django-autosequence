DEBUG = True
USE_TZ = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "autosequence",
    "tests"
]
SITE_ID = 1
MIDDLEWARE_CLASSES = ()
SECRET_KEY = 'test key'
