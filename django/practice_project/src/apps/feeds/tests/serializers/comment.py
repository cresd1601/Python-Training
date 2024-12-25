from django.test import TestCase
from apps.feeds.models import Post, Category, Comment
from apps.feeds.serializers import CommentSerializer
from django.contrib.auth import get_user_model


class CommentSerializerTest(TestCase):
    def setUp(self):
        # Create a user instance to associate with posts
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )

        # Create a category instance to associate with posts
        self.category = Category.objects.create(name='Test Category')

        # Create a post instance, associate it with the created category and user
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content for the post.',
            category=self.category,  # Ensure that category is set
            author=self.user  # Assign an author to the post
        )

    def test_valid_comment_serialization(self):
        # Prepare valid data for the serializer
        valid_data = {
            'content': 'This is a valid comment.',  # Assuming 'content' is the correct field
            'post': self.post.id,  # Link the comment to the post
            'author': self.user.id  # Link the comment to the user (author)
        }
        serializer = CommentSerializer(data=valid_data)

        # Check that the serializer is valid
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['content'], 'This is a valid comment.')

    def test_empty_comment_text_validation(self):
        # Prepare data with empty comment content
        empty_data = {
            'content': '',  # Assuming 'content' is the correct field
            'post': self.post.id,
            'author': self.user.id  # Link the comment to the user (author)
        }
        serializer = CommentSerializer(data=empty_data)

        # Check that the serializer is not valid
        self.assertFalse(serializer.is_valid())
        self.assertIn('content', serializer.errors)  # 'content' instead of 'text'
        self.assertEqual(serializer.errors['content'][0], "This field may not be blank.")
