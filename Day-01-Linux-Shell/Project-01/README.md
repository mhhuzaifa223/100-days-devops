# Project 01 — Automated System Health Checker

## Objective

Build a Bash script that checks the health of a Linux server and reports important system metrics.

## What It Checks

* CPU usage
* Memory usage
* Disk usage
* SSH service
* System uptime
* Overall system status

## Technologies

* Linux
* Bash
* `top`
* `free`
* `df`
* `awk`
* `grep`
* `systemctl`

## How It Works

The script collects system information and compares resource usage against defined thresholds.

```text
Linux Server
     │
     ├── CPU
     ├── Memory
     ├── Disk
     ├── SSH
     └── Uptime
          │
          ▼
     Health Check
          │
          ▼
   OK / WARNING / CRITICAL
```

## How to Run

```bash
chmod +x health_check.sh
./health_check.sh
```

## Example Output

```text
CPU Usage: 18.8%
Memory Usage: 12.8%
Disk Usage: 38%
SSH Status: active
Uptime: up 42 minutes

Overall Status: OK
```

## Troubleshooting Test

SSH availability was intentionally tested by stopping the SSH service:

```bash
sudo systemctl stop ssh
```

The health checker detected that SSH was unavailable.

SSH was then restored:

```bash
sudo systemctl start ssh
```

The system was verified again.

## Key Concepts Learned

* Linux system monitoring
* Bash variables
* Command substitution
* Conditional statements
* `grep`
* `awk`
* `df`
* `free`
* `top`
* `systemctl`
* Exit/status codes
* Threshold-based alerts
* Troubleshooting
