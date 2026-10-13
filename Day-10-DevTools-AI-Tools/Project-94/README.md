# Project 94: AI Security Finding Analyzer

## Overview
A Python-based tool that summarizes simulated security findings, counts severity levels, and suggests remediation priorities.

The current implementation uses rules rather than an AI model. It is a foundation for a future AI-assisted security analysis tool.

## Skills Practiced
- DevSecOps finding triage
- Severity classification
- Python text processing
- Automated testing
- Security remediation planning

## Files
- `security_findings.txt` — simulated findings
- `security_finding_analyzer.py` — analyzer
- `test_security_finding_analyzer.py` — automated checks
- `.gitignore` — excludes Python cache and environment files

## Run
    python3 security_finding_analyzer.py

## Test
    python3 test_security_finding_analyzer.py

## Sample Results
- Total findings: 5
- CRITICAL: 1
- HIGH: 2
- MEDIUM: 1
- LOW: 1

## Security Notes
The findings are simulated, not results of a live scan. Validate findings before remediation. If a credential is confirmed to have been exposed, remove it from the affected location and rotate it; deleting the text alone may not invalidate the credential.

## Future Improvements
- Parse JSON or SARIF reports from security tools
- Add deduplication and filtering
- Integrate an AI model for contextual explanations
- Add automated tests to CI

## Cleanup
This project uses local files only and creates no cloud resources.
