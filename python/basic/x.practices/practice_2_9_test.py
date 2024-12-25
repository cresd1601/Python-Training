import unittest
from collections import Counter
from practice_2_9 import read_file, count_word_frequencies, calculate_log_values  # Replace 'your_module' with the actual module name
from unittest.mock import mock_open, patch
from pathlib import Path
import math

class TestZipfAnalysis(unittest.TestCase):
    @patch("pathlib.Path.open", new_callable=mock_open, read_data="The quick brown fox jumps over the lazy dog")
    def test_read_file(self, mock_file):
        """Test reading and splitting text from file."""
        file_path = Path("dummy_path")
        words = read_file(file_path)
        expected_words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
        self.assertEqual(words, expected_words)

    def test_count_word_frequencies(self):
        """Test counting word frequencies."""
        words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'the']
        word_freq = count_word_frequencies(words)
        expected_word_freq = Counter({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
        self.assertEqual(word_freq, expected_word_freq)

    def test_calculate_log_values(self):
        """Test calculation of log(frequency) and log(rank)."""
        word_freq = {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1}
        log_f, log_r = calculate_log_values(word_freq)

        expected_log_f = [math.log(3), math.log(1), math.log(1), math.log(1), math.log(1)]
        expected_log_r = [math.log(1), math.log(2), math.log(3), math.log(4), math.log(5)]

        self.assertEqual(log_f, expected_log_f)
        self.assertEqual(log_r, expected_log_r)

if __name__ == '__main__':
    unittest.main()