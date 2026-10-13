import argparse
import shutil
import socket
import subprocess
import sys
import psutil


def system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    print("=== SYSTEM HEALTH ===")
    print(f"CPU: {cpu:.1f}%")
    print(f"Memory: {memory:.1f}%")
    print(f"Disk: {disk:.1f}%")

    if max(cpu, memory, disk) >= 90:
        print("Overall: CRITICAL")
        return 1
    if max(cpu, memory, disk) >= 70:
        print("Overall: WARNING")
        return 1

    print("Overall: HEALTHY")
    return 0


def disk_check(path):
    try:
        usage = shutil.disk_usage(path)
    except OSError as error:
        print(f"ERROR: {error}")
        return 2

    percent = usage.used / usage.total * 100
    print(f"Path: {path}")
    print(f"Disk usage: {percent:.1f}%")
    print(f"Free space: {usage.free / (1024 ** 3):.2f} GiB")

    if percent >= 90:
        print("Status: CRITICAL")
        return 1
    if percent >= 70:
        print("Status: WARNING")
        return 1

    print("Status: OK")
    return 0


def service_check(name):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", name],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as error:
        print(f"ERROR: {error}")
        return 2

    status = result.stdout.strip() or "unknown"
    print(f"Service: {name}")
    print(f"Status: {status}")

    if status == "active":
        print("Result: HEALTHY")
        return 0

    print("Result: WARNING")
    return 1


def network_check(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"{host}:{port} is REACHABLE")
        return 0
    except socket.gaierror as error:
        print(f"DNS FAILED: {error}")
        return 1
    except OSError as error:
        print(f"UNREACHABLE: {error}")
        return 1


def main():
    parser = argparse.ArgumentParser(description="Python DevOps Automation Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("health", help="Check CPU, memory, and disk")

    disk_parser = subparsers.add_parser("disk", help="Check disk usage")
    disk_parser.add_argument("path", nargs="?", default="/")

    service_parser = subparsers.add_parser("service", help="Check a systemd service")
    service_parser.add_argument("name", nargs="?", default="ssh")

    network_parser = subparsers.add_parser("network", help="Test a TCP connection")
    network_parser.add_argument("host", nargs="?", default="example.com")
    network_parser.add_argument("port", nargs="?", type=int, default=443)

    args = parser.parse_args()

    if args.command == "health":
        return system_health()
    if args.command == "disk":
        return disk_check(args.path)
    if args.command == "service":
        return service_check(args.name)
    if args.command == "network":
        if not 1 <= args.port <= 65535:
            print("ERROR: Port must be between 1 and 65535.")
            return 2
        return network_check(args.host, args.port)

    return 0


if __name__ == "__main__":
    sys.exit(main())
