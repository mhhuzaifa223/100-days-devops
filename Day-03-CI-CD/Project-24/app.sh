#!/bin/bash

echo "Application: Multi-Environment CI/CD"
echo "Environment: ${APP_ENV:-undefined}"
echo "Version: ${APP_VERSION:-undefined}"

if [ "$APP_ENV" = "production" ]; then
    echo "Production configuration active"
elif [ "$APP_ENV" = "staging-broken" ]; then
    echo "Staging configuration active"
elif [ "$APP_ENV" = "development" ]; then
    echo "Development configuration active"
else
    echo "Unknown environment"
    exit 1
fi
