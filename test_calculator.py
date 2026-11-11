import unittest

from calculator import add


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_addition_with_negative(self):
        self.assertEqual(add(-3, 2), -1)


if __name__ == "__main__":
    unittest.main()
