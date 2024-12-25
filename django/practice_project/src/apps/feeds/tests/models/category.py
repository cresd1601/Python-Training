from django.test import TestCase
from apps.feeds.models import Category
from apps.feeds.factories import CategoryFactory


class CategoryModelTests(TestCase):
    def test_category_creation(self):
        # Create a Category instance using the factory
        category = CategoryFactory.create(name="Test Category")

        # Check that the Category was created correctly
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, "Test Category")

    def test_category_string_representation(self):
        # Create a Category instance using the factory
        category = CategoryFactory.create(name="Test Category")

        # Check the string representation of the Category
        self.assertEqual(str(category), "Test Category")

    def test_category_name_max_length(self):
        # Create a valid category with name length exactly 100 characters
        category = CategoryFactory.create(name="A" * 100)
        self.assertEqual(category.name, "A" * 100)

        # Check that creating a category with a name longer than 100 characters raises an error
        with self.assertRaises(Exception):
            CategoryFactory.create(name="A" * 101)
