from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.factories import UserFactory


class SignInViewTests(APITestCase):
    def setUp(self):
        """Set up the test user and URL."""
        # Define the sign-in URL
        self.sign_in_url = reverse("signin")

        # Create a user using Factory Boy
        self.user = UserFactory(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()

    def test_sign_in_success(self):
        """Test successful sign-in with correct credentials."""
        # Correct username and password
        response = self.client.post(
            self.sign_in_url, {"username": "testuser", "password": "testpassword"}
        )

        # Check for successful sign-in
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("user_id", response.data)
        self.assertIn("access_token", response.data)
        self.assertIn("refresh_token", response.data)

    def test_sign_in_invalid_credentials(self):
        """Test sign-in with invalid credentials (wrong password)."""
        # Incorrect password
        response = self.client.post(
            self.sign_in_url, {"username": "testuser", "password": "wrongpassword"}
        )

        # Check for failed sign-in due to invalid credentials
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid username or password.", response.data)

    def test_sign_in_with_non_existent_user(self):
        """Test sign-in with a non-existent user."""
        # Non-existent user
        response = self.client.post(
            self.sign_in_url,
            {"username": "nonexistentuser", "password": "testpassword"},
        )

        # Check for failed sign-in due to non-existent user
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid username or password.", response.data)

    def test_sign_in_missing_fields(self):
        """Test sign-in with missing username or password fields."""
        # Missing username
        response = self.client.post(self.sign_in_url, {"password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)

        # Missing password
        response = self.client.post(self.sign_in_url, {"username": "testuser"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_sign_in_blank_fields(self):
        """Test sign-in with blank username or password."""
        # Blank username
        response = self.client.post(
            self.sign_in_url, {"username": "", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)

        # Blank password
        response = self.client.post(
            self.sign_in_url, {"username": "testuser", "password": ""}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
