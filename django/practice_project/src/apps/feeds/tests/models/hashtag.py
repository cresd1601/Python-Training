from django.test import TestCase
from apps.feeds.factories import HashtagFactory


class HashtagModelTests(TestCase):
    def test_create_hashtag(self):
        # Create a new hashtag using the factory
        hashtag = HashtagFactory.create(name="Django")

        # Check that the hashtag was created correctly
        self.assertEqual(hashtag.name, "Django")
        self.assertEqual(str(hashtag), "Django")

    def test_unique_hashtag_name(self):
        # Create the first hashtag with a specific name using the factory
        HashtagFactory.create(name="Python")

        # Try to create another hashtag with the same name and check for uniqueness constraint
        with self.assertRaises(Exception) as context:
            HashtagFactory.create(name="Python")

        self.assertTrue("unique constraint" in str(context.exception).lower())
