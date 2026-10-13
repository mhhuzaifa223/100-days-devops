# Project 84: Dependency Vulnerability Scanning

## Objective
Detect known vulnerabilities in application dependencies and remediate them using Trivy.

## Tools
- Trivy
- Python
- pip requirements file

## Initial Scan
Dependency: urllib3==1.26.5

Result: 10 vulnerabilities detected.

## Remediation
Updated urllib3 to version 2.8.0 based on the fixed versions reported by Trivy.

## Final Validation
Command: `trivy fs --scanners vuln .`

Result: **0 vulnerabilities detected** in requirements.txt.

## Key Learnings
- Dependency manifests can be scanned without installing the application.
- Outdated libraries can contain known security vulnerabilities.
- Trivy maps dependency versions to published vulnerability information.
- Dependencies should be updated to fixed versions and rescanned.
- Scan results depend on the vulnerability database available at scan time.
