# Project 17 — Git Hooks for Code Validation

## Objective

Learn how Git hooks can automatically run validation checks before Git operations such as commits.

## Technologies

- Git
- Bash
- Linux

## What I Practiced

- Understanding Git hooks
- Creating a pre-commit hook
- Making the hook executable
- Running validation before a commit
- Preventing invalid changes from being committed
- Testing successful validation
- Testing failed validation
- Understanding local Git automation

## Workflow

Developer Changes → git commit → Pre-Commit Hook → Validation → Commit Allowed or Rejected

## Commands Used

- git status
- git add
- git commit
- chmod +x
- ls -la
- mkdir
- cat

## Testing

A pre-commit hook was configured to perform a validation check before allowing a commit.

A valid change was tested to confirm that the commit was allowed.

An invalid change was then introduced to verify that the hook could reject the commit before it entered the Git history.

## Key Concepts Learned

- Git hooks
- Pre-commit hooks
- Local Git automation
- Automated validation
- Commit validation
- Executable scripts
- Preventing invalid commits

## Why This Matters

Git hooks can automate quality checks before changes enter the repository.

They can help catch simple problems early and prevent developers from committing changes that do not meet defined validation requirements.
