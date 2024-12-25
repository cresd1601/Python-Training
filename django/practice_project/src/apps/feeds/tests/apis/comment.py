from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.feeds.factories import PostFactory, CommentFactory, UserFactory


class CommentViewSetTest(APITestCase):
    """Test cases for the CommentViewSet API."""

    def setUp(self):
        """Set up test data for CommentViewSet."""
        # Create test users (admin and regular user)
        self.admin_user = UserFactory(is_staff=True)
        self.regular_user = UserFactory(is_staff=False)

        # Create a post to associate with comments
        self.post = PostFactory()

        # Define URLs
        self.list_url = reverse("post-comments-list", args=[self.post.id])
        self.create_url = self.list_url
        self.detail_url = lambda pk: reverse(
            "post-comments-detail", args=[self.post.id, pk]
        )

    def force_authenticate_as_regular_user(self):
        """Helper method to authenticate as regular user."""
        self.client.force_authenticate(user=self.regular_user)

    def force_authenticate_as_admin_user(self):
        """Helper method to authenticate as admin user."""
        self.client.force_authenticate(user=self.admin_user)

    def test_list_comments(self):
        """Test retrieving a list of comments for a specific post."""
        CommentFactory.create_batch(3, post=self.post)

        # Authenticate as regular user
        self.force_authenticate_as_regular_user()

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)

    def test_create_comment(self):
        """Test creating a comment for a specific post."""
        data = {"content": "This is a new comment"}
        self.force_authenticate_as_regular_user()

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["content"], data["content"])
        self.assertEqual(response.data["user"], self.regular_user.username)

    def test_create_comment_for_non_existing_post(self):
        """Test creating a comment for a non-existing post (should fail)."""
        data = {"content": "This is a new comment"}
        url = reverse("post-comments-list", args=[9999])  # Non-existing post ID
        self.force_authenticate_as_regular_user()

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_comment(self):
        """Test updating an existing comment."""
        comment = CommentFactory(post=self.post, user=self.regular_user)
        data = {"content": "Updated content"}
        url = self.detail_url(comment.id)

        self.force_authenticate_as_regular_user()
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Updated content")

    def test_update_comment_as_another_user(self):
        """Test that a regular user cannot update a comment made by another user."""
        comment = CommentFactory(post=self.post, user=self.regular_user)
        another_user = UserFactory(is_staff=False)
        data = {"content": "Updated content by another user"}
        url = self.detail_url(comment.id)

        self.client.force_authenticate(user=another_user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_comment(self):
        """Test deleting a comment."""
        comment = CommentFactory(post=self.post, user=self.regular_user)
        url = self.detail_url(comment.id)

        self.force_authenticate_as_regular_user()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that the comment is deleted (soft delete expected)
        comment.refresh_from_db()
        self.assertTrue(comment.is_deleted)

    def test_delete_comment_as_another_user(self):
        """Test that a regular user cannot delete a comment made by another user."""
        comment = CommentFactory(post=self.post, user=self.regular_user)
        another_user = UserFactory(is_staff=False)
        url = self.detail_url(comment.id)

        self.client.force_authenticate(user=another_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_comments_for_non_existing_post(self):
        """Test that accessing comments for a non-existing post results in 404."""
        url = reverse("post-comments-list", args=[9999])  # Non-existing post ID

        # Authenticate as regular user before making the GET request
        self.force_authenticate_as_regular_user()
        response = self.client.get(url)

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
