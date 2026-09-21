#!/bin/bash

LOG_FILE="$HOME/log-rotation-project/app.log"
MAX_SIZE=1000

SIZE=$(du -b "$LOG_FILE" | awk '{print $1}')

echo "Log size: $SIZE bytes"

if [ "$SIZE" -gt "$MAX_SIZE" ]; then
    echo "Log exceeds limit. Rotation required."
    TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
    ARCHIVE="$HOME/log-rotation-project/app_$TIMESTAMP.log"

    mv "$LOG_FILE" "$ARCHIVE"
    gzip "$ARCHIVE"

    touch "$LOG_FILE"

echo "Old log archived and compressed: $ARCHIVE.gz"
echo "New log created: $LOG_FILE"
else
    echo "Log size is within limit."
fi
