import unittest
from unittest.mock import mock_open, patch
from collections import defaultdict
from pathlib import Path
from practice_2_3 import clean_word, process_file, skip_gutenberg_header, print_word_stats

class TestGutenbergProcessing(unittest.TestCase):
    def test_clean_word(self):
        """Test the clean_word function."""
        self.assertEqual(clean_word("Hello!"), "hello")
        self.assertEqual(clean_word("It's"), "its")
        self.assertEqual(clean_word("123number"), "123number")  # Now it should retain '123'
        self.assertEqual(clean_word("...word..."), "word")
        self.assertEqual(clean_word(""), "")
        self.assertEqual(clean_word("!!!"), "")

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="*** START OF THE PROJECT GUTENBERG EBOOK\nword1\nword2\n*** END OF THIS PROJECT GUTENBERG EBOOK")
    def test_process_file(self, mock_file):
        """Test the process_file function with a mock file."""
        total_words, word_count = process_file(Path("dummy_path"))

        # Check the results
        self.assertEqual(total_words, 2)
        self.assertEqual(word_count, defaultdict(int, {'word1': 1, 'word2': 1}))

    @patch("builtins.print")  # Mock print to capture output
    def test_print_word_stats(self, mock_print):
        """Test the print_word_stats function to ensure proper output."""
        word_count = defaultdict(int, {"apple": 3, "banana": 1, "cherry": 2})
        total_words = 6

        # Call the function
        print_word_stats(total_words, word_count, top_n=2)

        # Capture print calls
        mock_print.assert_any_call("Total number of words: 6")
        mock_print.assert_any_call("Number of different words: 3")
        mock_print.assert_any_call("\nTop 2 most common words:")
        mock_print.assert_any_call("apple: 3")
        mock_print.assert_any_call("cherry: 2")

if __name__ == '__main__':
    unittest.main()