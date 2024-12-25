# apps/users/tests/serializers/sign_in.py

from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.factories import UserFactory


class SignInSerializerTests(APITestCase):
    """Test the SignInSerializer for user sign-in functionality."""

    def setUp(self):
        """Set up a user for testing using Factory Boy."""
        self.user = UserFactory.create(username="testuser", password="ValidPassword123")

    def test_sign_in_valid_user(self):
        """Test that the SignInSerializer works correctly with valid credentials."""
        data = {
            "username": self.user.username,
            "password": "ValidPassword123",
        }

        response = self.client.post("/api/auth/signin/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.data)
        self.assertIn("refresh_token", response.data)

        # Verify that the JWT tokens have a valid format
        access_token = response.data["access_token"]
        refresh_token = response.data["refresh_token"]

        # Check if the tokens are valid JWT strings
        self.assertTrue(access_token.startswith("eyJ") and "." in access_token)
        self.assertTrue(refresh_token.startswith("eyJ") and "." in refresh_token)

    def test_sign_in_invalid_user(self):
        """Test that the SignInSerializer raises a ValidationError with invalid credentials."""
        data = {"username": "wronguser", "password": "WrongPassword123"}

        response = self.client.post("/api/auth/signin/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid username or password.", str(response.data))

    def test_invalid_username_password(self):
        """Test the SignInSerializer with incorrect username and password."""
        data = {"username": "invaliduser", "password": "incorrectpassword"}

        response = self.client.post("/api/auth/signin/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid username or password.", str(response.data))
