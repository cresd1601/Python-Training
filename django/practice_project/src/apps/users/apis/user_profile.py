from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

# Utils
from utils import extend_schema, extend_schema_view

from apps.users.serializers import (
    UserProfileSerializer,
    UserProfileRequestSerializer,
    UserProfileResponseSerializer,
)


@extend_schema_view(
    get=extend_schema(
        summary="Retrieve user profile",
        description="Retrieve the current user's profile.",
        responses={200: UserProfileResponseSerializer},
    ),
    put=extend_schema(
        summary="Partially update user profile",
        description="Partially update the current user's profile.",
        request=UserProfileRequestSerializer,
        responses={200: UserProfileResponseSerializer},
    ),
)
class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "put"]

    def get_object(self):
        return self.request.user.profile
