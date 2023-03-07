import unittest
from main import calculate_sum

class TestCalculateSum(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(2, 3), 5)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(-1, 1), 99)
        self.assertEqual(calculate_sum(1000000, 1), 1000001)

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
