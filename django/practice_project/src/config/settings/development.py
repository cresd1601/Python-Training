from .base import *  # noqa: F403
from .base import INSTALLED_APPS, REST_FRAMEWORK, MIDDLEWARE

# Enable debug mode for development
DEBUG = True

# Extend the existing INSTALLED_APPS defined in base.py
INSTALLED_APPS.extend(["drf_spectacular", "debug_toolbar"])

MIDDLEWARE.extend(
    [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
)

INTERNAL_IPS = [
    "127.0.0.1",
]

# Update REST_FRAMEWORK settings for development
REST_FRAMEWORK.update(
    {
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    }
)

SPECTACULAR_SETTINGS = {
    "TITLE": "Practice Project",
    "DESCRIPTION": "Detailed description of practice API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api/",
    "CONTACT": {
        "name": "Quy Do",
        "email": "quy.do@asnet.com.vn",
    },
    "LICENSE": {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    "SWAGGER_UI_SETTINGS": {
        "docExpansion": "list",
    },
    "REDOC_UI_SETTINGS": {
        "hideDownloadButton": True,
    },
}

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
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "apps.users": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "apps.feeds": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
