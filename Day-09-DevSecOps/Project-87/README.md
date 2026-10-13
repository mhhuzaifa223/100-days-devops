# Project 87: Dynamic Application Security Testing (DAST)

## Objective
Explore runtime web application security testing with OWASP ZAP and a deliberately vulnerable local training application.

## Tools
- Docker
- OWASP Juice Shop
- OWASP ZAP Baseline Scanner

## Lab Setup
Started OWASP Juice Shop in Docker, bound to 127.0.0.1:3000 to keep the application local.
Verified the application responded with HTTP 200 OK using curl.

## Scan Attempt
Attempted to run the OWASP ZAP baseline scanner against the local training application. The scanner did not complete successfully in this environment, so no vulnerability findings or successful report generation are claimed.

## Key Learnings
- DAST tests a running application rather than analyzing source code.
- OWASP ZAP can automate baseline security checks.
- Verify application reachability before scanning.
- A hanging scanner should be stopped and investigated rather than repeatedly rerun.
- Scan only applications you own or have permission to test.

## Result
The local test application was reachable. ZAP scan completion and report generation remain unverified.
