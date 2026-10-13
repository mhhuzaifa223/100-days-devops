import unittest

import ops_assistant


class OperationsAssistantTests(unittest.TestCase):
    def test_approved_tasks(self):
        help_result = ops_assistant.run_task("show_help")
        self.assertIn("check_disk", help_result)
        self.assertIn("check_incident", help_result)
        self.assertIn("show_help", help_result)

    def test_disk_status(self):
        result = ops_assistant.run_task("check_disk")
        self.assertIn("used_percent", result)
        self.assertIn("free_gb", result)
        self.assertGreaterEqual(result["used_percent"], 0)
        self.assertLessEqual(result["used_percent"], 100)

    def test_incident_summary(self):
        result = ops_assistant.run_task("check_incident")
        self.assertEqual(result["total_lines"], 4)
        self.assertEqual(len(result["errors"]), 2)
        self.assertEqual(len(result["warnings"]), 1)

    def test_unapproved_task_is_rejected(self):
        result = ops_assistant.run_task("delete_everything")
        self.assertEqual(result["error"], "Task not approved")


if __name__ == "__main__":
    unittest.main()
