from .base import *  # noqa: F403

# Enable debug mode for development
DEBUG = True

# Extend the existing INSTALLED_APPS defined in base.py
INSTALLED_APPS.extend([
    'drf_spectacular',
    # Add any other third-party dev apps here
])

# Update REST_FRAMEWORK settings for development
REST_FRAMEWORK.update({
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
})

SPECTACULAR_SETTINGS = {
    'TITLE': 'Tutorial Project',
    'DESCRIPTION': 'Detailed description of tutorial API',
    'VERSION': '1.0.0',  # API version
    'SERVE_INCLUDE_SCHEMA': False,  # Whether to serve the raw schema with the documentation
    'SCHEMA_PATH_PREFIX': '/api/',  # Optional: Only include URLs under `/api/` in the schema
    'CONTACT': {
        'name': 'Your Name',
        'email': 'your-email@example.com',
    },
    'LICENSE': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT',
    },
    'SWAGGER_UI_SETTINGS': {
        'docExpansion': 'list',  # Collapse all sections by default
    },
    'REDOC_UI_SETTINGS': {
        'hideDownloadButton': True,  # Disable the download button in ReDoc
    },
}