# Sample Unit Test

import unittest 
from main import highest_duplicate_number


# unittest in an inbuilt module in Python that provides a rich set of tools for constructing and running tests.

class TestHighestDuplicateNumber(unittest.TestCase):
    
    def test_duplicate_number(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 16, 16]
        self.assertEqual(highest_duplicate_number(arr), 16)
        
    def test_no_duplicate(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(highest_duplicate_number(arr), -1)
        
    def test_empty_array(self):
        arr = []
        self.assertEqual(highest_duplicate_number(arr), -1)
        
if __name__ == '__main__':
    unittest.main()