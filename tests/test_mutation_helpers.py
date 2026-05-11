import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from linear_search import linear_search


class TestAdditionalForMutation(unittest.TestCase):
    """Teste suplimentare utile pentru mutation testing."""

    def test_mutatie_eq_to_gte(self):
        self.assertEqual(linear_search([10, 30, 25, 0, -1], 25), 2)

    def test_mutatie_eq_to_is(self):
        key = int("1000")
        v = [1, 2, int("1000"), 3, 4]
        self.assertEqual(linear_search(v, key), 2)

    def test_mutatie_duplicate_prima_aparitie(self):
        self.assertEqual(linear_search([7, 7, 7, 8, 9], 7), 0)

    def test_mutatie_gasire_pe_penultima_pozitie(self):
        self.assertEqual(linear_search([10, 20, 30, 40, 50], 40), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
