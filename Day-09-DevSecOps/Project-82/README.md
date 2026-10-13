# Project 82 — Docker Image Vulnerability Scanning

## Objective
Scan a Docker image for known vulnerabilities using Trivy.

## Tools
- Docker
- Trivy
- Linux

## Implementation
Scanned the Nginx 1.27 image with Trivy's vulnerability scanner.

Command used:

    trivy image --scanners vuln --timeout 20m nginx:1.27

The first attempt timed out during image-layer analysis while Trivy downloaded its vulnerability databases. The subsequent scan completed and displayed vulnerability findings, including issues in system packages such as util-linux and zlib.

## What I Learned
- How to scan container images for known CVEs.
- How Trivy uses a vulnerability database.
- How to interpret severity levels such as CRITICAL, HIGH, MEDIUM, and LOW.
- Why scanner timeouts may require a longer timeout value.
- Why a vulnerability marked will_not_fix needs careful risk assessment.

## Security Best Practices
- Prefer maintained image tags and rebuild images regularly.
- Review whether vulnerabilities have fixes and whether affected packages are used.
- Do not assume that every finding is exploitable in every deployment.
- Scan container images during CI/CD before deployment.
- Avoid deploying images with unresolved critical vulnerabilities without an approved risk decision.

## Result
Successfully scanned an Nginx container image and reviewed Trivy vulnerability findings.
