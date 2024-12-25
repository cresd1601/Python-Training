from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Utils
from utils import extend_schema_view, extend_schema

from apps.users.serializers import (
    SignInSerializer,
    SignInResponseSerializer,
    SignInRequestSerializer,
)


@extend_schema_view(
    post=extend_schema(
        summary="User sign in",
        description="Sign in to the application and receive access and refresh tokens along with the user ID.",
        request=SignInRequestSerializer,
        responses={status.HTTP_200_OK: SignInResponseSerializer},
    )
)
class SignInView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
