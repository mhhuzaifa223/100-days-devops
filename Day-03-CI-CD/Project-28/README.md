# Project 28 — DevSecOps Security Scanning Pipeline

## Objective

Learn how security checks can be integrated directly into a CI/CD pipeline so vulnerabilities are detected before insecure code or infrastructure reaches production.

## Technologies

- GitHub Actions or Jenkins
- Trivy
- SonarQube
- OWASP ZAP
- Checkov
- Docker
- Linux

## What I Practiced

- Integrating security into CI/CD
- Static Application Security Testing (SAST)
- Software Composition Analysis (SCA)
- Container image scanning
- Infrastructure-as-Code scanning
- Dynamic Application Security Testing (DAST)
- Failing pipelines when critical vulnerabilities are detected

## Pipeline Workflow

Code
→ Build
→ SAST
→ Dependency Scan
→ Build Container
→ Container Scan
→ IaC Scan
→ DAST
→ Deploy

## Security Checks

### SAST

Analyzes source code for security issues.

Example tool:

- SonarQube

### SCA

Checks application dependencies for known vulnerabilities.

Example tools:

- Snyk
- OWASP dependency scanners

### Container Scanning

Scans Docker images for vulnerable packages and dependencies.

Example tool:

- Trivy

### IaC Scanning

Checks infrastructure configuration for security problems.

Example tool:

- Checkov

### DAST

Tests a running application from an external perspective.

Example tool:

- OWASP ZAP

## Testing

Two scenarios should be tested.

### Secure Build

The application passes the configured security checks.

Expected result:

- Security scans complete successfully.
- No blocking vulnerabilities are detected.
- Pipeline continues.

### Vulnerable Build

Introduce or use a deliberately vulnerable dependency, container image, or configuration.

Expected result:

- Scanner detects the vulnerability.
- Pipeline reports the finding.
- Pipeline stops when the configured severity threshold is exceeded.

## Key Concepts Learned

- DevSecOps
- Security scanning
- SAST
- SCA
- DAST
- Container security
- IaC security
- Vulnerability severity
- Security quality gates
- Shift-left security

## Why This Matters

Security should be part of the development and deployment process rather than a final manual check.

Automated security scanning allows teams to identify vulnerabilities earlier and prevent high-risk changes from reaching production.
