# Project 06 — Log Analysis & Error Detection Tool

## Objective

Build a Bash-based log analysis tool that detects errors and warnings in an application log and provides a quick summary of the system's log health.

## Technologies

* Linux
* Bash
* `grep`
* Regular expressions
* `tail`
* Command substitution

## How It Works

```text id="2u4k1a"
Application Log
      ↓
Check Log File
      ↓
Count ERROR entries
      ↓
Count WARNING entries
      ↓
Identify Error Categories
      ↓
Display Recent Errors
      ↓
OK / ATTENTION REQUIRED
```

The tool analyzes a practice application log containing application events, database errors, authentication failures, and warnings.

## How to Run

```bash id="u2qlb6"
chmod +x log_analyzer.sh
./log_analyzer.sh
```

## Example Output

```text id="5y6p7z"
====== Log Analysis ======
Errors: 2
Warnings: 1
Database errors: 1
Authentication errors: 1
Status: ATTENTION REQUIRED

Recent Errors:
2026-09-21 10:10:00 ERROR Database connection failed
2026-09-21 10:11:00 ERROR Authentication failed
```

## Log Analysis Commands

Count errors:

```bash id="cl0p5t"
grep -c "ERROR" app.log
```

Count warnings:

```bash id="4j2q2a"
grep -c "WARNING" app.log
```

Find multiple log levels:

```bash id="07u7nb"
grep -E "ERROR|WARNING" app.log
```

Show recent errors:

```bash id="2gh1kw"
grep "ERROR" app.log | tail -5
```

## Testing

The tool was tested with:

* Multiple `ERROR` entries
* `WARNING` entries
* Database connection failures
* Authentication failures
* A log file containing no errors
* A missing log file

When the log file was missing, the script exited safely instead of attempting to analyze a nonexistent file.

## Troubleshooting

The script checks whether the log file exists before processing it.

```bash id="1e9blp"
if [ ! -f "$LOG_FILE" ]; then
    echo "ERROR: Log file not found"
    exit 1
fi
```

This prevents misleading results and makes the script safer for automation.

## Key Concepts Learned

* Linux log analysis
* Bash scripting
* `grep`
* `grep -c`
* `grep -E`
* Regular expressions
* Pipes
* `tail`
* Command substitution
* File existence checks
* Error detection
* Basic log monitoring
