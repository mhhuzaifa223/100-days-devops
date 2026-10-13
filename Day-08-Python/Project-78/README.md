# Project 78: Python Process Monitor

## Overview
A read-only Python tool that lists running processes and ranks them by resident memory usage.

## Features
- Enumerates running processes
- Displays process IDs and names
- Reports memory usage in MiB
- Sorts processes by memory consumption
- Handles processes that exit or deny access during inspection
- Does not terminate or modify processes

## Requirements
- Python 3.8+
- psutil

## Setup
python3 -m venv .venv
source .venv/bin/activate
pip install psutil

## Run
python process_monitor.py

## Learning outcomes
Practiced process inspection, sorting, exception handling, and Linux resource troubleshooting.
