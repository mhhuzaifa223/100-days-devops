#!/bin/bash

SOURCE="$HOME/backup-solution/app"
BACKUP_DIR="$HOME/backup-solution/backups"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/app_$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

if [ "$1" = "backup" ]; then

    echo "Starting backup..."

    if [ ! -d "$SOURCE" ]; then
        echo "ERROR: Source directory does not exist: $SOURCE"
        exit 1
    fi

    if tar -czf "$BACKUP_FILE" -C "$HOME/backup-solution" app; then
        echo "Backup created successfully"
        echo "Backup: $BACKUP_FILE"
    else
        echo "ERROR: Backup failed"
        exit 1
    fi

    echo "Cleaning old backups..."

    ls -t "$BACKUP_DIR"/*.tar.gz | tail -n +4 | xargs -r rm

    echo "Keeping latest 3 backups"

elif [ "$1" = "restore" ]; then

    LATEST_BACKUP=$(ls -t "$BACKUP_DIR"/*.tar.gz 2>/dev/null | head -1)

    if [ -z "$LATEST_BACKUP" ]; then
        echo "ERROR: No backup found"
        exit 1
    fi

    echo "Restoring: $LATEST_BACKUP"

    if tar -xzf "$LATEST_BACKUP" -C "$HOME/backup-solution"; then
        echo "Restore completed successfully"
    else
        echo "ERROR: Restore failed"
        exit 1
    fi

else

    echo "Usage:"
    echo "./backup_solution.sh backup"
    echo "./backup_solution.sh restore"
    exit 1

fi
