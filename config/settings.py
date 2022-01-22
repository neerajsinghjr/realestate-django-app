import os
from pathlib import Path
from dotenv import load_dotenv


# PROJECT ROOT DIRECTORY: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent           

# LOAD .ENV FILES;
load_dotenv()

# APP ENCRYPTED KEY;
SECRET_KEY = os.getenv("SECRET_KEY")

# DEBUG ENVIRONMENT;
DEBUG = bool(os.getenv('DEBUG'))

ALLOWED_HOSTS = []

# APPLICATION PRE-REQUISITES
INSTALLED_APPS = [
    # Django Contribs;
    'django.contrib.admin',                 # For Admin App;
    'django.contrib.auth',                  # Auth System - Login etc;
    'django.contrib.contenttypes',          
    'django.contrib.sessions',              # Manage User Session;
    'django.contrib.messages',              # Message User;
    'django.contrib.staticfiles',           # For Static Files;

    # App Configs;
    'config.apps.AppConfig',

    # # App Models
    # 'app.models'
    # 'app.models.User.User',
    # 'app.models.Realtor.Realtor',
    # 'app.models.Listing.Listing',
]

MIDDLEWARE = [
    # Django Middlewares;
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'views'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE CREDENTIALS;
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),           # 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),               # 'database name',
        'USER': os.getenv('DB_USERNAME'),           # 'username',
        'PASSWORD': os.getenv('DB_PASSWORD'),       # 'secret',
        'HOST': os.getenv('DB_HOST'),               # 'localhost',    
        'PORT': os.getenv('DB_PORT'),               # '3306',
    }
}


# PASSWORD VALIDATIONS;
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'public')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
