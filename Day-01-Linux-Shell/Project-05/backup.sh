#!/bin/bash

SOURCE="$HOME/backup-project/app"
BACKUP_DIR="$HOME/backup-project/backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/app_$TIMESTAMP.tar.gz"


mkdir -p  "$BACKUP_DIR"

if [ "$1" = "backup" ]; then

    echo "Starting backup..."

    if tar -czf "$BACKUP_FILE" -C "$HOME/backup-project" app; then
        echo "Backup created successfully"
        echo "Backup file: $BACKUP_FILE"
    else
        echo "Backup failed"
        exit 1
    fi

elif [ "$1" = "restore" ]; then

    echo "Available backups:"
    ls -1t "$BACKUP_DIR"/*.tar.gz

    LATEST_BACKUP=$(ls -t "$BACKUP_DIR"/*.tar.gz | head -1)

    echo "Restoring: $LATEST_BACKUP"

    if tar -xzf "$LATEST_BACKUP" -C "$HOME/backup-project"; then
        echo "Restore completed successfully"
    else
        echo "Restore failed"
        exit 1
    fi

else

    echo "Usage:"
    echo "./backup.sh backup"
    echo "./backup.sh restore"
    exit 1

fi
