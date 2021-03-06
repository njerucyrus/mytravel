"""
Django settings for mytravel project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# from django.core.urlresolvers import reverse_lazy
# LOGIN_REDIRECT_URL = reverse_lazy('index')
# LOGIN_URL = reverse_lazy('login')
# LOGOUT_URL = reverse_lazy('user_logout')




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+rg*&g)$dk(mq)#lt&8m_n4=l8zy5wyv-z(8&#r94*b_%l!*l0'

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
    'storages',
    'matatu',
    'api',
    'rest_framework',
    'crispy_forms',

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

ROOT_URLCONF = 'mytravel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates'), ],
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

WSGI_APPLICATION = 'mytravel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
# ALLOWED_HOSTS = ['*']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_files'),
)


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')


CRISPY_TEMPLATE_PACK = 'bootstrap3'


PRODUCTION = True
if PRODUCTION:
    API_KEY = 'f38227587e797f9c9d9ffbc6517e6bf77b0e20d752644ab8da9564e42267dc26'
    AT_USERNAME = 'njerucyrus'
    PRODUCT_NAME = 'Hudutech'
    METADATA = {}
    CURRENCY_CODE = 'KES'

    AWS_QUERYSTRING_AUTH = True

    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

    MEDIA_URL = 'http://%s.s3.amazonaws.com/media_root/' % AWS_STORAGE_BUCKET_NAME

    DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

else:

    API_KEY = 'f01d41160c4168aeba896eb541737b7c3d89497278d9808855dd76e2487b634c'
    AT_USERNAME = 'njerucyrus123'
    PRODUCT_NAME = 'Mytravel'
    CURRENCY_CODE = 'KES'
    METADATA = {"agentId": "654", "productId": "321"}


