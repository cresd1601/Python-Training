from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

from apps.users.models import User, UserProfile


class SignUpRequestSerializer(serializers.Serializer):
    """Serializer for the sign-up request containing user details."""

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class SignUpResponseSerializer(serializers.Serializer):
    """Serializer for the sign-up response containing user details and JWT tokens."""

    user_id = serializers.IntegerField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()


class SignUpSerializer(serializers.Serializer):
    """Serializer that handles user sign-up, account creation, and token generation."""

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate_username(self, value):
        """
        Validate the username, checking for uniqueness.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with that username already exists."
            )
        return value

    def validate_email(self, value):
        """
        Validate the email format and check for uniqueness.
        """
        # Use the validate_email This email is already in use from django.core.validators
        try:
            validate_email(value)
        except Exception:
            raise serializers.ValidationError("Enter a valid email address.")

        # Check if the email is already in use
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_password(self, value):
        """
        Validate the password strength using Django's built-in password validator.
        """
        try:
            validate_password(value)
        except Exception as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        """
        Create a new user and their associated profile.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        # Create the user profile with default values
        UserProfile.objects.create(user=user)

        return user

    def to_representation(self, instance):
        """
        Generate the response data containing user information and JWT tokens.
        Uses SignUpResponseSerializer to format the response.
        """
        refresh = RefreshToken.for_user(instance)

        response_data = {
            "user_id": instance.id,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }

        response_serializer = SignUpResponseSerializer(data=response_data)
        response_serializer.is_valid(raise_exception=True)

        return response_serializer.data
