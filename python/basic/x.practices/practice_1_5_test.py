import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_1_5 import usesAll, countWordsUsingOnlyAllowedLetters

class TestAllowedLetters(unittest.TestCase):
    def test_usesAll(self):
        # Test cases for usesAll function
        self.assertTrue(usesAll("hello", "helo"))  # "hello" contains all letters of "helo"
        self.assertFalse(usesAll("world", "helo"))  # "world" does not contain all letters of "helo"
        self.assertTrue(usesAll("aaa", "a"))  # "aaa" contains all letters of "a"
        self.assertFalse(usesAll("abc", "ab"))  # "abc" contains extra letter "c"

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="hello\nworld\ntest\nallowed\n")
    def test_countWordsUsingOnlyAllowedLetters(self, mock_file):
        # Create a mock Path object
        filePath = Path("dummy_path")

        # Test case where only some words use the allowed letters
        allowedLetters = "helo"
        wordsWithAllowedLetters, totalWords = countWordsUsingOnlyAllowedLetters(allowedLetters)
        self.assertEqual(wordsWithAllowedLetters, 1)  # Only "hello" matches
        self.assertEqual(totalWords, 4)               # 4 total words in mock file

        # Test case where none of the words use the allowed letters
        allowedLetters = "xyz"
        wordsWithAllowedLetters, totalWords = countWordsUsingOnlyAllowedLetters(allowedLetters)
        self.assertEqual(wordsWithAllowedLetters, 0)  # None of the words match
        self.assertEqual(totalWords, 4)

        # Test case where two words should match
        allowedLetters = "hellowrdt"
        wordsWithAllowedLetters, totalWords = countWordsUsingOnlyAllowedLetters(allowedLetters)

        # Check the results
        self.assertEqual(wordsWithAllowedLetters, 2)  # Only "hello" and "world" match
        self.assertEqual(totalWords, 4)

if __name__ == "__main__":
    unittest.main()