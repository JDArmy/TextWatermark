"""TextWatermark"""

# to be deleted
__version__ = "0.3.0"

# import logging

from textwatermark.main import TextWatermark

from . import log
from .config import settings

if settings.LOGENABLED:
    log.init_log()
