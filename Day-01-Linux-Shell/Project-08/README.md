# Project 08 — Log Rotation Automation

## Objective

Build a Bash script that monitors log file size and automatically rotates and compresses logs when they exceed a defined size limit.

## Technologies

* Linux
* Bash
* `du`
* `awk`
* `mv`
* `gzip`
* `touch`
* File management

## How It Works

```text
Check Log Size
      ↓
Compare With Limit
      ↓
  Within Limit?
   ↙          ↘
 YES           NO
  ↓             ↓
Keep Log     Rotate Log
                ↓
          Compress Archive
                ↓
          Create New Log
```

The script uses a configurable size threshold. When the log exceeds the limit, the existing log is renamed with a timestamp, compressed with gzip, and replaced with a new empty log file.

## How to Run

```bash
chmod +x log_rotate.sh
./log_rotate.sh
```

## Example Output

When the log is below the configured limit:

```text
Log size: 500 bytes
Log size is within limit.
```

When the log exceeds the limit:

```text
Log size: 1500 bytes
Log exceeds limit. Rotation required.
Old log archived and compressed: /home/seed/log-rotation-project/app_2026-09-21_12-00-00.log.gz
New log created: /home/seed/log-rotation-project/app.log
```

## Testing

The script was tested using different log sizes.

A small log was used to verify that no rotation occurred.

A larger log was then created to trigger rotation.

The resulting archive was verified using:

```bash
ls -lh ~/log-rotation-project/
```

The compressed log contents were checked with:

```bash
zcat ~/log-rotation-project/app_*.log.gz
```

## Troubleshooting

Check the current log size:

```bash
du -b ~/log-rotation-project/app.log
```

List rotated logs:

```bash
ls -lh ~/log-rotation-project/
```

If the archive cannot be created, verify:

* The log file exists.
* The destination directory is writable.
* The script has execute permission.
* Sufficient disk space is available.

## Key Concepts Learned

* Linux log management
* Bash automation
* File size monitoring
* `du`
* `awk`
* File rotation
* Timestamped filenames
* Gzip compression
* `mv`
* `touch`
* Automated log maintenance
