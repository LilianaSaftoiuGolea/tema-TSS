import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from linear_search import linear_search


class TestWhiteBoxStatementCoverage(unittest.TestCase):
    """Teste white-box pentru statement coverage."""

    def test_sc_raise_value_error(self):
        with self.assertRaises(ValueError):
            linear_search([], 1)

    def test_sc_return_index(self):
        self.assertEqual(linear_search([7, 8, 9, 10, 11], 9), 2)

    def test_sc_return_minus_one(self):
        self.assertEqual(linear_search([7, 8, 9, 10, 11], 99), -1)


class TestWhiteBoxDecisionConditionCoverage(unittest.TestCase):
    """Teste white-box pentru decision coverage și condition coverage."""

    def test_dc_len_true(self):
        with self.assertRaises(ValueError):
            linear_search([1, 2, 3, 4], 1)

    def test_dc_element_equal_key_true(self):
        self.assertEqual(linear_search([4, 5, 6, 7, 8], 6), 2)

    def test_dc_element_equal_key_false(self):
        self.assertEqual(linear_search([4, 5, 6, 7, 8], 99), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
