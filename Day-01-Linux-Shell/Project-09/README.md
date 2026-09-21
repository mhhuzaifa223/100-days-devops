# Project 09 — Real-Time System Monitor Dashboard

## Objective

Build a Bash-based terminal dashboard that continuously displays important Linux system metrics in real time.

## Technologies

* Linux
* Bash
* `top`
* `free`
* `df`
* `uptime`
* `ps`
* `clear`
* `sleep`

## What It Monitors

* CPU usage
* Memory usage
* Disk usage
* System uptime
* Number of running processes

## How It Works

```text
Collect System Metrics
        ↓
Display Metrics
        ↓
Wait 2 Seconds
        ↓
Refresh Dashboard
        ↓
Repeat
```

The dashboard continuously refreshes the terminal so the latest system information is displayed without manually running the commands again.

## How to Run

```bash
chmod +x system_monitor.sh
./system_monitor.sh
```

The dashboard can be stopped with:

```text
Ctrl+C
```

## Example Output

```text
================================
       SYSTEM MONITOR
================================
CPU Usage:      8.8%
Memory Usage:   12.8%
Disk Usage:     38%
Uptime:         up 1 hour, 20 minutes
Processes:      185
================================
```

The values change as the system workload changes.

## Testing

The dashboard was tested while the Linux system was running normally.

The refresh interval was set to two seconds:

```bash
sleep 2
```

System activity was observed while the dashboard continuously updated the displayed metrics.

The dashboard was stopped safely using:

```text
Ctrl+C
```

## Troubleshooting

The dashboard uses several standard Linux commands to collect metrics.

CPU:

```bash
top -bn1
```

Memory:

```bash
free
```

Disk:

```bash
df -h /
```

Uptime:

```bash
uptime -p
```

Processes:

```bash
ps aux
```

If a metric is incorrect, run the corresponding command manually to determine whether the problem is with the command or the dashboard script.

## Key Concepts Learned

* Real-time monitoring
* Bash `while` loops
* Infinite loops
* `clear`
* `sleep`
* CPU monitoring
* Memory monitoring
* Disk monitoring
* Process counting
* Command substitution
* Terminal dashboards
* Continuous system monitoring
