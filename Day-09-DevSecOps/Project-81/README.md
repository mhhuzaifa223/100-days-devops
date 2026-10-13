# Project 81 — Git Secret Scanning with Gitleaks

## Objective
Detect accidentally committed secrets using Gitleaks and a custom detection rule.

## Tools Used
- Linux
- Git
- Gitleaks
- TOML

## What I Learned
- Why API keys, passwords, and tokens must never be committed.
- How to scan Git history for potential secrets.
- How to create custom Gitleaks detection rules.
- Why deleting a secret from the current file does not remove it from previous commits.

## Implementation
Created a separate local Git repository named `lab-repo` and used fake training values to test secret detection.

Created a custom rule in `.gitleaks.toml` to detect values matching the pattern `TRAINING_SECRET_[A-Z0-9]{16}`.

## Scan Command
Run the following command from the test repository:

    gitleaks git . --config .gitleaks.toml

## Test Result
Gitleaks scanned three commits and detected one fake training secret.

## Security Best Practices
- Never commit real passwords, API keys, or access tokens.
- Revoke or rotate any real credential that is exposed.
- Removing a secret from the latest file does not erase it from Git history.
- Integrate secret scanning into local development and CI/CD pipelines.
- Remember that scanners can miss secrets; detection is not a replacement for secure credential management.

## Outcome
Successfully demonstrated Git-history secret scanning with Gitleaks and a custom rule using fake training data.
