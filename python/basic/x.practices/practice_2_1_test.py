import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_2_1 import process_file

class TestProcessWords(unittest.TestCase):
    @patch("pathlib.Path.open", new_callable=mock_open, read_data="Hello, world! This is a test.")
    def test_process_file(self, mock_file):
        file_path = Path("dummy_path")

        # Expected processed words
        expected_words = ["hello", "world", "this", "is", "a", "test"]

        # Call the function and get the result
        processed_words = process_file(file_path)

        # Check if the processed words match the expected result
        self.assertEqual(processed_words, expected_words)

if __name__ == "__main__":
    unittest.main()
