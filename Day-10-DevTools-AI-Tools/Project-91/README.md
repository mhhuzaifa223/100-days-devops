# Project 91: AI Log Analyzer

## Overview
A Python-based log analysis tool that summarizes application logs, counts log levels, identifies repeated errors, and provides rule-based troubleshooting recommendations.

This project is the foundation for a future AI-powered log analysis assistant. The current version uses Python rules and does not call an external AI model.

## Skills Practiced
- Python scripting and file handling
- Log parsing and error frequency analysis
- Automated validation using test assertions
- Basic incident troubleshooting
- Git and GitHub project documentation

## Project Files
- `sample.log` — sample application logs
- `log_analyzer.py` — log analysis script
- `test_log_analyzer.py` — automated output checks
- `README.md` — project documentation

## Run the Analyzer
Run from this directory:

    python3 log_analyzer.py

## Run Tests
    python3 test_log_analyzer.py

The test script checks the total line count, log-level counts, error frequencies, and database troubleshooting recommendation.

## Sample Findings
- 7 total log lines
- 3 INFO messages
- 1 WARNING message
- 3 ERROR messages
- Database connection timeout: 2 occurrences
- HTTP 500 failure: 1 occurrence

## Troubleshooting Guidance
Repeated database timeouts may indicate database availability, connectivity, or connection-limit issues. HTTP 500 errors should be investigated using application logs and stack traces around the failure.

These are diagnostic suggestions, not proof of the root cause.

## Limitations and Future Improvements
- Accept a log-file path as a command-line argument
- Add timestamp and severity filtering
- Integrate an AI model to summarize unfamiliar errors
- Add structured output such as JSON
- Add containerization and CI testing

## Cleanup
The project runs locally and creates no cloud resources. No cloud cleanup is required.
