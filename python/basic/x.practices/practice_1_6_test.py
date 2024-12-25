import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_1_6 import isAbecedarian, countAbecedarianWords

class TestAbecedarian(unittest.TestCase):
    def test_isAbecedarian(self):
        # Test cases for isAbecedarian function
        self.assertTrue(isAbecedarian("abc"))  # Letters are in alphabetical order
        self.assertFalse(isAbecedarian("cba"))  # Letters are not in alphabetical order
        self.assertTrue(isAbecedarian("a"))  # Single letter is always abecedarian
        self.assertTrue(isAbecedarian("abcdefg"))  # Alphabetically ordered
        self.assertFalse(isAbecedarian("apple"))  # Not ordered alphabetically

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="abc\nxyz\nbac\nhello\n")
    def test_countAbecedarianWords(self, mock_file):
        # Mock Path and file contents
        filePath = Path("dummy_path")

        # Capture print statements
        with patch('builtins.print') as mocked_print:
            countAbecedarianWords()

            # Test case: 2 abecedarian words ("abc" and "xyz")
            mocked_print.assert_any_call("Number of abecedarian words: 2")
            mocked_print.assert_any_call("Total number of words: 4")

if __name__ == "__main__":
    unittest.main()
