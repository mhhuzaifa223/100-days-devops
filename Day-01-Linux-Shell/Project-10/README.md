# Project 10 — Automated Backup & Restore Solution

## Objective

Build a Bash-based backup and restore solution that creates compressed application backups, manages backup retention, and provides a reliable recovery process.

## Technologies

* Linux
* Bash
* `tar`
* Gzip compression
* `find`
* `ls`
* `head`
* `xargs`
* File system operations

## How It Works

```text
Application Data
      ↓
Validate Source
      ↓
Create Timestamp
      ↓
Create .tar.gz Backup
      ↓
Store Backup
      ↓
Apply Retention Policy
      ↓
Keep Latest 3 Backups
```

For recovery:

```text
Latest Backup
      ↓
Extract Archive
      ↓
Restore Application
      ↓
Verify Files
```

## Backup Structure

The practice application contains:

```text
backup-solution/
├── app/
│   ├── config.txt
│   └── data/
│       ├── users.txt
│       └── database.txt
└── backups/
```

## How to Run

Create a backup:

```bash
chmod +x backup_solution.sh
./backup_solution.sh backup
```

Restore the latest backup:

```bash
./backup_solution.sh restore
```

## Backup Retention

The solution keeps the **3 most recent backups**.

Older backups are automatically removed:

```bash
ls -t "$BACKUP_DIR"/*.tar.gz | tail -n +4 | xargs -r rm
```

This prevents unlimited backup growth and reduces unnecessary disk usage.

## Example Output

Backup:

```text
Starting backup...
Backup created successfully
Backup: /home/seed/backup-solution/backups/app_2026-09-21_17-30-00.tar.gz
Cleaning old backups...
Keeping latest 3 backups
```

Restore:

```text
Restoring: /home/seed/backup-solution/backups/app_2026-09-21_17-30-00.tar.gz
Restore completed successfully
```

## Testing

The solution was tested by:

1. Creating application data.
2. Creating multiple backups.
3. Verifying the retention policy.
4. Deleting the application directory.
5. Restoring the latest valid backup.
6. Verifying the restored files.

Backup contents can be inspected without extraction:

```bash
tar -tzf backup.tar.gz
```

Restored files can be verified with:

```bash
find ~/backup-solution/app -type f
```

## Failure Testing

A backup was intentionally tested after the application directory had been removed.

This exposed the risk of creating an empty or invalid backup.

The solution was improved by validating that the source directory exists before creating a backup:

```bash
if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Source directory does not exist"
    exit 1
fi
```

This prevents invalid backups from being created.

## Troubleshooting

Check available backups:

```bash
ls -lh ~/backup-solution/backups/
```

Inspect an archive:

```bash
tar -tzf backup.tar.gz
```

Check disk space:

```bash
df -h
```

If restoration fails, verify:

* The backup file exists.
* The archive is not corrupted.
* The destination directory exists.
* The backup contains the expected files.
* Sufficient disk space is available.

## Key Concepts Learned

* Automated backups
* Disaster recovery
* Bash scripting
* `tar`
* Gzip compression
* Backup retention
* Timestamped backups
* File validation
* Restore procedures
* Backup verification
* Failure testing
* Recovery automation
* Safe backup management
