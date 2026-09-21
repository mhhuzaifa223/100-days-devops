# Project 05 — Automated Backup & Restore System

## Objective

Build a Bash script that creates compressed backups of application data and provides a reliable way to restore the data.

## Technologies

* Linux
* Bash
* `tar`
* Gzip compression
* File system operations
* Command-line arguments

## How It Works

```text
Application Data
      ↓
Create Timestamp
      ↓
Create .tar.gz Backup
      ↓
Store Backup
      ↓
Delete Application Data
      ↓
Restore Backup
      ↓
Verify Files
```

The practice application contains:

```text
backup-project/
└── app/
    ├── config.txt
    └── data/
        ├── users.txt
        └── database.txt
```

## How to Run

Create a backup:

```bash
chmod +x backup.sh
./backup.sh backup
```

Restore the latest backup:

```bash
./backup.sh restore
```

## Backup Format

Backups are stored using timestamped filenames:

```text
app_YYYY-MM-DD_HH-MM-SS.tar.gz
```

The `tar` archive is compressed using gzip to reduce storage size.

## Example

```text
Starting backup...
Backup created successfully
Backup file: /home/seed/backup-project/backups/app_2026-09-20_17-46-49.tar.gz
```

During restore:

```text
Available backups:
app_2026-09-20_17-46-49.tar.gz

Restoring: /home/seed/backup-project/backups/app_2026-09-20_17-46-49.tar.gz
Restore completed successfully
```

## Testing

The backup system was tested by:

1. Creating a backup.
2. Confirming the archive contents.
3. Deleting the application directory.
4. Restoring the backup.
5. Verifying the restored files.

Verification:

```bash
find ~/backup-project/app -type f
```

Expected files:

```text
app/config.txt
app/data/users.txt
app/data/database.txt
```

## Troubleshooting

The archive contents can be inspected without extracting the backup:

```bash
tar -tzf backup.tar.gz
```

A backup can be extracted using:

```bash
tar -xzf backup.tar.gz
```

The `-C` option can be used to control the extraction directory and avoid unwanted directory structures.

## Key Concepts Learned

* Linux backups
* Bash scripting
* `tar`
* Gzip compression
* Command-line arguments
* Timestamped filenames
* Backup verification
* Restore procedures
* File deletion and recovery
* Safe disaster-recovery testing
