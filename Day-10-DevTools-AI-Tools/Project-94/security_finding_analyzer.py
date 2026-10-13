from collections import Counter
from pathlib import Path

findings_file = Path("security_findings.txt")
text = findings_file.read_text(encoding="utf-8")

blocks = [
    block.strip()
    for block in text.split("\n\n")
    if block.strip()
]

severity_counts = Counter()
findings = []

remediation = {
    "CRITICAL": "Prioritize immediately. Remove exposed secrets and rotate affected credentials.",
    "HIGH": "Investigate promptly and apply a verified fix or package update.",
    "MEDIUM": "Harden the configuration and validate the change.",
    "LOW": "Address during routine security improvements.",
}

for block in blocks:
    fields = {}

    for line in block.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value

    if "FINDING" not in fields or "SEVERITY" not in fields:
        continue

    severity = fields["SEVERITY"].upper()
    severity_counts[severity] += 1

    findings.append({
        "name": fields["FINDING"],
        "tool": fields.get("TOOL", "Unknown"),
        "severity": severity,
        "detail": fields.get("DETAIL", "No details supplied."),
    })

print("=== Security Finding Analysis ===")
print(f"Total findings analyzed: {len(findings)}")

print("\nSeverity summary:")
for severity in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
    print(f"- {severity}: {severity_counts[severity]}")

print("\nFindings and remediation:")
for finding in findings:
    print(f"\n[{finding['severity']}] {finding['name']}")
    print(f"Tool: {finding['tool']}")
    print(f"Detail: {finding['detail']}")
    print(f"Recommendation: {remediation.get(finding['severity'], 'Review and validate the finding.')}")

print("\nNote: Validate each finding before deciding on remediation.")
