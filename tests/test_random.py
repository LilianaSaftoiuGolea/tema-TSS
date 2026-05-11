from __future__ import annotations

import os
import random
import sys
import unittest
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from linear_search import linear_search
from oracle import oracle_linear_search

SEED = 42
N_RANDOM_TESTS = 1000
VALUE_MIN = -2000
VALUE_MAX = 2000
JOURNAL_FILE = Path(os.environ.get("RANDOM_JOURNAL_FILE", "random_test_journal.txt"))


def _fresh_random_int(rng: random.Random) -> int:
    return int(str(rng.randint(VALUE_MIN, VALUE_MAX)))


def generate_random_case(rng: random.Random) -> Tuple[List[int], int, str]:
    v = [_fresh_random_int(rng) for _ in range(5)]
    mode = rng.choice(["present", "absent", "free"])

    if mode == "present":
        chosen = rng.choice(v)
        key = int(str(chosen))
    elif mode == "absent":
        key = _fresh_random_int(rng)
        while key in v:
            key = _fresh_random_int(rng)
    else:
        key = _fresh_random_int(rng)

    return v, key, mode


def write_journal(summary: Dict[str, int], failures: List[Dict[str, object]]) -> None:
    lines = [
        "Jurnal random testing L4\n",
        f"Seed: {SEED}\n",
        f"Numar cazuri generate: {summary['total']}\n",
        f"Cazuri key prezent: {summary['present']}\n",
        f"Cazuri key absent: {summary['absent']}\n",
        f"Cazuri key liber: {summary['free']}\n",
        f"Numar esecuri: {len(failures)}\n",
        "\n",
    ]

    if not failures:
        lines.append("Nu s-au detectat abateri fata de oracolul independent.\n")
    else:
        lines.append("Detalii esecuri:\n")
        for failure in failures:
            lines.extend(
                [
                    f"Case #{failure['case_id']}\n",
                    f"  mode = {failure['mode']}\n",
                    f"  v = {failure['v']}\n",
                    f"  key = {failure['key']}\n",
                    f"  expected = {failure['expected']}\n",
                    f"  actual = {failure['actual']}\n",
                    f"  violated_assertion = {failure['violated_assertion']}\n",
                    "\n",
                ]
            )

    JOURNAL_FILE.write_text("".join(lines), encoding="utf-8")


class TestRandomGeneratedSuite(unittest.TestCase):
    def test_random_generated_suite(self) -> None:
        rng = random.Random(SEED)
        failures: List[Dict[str, object]] = []
        summary = {"total": N_RANDOM_TESTS, "present": 0, "absent": 0, "free": 0}

        for case_id in range(1, N_RANDOM_TESTS + 1):
            v, key, mode = generate_random_case(rng)
            summary[mode] += 1

            expected = oracle_linear_search(v, key)
            actual = linear_search(v, key)

            if actual != expected:
                failures.append(
                    {
                        "case_id": case_id,
                        "mode": mode,
                        "v": v,
                        "key": key,
                        "expected": expected,
                        "actual": actual,
                        "violated_assertion": "assert actual == expected",
                    }
                )

        write_journal(summary, failures)
        self.assertEqual(
            failures,
            [],
            f"Au fost detectate {len(failures)} esecuri. Verifica {JOURNAL_FILE.name}",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
