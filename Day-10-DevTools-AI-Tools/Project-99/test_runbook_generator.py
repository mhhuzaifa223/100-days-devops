import subprocess
import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCRIPT = BASE_DIR / "runbook_generator.py"
RUNBOOK = BASE_DIR / "generated_runbook.md"


class TestRunbookGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        cls.content = RUNBOOK.read_text(encoding="utf-8")

    def test_runbook_is_generated(self):
        self.assertTrue(RUNBOOK.exists())

    def test_detects_api_incident(self):
        self.assertIn("HTTP 503", self.content)
        self.assertIn("API health check failed", self.content)

    def test_detects_high_cpu(self):
        self.assertIn("High CPU utilization", self.content)

    def test_contains_investigation_and_recovery(self):
        self.assertIn("Investigation Steps", self.content)
        self.assertIn("Recovery Verification", self.content)

    def test_contains_escalation_and_safety_guidance(self):
        self.assertIn("Escalation", self.content)
        self.assertIn("Safety Notes", self.content)
        self.assertIn("without authorization", self.content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
