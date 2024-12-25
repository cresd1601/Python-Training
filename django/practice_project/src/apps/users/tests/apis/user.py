from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.factories import UserFactory  # Import the factory


class UserViewSetTests(APITestCase):
    def setUp(self):
        """Set up admin and regular users using Factory Boy and generate tokens."""
        self.admin_user = UserFactory.create(
            username="admin",
            email="admin@example.com",
            is_staff=True,
            is_superuser=True,
        )
        self.regular_user = UserFactory.create(
            username="regular", email="regular@example.com"
        )

        self.user_data = {
            "username": "newuser",
            "password": "newpassword123",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
        }

        self.admin_token = self._get_jwt_token(self.admin_user)
        self.regular_token = self._get_jwt_token(self.regular_user)

    def _get_jwt_token(self, user):
        """Generate JWT token for the specified user."""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_create_user_as_admin(self):
        """Test that an admin user can create a new user (POST)."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        response = self.client.post("/api/users/", data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user_as_admin(self):
        """Test that an admin user can update another user's information (PUT)."""
        user_to_update = UserFactory.create(
            username="user_to_update", email="userupdate@example.com"
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")

        update_data = {
            "username": "unique_username_for_update",
            "password": "newpassword123",
            "first_name": "Updated",
            "last_name": "User",
        }
        response = self.client.put(f"/api/users/{user_to_update.id}/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_as_regular_user(self):
        """Test that a regular user cannot create a new user (POST)."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.regular_token}")
        response = self.client.post("/api/users/", data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_users_as_regular_user(self):
        """Test that a regular user cannot retrieve the list of users (GET)."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.regular_token}")
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_as_regular_user(self):
        """Test that a regular user cannot update another user's information (PUT)."""
        user_to_update = UserFactory.create(
            username="user_to_update", email="userupdate@example.com"
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.regular_token}")
        update_data = {"first_name": "Updated", "last_name": "User"}
        response = self.client.put(f"/api/users/{user_to_update.id}/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
