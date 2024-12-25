from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from apps.users.factories import UserFactory, UserProfileFactory


class UserProfileViewTests(APITestCase):
    def setUp(self):
        """Set up a user, associated profile, JWT token, and profile URL."""
        self.user = UserFactory.create()
        self.profile = UserProfileFactory.create(user=self.user)
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.profile_url = reverse("user-profile")

    def test_get_user_profile(self):
        """Test retrieving the user's profile (GET)."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Make the GET request to retrieve profile information
        response = self.client.get(self.profile_url)

        # Assert that the status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the profile data returned matches the expected values
        self.assertEqual(response.data["bio"], self.profile.bio)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user_profile(self):
        """Test updating the user's profile information (PUT)."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Prepare data for updating the profile bio field
        data = {
            "bio": "Updated bio text",
        }

        # Make the PUT request to update profile information
        response = self.client.put(self.profile_url, data, format="json")

        # Assert that the status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the profile bio was successfully updated
        self.user.refresh_from_db()
        self.assertEqual(self.user.profile.bio, "Updated bio text")
