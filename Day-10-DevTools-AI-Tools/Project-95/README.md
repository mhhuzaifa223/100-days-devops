# Project 95: DevOps Diagnostics Prototype

## Overview
A lightweight Python prototype exposing local DevOps diagnostic functions through a tool registry and returning structured JSON.

This project uses Python's standard library so it runs on Python 3.8 without external dependencies.

**Important:** This is an MCP-inspired prototype, not a standards-compliant MCP server. It does not implement the MCP protocol or communicate with an AI client.

## Tools
- `get_system_status` — returns status, UTC timestamp, process uptime, and disk usage.
- `get_disk_usage` — returns total, used, and free disk space plus usage percentage for a path.

## Run
    python3 devops_server.py

## Tests
    python3 -m unittest -v

## Safety
The tools perform read-only local diagnostics. They do not execute arbitrary shell commands, change permissions, or modify infrastructure.

## Compatibility
Uses Python 3.8+ and the standard library.

## Future Improvements
- Implement the official MCP protocol using a supported Python version and SDK
- Add input validation and structured error handling
- Connect the server to an authorized MCP client
- Add permission controls for any future diagnostic tools

## Cleanup
No cloud resources are created. The `.venv` directory is excluded from Git.
