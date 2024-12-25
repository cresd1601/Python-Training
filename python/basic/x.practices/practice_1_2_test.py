import unittest
from unittest.mock import mock_open, patch
from practice_1_2 import hasNoE, printWordsWithoutE

class TestWordsWithoutE(unittest.TestCase):
    def test_has_no_e(self):
        # Test words with and without 'e'
        self.assertTrue(hasNoE("sky"))
        self.assertFalse(hasNoE("elephant"))
        self.assertTrue(hasNoE("gym"))
        self.assertFalse(hasNoE("tree"))

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="apple\nsky\ntree\ngym\nballoon")
    @patch("builtins.print")  # Mock print to capture the output
    def test_print_words_without_e(self, mock_print, mock_file):
        # Call the function
        printWordsWithoutE()

        # Get the actual calls to print
        print_calls = [call.args[0] for call in mock_print.call_args_list]

        # Check the print calls based on the actual data provided
        self.assertIn("Number of words without 'e': 3", print_calls)
        self.assertIn("Percentage of words without 'e': 60.00%", print_calls)

if __name__ == '__main__':
    unittest.main()
