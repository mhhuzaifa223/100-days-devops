from collections import Counter
from pathlib import Path

log_file = Path("sample.log")
lines = log_file.read_text(encoding="utf-8").splitlines()

levels = Counter()
errors = Counter()

for line in lines:
    for level in ("ERROR", "WARNING", "INFO"):
        if f" {level} " in line:
            levels[level] += 1

    if " ERROR " in line:
        message = line.split(" ERROR ", 1)[1]
        errors[message] += 1

print("=== Log Analysis Report ===")
print(f"Total lines: {len(lines)}")

print("\nLog levels:")
for level, count in levels.items():
    print(f"- {level}: {count}")

print("\nErrors:")
for message, count in errors.most_common():
    print(f"- {message}: {count} occurrence(s)")

print("\nRecommendations:")
if any("Database connection timeout" in message for message in errors):
    print("- Check database availability, connectivity, and connection limits.")
if any("status 500" in message for message in errors):
    print("- Inspect application logs and stack traces around HTTP 500 errors.")
if not errors:
    print("- No errors detected.")
