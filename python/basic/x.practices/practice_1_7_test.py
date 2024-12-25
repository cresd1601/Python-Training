import unittest
from practice_1_7 import hasThreeConsecutiveDoubleLetters, findWordWithThreeDoubleLetters

class TestConsecutiveDoubleLetters(unittest.TestCase):
    def test_hasThreeConsecutiveDoubleLetters(self):
        # Test cases for hasThreeConsecutiveDoubleLetters function
        self.assertTrue(
            hasThreeConsecutiveDoubleLetters("bookkeeper"))  # "ookkee" contains three consecutive double letters
        self.assertTrue(
            hasThreeConsecutiveDoubleLetters("subbookkeeper"))  # "ookkee" contains three consecutive double letters
        self.assertFalse(hasThreeConsecutiveDoubleLetters("committee"))  # "tt" but no three consecutive double letters
        self.assertFalse(hasThreeConsecutiveDoubleLetters("hello"))  # No double letters
        self.assertFalse(
            hasThreeConsecutiveDoubleLetters("Mississippi"))  # Only two consecutive double letters, not three

    def test_findWordWithThreeDoubleLetters(self):
        # Test cases for findWordWithThreeDoubleLetters function
        words = ["committee", "bookkeeper", "Mississippi", "subbookkeeper"]

        # Find word with three consecutive double letters
        self.assertEqual(findWordWithThreeDoubleLetters(words), "bookkeeper")  # First match is "bookkeeper"

        # Test when no word has three consecutive double letters
        words_without_match = ["hello", "committee", "apple"]
        self.assertIsNone(findWordWithThreeDoubleLetters(words_without_match))  # No word should match

if __name__ == "__main__":
    unittest.main()
