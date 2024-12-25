import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_1_4 import usesOnly, countWordsUsingOnlyAllowedLetters

class TestOnlyAllowedLetters(unittest.TestCase):
    def test_usesOnly(self):
        # Test cases for usesOnly function
        self.assertTrue(usesOnly("hello", "helo"))
        self.assertFalse(usesOnly("world", "helo"))
        self.assertTrue(usesOnly("aaa", "a"))
        self.assertFalse(usesOnly("abc", "ab"))

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="hello\nworld\ntest\nallowed\n")
    def test_countWordsUsingOnlyAllowedLetters(self, mock_file):
        # Create a mock Path object
        filePath = Path("dummy_path")

        # Test case where only one word uses the allowed letters
        allowedLetters = "helo"
        wordsWithAllowedLetters, totalWords = countWordsUsingOnlyAllowedLetters(filePath, allowedLetters)
        self.assertEqual(wordsWithAllowedLetters, 1)  # Only "hello" matches
        self.assertEqual(totalWords, 4)               # 4 total words in mock file

        # Test case where none of the words use the allowed letters
        allowedLetters = "xyz"
        wordsWithAllowedLetters, totalWords = countWordsUsingOnlyAllowedLetters(filePath, allowedLetters)
        self.assertEqual(wordsWithAllowedLetters, 0)  # None of the words match
        self.assertEqual(totalWords, 4)

        # Test case where only two words use the allowed letters
        allowedLetters = "hellowrdt"
        wordsWithAllowedLetters, totalWords = countWordsUsingOnlyAllowedLetters(filePath, allowedLetters)
        self.assertEqual(wordsWithAllowedLetters, 2)  # Only "hello" and "world" match

# Run the tests
if __name__ == "__main__":
    unittest.main()
