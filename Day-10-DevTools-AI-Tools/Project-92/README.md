# Project 92: AI CI/CD Failure Analyzer

## Overview
A Python-based tool that examines CI/CD pipeline logs, extracts errors, identifies recognized failure patterns, and suggests troubleshooting steps.

The current implementation is rule-based. It is a foundation for a future AI-powered pipeline diagnosis tool, not an LLM integration.

## Skills Practiced
- Python log parsing
- CI/CD failure diagnosis
- Root-cause investigation
- Automated testing
- Git and GitHub documentation

## Files
- `pipeline.log` — simulated failed pipeline output
- `ci_failure_analyzer.py` — analyzer
- `test_ci_failure_analyzer.py` — automated checks
- `.gitignore` — excludes Python cache and environment files

## Run
    python3 ci_failure_analyzer.py

## Test
    python3 test_ci_failure_analyzer.py

## Simulated Failure
The pipeline fails because Python cannot import the `requests` module.

## Recommendations
- Check `requirements.txt`.
- Ensure dependencies install before tests run.
- Reproduce the failure in a clean virtual environment.
- Inspect the first meaningful error rather than relying only on the final exit code.

The suggested cause is based on log patterns and should be verified against the actual CI environment.

## Future Improvements
- Accept an arbitrary log-file path
- Add GitHub Actions integration
- Analyze more failure patterns
- Integrate an AI model for unfamiliar errors

## Cleanup
This project runs locally and creates no cloud resources.
