from .base import *  # noqa: F403
from .base import BASE_DIR

DEBUG = False

MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "staticfiles"


CSRF_TRUSTED_ORIGINS = ["http://localhost:1337"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "apps.users": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
        },
        "apps.feeds": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}
