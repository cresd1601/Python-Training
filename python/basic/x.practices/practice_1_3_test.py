import unittest
from unittest.mock import mock_open, patch
from practice_1_3 import avoids, countWordsWithoutForbiddenLetter

class TestAvoids(unittest.TestCase):
    def test_avoids(self):
        # Test the avoids function
        self.assertTrue(avoids("apple", "xyz"))  # "apple" doesn't have 'x', 'y', or 'z'
        self.assertFalse(avoids("apple", "ae"))  # "apple" contains 'a' and 'e'
        self.assertTrue(avoids("sky", "e"))      # "sky" doesn't have 'e'
        self.assertFalse(avoids("tree", "r"))    # "tree" contains 'r'

    @patch("builtins.input", return_value="ae")  # Mock input to simulate forbidden letters input
    @patch("pathlib.Path.open", new_callable=mock_open, read_data="apple\nsky\ntree\ngym\nballoon")
    @patch("builtins.print")  # Mock print to capture the output
    def test_count_words_without_forbidden_letter(self, mock_print, mock_file, mock_input):
        # Call the function
        countWordsWithoutForbiddenLetter("ae")

        # Check the print calls
        mock_print.assert_any_call("Number of words without forbidden letters: 2")
        mock_print.assert_any_call("Total number of words: 5")

if __name__ == '__main__':
    unittest.main()
