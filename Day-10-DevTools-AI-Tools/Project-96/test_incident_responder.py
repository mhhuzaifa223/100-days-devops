import subprocess
import sys
import unittest


class IncidentResponderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        result = subprocess.run(
            [sys.executable, "incident_responder.py"],
            capture_output=True,
            text=True,
            check=True,
        )
        cls.output = result.stdout

    def test_incident_detected(self):
        self.assertIn("API availability failure", self.output)
        self.assertIn("Severity: HIGH", self.output)

    def test_diagnostic_actions_present(self):
        self.assertIn("Check application logs", self.output)
        self.assertIn("Verify API and dependency health", self.output)
        self.assertIn("Check recent deployments", self.output)

    def test_no_automatic_changes(self):
        self.assertIn("No services were restarted", self.output)


if __name__ == "__main__":
    unittest.main()
