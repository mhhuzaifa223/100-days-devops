# Project 21 — Basic CI Pipeline

## Objective

Build a basic GitHub Actions CI pipeline that validates and runs a Bash application.

## Technologies

- Git
- GitHub
- GitHub Actions
- Bash
- Linux

## Project Structure

    100-days-devops/
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    └── Day-03-CI-CD/
        └── Project-21/
            ├── app.sh
            └── README.md

## How It Works

1. Developer changes the application.
2. Developer pushes changes to GitHub or opens a Pull Request.
3. GitHub Actions starts an Ubuntu runner.
4. The repository is checked out.
5. Bash syntax is validated.
6. The application is executed.
7. The workflow passes or fails based on the command exit codes.

## CI Workflow

    name: Basic CI Pipeline

    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main

    jobs:
      validate:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Check Bash syntax
            run: bash -n Day-03-CI-CD/Project-21/app.sh

          - name: Run Application
            run: bash Day-03-CI-CD/Project-21/app.sh

## Local Testing

Check Bash syntax:

    bash -n app.sh

Run the application:

    ./app.sh

Expected output:

    DevOps CI Pipeline
    Application is running successfully

## Failure Testing

A missing quotation mark was intentionally introduced into app.sh.

The command:

    bash -n app.sh

returned:

    unexpected EOF while looking for matching '"'
    syntax error: unexpected end of file

The problem was fixed by restoring the missing quotation mark.

## Troubleshooting

### File Not Found

Initially the workflow tried:

    bash -n app.sh

The workflow runs from the repository root, while app.sh is located inside:

    Day-03-CI-CD/Project-21/

The correct path is:

    bash -n Day-03-CI-CD/Project-21/app.sh

### Untracked Files

The application must be committed and pushed to GitHub before GitHub Actions can access it.

Commands used:

    git add Day-03-CI-CD/Project-21/
    git commit -m "Add Project 21 CI application"
    git push

## Key Concepts Learned

- Continuous Integration
- GitHub Actions
- Workflow triggers
- Jobs
- Steps
- GitHub Actions runners
- Ubuntu runners
- YAML hierarchy
- YAML lists
- uses
- run
- Bash syntax validation
- Exit codes
- Repository-relative paths
- Git tracked vs untracked files
- CI troubleshooting

## Result

The CI pipeline successfully validates and executes the Bash application.

The pipeline was also intentionally broken and successfully troubleshot.

