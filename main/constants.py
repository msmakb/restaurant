from pathlib import Path
from typing import Final
from collections import namedtuple as _NT

_base_dir = Path(__file__).resolve().parent.parent
_main_app__templates_folder: Final[str] = '.'

LOGGERS = _NT('str', [
    'MAIN',
    'MIDDLEWARE',
    'MODELS',
])(
    'SmartHome.Main',
    'SmartHome.Middleware',
    'SmartHome.Models',
)
PATH = _NT('str', [
    'INDEX_PAGE',
])(
    'index',
)
TEMPLATES = _NT('str', [
    'INDEX_PAGE_TEMPLATE',
])(
    f'{_main_app__templates_folder}/index.html',
)
