# Project 75: Website Availability Checker

## Overview
A Python command-line tool that checks website availability, HTTP status, and response time.

## Features
- Accepts a URL as a command-line argument
- Measures response time in milliseconds
- Reports HTTP status codes
- Handles HTTP errors, connection failures, and timeouts
- Uses the system CA bundle for TLS certificate verification

## Requirements
- Python 3.8+
- Ubuntu system CA certificates

## Run
python website_checker.py https://example.com

## Learning outcomes
Practiced HTTP requests, SSL/TLS certificate verification, timing, command-line arguments, and exception handling.
