import subprocess
import sys

service = sys.argv[1] if len(sys.argv) > 1 else "ssh"

try:
    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True,
        timeout=5,
        check=False,
    )

    status = result.stdout.strip() or "unknown"

    print("=== SERVICE MONITOR ===")
    print(f"Service: {service}")
    print(f"Status: {status}")

    if status == "active":
        print("Result: HEALTHY")
    else:
        print("Result: WARNING")
        sys.exit(1)

except FileNotFoundError:
    print("ERROR: systemctl was not found. This script requires systemd.")
    sys.exit(2)
except subprocess.TimeoutExpired:
    print(f"ERROR: Timed out checking service: {service}")
    sys.exit(2)
