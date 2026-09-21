#!/bin/bash

echo "========System health Report=========="
echo "Hostname: $(hostname)"

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}' )

Memory=$(free | awk '/Mem:/ {printf "%.1f", ($2-$7)/$2*100}')

Disk=$(df -h / | awk 'NR==2 {print $5}')

SSH_Status=$(systemctl is-active ssh)
echo "SSH: $SSH_Status"

UPTIME=$(uptime -p)
echo "Uptime: $UPTIME"

if (( ${CPU%.*} < 70 )); then
    CPU_STATUS="OK"
elif (( ${CPU%.*} < 90 )); then
    CPU_STATUS="WARNING"
else
    CPU_STATUS="CRITICAL"
fi
echo "CPU Usage: $CPU% [$CPU_STATUS]"

if (( ${Memory%.*} < 70 )); then
   MEMORY_STATUS="OK"
elif (( ${Memory%.*} < 90 )); then
   MEMORY_STATUS="WARNING"
else
   MEMORY_STATUS="CRITICAL"
fi
echo "Memory Usage: $Memory%[$MEMORY_STATUS]"

DISK_NUMBER=${Disk%\%}
if (( DISK_NUMBER < 70 )); then
    DISK_STATUS="OK"
elif (( DISK_NUMBER < 90)); then
    DISK_STATUS="WARNING"
else
    DISK_STATUS="CRITICAL"
fi
echo "Disk Usage: $Disk [$DISK_STATUS]"

if [[ "$CPU_STATUS" == "CRITICAL" || "$MEMORY_STATUS" == "CRITICAL" || "$DISK_STATUS" == "CRITICAL" || "$SSH_Status" == "inactive" ]]; then
   OVERALL_STATUS="CRITICAL"
elif [[ "$CPU_STATUS" == "WARNING" || "$MEMORY_STATUS" == "WARNING" || "$DISK_STATUS" == "WARNING" ]]; then
   OVERALL_STATUS="WARNING"
else
   OVERALL_STATUS="OK"
fi
echo "Overall Status: $OVERALL_STATUS"
echo "==============================="
