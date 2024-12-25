from rest_framework import serializers
from apps.users.models import User
from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError


class UserRequestSerializer(serializers.Serializer):
    """
    Serializer for user creation. All fields are required.
    """

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)


class UserResponseSerializer(serializers.Serializer):
    """
    Serializer for returning user data (response format).
    """

    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating, updating, and retrieving users.
    """

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]

    def validate_username(self, username):
        """
        Ensure the username is unique.
        """
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "A user with that username already exists."
            )
        return username

    def validate_email(self, email):
        """
        Validate the email format and check for uniqueness.
        """
        # Validate email format using Django's built-in validate_email function
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")

        # Check if the email is already in use by another user
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already in use.")

        return email

    def to_representation(self, instance):
        """
        Convert user instance to response format.
        Exclude the password field from the response.
        """
        response_data = super().to_representation(instance)

        # Remove the password from the response
        response_data.pop("password", None)

        return response_data
