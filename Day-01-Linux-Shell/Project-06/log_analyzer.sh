#!/bin/bash

LOG_FILE="$HOME/log-project/app.log"

if [ ! -f "$LOG_FILE" ]; then
   echo "Error: Log file not found: $LOG_FILE"
   exit 1
fi

echo "====== Log Analysis ======"

ERRORS=$(grep -c "ERROR" "$LOG_FILE")
WARNING=$(grep -c "WARNING" "$LOG_FILE")
DATABASE_ERRORS=$(grep -c "Database connection failed" "$LOG_FILE")
AUTH_ERRORS=$(grep -c "Authentication failed" "$LOG_FILE")

echo "Errors: $ERRORS"
echo "Warning: $WARNING"
echo "Database errors: $DATABASE_ERRORS"
echo "Authentication errors: $AUTH_ERRORS"

if [ "$ERRORS" -gt 0 ]; then
   echo "Status: ATTENTION REQUIRED"
else 
   echo "Status: OK"
fi

echo ""
echo "Recent Errors:"
grep "ERROR" "$LOG_FILE" | tail -5
