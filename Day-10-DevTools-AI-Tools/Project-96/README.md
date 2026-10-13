# Project 96: Agentic Incident Response System

## Overview
A Python-based incident-response prototype that reads incident logs, identifies recognized failure patterns, assigns an initial severity, and recommends diagnostic actions.

The current implementation uses deterministic rules. It is not yet an autonomous AI agent.

## Skills Practiced
- Incident triage and severity assessment
- Log-pattern detection
- Root-cause investigation
- Safe incident-response planning
- Python automated testing

## Files
- `incident.log` — simulated incident data
- `incident_responder.py` — detection and response-plan generation
- `test_incident_responder.py` — automated tests
- `.gitignore` — excludes Python cache and environment files

## Run
    python3 incident_responder.py

## Test
    python3 -m unittest -v

## Example Scenario
The sample log contains an API health-check failure, an HTTP 503 error, and elevated CPU utilization.

The tool classifies this as a high-severity API availability incident and recommends checking logs, dependencies, recent deployments, and CPU metrics.

## Safety
The tool only reads a local sample file and prints recommendations. It does not restart services, modify infrastructure, or perform automatic remediation.

Severity is an initial assessment and must be confirmed against actual customer impact and monitoring data.

## Future Improvements
- Integrate monitoring alerts
- Add incident deduplication and timestamps
- Generate structured JSON reports
- Add human-approved remediation workflows
- Integrate an AI model for contextual analysis

## Cleanup
No cloud resources are created.
