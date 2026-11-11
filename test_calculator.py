
import unittest

from calculator import add, subtract


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_addition_with_negative(self):
        self.assertEqual(add(-3, 2), -1)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtraction_with_negative(self):
        self.assertEqual(subtract(-3, 2), -5)

    def test_subtraction_with_zero(self):
        self.assertEqual(subtract(10, 0), 10)


if __name__ == "__main__":
    unittest.main()
