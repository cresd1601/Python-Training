# test_models.py
from django.test import TestCase
from apps.users.models import UserProfile
from apps.users.factories import UserFactory, UserProfileFactory


class UserProfileModelTests(TestCase):
    def setUp(self):
        """Set up a User instance for testing."""
        self.user = UserFactory(username="testuser")

    def test_user_profile_creation(self):
        """Test creation of a UserProfile instance."""
        profile = UserProfileFactory(user=self.user, bio="This is a test bio.")

        # Verify the UserProfile was created with the expected attributes
        self.assertIsInstance(profile, UserProfile)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.bio, "This is a test bio.")

    def test_user_profile_string_representation(self):
        """Test the string representation of a UserProfile instance."""
        profile = UserProfileFactory(user=self.user, bio="This is a test bio.")

        # Verify the string representation of UserProfile matches the expected format
        self.assertEqual(str(profile), "Profile of testuser")

    def test_user_profile_on_user_delete(self):
        """Test UserProfile deletion when the associated User is deleted."""
        profile = UserProfileFactory(user=self.user)

        # Delete the user and check if the associated profile is also deleted
        self.user.delete()
        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(user_id=profile.user_id)
