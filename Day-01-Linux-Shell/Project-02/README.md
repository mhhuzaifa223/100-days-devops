# Project 02 — Disk Usage Alerting Script

## Objective

Build a Bash script that monitors Linux disk usage and generates alerts when storage consumption reaches defined thresholds.

## Technologies

* Linux
* Bash
* `df`
* `awk`
* Conditional statements
* Threshold-based alerting

## How It Works

```text
Check Disk Usage
       ↓
Extract Percentage
       ↓
Remove % Symbol
       ↓
Compare Threshold
       ↓
OK / WARNING / CRITICAL
```

The script monitors the root filesystem and uses the following thresholds:

* Below 80% → OK
* 80–89% → WARNING
* 90% or higher → CRITICAL

## How to Run

```bash
chmod +x disk_alert.sh
./disk_alert.sh
```

## Example Output

```text
Disk Usage: 38%
Status: OK
```

For a simulated high-usage condition:

```text
Disk Usage: 85%
Status: WARNING
ALERT: Disk usage is above 80%
```

Critical condition:

```text
Disk Usage: 95%
Status: CRITICAL
ALERT: Disk usage is critically high!
```

## Testing

High disk usage conditions were simulated by changing the value used for testing instead of filling the actual filesystem.

This allowed the alert logic to be tested safely without risking the Linux system.

## Troubleshooting

The script extracts the disk percentage from:

```bash
df -h / | awk 'NR==2 {print $5}'
```

The `%` symbol is then removed before numerical comparison:

```bash
DISK_NUMBER=${DISK%\%}
```

This allows Bash to compare the value numerically against the configured thresholds.

## Key Concepts Learned

* Linux disk monitoring
* `df -h`
* `awk`
* Bash variables
* String manipulation
* Numeric comparisons
* Threshold-based alerts
* Safe testing
* Monitoring automation
