import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_2_7 import load_book_words, choose_random_word  # Replace 'your_module' with the actual module name

class TestWordSelection(unittest.TestCase):

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="Hello, world! This is a test.")
    def test_load_book_words(self, mock_file):
        """Test loading and cleaning words from a book."""
        file_path = Path("dummy_path")
        words = load_book_words(file_path)
        expected_words = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(words, expected_words)

    @patch("random.choice")
    def test_choose_random_word(self, mock_random_choice):
        """Test choosing a random word from the list of words."""
        words = ["apple", "banana", "cherry"]
        mock_random_choice.return_value = "banana"

        # Call the function and check the random word
        chosen_word = choose_random_word(words)
        self.assertEqual(chosen_word, "banana")

        # Ensure that random.choice was called with the correct argument
        mock_random_choice.assert_called_once_with(words)

if __name__ == '__main__':
    unittest.main()