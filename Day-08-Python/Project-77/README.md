# Project 77: Python Disk Space Alert Tool

## Overview
A Python CLI tool that checks filesystem usage and reports OK, WARNING, or CRITICAL status.

## Features
- Checks a specified filesystem path
- Reports disk usage percentage and free space
- Uses configurable warning (70%) and critical (90%) thresholds
- Handles invalid paths gracefully
- Returns a nonzero exit code for alerts or errors

## Requirements
- Python 3.8+
- No third-party packages required

## Usage
Check root:
python disk_alert.py

Check another path:
python disk_alert.py /tmp

## Learning outcomes
Practiced shutil, filesystem monitoring, thresholds, exception handling, and exit codes.
