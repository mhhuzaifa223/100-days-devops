import socket
import sys
from time import perf_counter

host = sys.argv[1] if len(sys.argv) > 1 else "example.com"

try:
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 443
    if not 1 <= port <= 65535:
        raise ValueError
except ValueError:
    print("ERROR: Port must be an integer between 1 and 65535.")
    raise SystemExit(2)

print("=== NETWORK CONNECTIVITY CHECK ===")
print(f"Host: {host}")
print(f"TCP Port: {port}")

try:
    addresses = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    unique_ips = sorted({item[4][0] for item in addresses})
    print(f"Resolved IPs: {', '.join(unique_ips)}")

    start = perf_counter()
    with socket.create_connection((host, port), timeout=5):
        elapsed = (perf_counter() - start) * 1000

    print(f"Connection time: {elapsed:.2f} ms")
    print("Result: REACHABLE")

except socket.gaierror as error:
    print(f"Result: DNS FAILED ({error})")
    raise SystemExit(1)
except (TimeoutError, OSError) as error:
    print(f"Result: UNREACHABLE ({error})")
    raise SystemExit(1)
