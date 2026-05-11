import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from linear_search import linear_search


class TestBlackBoxEquivalence(unittest.TestCase):
    """Teste black-box prin partiționare în clase de echivalență."""

    def test_bb_key_prezent(self):
        self.assertEqual(linear_search([10, 20, 30, 40, 50], 30), 2)

    def test_bb_key_absent(self):
        self.assertEqual(linear_search([10, 20, 30, 40, 50], 99), -1)

    def test_bb_valori_negative(self):
        self.assertEqual(linear_search([-5, -3, -1, 0, 2], -1), 2)

    def test_bb_lungime_sub_5(self):
        with self.assertRaises(ValueError):
            linear_search([1, 2, 3, 4], 2)

    def test_bb_lungime_peste_5(self):
        with self.assertRaises(ValueError):
            linear_search([1, 2, 3, 4, 5, 6], 2)


class TestBlackBoxBoundary(unittest.TestCase):
    """Teste black-box prin analiza valorilor de frontieră."""

    def test_bva_prima_pozitie(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)

    def test_bva_pozitia_din_mijloc(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)

    def test_bva_ultima_pozitie(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 5), 4)

    def test_bva_lungime_4(self):
        with self.assertRaises(ValueError):
            linear_search([1, 2, 3, 4], 1)

    def test_bva_lungime_6(self):
        with self.assertRaises(ValueError):
            linear_search([1, 2, 3, 4, 5, 6], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
