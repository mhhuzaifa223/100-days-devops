# Project 99 — DevOps AI Runbook Generator

## Overview
A dependency-free Python prototype that converts incident log evidence into a structured troubleshooting runbook.

This is a rule-based prototype, not a real AI model. It uses predefined patterns and templates to suggest investigation and recovery checks.

## Features
- Reads local incident logs.
- Recognizes API health-check failures and HTTP 503 errors.
- Identifies high-CPU warnings.
- Generates investigation and recovery steps.
- Includes escalation guidance and safety notes.
- Provides automated unit tests.

## Requirements
- Python 3.8+
- No third-party dependencies

## Run
From this directory:

    python3 runbook_generator.py

The generated runbook is saved as `generated_runbook.md`.

## Test
Run:

    python3 -m unittest -v

## Example Incident
The included `incident.log` contains a high-CPU warning, API health-check failure, HTTP 503 error, and failed retry.

## Safety
The generated steps are suggestions, not a confirmed root-cause analysis. The tool performs no automatic remediation and does not modify production infrastructure. Review every recommendation before acting.

## Limitations
- Uses fixed rules rather than a language model.
- Recognizes only a limited set of incident patterns.
- Does not integrate with monitoring platforms, ticketing systems, or live infrastructure.

## Skills Practiced
Python scripting, log analysis, runbook automation, testing, incident response, and Git version control.
