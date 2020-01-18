"""
Django settings for vizsla project unit tests.

"""

import os
import django_heroku
from django.utils.crypto import get_random_string


# SECURITY WARNING: keep the secret key used in production secret!
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_string(50, chars))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vizsla_admin',
    'coincatalog',
    'numista'
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

ROOT_URLCONF = 'vizsla.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'vizsla.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=django,public'
        },
        'NAME': 'vizsla',
        'USER': 'fovizsla',
        'PASSWORD': 'fueloep2019',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                'options': '-c search_path=django,public'
            },
            'NAME': 'test_vizsla',
            'USER': 'fovizsla',
            'PASSWORD': 'fueloep2019',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    },
    'numista': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=numista,public'
        },
        'NAME': 'vizsla',
        'USER': 'fovizsla',
        'PASSWORD': 'fueloep2019',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                'options': '-c search_path=numista,public'
            },
            'NAME': 'test_vizsla',
            'USER': 'fovizsla',
            'PASSWORD': 'fueloep2019',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
}

DATABASE_ROUTERS = ['vizsla.dbrouters.AppRouter']

APP_SCHEMAS = ['numista']

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

MIGRATION_MODULES = {
    'auth': None,
    'contenttypes': None,
    'default': None,
    'sessions': None,
    'vizsla_admin': None
}
