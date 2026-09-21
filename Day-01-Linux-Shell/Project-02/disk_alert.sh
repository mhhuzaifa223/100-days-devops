#!/bin/bash

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

DISK=$(df -h / | awk 'NR==2 {print $5}')
echo "Disk Usage: $DISK"

DISK_NUMBER=${DISK%\%}

if (( DISK_NUMBER >= 90 )); then
    echo "Status: CRITICAL"
    echo "ALERT: $TIMESTAMP WARNING  Disk usage is $DISK_NUMBER%"
elif (( DISK_NUMBER >= 80 )); then
    echo "Status: WARNING"
    echo "ALERT: $TIMESTAMP CRITICAL Disk usage is $DISK_NUMBER%"
else
    echo "Status: OK"
fi
