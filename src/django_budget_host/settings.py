"""
Django settings for django_budget_host project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from django_budget_host.wrapping_paper import conf, secret_key_not_configured
import sys

from pathlib import Path

BASE_DIR = conf.get_project_root()
DOT_DIR = conf.get_dot_directory()
SECRET_KEY = secret_key_not_configured()
DEBUG = True
ALLOWED_HOSTS = []
LOGGING = conf.default_logging()

CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS = [
    'crispy_forms',
    "crispy_bootstrap3",
    'django_budget.base',
    'django_budget.budget',
    'django_budget.category',
    'django_budget.transaction',
    'django_budget.summary',
    'django_budget.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
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

ROOT_URLCONF = 'django_budget_host.urls'

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates/default"],
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

WSGI_APPLICATION = 'django_budget_host.wsgi.application'

DATABASES = conf.default_database()

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

LANGUAGE_CODE = conf.default_language_code()
TIME_ZONE = conf.default_timezone()
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_ROOT = conf.create_dir_if_not_exists(DOT_DIR / 'media')
MEDIA_URL = '/files/'
STATIC_ROOT = conf.create_dir_if_not_exists(DOT_DIR / 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

DEFAULT_AUTO_FIELD = conf.default_auto_field()

sys.path.insert(0, str(conf.get_dot_directory()))
from settings import *
sys.path.pop(0)