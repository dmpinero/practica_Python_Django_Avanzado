# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*y%^1+w(u(i@$!h22anpeg_3=%g#a63l)wn)zlkbfldqhd+rt!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'practica_Python_Django_Avanzado',
    'blogs',
    'users',
    'files',
    'fotos',
    'integracion_terceros',
    'easy_thumbnails',
    'oauth2_provider',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'practica_Python_Django_Avanzado.urls'

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

WSGI_APPLICATION = 'practica_Python_Django_Avanzado.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',       # Permitir autenticación por oAuth2
    ),
}

# To serve uploaded files
BASE_URL = 'http://127.0.0.1:8000'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Celery
USE_CELERY = True
BROKER_URL = 'amqp://guest:guest@localhost:5672//' # Utiliza RabbitMQ como cola de tareas (Message broker)

# Media URL
THUMBNAIL_HIGH_RESOLUTION = True
# Tamaño de los distintas imágenes para los dispositivos móviles

# Establece a 3600 puntos el alto y ancho de la imagen máxima
DEFAULT_IMAGE_SIZE = (3600, 3600)
# Establece opciones de las imágenes (ancho y alto a 3600 puntos. Se recorta (crop)
DEFAULT_IMAGE_OPTIONS = {'size': DEFAULT_IMAGE_SIZE, 'crop': True}
# Nombre de los archivos generados
THUMBNAIL_NAMER = 'easy_thumbnails.namers.alias'
# Tamaño de los distintas imágenes para los dispositivos móviles
THUMBNAIL_ALIASES = {
    '': {
        'iphone6_7': {'size': (375, 375), 'crop': True},
        'iphone6s_plus': {'size': (414, 414), 'crop': True},
        'iphone5': {'size': (320, 320), 'crop': True},
        'samsung': {'size': (360, 320), 'crop': True},
        'ipad': {'size': (1024, 1024), 'crop': True},
        'ipad2': {'size': (768, 768), 'crop': True},
        'samsung_galaxy': {'size': (800, 800), 'crop': True},
    },
}

# Autenticación por JWT
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True, # Permitir refrescar token JWT
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),  # Expiración del token en 5 minutos
}