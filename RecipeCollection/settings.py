import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key

# Generate a new secret key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Set DEBUG to True during development
DEBUG = True

# Allowed hosts for local development
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# URL configuration
ROOT_URLCONF = 'RecipeCollection.urls'  # Ensure this points to your project's URLs

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipes',  # Your recipes app
]

# TEMPLATES configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Optional: Add a global template directory
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

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Default auto field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Using SQLite database
        'NAME': BASE_DIR / "db.sqlite3",  # Database file in the base directory
    }
}
