from collections import Counter
from pathlib import Path
import sys

log_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sample.log")

if not log_file.is_file():
    print(f"Error: Log file not found: {log_file}")
    raise SystemExit(1)

counts = Counter()
errors = Counter()

with log_file.open("r", encoding="utf-8") as file:
    for line in file:
        if " ERROR " in line:
            counts["ERROR"] += 1
            errors[line.strip().split(" ERROR ", 1)[1]] += 1
        elif " WARNING " in line:
            counts["WARNING"] += 1
        elif " INFO " in line:
            counts["INFO"] += 1

print("=== LOG ANALYSIS REPORT ===")
print(f"File: {log_file}")
print(f"Errors: {counts['ERROR']}")
print(f"Warnings: {counts['WARNING']}")
print(f"Info entries: {counts['INFO']}")

print("\n=== MOST FREQUENT ERRORS ===")
if errors:
    for message, count in errors.most_common():
        print(f"{count}x - {message}")
else:
    print("No errors found.")
