# Project 71: Python System Health Monitor

## Overview
A Python script that monitors basic Linux system health.

## Features
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- SSH service status check
- OK, WARNING, and CRITICAL thresholds
- Overall system health status

## Requirements
- Python 3
- psutil

## Setup
python3 -m venv .venv
source .venv/bin/activate
pip install psutil

## Run
python health_monitor.py

## Thresholds
- OK: below 70%
- WARNING: 70% to below 90%
- CRITICAL: 90% or above

## Learning outcomes
Practiced Python functions, conditionals, system metrics, subprocess execution, and basic monitoring.
