from rest_framework.test import APITestCase
from apps.users.serializers import UserSerializer
from apps.users.factories import UserFactory


class UserSerializerTests(APITestCase):
    def setUp(self):
        """
        Create sample user data using Factory Boy.
        """
        self.user_data = {
            "username": "testuser",
            "password": "testpassword123",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        # Create an existing user for testing duplicates
        self.existing_user = UserFactory.create(
            username="existinguser", email="existinguser@example.com"
        )

    def test_valid_user_data(self):
        """
        Test that valid user data creates a user and serializes it correctly.
        """
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        # Save the user instance and test serialized output
        user = serializer.save()
        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.email, self.user_data["email"])
        self.assertEqual(user.first_name, self.user_data["first_name"])
        self.assertEqual(user.last_name, self.user_data["last_name"])
        self.assertNotIn("password", serializer.data)

    def test_duplicate_username(self):
        """
        Test that a duplicate username raises a validation error.
        """
        # Create a user with the same username using Factory Boy
        duplicate_user_data = self.user_data.copy()
        duplicate_user_data["username"] = self.existing_user.username
        serializer = UserSerializer(data=duplicate_user_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)
        self.assertEqual(
            serializer.errors["username"], ["A user with that username already exists."]
        )

    def test_invalid_email_format(self):
        """
        Test that an invalid email format raises a validation error.
        """
        invalid_email_data = self.user_data.copy()
        invalid_email_data["email"] = "invalid-email"

        serializer = UserSerializer(data=invalid_email_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(serializer.errors["email"], ["Enter a valid email address."])

    def test_duplicate_email(self):
        """
        Test that a duplicate email raises a validation error.
        """
        duplicate_email_data = self.user_data.copy()
        duplicate_email_data["email"] = self.existing_user.email

        serializer = UserSerializer(data=duplicate_email_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(
            serializer.errors["email"],
            ["This email is already in use."],
        )

    def test_password_is_write_only(self):
        """
        Test that the password is not included in the serialized output.
        """
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertNotIn("password", serializer.data)
