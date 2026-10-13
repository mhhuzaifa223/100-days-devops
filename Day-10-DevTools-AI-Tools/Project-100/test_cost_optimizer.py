import json
import tempfile
import unittest
from pathlib import Path

from cost_optimizer import analyze_resources


class TestCostOptimizer(unittest.TestCase):
    def setUp(self):
        self.resources = [
            {
                "name": "dev-test-server",
                "type": "EC2",
                "environment": "development",
                "monthly_cost": 45.00,
                "cpu_utilization": 4,
                "running": True,
                "owner": "development-team",
            },
            {
                "name": "production-api",
                "type": "EC2",
                "environment": "production",
                "monthly_cost": 120.00,
                "cpu_utilization": 55,
                "running": True,
                "owner": "platform-team",
            },
            {
                "name": "unused-test-volume",
                "type": "EBS",
                "environment": "development",
                "monthly_cost": 12.00,
                "cpu_utilization": 0,
                "running": False,
                "owner": "development-team",
            },
            {
                "name": "staging-server",
                "type": "EC2",
                "environment": "staging",
                "monthly_cost": 60.00,
                "cpu_utilization": 8,
                "running": True,
                "owner": "qa-team",
            },
        ]

    def test_total_monthly_cost(self):
        report = analyze_resources(self.resources)
        self.assertEqual(report["total_monthly_cost"], 237.00)

    def test_resource_count(self):
        report = analyze_resources(self.resources)
        self.assertEqual(report["resource_count"], 4)

    def test_identifies_three_resources_for_review(self):
        report = analyze_resources(self.resources)
        names = {item["resource"] for item in report["findings"]}
        self.assertEqual(
            names,
            {"dev-test-server", "unused-test-volume", "staging-server"},
        )

    def test_cost_under_review(self):
        report = analyze_resources(self.resources)
        self.assertEqual(report["potential_monthly_savings"], 117.00)

    def test_production_server_is_not_flagged_by_low_cpu_rule(self):
        report = analyze_resources(self.resources)
        names = {item["resource"] for item in report["findings"]}
        self.assertNotIn("production-api", names)

    def test_empty_inventory(self):
        report = analyze_resources([])
        self.assertEqual(report["resource_count"], 0)
        self.assertEqual(report["total_monthly_cost"], 0.00)
        self.assertEqual(report["potential_monthly_savings"], 0.00)
        self.assertEqual(report["findings"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
