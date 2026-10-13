# Project 98: AI DevOps ChatOps Assistant

## Overview
A local, chat-style Python prototype that accepts supported DevOps requests and summarizes a sample incident log.

The current implementation uses predefined rules. It does not connect to an AI model or Slack.

## Supported Requests
- `help` — list supported requests
- `status` — summarize errors and warnings in `incident.log`
- `exit` — quit the interactive session

Unsupported requests are rejected without performing any operation.

## Files
- `incident.log` — simulated monitoring output
- `chatops_assistant.py` — interactive chat loop and request routing
- `test_chatops_assistant.py` — automated tests
- `.gitignore` — excludes Python cache and environment files

## Run
    python3 chatops_assistant.py

## Test
    python3 -m unittest -v

## Safety
This prototype only reads a local sample log and prints a response. It does not execute arbitrary commands or modify production infrastructure.

## Future Improvements
- Add Slack or Microsoft Teams integration
- Add authenticated users and role-based permissions
- Integrate an AI model with an explicit tool allowlist
- Add approval gates for any future operational actions
- Run tests in CI

## Cleanup
No cloud resources are created.
