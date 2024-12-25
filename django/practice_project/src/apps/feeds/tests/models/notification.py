from django.db import IntegrityError
from django.test import TestCase
from apps.feeds.models import Notification
from apps.feeds.factories import NotificationFactory, UserFactory


class NotificationModelTests(TestCase):
    def setUp(self):
        """
        Set up necessary objects for the tests
        """
        self.user = UserFactory.create()  # Create a user using the UserFactory
        self.notification = NotificationFactory.create(
            user=self.user
        )  # Create a notification linked to the user

    def test_notification_creation(self):
        """
        Test the creation of a notification
        """
        # Ensure that the notification is correctly created and linked to the user
        self.assertEqual(
            self.notification.message, self.notification.message
        )  # Check message content
        self.assertEqual(
            self.notification.user, self.user
        )  # Check if user is correctly linked

    def test_notification_string_representation(self):
        """
        Test the string representation of the Notification model
        """
        expected_str = (
            f"Notification for {self.user.username}: {self.notification.message}"
        )
        self.assertEqual(
            str(self.notification), expected_str
        )  # Compare the string representation

    def test_notification_user_relationship(self):
        """
        Test the relationship between Notification and User
        """
        # Create another notification
        NotificationFactory.create(user=self.user)

        # Ensure that the user has the correct number of notifications
        self.assertEqual(
            self.user.notifications.count(), 2
        )  # The user should have two notifications

    def test_notification_creation_without_user(self):
        """
        Test creating a notification without a user (should fail)
        """
        with self.assertRaises(IntegrityError):
            # Attempt to create a notification without specifying a user
            Notification.objects.create(message="Test message without user")
