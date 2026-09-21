#!/bin/bash

while true;do

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
MEMORY=$(free | awk '/Mem:/ {printf "%.1f", ($2-$7)/$2*100}')
DISK=$(df -h / | awk 'NR==2 {print $5}')
UPTIME=$(uptime -p)
PROCESSES=$(ps aux | wc -l)

clear

echo "================================"
echo "       SYSTEM MONITOR"
echo "================================"
echo "CPU Usage:      $CPU%"
echo "Memory Usage:   $MEMORY%"
echo "Disk Usage:     $DISK"
echo "Uptime:         $UPTIME"
echo "Processes:      $PROCESSES"
echo "================================"

sleep 2
done
