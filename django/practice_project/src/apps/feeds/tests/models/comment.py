from django.test import TestCase
from apps.users.factories import UserFactory
from apps.feeds.factories import PostFactory, CategoryFactory, CommentFactory
from django.utils.timezone import now


class CommentModelTests(TestCase):
    def setUp(self):
        # Set up a user, category, and post for testing using factories
        self.user = UserFactory.create()
        self.category = CategoryFactory.create(name="Test Category")
        self.post = PostFactory.create(user=self.user, category=self.category)

    def test_create_comment(self):
        # Create a comment associated with the post and user using factory
        comment = CommentFactory.create(
            post=self.post, user=self.user, content="This is a test comment."
        )

        # Check that the comment is created with the correct content and associations
        self.assertEqual(comment.content, "This is a test comment.")
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertTrue(comment.created)
        self.assertTrue(comment.modified)
        self.assertEqual(str(comment), f"Comment by {self.user} on {self.post}")

    def test_timestamp_fields(self):
        # Create a comment and verify created and modified fields using factory
        comment = CommentFactory.create(
            post=self.post, user=self.user, content="Another test comment."
        )

        # Ensure created and modified are set to the current time
        self.assertLessEqual(comment.created, now())
        self.assertLessEqual(comment.modified, now())

        # Update the comment and check modified timestamp changes
        old_modified = comment.modified
        comment.content = "Updated content."
        comment.save()

        self.assertNotEqual(comment.modified, old_modified)
