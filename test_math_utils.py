"""Unit tests for math_utils."""

import unittest

from math_utils import add


class AddTests(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 7), 7)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_mixed_int_and_float(self):
        self.assertEqual(add(1, 2.5), 3.5)

    def test_large_numbers(self):
        self.assertEqual(add(10**18, 10**18), 2 * 10**18)


if __name__ == "__main__":
    unittest.main()
