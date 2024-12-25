from django.test import TestCase
from apps.users.models import User
from apps.feeds.models import Category
from apps.feeds.serializers import PostSerializer


class PostSerializerTest(TestCase):
    def setUp(self):
        # Create a user instance
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a category instance
        self.category = Category.objects.create(name="Test Category")

    def create_mock_request(self, user):
        """Create a simple mock request with the user."""

        class MockRequest:
            def __init__(self, user):
                self.user = user

        return MockRequest(user)

    def test_post_serializer_creation(self):
        """Test creating a post with valid data."""
        valid_data = {
            "title": "New Post",
            "content": "This is a new post content.",
            "category": self.category.id,
            "status": 1,  # Assuming status is an integer
        }

        # Create a mock request
        request = self.create_mock_request(self.user)

        # Create the serializer instance with valid data
        serializer = PostSerializer(data=valid_data, context={"request": request})

        # Validate and save the post
        self.assertTrue(serializer.is_valid())
        post = serializer.save()

        # Verify the post was created correctly
        self.assertEqual(post.title, valid_data["title"])
        self.assertEqual(post.content, valid_data["content"])
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.category, self.category)
