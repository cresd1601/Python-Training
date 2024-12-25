from rest_framework.test import APITestCase
from apps.users.factories import UserFactory


class SignUpSerializerTests(APITestCase):
    def setUp(self):
        # Use Factory Boy to create a user instance for testing
        self.existing_user = UserFactory.create(
            username="testuser", email="test@example.com"
        )

        # Example data for signup tests
        self.existing_user_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "password": "testpassword123",
        }

        self.short_password_data = {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@example.com",
            "password": "short",  # Short password
        }

        self.url = "/api/auth/signup/"

    def test_email_unique(self):
        # Attempt to create a user with an existing email
        response = self.client.post(self.url, self.existing_user_data)
        # Check that the response contains the correct error message for email uniqueness
        self.assertIn("email", response.data)
        self.assertEqual(response.data["email"][0], "This email is already in use.")

    def test_invalid_email(self):
        # Attempt to create a user with an invalid email format
        invalid_email_data = self.existing_user_data.copy()
        invalid_email_data["email"] = "invalid-email"  # Invalid email format
        response = self.client.post(self.url, invalid_email_data)
        # Check for the correct email format validation error
        self.assertIn("email", response.data)
        self.assertEqual(response.data["email"][0], "Enter a valid email address.")

    def test_password_validation(self):
        # Test that a weak password raises a validation error
        response = self.client.post(self.url, self.short_password_data)
        # Check that the password field contains the validation error
        self.assertIn("password", response.data)
        self.assertEqual(
            response.data["password"][0],
            "This password is too short. It must contain at least 8 characters.",
        )

    def test_successful_signup_with_response(self):
        # Test signup with valid data using the factory
        valid_data = {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@example.com",
            "password": "validpassword123",
        }
        response = self.client.post(self.url, valid_data)
        # Check the response for user_id and token data
        self.assertIn("user_id", response.data)
        self.assertIn("access_token", response.data)
