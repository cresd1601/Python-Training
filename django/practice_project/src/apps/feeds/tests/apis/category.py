from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.feeds.factories import UserFactory, CategoryFactory


class CategoryViewSetTest(APITestCase):
    """Test cases for the CategoryViewSet API, covering CRUD operations and search functionality."""

    def setUp(self):
        # Create test users (admin and regular)
        self.admin_user = UserFactory(is_staff=True)
        self.regular_user = UserFactory(is_staff=False)

        # URLs
        self.list_url = reverse("category-list")
        self.detail_url = lambda pk: reverse("category-detail", args=[pk])

        # Create categories
        self.categories = CategoryFactory.create_batch(3)

    def force_authenticate_as_admin_user(self):
        """Helper method to authenticate as an admin user."""
        self.client.force_authenticate(user=self.admin_user)

    def force_authenticate_as_regular_user(self):
        """Helper method to authenticate as a regular user."""
        self.client.force_authenticate(user=self.regular_user)

    def test_list_categories(self):
        """Test retrieving a list of categories."""
        self.force_authenticate_as_admin_user()

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)

    def test_create_category_as_admin(self):
        """Test creating a category when authenticated as an admin."""
        self.force_authenticate_as_admin_user()

        data = {"name": "New Category"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Category")

    def test_create_category_as_non_admin(self):
        """Test that a non-admin (regular user) cannot create a category."""
        self.force_authenticate_as_regular_user()

        data = {"name": "New Category"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_category(self):
        """Test retrieving a single category by its ID."""
        category = self.categories[0]
        url = self.detail_url(category.id)

        self.force_authenticate_as_admin_user()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], category.name)

    def test_update_category_as_admin(self):
        """Test updating a category when authenticated as an admin."""
        category = self.categories[0]
        url = self.detail_url(category.id)
        data = {"name": "Updated Category"}

        self.force_authenticate_as_admin_user()
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Category")

    def test_update_category_as_non_admin(self):
        """Test that a non-admin (regular user) cannot update a category."""
        self.force_authenticate_as_regular_user()

        category = self.categories[0]
        url = self.detail_url(category.id)
        data = {"name": "Updated Category"}

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_soft_delete_category_as_admin(self):
        """Test soft-deleting a category when authenticated as an admin."""
        category = self.categories[0]
        url = self.detail_url(category.id)

        self.force_authenticate_as_admin_user()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        category.refresh_from_db()
        self.assertTrue(category.is_deleted)

    def test_soft_delete_category_as_non_admin(self):
        """Test that a non-admin (regular user) cannot soft-delete a category."""
        self.force_authenticate_as_regular_user()

        category = self.categories[0]
        url = self.detail_url(category.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_category(self):
        """Test searching categories by name."""
        category = self.categories[0]
        url = self.list_url + "?search=" + category.name

        self.force_authenticate_as_admin_user()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], category.name)

    def test_paginate_categories(self):
        """Test that categories are properly paginated."""
        url = self.list_url + "?page=1"

        self.force_authenticate_as_admin_user()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data["results"]), 0)
