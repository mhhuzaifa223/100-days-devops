import unittest

import devops_server


class DevOpsServerTests(unittest.TestCase):
    def test_disk_usage_fields(self):
        result = devops_server.get_disk_usage("/")
        for field in (
            "path", "total_gb", "used_gb", "free_gb", "used_percent"
        ):
            self.assertIn(field, result)

        self.assertEqual(result["path"], "/")
        self.assertGreater(result["total_gb"], 0)
        self.assertGreaterEqual(result["used_percent"], 0)
        self.assertLessEqual(result["used_percent"], 100)

    def test_system_status(self):
        result = devops_server.get_system_status()
        self.assertEqual(result["status"], "ok")
        self.assertIn("timestamp_utc", result)
        self.assertIn("uptime_seconds", result)
        self.assertIn("disk", result)

    def test_registered_tools(self):
        self.assertIn("get_system_status", devops_server.TOOLS)
        self.assertIn("get_disk_usage", devops_server.TOOLS)


if __name__ == "__main__":
    unittest.main()
