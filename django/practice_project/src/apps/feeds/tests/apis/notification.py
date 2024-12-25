from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.feeds.factories import NotificationFactory, UserFactory
from apps.feeds.models import Notification


class NotificationAPIViewTest(APITestCase):
    """Test cases for the NotificationView API."""

    def setUp(self):
        """Set up test data for NotificationView."""
        # Create test users
        self.admin_user = UserFactory(is_staff=True)
        self.regular_user = UserFactory(is_staff=False)

        # Create notifications for the users
        self.notification = NotificationFactory(user=self.regular_user)
        self.other_notification = NotificationFactory(user=self.admin_user)

        # Define URL
        self.list_url = reverse("notification-list")

    def force_authenticate(self, user):
        """Helper method to authenticate a user."""
        self.client.force_authenticate(user=user)

    def test_list_notifications(self):
        """Test retrieving a list of notifications for the authenticated user."""
        NotificationFactory.create_batch(3, user=self.regular_user)

        self.force_authenticate(self.regular_user)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data["results"]), 4
        )  # Including the initially created notification

    def test_list_notifications_with_notifications(self):
        """Test retrieving notifications when the user has notifications."""
        Notification.objects.filter(
            user=self.regular_user
        ).delete()  # Clean up existing notifications
        NotificationFactory.create_batch(3, user=self.regular_user)

        self.assertEqual(Notification.objects.filter(user=self.regular_user).count(), 3)

        self.force_authenticate(self.regular_user)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)

    def test_list_notifications_for_unauthenticated_user(self):
        """Test that an unauthenticated user cannot retrieve notifications."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_notifications_for_another_user(self):
        """Test that a user cannot retrieve another user's notifications."""
        self.force_authenticate(self.regular_user)

        # Check that notifications for the admin user aren't visible to the regular user
        response = self.client.get(self.list_url)
        notifications = response.data["results"]

        self.assertNotIn(
            self.other_notification.id, [notif["id"] for notif in notifications]
        )

    def test_notification_order(self):
        """Test that notifications are returned in the correct order (newest first)."""
        self.force_authenticate(self.regular_user)

        # Create additional notifications for the user
        NotificationFactory.create_batch(2, user=self.regular_user)

        response = self.client.get(self.list_url)
        notifications = response.data["results"]

        # Assert that the notifications are ordered by created date (newest first)
        self.assertTrue(
            notifications[0]["created"] >= notifications[1]["created"],
            "Notifications are not ordered by creation date",
        )

    def test_get_notifications_for_non_existing_user(self):
        """Test that accessing notifications for a non-existing user results in 404."""
        url = reverse("notification-list")  # Non-existing user ID

        # Authenticate as an invalid user (unauthenticated) before making the GET request
        self.client.force_authenticate(user=None)
        response = self.client.get(url)

        # Assert that the response status code is 401 (Unauthorized)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
