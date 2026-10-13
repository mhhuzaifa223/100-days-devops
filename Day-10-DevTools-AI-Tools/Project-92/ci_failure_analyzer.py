from collections import Counter
from pathlib import Path

log_file = Path("pipeline.log")
lines = log_file.read_text(encoding="utf-8").splitlines()

levels = Counter()
errors = []

for line in lines:
    for level in ("INFO", "WARNING", "ERROR"):
        if f" {level} " in line:
            levels[level] += 1

    if " ERROR " in line:
        errors.append(line.split(" ERROR ", 1)[1])

print("=== CI/CD Failure Analysis ===")
print(f"Total log lines: {len(lines)}")
print(f"Errors found: {len(errors)}")

print("\nFailure details:")
for error in errors:
    print(f"- {error}")

print("\nLikely cause and recommendations:")

combined_errors = " ".join(errors).lower()

if "modulenotfounderror" in combined_errors or "no module named" in combined_errors:
    print("- Likely cause: a required Python module is missing from the CI environment.")
    print("- Check requirements.txt and ensure dependency installation completes before tests.")
    print("- Reproduce the failure locally in a clean virtual environment.")
elif "permission denied" in combined_errors:
    print("- Likely cause: the pipeline user lacks required permissions.")
    print("- Check file permissions and the identity running the job.")
elif "connection refused" in combined_errors or "timed out" in combined_errors:
    print("- Likely cause: a service is unavailable or unreachable.")
    print("- Check service health, hostname, port, and network configuration.")
elif errors:
    print("- Cause not recognized by the current rules.")
    print("- Inspect the first meaningful error and surrounding log lines.")
else:
    print("- No errors detected in the log.")
