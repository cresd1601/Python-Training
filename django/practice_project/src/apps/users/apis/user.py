from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Utils
from utils import extend_schema_view, extend_schema, StandardPagination

from apps.users.models import User
from apps.users.serializers import (
    UserSerializer,
    UserRequestSerializer,
    UserResponseSerializer,
)


@extend_schema_view(
    list=extend_schema(
        summary="List all users",
        description="Retrieve a paginated list of all users.",
        responses={200: UserResponseSerializer},
    ),
    retrieve=extend_schema(
        summary="Retrieve user details",
        description="Retrieve detailed information of a specific user by their ID.",
        responses={200: UserResponseSerializer},
    ),
    create=extend_schema(
        summary="Create a new user",
        description="Create a new user in the system with the provided details.",
        request=UserRequestSerializer,
        responses={200: UserResponseSerializer},
    ),
    update=extend_schema(
        summary="Update user information",
        description="Update an existing user's information by their ID.",
        request=UserRequestSerializer,
        responses={200: UserResponseSerializer},
    ),
    destroy=extend_schema(
        summary="Soft delete a user",
        description="Soft delete a specific user by their ID.",
    ),
)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = StandardPagination
    http_method_names = ["get", "post", "put", "delete"]
