from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Utils
from utils import extend_schema, extend_schema_view

from apps.users.serializers import (
    SignUpSerializer,
    SignUpRequestSerializer,
    SignUpResponseSerializer,
)


@extend_schema_view(
    post=extend_schema(
        summary="User sign up",
        description="Sign up a new user and return tokens with user ID.",
        request=SignUpRequestSerializer,
        responses={status.HTTP_201_CREATED: SignUpResponseSerializer},
    )
)
class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
