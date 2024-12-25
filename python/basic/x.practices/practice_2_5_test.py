import unittest
from practice_2_5 import histogram, choose_from_hist  # Replace 'your_module' with the actual module name

class TestHistogramFunctions(unittest.TestCase):

    def test_histogram(self):
        """Test that the histogram function returns correct frequencies."""
        data = ['a', 'a', 'b', 'c', 'c', 'c']
        expected_hist = {'a': 2, 'b': 1, 'c': 3}
        self.assertEqual(histogram(data), expected_hist)

        # Test with an empty list
        self.assertEqual(histogram([]), {})

        # Test with a list of one element
        self.assertEqual(histogram(['a']), {'a': 1})

    def test_choose_from_hist(self):
        """Test that choose_from_hist returns values based on their frequency."""
        data = ['a', 'a', 'b']
        hist = histogram(data)

        # Run multiple trials to see if the selection follows the expected frequencies
        trials = 10000
        results = {'a': 0, 'b': 0}

        # Mock random.choice to ensure deterministic testing (optional)
        for _ in range(trials):
            chosen = choose_from_hist(hist)
            results[chosen] += 1

        # Check if 'a' is chosen roughly 2/3 of the time and 'b' 1/3
        self.assertAlmostEqual(results['a'] / trials, 2 / 3, delta=0.05)
        self.assertAlmostEqual(results['b'] / trials, 1 / 3, delta=0.05)

if __name__ == '__main__':
    unittest.main()