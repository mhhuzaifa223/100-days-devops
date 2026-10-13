from pathlib import Path
from datetime import datetime, timezone

log_file = Path(__file__).parent / "incident.log"
output_file = Path(__file__).parent / "generated_runbook.md"

lines = log_file.read_text(encoding="utf-8").splitlines()
text = "\n".join(lines).lower()

symptoms = []
steps = []

if "503 service unavailable" in text or "health check failed" in text:
    symptoms.append("API health check failed or returned HTTP 503.")
    steps.extend([
        "Check application logs around the incident timestamp.",
        "Verify API health and dependent services.",
        "Review recent deployments and configuration changes.",
        "Confirm the endpoint and dependency connectivity.",
    ])

if "cpu utilization reached" in text:
    symptoms.append("High CPU utilization was reported.")
    steps.extend([
        "Inspect CPU metrics over the incident window.",
        "Identify resource-intensive processes or containers.",
        "Compare CPU usage with request volume and recent changes.",
    ])

if not symptoms:
    symptoms.append("No known incident pattern was recognized.")
    steps.append("Review the source logs and monitoring data manually.")

runbook = [
    "# Generated DevOps Incident Runbook",
    "",
    f"Generated (UTC): {datetime.now(timezone.utc).isoformat()}",
    "",
    "## Incident Summary",
    *[f"- {symptom}" for symptom in symptoms],
    "",
    "## Investigation Steps",
    *[f"{number}. {step}" for number, step in enumerate(steps, start=1)],
    "",
    "## Recovery Verification",
    "1. Recheck the API health endpoint.",
    "2. Confirm error rates and resource usage have returned to acceptable levels.",
    "3. Monitor for recurring failures before closing the incident.",
    "",
    "## Escalation",
    "Escalate to the service owner if the API remains unavailable, customer impact continues, or the cause cannot be established.",
    "",
    "## Safety Notes",
    "- Treat these steps as a starting point, not a confirmed diagnosis.",
    "- Do not restart services or change production resources without authorization.",
    "- CPU usage may be correlated with the outage without being its root cause.",
    "",
]

output_file.write_text("\n".join(runbook), encoding="utf-8")

print(f"Runbook generated: {output_file.name}")
print(f"Symptoms identified: {len(symptoms)}")
print(f"Investigation steps: {len(steps)}")
print("\n--- Runbook Preview ---")
print(output_file.read_text(encoding="utf-8"))
