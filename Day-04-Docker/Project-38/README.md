# Project 38 — Docker Image Security Scanning

## Objective

Scan a Docker image for known vulnerabilities using Trivy and investigate the reported security findings.

## Technologies

- Docker
- Trivy
- Python
- Flask
- Debian
- Container Security

## How It Works

Trivy analyzes the Docker image and checks:

- Operating system packages
- Language-specific dependencies
- Known CVEs
- Secrets

The scan was performed against the Project 37 Docker image.

## Security Scan

Initial scan:

    trivy image project-37:1.0

Result:

    Total: 167
    UNKNOWN: 2
    LOW: 61
    MEDIUM: 59
    HIGH: 45
    CRITICAL: 0

A focused scan was then performed:

    trivy image --severity HIGH,CRITICAL project-37:1.0

Result:

    Total: 45
    HIGH: 45
    CRITICAL: 0

## Findings

The HIGH findings were primarily associated with Debian operating system packages rather than the Python application dependencies.

Examples included:

- util-linux
- bsdutils
- libacl1
- libsystemd0
- ncurses
- perl-base

The Python packages detected by Trivy had zero reported vulnerabilities.

## Remediation Investigation

The Docker base image was refreshed:

    docker pull python:3.12-slim

The application was then rebuilt without using the Docker build cache:

    docker build --no-cache -t project-37:2.0 .

The new image was scanned again:

    trivy image --severity HIGH,CRITICAL project-37:2.0

Result:

    Total: 45
    HIGH: 45
    CRITICAL: 0

The vulnerability count did not change because the refreshed image still used Debian 13.7 and the reported vulnerabilities were primarily in the Debian package layer.

## Important Security Lesson

A vulnerability count alone does not determine the actual risk.

A DevOps engineer should investigate:

- Which layer contains the vulnerability
- Which package is affected
- Whether a fixed version exists
- Whether the package is required
- Whether the vulnerable functionality is reachable
- Whether the base image can be replaced
- Whether the CI/CD pipeline should block the deployment

## Testing / Failure Scenario

The Trivy database download initially timed out because the VM had a slow connection to the vulnerability database.

The scan was successfully completed after increasing the timeout:

    trivy image --timeout 60m project-37:1.0

## Troubleshooting

### Trivy database timeout

Increase the timeout:

    trivy image --timeout 60m project-37:1.0

### Scan only HIGH and CRITICAL

    trivy image --severity HIGH,CRITICAL project-37:1.0

### Scan only vulnerabilities

    trivy image --scanners vuln project-37:1.0

## Key Concepts Learned

- Container image security scanning
- CVEs
- Vulnerability severity
- OS package vulnerabilities
- Application dependency vulnerabilities
- Base image security
- Trivy
- Security remediation
- CI/CD security gates
- False-positive and risk assessment concepts

## Result

Successfully scanned a Docker image with Trivy, analyzed HIGH and CRITICAL findings, investigated the base image as the source of the findings, and verified that the image contained zero CRITICAL vulnerabilities.
