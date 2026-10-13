# Project 83: Dockerfile Security Scanning and Remediation

## Objective
Identify and fix Dockerfile security misconfigurations using Trivy.

## Tools
- Docker
- Trivy

## Initial Findings
The initial Dockerfile contained five misconfigurations:
- MEDIUM: Used the mutable `ubuntu:latest` tag.
- HIGH: Explicitly ran the container as root.
- HIGH: Ran `apt-get update` separately from package installation.
- LOW: Did not define a health check.
- CRITICAL: Defined an API token through an environment variable.

The token was fake training data, not a real credential.

## Remediation
- Pinned the base image to `ubuntu:24.04`.
- Combined package update and installation in one `RUN` instruction.
- Removed package-manager cache files.
- Created and selected a non-root user with UID 10001.
- Added a Docker `HEALTHCHECK`.
- Removed the hard-coded API token.

## Validation
Command: `trivy config .`

Result: **0 misconfigurations detected** across the Dockerfile.

## Key Learnings
- Why mutable image tags reduce build reproducibility.
- Why containers should run as non-root users.
- How to reduce Docker image layers and package-cache leftovers.
- Why secrets should not be embedded in Dockerfile environment variables.
- How Trivy detects and verifies remediation of Dockerfile misconfigurations.
