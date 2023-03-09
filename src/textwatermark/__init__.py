"""TextWatermark"""
__version__ = "0.2.1"

import logging

from . import log
from .config import settings

if settings.LOGENABLED:
    log.init_log()
