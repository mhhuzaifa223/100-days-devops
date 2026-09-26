# Project 24 — Multi-Environment CI/CD Pipeline

## Objective

Build a GitHub Actions CI/CD pipeline that promotes an application through:

Development → Staging → Production

The pipeline ensures that production only runs when staging succeeds.

## Technologies

- GitHub Actions
- Bash
- YAML
- Linux
- CI/CD
- Environment Variables

## Project Structure

Project-24/
├── app.sh
└── README.md

GitHub Actions workflow:

.github/workflows/project-24-multi-environment.yml

## Application

The application uses environment variables to determine the current deployment environment and version.

Variables used:

APP_ENV
APP_VERSION

Supported environments:

development
staging
production

## Local Test

Run the application locally:

APP_ENV=development APP_VERSION=1.0.0 ./app.sh

Example output:

Application: Multi-Environment CI/CD
Environment: development
Version: 1.0.0
Development configuration active

## CI/CD Pipeline

The pipeline contains three sequential jobs:

Development
    ↓
Staging
    ↓
Production

Development runs first.

Staging depends on Development.

Production depends on Staging.

The workflow uses GitHub Actions `needs` to control the deployment order.

## Environment Configuration

Development:

APP_ENV=development
APP_VERSION=1.0.0

Staging:

APP_ENV=staging
APP_VERSION=1.0.0-rc

Production:

APP_ENV=production
APP_VERSION=1.0.0

## Pipeline Dependency

Staging uses:

needs: development

Production uses:

needs: staging

This means a failed environment prevents the next environment from running.

## Failure Testing

The staging environment was intentionally broken by changing the staging condition in app.sh.

The pipeline then produced:

Development: SUCCESS
Staging: FAILED
Production: SKIPPED

This confirmed that the production stage is protected by the staging result.

## Troubleshooting

The first attempt to modify the staging condition did not change the file because the command searched for:

APP_ENV=staging

The actual Bash condition was:

"$APP_ENV" = "staging"

The file was inspected with grep to identify the correct text before modifying it.

After correcting the condition, the pipeline was committed and pushed again.

## Recovery

The staging condition was restored to:

"$APP_ENV" = "staging"

The pipeline was executed again.

Final result:

Development: SUCCESS
Staging: SUCCESS
Production: SUCCESS

## Key Concepts Learned

- Multi-environment CI/CD
- GitHub Actions jobs
- Job dependencies
- `needs`
- Environment variables
- Development environments
- Staging environments
- Production environments
- Deployment gates
- Failure testing
- Pipeline troubleshooting
- CI/CD recovery

## Result

Project 24 successfully demonstrates a controlled CI/CD promotion process from Development to Staging to Production.

A staging failure automatically prevents production from running, providing a basic safety mechanism for production deployments.
