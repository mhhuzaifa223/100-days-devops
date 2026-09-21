# Project 07 — Application Process Watchdog

## Objective

Build a Bash watchdog that monitors an application process and automatically restarts it when the process is no longer running.

## Technologies

* Linux
* Bash
* `pgrep`
* Process management
* Background processes
* `sleep`
* Process restart automation

## How It Works

```text
Check Application Process
          ↓
   Is Process Running?
       ↙       ↘
     YES        NO
      ↓          ↓
  Continue    Restart
                 ↓
          Verify Process
                 ↓
          Success / Failure
```

The practice watchdog monitors a test `sleep` process to simulate an application running on a Linux server.

## How to Run

```bash
chmod +x process_watchdog.sh
./process_watchdog.sh
```

## Example Output

When the process is running:

```text
Process sleep is running
```

When the process has stopped:

```text
ALERT: Process sleep is not running
Restarting sleep...
Process sleep restarted successfully
```

## Testing

The watchdog was tested by starting the process:

```bash
sleep 300 &
```

The process was then intentionally stopped:

```bash
pkill -x sleep
```

The watchdog detected that the process was no longer running and automatically restarted it.

The restarted process was verified using:

```bash
pgrep -x sleep
```

## Troubleshooting

Check whether the process is running:

```bash
pgrep -x sleep
```

List matching processes:

```bash
ps aux | grep sleep
```

If the watchdog cannot restart the process, verify that:

* The process name is correct.
* The application exists in the system `PATH`.
* The user has permission to start it.
* The application itself is not immediately crashing.

## Key Concepts Learned

* Linux processes
* Process IDs (PIDs)
* `pgrep`
* `ps`
* Background processes
* Process monitoring
* Automatic restart
* Failure detection
* Basic watchdog automation
* Verification after recovery
