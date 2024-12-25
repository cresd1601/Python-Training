from django.conf import settings

if not settings.DEBUG:
    from .production import *  # noqa: F403
else:
    from .development import *  # noqa: F403
