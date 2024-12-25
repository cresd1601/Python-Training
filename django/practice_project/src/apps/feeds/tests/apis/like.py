from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.feeds.factories import PostFactory, UserFactory
from apps.feeds.models import Like


class LikeAPIViewTest(APITestCase):
    """Test cases for the LikeAPIView API."""

    def setUp(self):
        """Set up test data, including users, posts, and likes."""
        self.user = UserFactory(is_staff=False)  # Regular user
        self.admin_user = UserFactory(is_staff=True)  # Admin user
        self.post = PostFactory()  # Create a test post
        self.url = reverse(
            "like-post", args=[self.post.id]
        )  # URL for liking/unliking a post

    def force_authenticate(self, user):
        """Authenticate the client as the specified user."""
        self.client.force_authenticate(user=user)

    def test_like_post(self):
        """Test liking a post (creating a Like)."""
        self.force_authenticate(self.user)  # Authenticate as regular user

        response = self.client.post(self.url)

        # Assert that the like was created and the response status is HTTP 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Post liked")
        self.assertTrue(Like.objects.filter(post=self.post, user=self.user).exists())

    def test_unlike_post(self):
        """Test unliking a post (deleting an existing Like)."""
        # Create a like before testing unliking
        Like.objects.create(post=self.post, user=self.user)
        self.force_authenticate(self.user)  # Authenticate as regular user

        response = self.client.post(self.url)

        # Assert that the like was deleted and the response status is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Post unliked")
        self.assertFalse(Like.objects.filter(post=self.post, user=self.user).exists())

    def test_like_post_for_non_existing_post(self):
        """Test trying to like a post that doesn't exist (404 error)."""
        non_existing_post_id = 9999  # Using a post ID that doesn't exist
        url = reverse("like-post", args=[non_existing_post_id])

        self.force_authenticate(self.user)  # Authenticate as regular user

        response = self.client.post(url)

        # Assert that a 404 response is returned
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Post not found")

    def test_like_post_as_admin(self):
        """Test that an admin user can like a post."""
        self.force_authenticate(self.admin_user)  # Authenticate as admin user

        response = self.client.post(self.url)

        # Assert that the like was created and the response status is HTTP 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Post liked")
        self.assertTrue(
            Like.objects.filter(post=self.post, user=self.admin_user).exists()
        )

    def test_unlike_post_as_admin(self):
        """Test that an admin user can unlike a post."""
        Like.objects.create(
            post=self.post, user=self.admin_user
        )  # Create a like for admin user
        self.force_authenticate(self.admin_user)  # Authenticate as admin user

        response = self.client.post(self.url)

        # Assert that the like was deleted and the response status is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Post unliked")
        self.assertFalse(
            Like.objects.filter(post=self.post, user=self.admin_user).exists()
        )
