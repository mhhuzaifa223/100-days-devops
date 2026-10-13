import subprocess
import sys

result = subprocess.run(
    [sys.executable, "log_analyzer.py"],
    capture_output=True,
    text=True,
    check=True,
)

output = result.stdout

checks = [
    "Total lines: 7",
    "- INFO: 3",
    "- WARNING: 1",
    "- ERROR: 3",
    "Database connection timeout: 2 occurrence(s)",
    "Request failed with status 500: 1 occurrence(s)",
    "Check database availability, connectivity, and connection limits.",
]

for expected in checks:
    assert expected in output, f"Missing expected result: {expected}"

print(f"All {len(checks)} checks passed.")
