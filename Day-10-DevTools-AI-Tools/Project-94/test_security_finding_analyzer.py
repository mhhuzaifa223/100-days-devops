import subprocess
import sys

result = subprocess.run(
    [sys.executable, "security_finding_analyzer.py"],
    capture_output=True,
    text=True,
    check=True,
)

output = result.stdout

checks = [
    "Total findings analyzed: 5",
    "- CRITICAL: 1",
    "- HIGH: 2",
    "- MEDIUM: 1",
    "- LOW: 1",
    "Hardcoded secret detected in config.py",
    "Container image contains a vulnerable package",
    "subprocess call uses shell=True",
    "Remove exposed secrets and rotate affected credentials.",
]

for expected in checks:
    assert expected in output, f"Missing expected result: {expected}"

print(f"All {len(checks)} checks passed.")
