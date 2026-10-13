# Project 80: Python DevOps Automation Toolkit

## Overview
A command-line toolkit that combines common Linux and network health checks.

## Features
- System health: CPU, memory, and disk
- Disk usage and free-space reporting
- Linux systemd service status checks
- TCP connectivity checks
- Configurable hostnames, ports, paths, and services
- Exit codes for health alerts and errors

## Requirements
- Python 3.8+
- psutil
- Linux with systemd for service checks

## Setup
python3 -m venv .venv
source .venv/bin/activate
pip install psutil

## Usage
python devops_toolkit.py health
python devops_toolkit.py disk /
python devops_toolkit.py service ssh
python devops_toolkit.py network example.com 443

## Thresholds
- OK: below 70%
- WARNING: 70% to below 90%
- CRITICAL: 90% or above

## Learning outcomes
Combined Python functions, argparse, system metrics, subprocess, filesystem checks, sockets, exception handling, and exit codes.
