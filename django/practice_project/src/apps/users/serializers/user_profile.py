from rest_framework import serializers
from apps.users.models import User, UserProfile


class UserProfileRequestSerializer(serializers.Serializer):
    """
    Serializer for updating the user's profile information.
    Fields are optional, allowing for partial updates.
    """

    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)


class UserProfileResponseSerializer(serializers.Serializer):
    """
    Serializer for returning the user's profile information.
    All fields are required in the response.
    """

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    bio = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile, allowing for both retrieval and updating.
    Handles validation, updating, and representation of the profile.
    """

    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ["email", "first_name", "last_name", "bio"]

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        # Check for duplicate emails, excluding the current user's email
        if User.objects.filter(email=value).exclude(id=self.instance.user.id).exists():
            raise serializers.ValidationError("This email is already in use.")

        return value

    def update(self, instance, validated_data):
        """
        Updates the user and user profile with the provided data.
        """
        user = instance.user

        # Update user fields
        for field in ["first_name", "last_name", "email"]:
            if validated_data.get(field):
                setattr(user, field, validated_data.get(field))

        user.save()

        # Update profile bio if provided
        if "bio" in validated_data:
            instance.bio = validated_data["bio"]
            instance.save()

        return instance

    def to_representation(self, instance):
        """
        Customize the representation of the profile data, including user fields.
        """
        user = instance.user
        response_data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "bio": instance.bio,
        }

        return UserProfileResponseSerializer(response_data).data
