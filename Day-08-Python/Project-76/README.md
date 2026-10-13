# Project 76: Automated Service Monitor

## Overview
A Python command-line tool that checks Linux systemd service status.

## Features
- Checks whether a service is active
- Accepts a service name as a command-line argument
- Reports HEALTHY or WARNING
- Handles missing systemctl and command timeouts
- Returns a nonzero exit code when a service is not active

## Requirements
- Python 3.8+
- Linux with systemd

## Usage
Check the default SSH service:
python service_monitor.py

Check a specific service:
python service_monitor.py cron

Test a nonexistent service:
python service_monitor.py nonexistent-service

## Learning outcomes
Practiced subprocess, command-line arguments, exception handling, exit codes, and Linux service monitoring.
