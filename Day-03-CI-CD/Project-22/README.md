# Project 22 — CI Pipeline with Automated Testing

## Objective

Learn how Continuous Integration pipelines can automatically run tests whenever code changes are pushed to a repository.

## Technologies

- Git
- GitHub Actions
- YAML
- Linux
- Bash

## What I Practiced

- Creating an automated CI workflow
- Running tests automatically
- Defining multiple workflow steps
- Checking test results in GitHub Actions
- Understanding successful and failed test runs
- Using CI to detect problems before merging changes

## CI Testing Workflow

Developer → Push Code → GitHub Actions → Install/Prepare → Run Tests → Pass or Fail

## Files Used

- `.github/workflows/ci.yml`
- Test files used by the project

## Commands Used

- git status
- git add
- git commit
- git push

## Testing

Automated tests were configured as part of the CI pipeline.

The workflow was triggered by repository changes and executed the defined test commands automatically.

A successful run confirmed that the tests passed, while a failed test demonstrated how CI reports problems to the developer.

## Key Concepts Learned

- Automated testing
- Continuous Integration
- GitHub Actions
- Test automation
- Workflow steps
- CI feedback
- Failed pipeline detection
- Automated quality checks

## Why This Matters

Automated testing in CI helps detect bugs and broken changes early.

Instead of relying only on manual testing, every code change can be automatically checked before it is merged or released.
