# Project 74: Automated Backup Script

## Overview
A Python utility that backs up files into timestamped ZIP archives and verifies archive integrity.

## Features
- Creates timestamped ZIP backups
- Recursively backs up source files
- Compresses files using ZIP_DEFLATED
- Verifies archive integrity
- Reports file count and archive size
- Handles missing source directories and empty folders

## Requirements
- Python 3.8+
- No third-party packages required

## Run
python backup.py

## Test
Inspect the generated archive:
unzip -l backups/*.zip

## Safety note
This project uses sample files in source_data/; it does not back up system files or databases directly.

## Learning outcomes
Practiced pathlib, datetime, ZIP archives, exception handling, and file verification.
