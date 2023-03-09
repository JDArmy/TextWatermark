"""TextWatermark"""
__version__ = "0.2.0"

import logging

from textwatermark import log
from textwatermark.config import settings

if settings.LOGENABLED:
    log.init_log()
