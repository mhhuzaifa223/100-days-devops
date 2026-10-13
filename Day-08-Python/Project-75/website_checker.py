import os
os.environ.setdefault("SSL_CERT_FILE", "/etc/ssl/certs/ca-certificates.crt")
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from time import perf_counter
import sys

url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"

if not url.startswith(("http://", "https://")):
    url = "https://" + url

request = Request(url, headers={"User-Agent": "Python-Website-Checker/1.0"})
start = perf_counter()

try:
    with urlopen(request, timeout=10) as response:
        status = response.status
        elapsed = (perf_counter() - start) * 1000
        print("=== WEBSITE CHECK ===")
        print(f"URL: {url}")
        print(f"HTTP Status: {status}")
        print(f"Response Time: {elapsed:.2f} ms")
        print(f"Result: {'AVAILABLE' if 200 <= status < 400 else 'CHECK REQUIRED'}")

except HTTPError as error:
    elapsed = (perf_counter() - start) * 1000
    print(f"URL: {url}")
    print(f"HTTP Status: {error.code}")
    print(f"Response Time: {elapsed:.2f} ms")
    print("Result: CHECK REQUIRED")

except (URLError, TimeoutError, OSError) as error:
    elapsed = (perf_counter() - start) * 1000
    print(f"URL: {url}")
    print(f"Response Time: {elapsed:.2f} ms")
    print(f"Result: UNREACHABLE ({error})")
    sys.exit(1)
