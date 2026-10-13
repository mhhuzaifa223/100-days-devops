from pathlib import Path

log_text = Path("incident.log").read_text(encoding="utf-8")
log_lower = log_text.lower()

incident = {
    "type": "Unknown",
    "severity": "LOW",
    "evidence": [],
    "actions": [],
}

if "health check failed" in log_lower or "503 service unavailable" in log_lower:
    incident["type"] = "API availability failure"
    incident["severity"] = "HIGH"
    incident["evidence"].append("API health check failed or returned HTTP 503.")
    incident["actions"].extend([
        "Check application logs around the failure timestamp.",
        "Verify API and dependency health.",
        "Check recent deployments and configuration changes.",
        "Confirm recovery with a health check before closing the incident.",
    ])

if "cpu utilization reached" in log_lower:
    incident["evidence"].append("The log reports elevated CPU utilization.")
    incident["actions"].append(
        "Check CPU metrics and identify the process consuming resources."
    )

print("=== Incident Response Plan ===")
print(f"Incident: {incident['type']}")
print(f"Severity: {incident['severity']}")

print("\nEvidence:")
if incident["evidence"]:
    for item in incident["evidence"]:
        print(f"- {item}")
else:
    print("- No recognized evidence found.")

print("\nRecommended actions:")
if incident["actions"]:
    for number, action in enumerate(incident["actions"], start=1):
        print(f"{number}. {action}")
else:
    print("- Review the logs and monitoring data manually.")

print("\nSafety: No services were restarted and no infrastructure was changed.")
print("The severity is an initial assessment; confirm impact before escalation.")
