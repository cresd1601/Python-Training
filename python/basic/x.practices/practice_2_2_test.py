import unittest
from unittest.mock import mock_open, patch
from collections import defaultdict
from pathlib import Path
from practice_2_2 import clean_word, skip_gutenberg_header, process_file, print_word_stats

class TestGutenbergProcessing(unittest.TestCase):
    def test_clean_word(self):
        """Test the clean_word function."""
        self.assertEqual(clean_word("Hello!"), "hello")
        self.assertEqual(clean_word("It's"), "its")
        self.assertEqual(clean_word("123number"), "123number")
        self.assertEqual(clean_word("...word..."), "word")
        self.assertEqual(clean_word(""), "")
        self.assertEqual(clean_word("!!!"), "")

    @patch("builtins.open", new_callable=mock_open,
           read_data="Some text\n*** START OF THE PROJECT GUTENBERG EBOOK\nContent after header\n")
    def test_skip_gutenberg_header(self, mock_file):
        """Test the skip_gutenberg_header function."""
        with mock_file() as file:
            skip_gutenberg_header(file)
            remaining_lines = list(file)  # After skipping, we read remaining lines
            self.assertEqual(remaining_lines, ['Content after header\n'])  # Expect newline

    @patch("pathlib.Path.open", new_callable=mock_open,
           read_data="*** START OF THE PROJECT GUTENBERG EBOOK\nword1\nword2\n")
    def test_process_file(self, mock_file):
        """Test the process_file function with a mock file."""
        total_words, word_count = process_file(Path("dummy_path"))  # Pass a Path object

        print(f"Test process_file: total_words={total_words}, word_count={word_count}")  # Debugging output
        self.assertEqual(total_words, 2)
        self.assertEqual(word_count, defaultdict(int, {"word1": 1, "word2": 1}))

    @patch("builtins.print")  # Mocking print to capture output
    def test_print_word_stats(self, mock_print):
        """Test the print_word_stats function to ensure proper output."""
        word_count = defaultdict(int, {"apple": 3, "banana": 1, "cherry": 2})
        total_words = 6

        # Call the function
        print_word_stats(total_words, word_count, top_n=2)

        # Capture print calls
        mock_print.assert_any_call("Total number of words: 6")
        mock_print.assert_any_call("Number of different words: 3")
        mock_print.assert_any_call("\nMost common words:")  # Adjusted for expected newline
        mock_print.assert_any_call("apple: 3")
        mock_print.assert_any_call("cherry: 2")

if __name__ == '__main__':
    unittest.main()