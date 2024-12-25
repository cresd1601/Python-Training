from django.test import TestCase
from apps.feeds.factories import PostFactory, CategoryFactory
from apps.users.factories import UserFactory
from apps.feeds.models import Post
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()


class PostModelTests(TestCase):
    def setUp(self):
        # Generate a unique username and password for the user
        self.username = fake.user_name()
        self.password = fake.password()

        # Create a user and a category using the factories
        self.user = UserFactory.create(username=self.username, password=self.password)
        self.category = CategoryFactory.create(name="Test Category")

    def test_post_creation(self):
        # Create a Post instance using the PostFactory
        post = PostFactory.create(
            title="Test Post",
            content="This is a test post content.",
            user=self.user,
            category=self.category,
        )

        # Check that the Post was created correctly
        self.assertIsInstance(post, Post)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test post content.")
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.category, self.category)

    def test_post_string_representation(self):
        # Create a Post instance using the factory
        post = PostFactory.create(
            title="Test Post",
            content="This is a test post content.",
            user=self.user,
            category=self.category,
        )

        # Check the string representation of the Post
        self.assertEqual(str(post), "Test Post")

    def test_post_foreign_key_relationships(self):
        # Create a Post instance using the factory
        post = PostFactory.create(
            title="Test Post",
            content="This is a test post content.",
            user=self.user,
            category=self.category,
        )

        # Verify that the post's user and category are set correctly
        self.assertEqual(post.user.username, self.username)  # Use dynamic username
        self.assertEqual(
            post.category.name, "Test Category"
        )  # Consistent category name
