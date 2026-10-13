# Project 93: AI Kubernetes Troubleshooting Assistant

## Overview
A Python-based troubleshooting assistant that detects common Kubernetes workload failures from sample output and recommends diagnostic commands.

The current version uses rule-based pattern matching. It is a foundation for an AI-powered assistant, not an actual LLM integration.

## Skills Practiced
- Kubernetes workload troubleshooting
- Reading pod status and warning messages
- Python text processing
- Automated testing
- Incident investigation

## Files
- `kubernetes.log` — simulated pod status and warning output
- `k8s_troubleshooter.py` — issue detection and recommendations
- `test_k8s_troubleshooter.py` — automated output checks
- `.gitignore` — excludes Python cache and environment files

## Run
    python3 k8s_troubleshooter.py

## Test
    python3 test_k8s_troubleshooter.py

## Issues Covered

### CrashLoopBackOff
A container repeatedly starts and exits. Suggested checks include pod events, container logs, and logs from the previous container instance.

### ImagePullBackOff
Kubernetes cannot successfully pull a container image. Check the image name and tag, registry access, and image pull secrets.

## Important
This project analyzes simulated output, not a live Kubernetes cluster. Its recommendations identify likely troubleshooting paths, not confirmed root causes.

## Future Improvements
- Parse actual `kubectl` output files
- Add more Kubernetes failure patterns
- Integrate an AI model for unfamiliar errors
- Add a CI workflow to run the tests

## Cleanup
This project uses local sample files only. No Kubernetes cluster or cloud resources were created.
