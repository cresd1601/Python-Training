from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class SignInRequestSerializer(serializers.Serializer):
    """Serializer for the sign-in request containing username and password."""

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class SignInResponseSerializer(serializers.Serializer):
    """Serializer for the sign-in response containing user details and JWT tokens."""

    user_id = serializers.IntegerField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()


class SignInSerializer(serializers.Serializer):
    """Serializer that handles user sign-in, authentication, and token generation."""

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        """Authenticates the user and generates JWT tokens."""
        username = validated_data.get("username")
        password = validated_data.get("password")

        # Authenticate the user by username (not email)
        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError("Invalid username or password.")

        validated_data["user"] = user
        return validated_data

    def to_representation(self, instance):
        """Generates the response data containing user info and JWT tokens using SignInResponseSerializer."""
        user = instance["user"]
        refresh = RefreshToken.for_user(user)

        # Use SignInResponseSerializer for the final response
        return SignInResponseSerializer(
            {
                "user_id": user.id,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
        ).data
