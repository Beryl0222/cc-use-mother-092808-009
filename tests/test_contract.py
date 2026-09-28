import json
import unittest
from pathlib import Path

from q009_contract.contract import validate_event


class ContractTest(unittest.TestCase):
    def test_example_is_valid(self):
        path = Path(__file__).parents[1] / "fixtures" / "event.json"
        self.assertEqual(validate_event(json.loads(path.read_text(encoding="utf-8"))), [])

    def test_timezone_is_required(self):
        value = json.loads((Path(__file__).parents[1] / "fixtures" / "event.json").read_text(encoding="utf-8"))
        value["occurred_at"] = "2026-09-28T10:00:00"
        self.assertIn("occurred_at 必须带时区", validate_event(value))


if __name__ == "__main__":
    unittest.main()
