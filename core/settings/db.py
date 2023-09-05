from pathlib import Path
from os import environ

from main.constants import _base_dir

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
if environ.get('PRODUCTION') == "TRUE":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': environ.get('DB_NAME'),
            'USER': environ.get('DB_USER'),
            'PASSWORD': environ.get('DB_PASSWORD'),
            'HOST':'localhost',
            'PORT':'3306',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': _base_dir / 'db.sqlite3',
        }
    }
