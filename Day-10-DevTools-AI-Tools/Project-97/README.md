# Project 97: DevOps Operations Assistant

## Overview
A local Python prototype that maps approved task names to predefined diagnostic functions and returns structured results.

The implementation is rule-based and does not use an AI model. It demonstrates a safe foundation for a future AI-assisted operations tool.

## Approved Tasks
- `check_disk` — reads root filesystem usage.
- `check_incident` — summarizes a local sample incident log.
- `show_help` — lists the approved tasks.

## Files
- `tasks.json` — approved task configuration
- `incident.log` — simulated incident data
- `ops_assistant.py` — task routing and diagnostics
- `test_ops_assistant.py` — automated tests
- `.gitignore` — excludes Python cache and environment files

## Run
    python3 ops_assistant.py

## Test
    python3 -m unittest -v

## Safety
The assistant rejects unknown task names and does not execute arbitrary shell commands. Its predefined functions perform read-only diagnostics.

This is a local prototype, not a fully autonomous AI agent. Any future remediation feature should require explicit authorization and appropriate safeguards.

## Future Improvements
- Add command-line task selection
- Validate task configuration more strictly
- Return structured error messages
- Integrate an AI model with a strict allowlist of tools
- Add CI tests

## Cleanup
No cloud resources are created.
