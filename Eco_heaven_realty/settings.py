"""
Django settings for Eco_heaven_realty project.

Generated by 'django-admin startproject' using Django 4.1.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uh&w7x!m3kyqu=9a(f&hbw8av1nnj4s#2uj6=f4@h01neva4vv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost","192.168.246.77"]

# ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    "Eco_app",
    "Eco_home",
    "Eco_admin",
    "Eco_blog",


    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.google",

    'social_django',

    
]

SITE_ID = 1

AUTH_USER_MODEL = "Eco_app.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

# SESSION_ENGINE = ''
ROOT_URLCONF = 'Eco_heaven_realty.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'Eco_heaven_realty.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Eco_Heaven',
        'USER': 'postgres',
        'PASSWORD': '14719859Aa$',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',

    'social_core.backends.google.GoogleOAuth2',
)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default authentication urls
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_URL="logout" 
LOGOUT_REDIRECT_URL="index"

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# client id   : 964788912820-mf0thb5dd7hadi4oodie15up4q4nu2nf.apps.googleusercontent.com

# client secret: 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

# SOCIAL_AUTH_URL_NAMESPACE = 'social'

# SOCIAL_AUTH_JSONFIELD_ENABLED = True

# SOCIAL_AUTH_REQUIRE_POST = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '964788912820-mf0thb5dd7hadi4oodie15up4q4nu2nf.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' 