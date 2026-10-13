import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "resources.json"


def analyze_resources(resources):
    total_cost = sum(float(resource["monthly_cost"]) for resource in resources)
    findings = []

    for resource in resources:
        cost = float(resource["monthly_cost"])
        cpu = float(resource["cpu_utilization"])
        name = resource["name"]
        environment = resource["environment"]
        resource_type = resource["type"]

        if resource_type == "EBS" and not resource["running"]:
            findings.append({
                "resource": name,
                "monthly_cost": cost,
                "recommendation": (
                    "Verify whether this volume is unattached or unnecessary. "
                    "Check snapshots and retention requirements before deletion."
                ),
            })
        elif (
            resource_type == "EC2"
            and environment != "production"
            and cpu < 10
            and resource["running"]
        ):
            findings.append({
                "resource": name,
                "monthly_cost": cost,
                "recommendation": (
                    "Review workload and usage. Consider rightsizing, "
                    "scheduling shutdowns when appropriate, or removing "
                    "the resource if its owner confirms it is unnecessary."
                ),
            })

    potential_monthly_savings = sum(
        finding["monthly_cost"] for finding in findings
    )

    return {
        "resource_count": len(resources),
        "total_monthly_cost": round(total_cost, 2),
        "findings": findings,
        "potential_monthly_savings": round(potential_monthly_savings, 2),
    }


def main():
    resources = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    report = analyze_resources(resources)

    print("=== DevOps Cost Optimization Report ===")
    print(f"Resources analyzed: {report['resource_count']}")
    print(f"Total monthly cost: ${report['total_monthly_cost']:.2f}")
    print(f"Resources to investigate: {len(report['findings'])}")
    print(
        "Estimated monthly cost under review: "
        f"${report['potential_monthly_savings']:.2f}"
    )

    for finding in report["findings"]:
        print(f"\nResource: {finding['resource']}")
        print(f"Monthly cost: ${finding['monthly_cost']:.2f}")
        print(f"Recommendation: {finding['recommendation']}")

    print("\nSafety: estimates are not guaranteed savings.")
    print("Verify usage, dependencies, and owner approval before changes.")


if __name__ == "__main__":
    main()
