from django.test import TestCase
from apps.feeds.models import Category
from apps.feeds.serializers import CategorySerializer


class CategorySerializerTest(TestCase):
    def setUp(self):
        # Create a category instance to use for tests
        self.category = Category.objects.create(name='Test Category')

    def test_valid_category_serialization(self):
        # Prepare valid data for the serializer
        valid_data = {
            'name': 'New Category'
        }
        serializer = CategorySerializer(data=valid_data)

        # Check that the serializer is valid
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'New Category')

    def test_duplicate_category_name_validation(self):
        # Prepare data that duplicates the existing category name
        duplicate_data = {
            'name': 'Test Category'  # This should raise a validation error
        }
        serializer = CategorySerializer(data=duplicate_data)

        # Check that the serializer is not valid
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertEqual(
            serializer.errors['name'][0],
            "Category with this name already exists."
        )

    def test_empty_category_name_validation(self):
        # Prepare data with an empty category name
        empty_data = {
            'name': ''
        }
        serializer = CategorySerializer(data=empty_data)

        # Check that the serializer is not valid
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertEqual(serializer.errors['name'][0], "This field may not be blank.")
