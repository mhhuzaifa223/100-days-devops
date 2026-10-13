# Project 79: Python Network Connectivity Checker

## Overview
A Python CLI tool that resolves hostnames and tests TCP connectivity to a specified port.

## Features
- DNS hostname resolution
- Displays resolved IP addresses
- Tests TCP connections with a timeout
- Measures connection time in milliseconds
- Handles DNS failures, refused connections, and invalid ports
- Supports custom hostnames and ports

## Requirements
- Python 3.8+
- No third-party packages required

## Usage
Check HTTPS connectivity:
python network_checker.py

Check a specific host and port:
python network_checker.py example.com 443

Test a local port:
python network_checker.py localhost 1

## Learning outcomes
Practiced socket programming, DNS resolution, TCP connectivity, timing, command-line arguments, and exception handling.
