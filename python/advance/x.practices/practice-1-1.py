
import unittest
from datetime import datetime

# Stock Class Implementation
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None
    
    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price = price


# Unit Tests for Stock Class
class StockTest(unittest.TestCase):

    def setUp(self):
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 13), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.goog.update(datetime(2014, 2, 13), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)

if __name__ == "__main__":
    unittest.main()
