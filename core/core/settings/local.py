# core/settings/local.py
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-buj7m*i+njpxjehi=8p(ydb_^_ty6m#atd(mg+&1y9*!g&gsfe'
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}