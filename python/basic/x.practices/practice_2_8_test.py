import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from practice_2_8 import read_file, markov_analysis  # Replace 'your_module' with the actual module name

class TestMarkovAnalysis(unittest.TestCase):

    @patch("pathlib.Path.open", new_callable=mock_open, read_data="the quick brown fox jumps over the lazy dog")
    def test_read_file(self, mock_file):
        """Test reading a file and splitting it into words."""
        file_path = Path("dummy_path")
        words = read_file(file_path)
        expected_words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        self.assertEqual(words, expected_words)

    def test_markov_analysis(self):
        """Test Markov analysis function to generate a dictionary of prefixes to suffixes."""
        words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        prefix_length = 2
        markov_dict = markov_analysis(words, prefix_length)

        expected_markov_dict = {
            ("the", "quick"): ["brown"],
            ("quick", "brown"): ["fox"],
            ("brown", "fox"): ["jumps"],
            ("fox", "jumps"): ["over"],
            ("jumps", "over"): ["the"],
            ("over", "the"): ["lazy"],
            ("the", "lazy"): ["dog"]
        }

        self.assertEqual(markov_dict, expected_markov_dict)

if __name__ == '__main__':
    unittest.main()