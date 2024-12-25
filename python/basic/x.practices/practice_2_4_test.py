import unittest
from unittest.mock import mock_open, patch
from collections import defaultdict
from pathlib import Path
from practice_2_4 import clean_word, load_word_list, process_file, categorize_unknown_words, print_categorized_word_stats


class TestGutenbergProcessing(unittest.TestCase):

    def test_clean_word(self):
        """Test the clean_word function."""
        self.assertEqual(clean_word("Hello!"), "hello")
        self.assertEqual(clean_word("It's"), "its")
        self.assertEqual(clean_word("123number"), "number")  # As clean_word removes numbers
        self.assertEqual(clean_word("...word..."), "word")
        self.assertEqual(clean_word(""), "")
        self.assertEqual(clean_word("!!!"), "")

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="apple\nbanana\ncherry\n")
    def test_load_word_list(self, mock_file):
        """Test loading a word list from a file."""
        word_list = load_word_list(Path("dummy_path"))
        expected_word_list = {"apple", "banana", "cherry"}
        self.assertEqual(word_list, expected_word_list)

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="*** START OF THE PROJECT GUTENBERG EBOOK\nword1\nword2\n")
    def test_process_file(self, mock_file):
        """Test the process_file function with a mock file."""
        word_list = {"word1"}
        word_count, unknown_words = process_file(Path("dummy_path"), word_list)

        # Since clean_word removes numbers, 'word1' and 'word2' are both treated as 'word'
        expected_word_count = defaultdict(int, {"word": 2})
        expected_unknown_words = {"word"}

        self.assertEqual(word_count, expected_word_count)
        self.assertEqual(unknown_words, expected_unknown_words)

    def test_categorize_unknown_words(self):
        """Test categorizing unknown words into typos, common words, and obscure words."""
        unknown_words = {"the", "of", "obscureword", "a", "b"}
        word_list = {"the", "of"}

        typos, common_words, obscure_words = categorize_unknown_words(unknown_words, word_list)

        expected_typos = {"a", "b"}  # 'of' is not a typo, because it is in the word list
        expected_common_words = {"the", "of"}
        expected_obscure_words = {"obscureword"}

        # Assert the categorization
        self.assertEqual(typos, expected_typos)
        self.assertEqual(common_words, expected_common_words)
        self.assertEqual(obscure_words, expected_obscure_words)

    @patch("builtins.print")
    def test_print_categorized_word_stats(self, mock_print):
        """Test the output of print_categorized_word_stats."""
        typos = {"a", "b"}
        common_words = {"the", "of"}
        obscure_words = {"obscureword"}

        # Call the function to check printed output
        print_categorized_word_stats(typos, common_words, obscure_words)

        # Assert the print calls
        mock_print.assert_any_call("\nNumber of typos: 2")
        mock_print.assert_any_call(f"Number of common words that should be in the word list: {len(common_words)}")
        mock_print.assert_any_call(f"Number of obscure words: {len(obscure_words)}")
        mock_print.assert_any_call("\nSample typos:")
        mock_print.assert_any_call("a")
        mock_print.assert_any_call("b")
        mock_print.assert_any_call("\nSample common words:")
        mock_print.assert_any_call("of")
        mock_print.assert_any_call("the")
        mock_print.assert_any_call("\nSample obscure words:")
        mock_print.assert_any_call("obscureword")


if __name__ == '__main__':
    unittest.main()