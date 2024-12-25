from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from apps.users.factories import UserFactory


class UserModelTests(TestCase):
    def setUp(self):
        """Set up a User instance for testing."""
        self.user = UserFactory()

    def test_user_str_method(self):
        """Test that the __str__ method returns the username."""
        self.assertEqual(str(self.user), self.user.username)

    def test_user_groups_relationship(self):
        """Test the relationship between User and Group models."""
        # Create a test group and assign it to the user
        group = Group.objects.create(name="Test Group")
        self.user.groups.add(group)

        # Verify that the user is in the group and the group is correctly assigned
        self.assertIn(group, self.user.groups.all())
        self.assertEqual(group, self.user.groups.first())

    def test_user_permissions_relationship(self):
        """Test the relationship between User and Permission models."""
        # Create a test permission and assign it to the user
        permission = Permission.objects.create(
            codename="test_permission", name="Can test permission", content_type_id=1
        )
        self.user.user_permissions.add(permission)

        # Verify that the permission is assigned to the user and matches the expected value
        self.assertIn(permission, self.user.user_permissions.all())
        self.assertEqual(permission, self.user.user_permissions.first())
