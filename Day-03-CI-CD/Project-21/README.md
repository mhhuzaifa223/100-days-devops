# Project 21 — Basic CI Pipeline

## Objective

Learn the fundamentals of Continuous Integration by creating a simple automated pipeline that validates code whenever changes are pushed to a Git repository.

## Technologies

- Git
- GitHub Actions
- YAML
- Linux

## What I Practiced

- Understanding Continuous Integration
- Creating a GitHub Actions workflow
- Defining workflow triggers
- Creating CI jobs
- Running automated commands
- Checking pipeline results
- Understanding successful and failed CI runs

## CI Workflow

Developer → Git Push → GitHub Actions → CI Job → Validation → Pass or Fail

## Files Used

- `.github/workflows/ci.yml`

## Commands Used

- git status
- git add
- git commit
- git push

## Testing

A GitHub Actions workflow was configured to run automatically when changes were pushed to the repository.

The workflow executed validation commands and reported whether the CI job completed successfully.

## Key Concepts Learned

- Continuous Integration
- CI pipeline
- GitHub Actions
- Workflow
- Workflow trigger
- Job
- Step
- Automated validation
- Pipeline success and failure

## Why This Matters

Continuous Integration helps teams detect problems early by automatically validating changes whenever developers push code.

This reduces manual testing and provides fast feedback before changes move further through the delivery process.
