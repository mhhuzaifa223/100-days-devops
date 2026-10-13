# Project 86: SAST Pipeline with Bandit

## Objective
Use Static Application Security Testing (SAST) to identify security weaknesses in Python code and automate scanning with GitHub Actions.

## Tools
- Python
- Bandit
- GitHub Actions

## Implementation
1. Created a Python application for security testing.
2. Scanned the initial code with Bandit.
3. Identified risky subprocess usage and insecure temporary-file handling.
4. Removed unnecessary subprocess execution and used Python's secure temporary-file utility.
5. Re-ran Bandit and achieved zero findings.
6. Created a GitHub Actions workflow to scan the application on relevant pushes and pull requests.

## Run Locally
Install Bandit with `python3 -m pip install --user bandit`, then run:

    python3 app.py
    bandit -r app.py -f txt

## Workflow
The automated workflow is stored at `.github/workflows/sast.yml`.

## Key Learnings
- SAST analyzes source code without running the application.
- Bandit detects common Python security issues.
- Avoid shell execution when it is unnecessary.
- Use secure temporary-file utilities instead of predictable temporary paths.
- CI pipelines can enforce security checks during code changes.

## Result
The final local Bandit scan reported zero issues across all severity and confidence levels.
