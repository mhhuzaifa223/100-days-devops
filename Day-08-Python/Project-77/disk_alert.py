import shutil
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "/"
warning_threshold = 70
critical_threshold = 90

try:
    usage = shutil.disk_usage(path)
except OSError as error:
    print(f"ERROR: Cannot check {path}: {error}")
    raise SystemExit(2)

used_percent = usage.used / usage.total * 100
free_gb = usage.free / (1024 ** 3)

if used_percent >= critical_threshold:
    status = "CRITICAL"
elif used_percent >= warning_threshold:
    status = "WARNING"
else:
    status = "OK"

print("=== DISK SPACE ALERT ===")
print(f"Path: {path}")
print(f"Disk usage: {used_percent:.1f}%")
print(f"Free space: {free_gb:.2f} GiB")
print(f"Status: {status}")

if status != "OK":
    print(f"ALERT: Disk usage has reached the {status} threshold.")
    raise SystemExit(1)
