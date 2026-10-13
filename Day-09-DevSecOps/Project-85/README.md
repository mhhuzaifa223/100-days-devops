# Project 85 — Git Secrets Detection and Remediation

## Objective
Detect accidentally committed credentials with Gitleaks, remove the exposed values from Git history, and verify that the repository is clean.

## Tools
- Gitleaks
- Git
- Bash
- Ubuntu Linux

## Lab Scenario
Created a local training repository containing fake API and database credentials. Gitleaks scanned the Git history and detected one leak.

## Remediation
- Replaced hardcoded credentials with environment-variable lookups.
- Amended the training commit so the earlier example was removed from the repository's current history.
- Re-ran Gitleaks to verify the result.

## Verification
The final command, `gitleaks git . --redact`, reported **no leaks found**.

## Security Lessons
- Never hardcode real credentials in source code.
- Use environment variables or a dedicated secrets manager.
- Scan Git history, not just the current file.
- If a real credential is exposed, revoke or rotate it immediately. Removing it from Git history alone does not make it safe.
- Keep the intentionally vulnerable training repository local and out of the public portfolio repository.

## Result
Successfully detected a fake secret, remediated the sample, and confirmed a clean Gitleaks scan.
