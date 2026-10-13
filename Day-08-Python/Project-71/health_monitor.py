import subprocess
import psutil

print("=== SYSTEM HEALTH MONITOR ===")

# CPU usage
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

# Memory usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")

# Disk usage
disk = psutil.disk_usage("/")
disk_percent = disk.percent
print(f"Disk Usage: {disk_percent:.1f}%")

# SSH service status
try:
    result = subprocess.run(
        ["systemctl", "is-active", "ssh"],
        capture_output=True,
        text=True,
        timeout=5
    )
    ssh_status = result.stdout.strip() or "unknown"
except (FileNotFoundError, subprocess.TimeoutExpired):
    ssh_status = "unknown"

print(f"SSH Service: {ssh_status}")

# Individual metric statuses
def get_status(value):
    if value >= 90:
        return "CRITICAL"
    elif value >= 70:
        return "WARNING"
    else:
        return "OK"

print(f"CPU Status: {get_status(cpu)}")
print(f"Memory Status: {get_status(memory.percent)}")
print(f"Disk Status: {get_status(disk_percent)}")

# Overall health
if cpu >= 90 or memory.percent >= 90 or disk_percent >= 90:
    print("Overall Status: CRITICAL")
elif cpu >= 70 or memory.percent >= 70 or disk_percent >= 70:
    print("Overall Status: WARNING")
elif ssh_status != "active":
    print("Overall Status: WARNING")
else:
    print("Overall Status: HEALTHY")
