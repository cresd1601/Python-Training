from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.urls import reverse
from apps.users.models import User
from apps.users.factories import UserFactory


class SignUpViewTests(APITestCase):
    def setUp(self):
        """Set up the sign-up URL for testing."""
        self.sign_up_url = reverse("signup")

    def test_sign_up_with_valid_data(self):
        """Test signing up a user with valid data (POST)."""
        data = {
            "username": "newuser",
            "password": "TestPass123!",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
        }
        response = self.client.post(self.sign_up_url, data=data, format="json")

        # Verify the sign-up was successful and tokens are returned
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertIn("access_token", response.data)
        self.assertIn("refresh_token", response.data)
        self.assertEqual(
            response.data["user_id"], User.objects.get(username="newuser").id
        )

    def test_sign_up_with_existing_username(self):
        """Test sign-up fails when using an existing username (POST)."""
        UserFactory.create(username="existinguser", password="TestPass123!")

        data = {
            "username": "existinguser",
            "password": "NewPass123!",
            "email": "newuser@example.com",
            "first_name": "Existing",
            "last_name": "User",
        }
        response = self.client.post(self.sign_up_url, data=data, format="json")

        # Verify sign-up fails due to existing username
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)
        self.assertEqual(
            response.data["username"][0], "A user with that username already exists."
        )

    def test_sign_up_with_invalid_data(self):
        """Test sign-up fails when required data is missing (POST)."""
        data = {
            "username": "invaliduser",
            "email": "invaliduser@example.com",
            "first_name": "Invalid",
            "last_name": "User",
        }
        response = self.client.post(self.sign_up_url, data=data, format="json")

        # Verify sign-up fails due to missing password
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
        self.assertEqual(response.data["password"][0], "This field is required.")

    def test_sign_up_with_short_password(self):
        """Test sign-up fails when password is too short (POST)."""
        data = {
            "username": "shortpassworduser",
            "password": "short",  # Invalid password length < 8
            "email": "shortpassworduser@example.com",
            "first_name": "Short",
            "last_name": "Password",
        }
        response = self.client.post(self.sign_up_url, data=data, format="json")

        # Verify sign-up fails due to invalid password length
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
        self.assertEqual(
            response.data["password"][0],
            "This password is too short. It must contain at least 8 characters.",
        )

    def test_sign_up_with_invalid_email(self):
        """Test sign-up fails when email format is invalid (POST)."""
        data = {
            "username": "invalidemailuser",
            "password": "ValidPassword123!",
            "email": "invalidemail.com",  # Invalid email format
            "first_name": "Invalid",
            "last_name": "Email",
        }
        response = self.client.post(self.sign_up_url, data=data, format="json")

        # Verify sign-up fails due to invalid email format
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertEqual(response.data["email"][0], "Enter a valid email address.")
