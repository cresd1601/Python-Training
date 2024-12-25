import unittest
from practice_1_9 import isReversible, findReversibleAges

class TestReversibleAges(unittest.TestCase):
    def test_isReversible(self):
        # Test cases for isReversible function
        self.assertTrue(isReversible(12, 21))  # "12" reversed is "21"
        self.assertTrue(isReversible(7, 70))  # "07" reversed is "70" (zfill ensures two digits)
        self.assertTrue(isReversible(13, 31))  # "13" reversed is "31"
        self.assertTrue(isReversible(18, 81))  # "18" reversed is "81" (adjusted expectation)

    def test_findReversibleAges(self):
        # Test the findReversibleAges function
        valid_ages = findReversibleAges()

        # Check if some known valid reversible pairs are present
        expected_ages = [
            (13, 31),  # Example reversible pair
            (15, 51),  # Another example
        ]

        # Check if the expected reversible ages are in the results
        for child_age, mom_age in expected_ages:
            self.assertIn((child_age, mom_age), valid_ages)

        # Optionally check for the length of valid ages
        self.assertGreater(len(valid_ages), 0)  # Ensure the list is not empty

if __name__ == "__main__":
    unittest.main()
