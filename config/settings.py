import os
from pathlib import Path
from dotenv import load_dotenv
from django.contrib.messages import constants as messages


# PROJECT ROOT DIRECTORY: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent           

# LOAD .ENV FILES;
load_dotenv()

# APP ENCRYPTED KEY;
SECRET_KEY = os.getenv("SECRET_KEY")

# DEBUG ENVIRONMENT;
DEBUG = bool(os.getenv('DEBUG'))

ALLOWED_HOSTS = []

# DJANGO APPS;
INSTALLED_APPS = [
    # Django Contribs;
    'django.contrib.admin',                 # Admin App ~ Django Inbuilt;
    'django.contrib.auth',                  # Auth System - Login etc;
    'django.contrib.contenttypes',          
    'django.contrib.sessions',              # Manage User Session;
    'django.contrib.messages',              # Message User;
    'django.contrib.staticfiles',           # For Static Files;
    'django.contrib.humanize',              # Humanizer;
    # App Configs;
    'config.app.AppConfig',                 # Dev App Config;
    'django_pdb',                           # Django Python Debugger;
]

# DJANGO MIDDLEWARES;
MIDDLEWARE = [
    # Django Middlewares;
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_pdb.middleware.PdbMiddleware',
]

ROOT_URLCONF = 'config.urls'

# DJANGO TEMPLATES;
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


# PASSWORD VALIDATIONS: https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# INTER-NATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# STATICS FILES REGISTER
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'public')
]


# MEDIA FILES REGISTER;
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# DEFAULT PRIMARY KEY;
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTHENTICATION MESSAGES;
MESSAGE_TAGS = {
    messages.ERROR : 'danger',
}