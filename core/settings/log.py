from os import environ
import sys
from pathlib import Path

from django.utils import timezone

from main.constants import _base_dir, LOGGERS


LOGGING_LEVEL = 'INFO' if environ.get('PRODUCTION') == 'TRUE' else 'DEBUG'

LOGS_PATH = _base_dir.parent / 'logs'

Path(LOGS_PATH).mkdir(parents=True, exist_ok=True)

LOG_FILE_NAME = str(timezone.datetime.date(timezone.now())) + '_RES.log'

if environ.get('PRODUCTION') == "TRUE":
    HANDLERS = [
        'file',
    ]
else:
    HANDLERS = [
        'file',
        'console',
    ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "{asctime} [{levelname}] - {name}.{module}.('{funcName}') - {message}",
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.__stdout__,
            'formatter': 'simple',
        },
        'file': {
            'level': LOGGING_LEVEL,
            'class': 'logging.FileHandler',
            'filename': LOGS_PATH / LOG_FILE_NAME,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        "django": {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        "django.server": {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        "django.template": {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        "django.db.backends.schema": {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        "django.security.*": {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        LOGGERS.MIDDLEWARE: {
            'handlers': HANDLERS,
            'level': 'WARNING',
            'propagate': False,
        },
        LOGGERS.MAIN: {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        LOGGERS.MODELS: {
            'handlers': HANDLERS,
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
    },
}
