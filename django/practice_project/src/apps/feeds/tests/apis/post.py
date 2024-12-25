from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.feeds.factories import PostFactory, UserFactory
from apps.feeds.models import Hashtag, Category


class PostViewSetTest(APITestCase):
    """Test cases for the PostViewSet API."""

    def setUp(self):
        """Set up test data for PostViewSet."""
        # Create test users
        self.admin_user = UserFactory(is_staff=True)
        self.regular_user = UserFactory(is_staff=False)

        # Create posts
        self.post = PostFactory(user=self.regular_user)
        self.other_post = PostFactory(user=self.admin_user)

        # Define URLs
        self.list_url = reverse("post-list")
        self.detail_url = lambda pk: reverse("post-detail", args=[pk])

    def authenticate(self, user):
        """Helper method to authenticate a given user."""
        self.client.force_authenticate(user=user)

    def test_list_posts(self):
        """Test retrieving a list of posts."""
        PostFactory.create_batch(3, user=self.regular_user)
        self.authenticate(self.regular_user)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 5)

    def test_list_posts_with_filters(self):
        """Test retrieving posts with filters (hashtag, search, order_by)."""
        hashtag = Hashtag.objects.create(name="test")
        PostFactory.create_batch(3, user=self.regular_user)
        posts_with_hashtags = PostFactory.create_batch(3, user=self.regular_user)
        for post in posts_with_hashtags:
            post.hashtags.add(hashtag)

        self.authenticate(self.regular_user)

        # Filter by hashtag
        response = self.client.get(self.list_url, {"hashtag": hashtag.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)

        # Search filter
        search_term = "test title"
        PostFactory.create(title=search_term, user=self.regular_user)
        response = self.client.get(self.list_url, {"search": search_term})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data["results"]), 0)

        # Order by likes
        response = self.client.get(self.list_url, {"order_by": "likes"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        """Test creating a post."""
        category = Category.objects.create(name="Test Category")
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "category": category.id,
        }

        self.authenticate(self.regular_user)
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["category"], category.id)

    def test_create_post_as_admin(self):
        """Test that an admin can create a post."""
        category = Category.objects.create(name="Admin Category")
        data = {
            "title": "Admin Post",
            "content": "Admin content.",
            "category": category.id,
        }

        self.authenticate(self.admin_user)
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["category"], category.id)

    def test_update_post(self):
        """Test updating a post."""
        data = {"title": "Updated Post", "content": "Updated content."}

        self.authenticate(self.regular_user)
        response = self.client.put(self.detail_url(self.post.id), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["content"], data["content"])

    def test_update_post_as_admin(self):
        """Test that an admin can update a post by another user."""
        data = {"title": "Admin Update", "content": "Admin updated content."}

        self.authenticate(self.admin_user)
        response = self.client.put(self.detail_url(self.post.id), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])

    def test_update_post_by_unauthorized_user(self):
        """Test that an unauthorized (unauthenticated) user cannot update another user's post."""
        data = {"title": "Unauthorized Update", "content": "Should not be updated."}

        # No authentication, simulating an unauthenticated user
        response = self.client.put(self.detail_url(self.other_post.id), data)

        # Assert that the update is unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_post(self):
        """Test soft-deleting a post."""
        self.authenticate(self.regular_user)

        response = self.client.delete(self.detail_url(self.post.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure post is marked as deleted
        self.post.refresh_from_db()
        self.assertTrue(self.post.is_deleted)

    def test_delete_post_as_admin(self):
        """Test that an admin can delete a post."""
        self.authenticate(self.admin_user)

        response = self.client.delete(self.detail_url(self.post.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure post is soft-deleted
        self.post.refresh_from_db()
        self.assertTrue(self.post.is_deleted)

    def test_anonymous_user_access(self):
        """Test that an anonymous user cannot access posts."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permissions_for_admin_user(self):
        """Test that an admin has full access to posts."""
        self.authenticate(self.admin_user)

        # List posts
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update a post
        data = {"title": "Admin Modified", "content": "Modified by admin."}
        response = self.client.put(self.detail_url(self.post.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete a post
        response = self.client.delete(self.detail_url(self.post.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_posts_ordered_by_comments(self):
        """Test retrieving posts ordered by number of comments."""
        # Create posts with varying numbers of comments
        post2 = PostFactory.create(user=self.regular_user)
        post3 = PostFactory.create(user=self.regular_user)

        # Add comments to some posts
        post2.comments.create(content="First comment", user=self.regular_user)
        post3.comments.create(content="First comment", user=self.regular_user)
        post3.comments.create(content="Second comment", user=self.regular_user)

        # Authenticate user
        self.authenticate(self.regular_user)

        # Order posts by number of comments (desc)
        response = self.client.get(self.list_url, {"order_by": "comments"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_posts_ordered_by_likes(self):
        """Test retrieving posts ordered by number of likes."""
        # Create posts with varying numbers of likes
        post2 = PostFactory.create(user=self.regular_user)
        post3 = PostFactory.create(user=self.regular_user)

        # Add likes to some posts
        post2.likes.create(user=self.regular_user)
        post3.likes.create(user=self.regular_user)
        post3.likes.create(user=self.regular_user)

        # Authenticate user
        self.authenticate(self.regular_user)

        # Order posts by number of likes (desc)
        response = self.client.get(self.list_url, {"order_by": "likes"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
