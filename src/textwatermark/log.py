"""Log"""
import os
from logging.config import dictConfig

from .config import settings

os.makedirs(settings.LOGPATH, exist_ok=True)


def init_log() -> None:
    """Init log config."""

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
            },
        },
        "handlers": {
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": os.path.join(settings.LOGPATH, "all.log"),
                "maxBytes": 1024 * 1024 * 1024 * 200,  # 200M
                "backupCount": "5",
                "encoding": "utf-8",
            },
        },
        "loggers": {
            "": {"level": settings.LOGLEVEL, "handlers": ["file"]},
        },
    }

    dictConfig(log_config)
