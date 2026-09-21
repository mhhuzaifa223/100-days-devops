#!/bin/bash

PROCESS="sleep"

if pgrep -x "$PROCESS" > /dev/null; then
   echo "Process is $PROCESS is running"
else 
   echo "ALERT: Process $PROCESS is not running"
   echo "Restarting $PROCESS...."
   
   "$PROCESS" 300 &
   sleep 1

   if pgrep -x "$PROCESS" > /dev/null; then
      echo "Process $PROCESS restarted successfully"
   else
      echo "ERROR: Failed to restart $PROCESS"
      exit 1
      fi
fi
