# Project 23 — CI Environment Variables and Secrets

## Objective

Learn how CI pipelines use environment variables and securely consume sensitive values through GitHub Secrets.

## Technologies

- Bash
- Linux
- Git
- GitHub
- GitHub Actions
- GitHub Secrets

## Project Structure

    100-days-devops/
    ├── .github/
    │   └── workflows/
    │       ├── ci.yml
    │       ├── project-22-tests.yml
    │       └── project-23-env.yml
    │
    └── Day-03-CI-CD/
        └── Project-23/
            ├── app.sh
            └── README.md

## Application

The application reads two environment variables:

    APP_NAME
    APP_ENV

The application does not contain these values directly in the source code.

Example:

    echo "Application: $APP_NAME"
    echo "Environment: $APP_ENV"

## CI Environment Variables

The GitHub Actions workflow defines:

    APP_NAME: DevOps-CI-App
    APP_ENV: testing

These variables are available to the application during the CI job.

The workflow executes:

    bash Day-03-CI-CD/Project-23/app.sh

## GitHub Secret

A repository secret named:

    DEMO_SECRET

was created in GitHub.

The secret value was never placed inside the repository.

The workflow receives it at runtime:

    DEMO_SECRET: ${{ secrets.DEMO_SECRET }}

This keeps the sensitive value outside the source code.

## Secret Availability Check

The pipeline verifies that the secret exists without printing its value:

    if [ -n "$DEMO_SECRET" ]; then
      echo "Secret is available to the CI job"
    else
      echo "Secret is missing"
      exit 1
    fi

This checks whether the variable contains a value.

## Secret Masking Test

A temporary test intentionally printed the secret value:

    echo "Secret value: $DEMO_SECRET"

GitHub Actions masked the secret in the workflow logs instead of displaying the actual value.

The temporary test was then removed.

This demonstrated that GitHub Secrets are injected at runtime and GitHub masks recognized secret values in logs.

## Workflow

The workflow is stored at:

    .github/workflows/project-23-env.yml

The workflow:

    1. Checks out the repository.
    2. Defines CI environment variables.
    3. Injects the GitHub Secret.
    4. Runs the application.
    5. Verifies the secret is available.
    6. Completes successfully.

## Troubleshooting

### Python-Based File Modification Did Not Change the Workflow

An automated text replacement initially made no changes because the expected text did not exactly match the workflow.

The actual workflow used:

    Verify Secret is available

while the replacement expected different capitalization.

The file was inspected directly before making the correction.

### YAML Syntax Error

A temporary secret-masking step caused GitHub to report:

    Invalid workflow file

The shell command was changed to YAML multiline syntax:

    run: |
      echo "Secret value: $DEMO_SECRET"

The workflow then passed successfully.

## Security Principles

Sensitive values should not be hardcoded into:

- Source code
- README files
- Git commits
- Workflow files

Instead, sensitive values should be stored in an appropriate secret-management system and injected into CI jobs when required.

## Key Concepts Learned

- Environment variables
- GitHub Actions environment variables
- GitHub repository secrets
- Runtime secret injection
- Secret masking
- YAML multiline commands
- CI security
- Sensitive data handling
- Repository security
- CI troubleshooting

## Result

The project successfully demonstrated how a CI pipeline can:

- Use normal environment variables.
- Consume GitHub Secrets.
- Verify secret availability without exposing the value.
- Mask sensitive values in workflow logs.
- Keep secrets outside the Git repository.

The temporary secret-printing test was removed after verification.
