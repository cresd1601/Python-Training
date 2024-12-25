import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_2_6 import load_words, load_book, find_unknown_words  # Replace 'your_module' with the actual module name

class TestWordProcessing(unittest.TestCase):

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="apple\nbanana\ncherry\n")
    def test_load_words(self, mock_file):
        """Test loading words from a file."""
        file_path = Path("dummy_path")
        words = load_words(file_path)
        expected_words = {"apple", "banana", "cherry"}
        self.assertEqual(words, expected_words)

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="Hello, world! This is a test.")
    def test_load_book(self, mock_file):
        """Test loading and cleaning words from a book."""
        file_path = Path("dummy_path")
        words = load_book(file_path)
        expected_words = {"hello", "world", "this", "is", "a", "test"}
        self.assertEqual(words, expected_words)

    def test_find_unknown_words(self):
        """Test finding unknown words in the book."""
        book_words = {"hello", "world", "python", "programming"}
        word_list = {"hello", "world"}
        unknown_words = find_unknown_words(book_words, word_list)
        expected_unknown_words = {"python", "programming"}
        self.assertEqual(unknown_words, expected_unknown_words)

if __name__ == '__main__':
    unittest.main()