# core/settings/prod.py
import os
from dotenv import load_dotenv
from .base import *

# Load environment variables from your .env file
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['api.love.cosasoft.org']
CORS_ALLOWED_ORIGINS = ["https://love.cosasoft.org"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Required for Nginx to serve static files in production
STATIC_ROOT = BASE_DIR / 'staticfiles'