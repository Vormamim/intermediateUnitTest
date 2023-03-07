import unittest
import os

class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file("test.txt"), "Hello, world!")

        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent.txt")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None

if __name__ == '__main__':
    unittest.main()
