from django.conf import settings


def get_development_imports():
    """Import necessary components for the development environment."""
    from drf_spectacular.utils import (
        extend_schema,
        extend_schema_view,
        OpenApiParameter,
    )

    return extend_schema, extend_schema_view, OpenApiParameter


def get_no_op_decorators():
    """Return no-op decorators and classes for when drf-spectacular is not available."""

    def extend_schema(*args, **kwargs):
        def decorator(view_func):
            return view_func  # Simply return the original view function

        return decorator

    def extend_schema_view(*args, **kwargs):
        def decorator(view_func):
            return view_func  # Simply return the original view function

        return decorator

    class OpenApiParameter:
        QUERY = "query"  # Add this attribute to support 'QUERY' usage

        def __init__(self, name, type_, in_, description=None, enum=None):
            self.name = name
            self.type_ = type_
            self.in_ = in_
            self.description = description
            self.enum = enum

    return extend_schema, extend_schema_view, OpenApiParameter


# Conditional imports based on the DEBUG setting in Django's settings
if settings.DEBUG:
    try:
        extend_schema, extend_schema_view, OpenApiParameter = get_development_imports()
    except ImportError:
        extend_schema, extend_schema_view, OpenApiParameter = get_no_op_decorators()
else:
    # Production environment uses no-op decorators
    extend_schema, extend_schema_view, OpenApiParameter = get_no_op_decorators()
