import re
from os import environ

from core.settings.base import *
from core.settings.db import *
from core.settings.log import *
from core.settings.urls import *

# Version
PROJECT_VERSION = '0.1.0'

# Internationalization
WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'ar-ye'

TIME_ZONE = 'Asia/Aden'

USE_I18N = True

USE_TZ = False

DEBUG = False if environ.get('PRODUCTION') == "TRUE" else True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100

DATA_UPLOAD_MAX_NUMBER_FILES = 5

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon.ico$'),
    re.compile(r'^/robots.txt$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'\.(cgi|php|pl)$'),
]

PRODUCTION = not DEBUG

if PRODUCTION:

    SECURE_SSL_REDIRECT = True

    SECRET_KEY = environ.get('SECRET_KEY')

else:

    SECRET_KEY = 'django-insecure-z2j-620i=zxjowc25a8qt)+#x)x9jvj*qc*d@cu^@pw*j-1)7*'

# Hosts
ALLOWED_HOSTS = [

]
