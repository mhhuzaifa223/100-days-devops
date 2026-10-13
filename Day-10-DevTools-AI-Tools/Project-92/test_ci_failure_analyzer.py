import subprocess
import sys

result = subprocess.run(
    [sys.executable, "ci_failure_analyzer.py"],
    capture_output=True,
    text=True,
    check=True,
)

output = result.stdout

checks = [
    "Total log lines: 6",
    "Errors found: 3",
    "ModuleNotFoundError: No module named 'requests'",
    "Likely cause: a required Python module is missing",
    "Check requirements.txt",
    "Reproduce the failure locally",
]

for expected in checks:
    assert expected in output, f"Missing expected result: {expected}"

print(f"All {len(checks)} checks passed.")
