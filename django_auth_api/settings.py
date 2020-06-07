

from pathlib import Path
from os import getenv, path
import dotenv
from django.core.management.utils import get_random_secret_key


BASE_DIR = Path(__file__).resolve().parent.parent







DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'corsheaders',
    'rest_framework',
    'djoser',
    'social_django',
]

MIDDLEWARE = [
    
    'corsheaders.middleware.CorsMiddleware', # must be as high as possible ~~~ for connection between frontend and backend servers which are not at the same domain

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_auth_api.urls'

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

WSGI_APPLICATION = 'django_auth_api.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



########### custom



my_dotenv_file = BASE_DIR / '.env.local'

if path.isfile(my_dotenv_file):
    dotenv.load_dotenv(my_dotenv_file)


SECRET_KEY = getenv('DJANGO_SECRET_KEY', get_random_secret_key())

DEBUG = getenv('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS',
                       '127.0.0.1,localhost').split(',')


# CUSTOM USER

AUTH_USER_MODEL = 'accounts.UserAccount'


# REST FRAMEWORK API

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'accounts.authentication.CustomJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# DJOSER AUTHENTICATION


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': getenv('REDIRECT_URLS').split(',')
}

# DJANGO CORS

CORS_ALLOWED_ORIGINS = getenv(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000'  # all the front end domains allowed to access the api
).split(',')
CORS_ALLOW_CREDENTIALS = True  # To allow cookies between frontend and backend domains


# AUTH COOKIES

AUTH_COOKIE = 'access'  # Name of the cookie used for authentication  (same as token name in JWT header) 
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24 * 7
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'   # set to "Strict" if same domain for BE and FE



# SOCIAL LOGIN

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv('GOOGLE_AUTH_KEY')  # client id from google cloud
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv('GOOGLE_AUTH_SECRET_KEY')  # client secret from google
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

SOCIAL_AUTH_FACEBOOK_KEY = getenv('FACEBOOK_AUTH_KEY')           # App id in fb devellopers
SOCIAL_AUTH_FACEBOOK_SECRET = getenv('FACEBOOK_AUTH_SECRET_KEY')   # App secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'email, first_name, last_name'
}


# SMTP

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= getenv('EMAIL_HOST') 
EMAIL_HOST_USER= getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD= getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT= getenv('EMAIL_PORT')
EMAIL_USE_SSL=True



# IDENTITY

DOMAIN = getenv('DOMAIN')  ## Your front end domain
SITE_NAME = 'Django Authentication'
