from pathlib import Path
import os # Importing the os module for interacting with the operating system
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv() # Loading environment variables from .env file

SECRET_KEY = os.environ.get("SECRET_KEY") # Getting the secret key from environment variables

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] # Allowed hosts for the Django application

CORS_ALLOWED_ORIGINS = [
    "https://localhost:5173",
    "https://knowshare-2e1a84c86803.herokuapp.com",
] # Allowing specified CORS origins

CSRF_ALLOWED_ORIGINS = [
    "https://localhost:5173",
    "https://knowshare-2e1a84c86803.herokuapp.com",
] # Allowing specified CSRF origins

CSRF_TRUSTED_ORIGINS = [
    "https://localhost:5173",
    "https://knowshare-2e1a84c86803.herokuapp.com",
] # Specifying trusted CSRF origins

CSRF_COOKIE_HTTPONLY = False  # Setting CSRF cookie to be accessible from JavaScript
CSRF_COOKIE_SECURE = True   # Setting CSRF cookie to be transmitted only over HTTPS
CSRF_COOKIE_SAMESITE = 'None'  # Setting CSRF cookie SameSite attribute to 'None'

CORS_ALLOW_CREDENTIALS = True  # Allowing credentials during CORS requests
SESSION_COOKIE_SAMESITE = 'None'  # Setting session cookie SameSite attribute to 'None'
SESSION_COOKIE_SECURE = True  # Setting session cookie to be transmitted only over HTTPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'sslserver', #comment
    
    'rest_framework', #comment
    'corsheaders', #comment
    
    'customuser', #comment
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Including WhiteNoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'corsheaders.middleware.CorsMiddleware', # Including CorsMiddleware for handling CORS headers
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fortunehunters.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
} #comment

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

WSGI_APPLICATION = 'fortunehunters.wsgi.application'

DATABASES = {
	'default': {  
		'ENGINE': 'django.db.backends.postgresql_psycopg2',  
		'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get("DB_PORT"),
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

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#AUTH_USER_MODEL = 'customusers.CustomUser' # Customizing the user model

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Setting the media root directory
MEDIA_URL = '/media/' # Setting the media URL


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Configuring static files storage with Whitenoise