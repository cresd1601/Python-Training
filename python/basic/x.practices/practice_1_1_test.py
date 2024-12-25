import unittest
from unittest.mock import mock_open, patch
from practice_1_1 import find_long_words

class TestFindLongWords(unittest.TestCase):

    @patch("pathlib.Path.open", new_callable=mock_open,
           read_data="short\nthisisaverylongwordindeed\nanotherlongwordbuthasspaces\nnormalword")
    def test_find_long_words(self, mock_file):
        result = find_long_words('dummy-file.txt')
        self.assertEqual(result, ["thisisaverylongwordindeed", "anotherlongwordbuthasspaces"])

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="short\nword\n")
    def test_find_long_words_no_long_words(self, mock_file):
        result = find_long_words('dummy-file.txt')
        self.assertEqual(result, [])

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="")
    def test_find_long_words_empty_file(self, mock_file):
        result = find_long_words('dummy-file.txt')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
