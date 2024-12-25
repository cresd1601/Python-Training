import unittest
from practice_1_8 import isPalindrome, findOdometerReading

class TestOdometerPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        # Test cases for isPalindrome function
        self.assertTrue(isPalindrome(121))  # Palindromic number
        self.assertTrue(isPalindrome("1221"))  # Palindromic string
        self.assertFalse(isPalindrome(123))  # Not a palindrome
        self.assertFalse(isPalindrome("1234"))  # Not a palindrome
        self.assertTrue(isPalindrome(1))  # Single digit is always a palindrome

    def test_findOdometerReading(self):
        # Test the actual findOdometerReading function
        odometer_reading = findOdometerReading()
        # Assert the correct value returned by the function. The correct value is known to be 198888.
        self.assertEqual(odometer_reading, 198888)

if __name__ == "__main__":
    unittest.main()
