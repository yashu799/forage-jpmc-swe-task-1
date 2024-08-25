import unittest
from client3 import getDataPoint, getRatio

class TestClientFunctions(unittest.TestCase):

    def test_getDataPoint(self):
        # Sample data
        quotes = [
            {'stock': 'ABC', 'top_bid': {'price': '100'}, 'top_ask': {'price': '105'}},
            {'stock': 'DEF', 'top_bid': {'price': '200'}, 'top_ask': {'price': '195'}}
        ]
        # Expected results for the above data
        expected_data_points = [
            ('ABC', 100.0, 105.0, 100.0),
            ('DEF', 200.0, 195.0, 200.0)
        ]
        # Test each quote
        for quote, expected in zip(quotes, expected_data_points):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getRatio(self):
        # Test cases for getRatio
        self.assertEqual(getRatio(100, 50), 2.0)
        self.assertEqual(getRatio(0, 50), 0)
        self.assertEqual(getRatio(100, 0), float('inf'))

if __name__ == '__main__':
    unittest.main()
