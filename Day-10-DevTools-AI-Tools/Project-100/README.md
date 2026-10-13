# Project 100 — DevOps Cost Optimization Assistant

## Overview
A dependency-free Python FinOps prototype that reviews a sample cloud-resource inventory, calculates monthly costs, and highlights resources that may deserve cost-optimization investigation.

This is a rule-based prototype, not a real AI model. It does not connect to AWS or make infrastructure changes.

## Features
- Reads resource inventory from JSON.
- Calculates total monthly cost.
- Flags selected low-utilization non-production resources.
- Flags stopped EBS volumes for investigation.
- Reports the monthly cost associated with flagged resources.
- Includes automated tests.

## Requirements
- Python 3.8+
- No third-party dependencies

## Run
    python3 cost_optimizer.py

## Test
    python3 -m unittest -v

## Sample Results
The included inventory contains four fictional resources:
- Total monthly cost: $237.00
- Cost associated with flagged resources: $117.00
- Resources flagged for investigation: 3

The flagged amount is not guaranteed savings. It is the cost of resources selected for review.

## Safety and Limitations
- The inventory is sample data; no AWS APIs are called.
- Low CPU utilization does not by itself prove a resource is unnecessary.
- Verify ownership, workload patterns, dependencies, backups, snapshots, and retention requirements before making changes.
- Obtain authorization before modifying or deleting resources.
- The current rules are illustrative and do not account for all pricing, discounts, commitments, or regional differences.

## Skills Practiced
Python, JSON processing, unit testing, cost analysis, FinOps principles, and infrastructure safety.
