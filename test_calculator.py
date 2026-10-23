
import unittest
from calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_invalid_zero_input(self):
        with self.assertRaises(ValueError):
            add(0, 5)

    def test_invalid_negative_input(self):
        with self.assertRaises(ValueError):
            multiply(-2, 5)

    def test_invalid_decimal_input(self):
        with self.assertRaises(TypeError):
            add(2.5, 5)


if __name__ == "__main__":
    unittest.main()
