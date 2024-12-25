from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

# Utils
from utils import (
    StandardPagination,
    extend_schema_view,
    extend_schema,
)

# Models
from apps.feeds.models import Category

# Serializers
from apps.feeds.serializers import CategorySerializer

# Permissions
from apps.feeds.permissions import IsAdminOrReadOnlyPermission


@extend_schema_view(
    list=extend_schema(
        summary="List all categories",
        description="Retrieve a paginated list of categories with optional filters.",
        responses={200: CategorySerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific category",
        description="Retrieve details of a specific category by its ID.",
        responses={200: CategorySerializer},
    ),
    create=extend_schema(
        summary="Create a new category",
        description="Create a new category. Only accessible to admin users.",
        request=CategorySerializer,
        responses={201: CategorySerializer},
    ),
    update=extend_schema(
        summary="Update an existing category",
        description="Update an existing category by its ID. Only accessible to admin users.",
        request=CategorySerializer,
        responses={200: CategorySerializer},
    ),
    destroy=extend_schema(
        summary="Soft delete a category",
        description="Soft delete an existing category by its ID.",
    ),
)
class CategoryViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """
    A view for managing category objects with caching, pagination, and custom permissions.
    """

    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyPermission]
    serializer_class = CategorySerializer
    pagination_class = StandardPagination
    queryset = Category.objects.active()
