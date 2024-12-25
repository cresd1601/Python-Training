from rest_framework.test import APITestCase
from rest_framework import status
from apps.users.models import User, UserProfile
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfileSerializerTests(APITestCase):
    def setUp(self):
        # Create a user and associated profile
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="TestPassword123",
        )
        self.user_profile = UserProfile.objects.create(user=self.user)

        # Create login token
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_successful_profile_update(self):
        """
        Test that the profile updates successfully with valid data.
        """
        url = reverse(
            "user-profile"
        )  # Assuming 'user-profile' points to /api/profiles/me/
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        data = {
            "email": "newemail@example.com",
            "first_name": "Updated",
            "last_name": "User",
            "bio": "Updated bio",
        }

        response = self.client.put(url, data, format="json")

        # Ensure the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the profile data has been updated
        self.user.refresh_from_db()
        self.user_profile.refresh_from_db()

        self.assertEqual(self.user.email, data["email"])
        self.assertEqual(self.user.first_name, data["first_name"])
        self.assertEqual(self.user.last_name, data["last_name"])
        self.assertEqual(self.user_profile.bio, data["bio"])

    def test_invalid_email(self):
        """
        Test that an invalid email results in a validation error.
        """
        url = reverse(
            "user-profile"
        )  # Assuming 'user-profile' points to /api/profiles/me/
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        data = {
            "email": "invalid-email",
        }

        response = self.client.put(url, data, format="json")

        # Ensure the response status is a bad request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_unique_validation(self):
        """
        Test that an email must be unique for the user.
        """
        # Create a second user
        second_user = User.objects.create_user(
            username="seconduser",
            email="seconduser@example.com",
            password="TestPassword123",
        )

        UserProfile.objects.create(user=second_user)

        url = reverse(
            "user-profile"
        )  # Assuming 'user-profile' points to /api/profiles/me/
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        # Try to update with the second user's email
        data = {"email": second_user.email}

        response = self.client.put(url, data, format="json")

        # Ensure the response status is a bad request due to email conflict
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update(self):
        """
        Test that a partial update works for the profile.
        """
        url = reverse(
            "user-profile"
        )  # Assuming 'user-profile' points to /api/profiles/me/
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        # Only updating the bio field
        data = {"bio": "New bio for partial update"}

        response = self.client.put(url, data, format="json")

        # Ensure the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the profile bio is updated
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.bio, data["bio"])

    def test_user_profile_retrieval(self):
        """
        Test that the user's profile is correctly returned in the response.
        """
        url = reverse(
            "user-profile"
        )  # Assuming 'user-profile' points to /api/profiles/me/
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        response = self.client.get(url)

        # Ensure the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the response contains the correct profile data
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["first_name"], self.user.first_name)
        self.assertEqual(response.data["last_name"], self.user.last_name)
        self.assertEqual(response.data["bio"], self.user_profile.bio)
