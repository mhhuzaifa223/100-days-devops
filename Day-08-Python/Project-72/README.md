# Project 72: Python Log Analyzer

## Overview
A Python command-line tool that analyzes log files and summarizes INFO, WARNING, and ERROR entries.

## Features
- Counts INFO, WARNING, and ERROR entries
- Identifies repeated error messages
- Accepts a log filename as a command-line argument
- Reports missing files clearly

## Requirements
- Python 3.8+
- No third-party packages required

## Run
Analyze the sample log:
python log_analyzer.py

Analyze another log:
python log_analyzer.py /path/to/application.log

## Test
Try a nonexistent file:
python log_analyzer.py missing.log

## Learning outcomes
Practiced file handling, pathlib, Counter, command-line arguments, loops, conditionals, and error handling.
