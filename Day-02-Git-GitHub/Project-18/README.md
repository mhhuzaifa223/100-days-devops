# Project 18 — GitHub Protected Branch Production Workflow

## Objective

Learn how protected branches can prevent unsafe direct changes to important branches and enforce a controlled Pull Request workflow.

## Technologies

- Git
- GitHub
- Linux

## What I Practiced

- Understanding protected branches
- Working with the main branch as a protected branch
- Using feature branches for changes
- Creating Pull Requests
- Requiring review before merging
- Preventing direct changes to protected branches
- Merging approved changes through Pull Requests
- Understanding branch protection rules

## Workflow

Feature Branch → Commit → Push → Pull Request → Review → Approval → Merge into Protected Main Branch

## Commands Used

- git switch -c
- git switch
- git status
- git add
- git commit
- git push
- git pull

## Testing

A feature branch was used for development instead of modifying the main branch directly.

The changes were pushed to GitHub and integrated through a Pull Request workflow.

Branch protection rules were used to demonstrate how direct changes to the protected main branch can be restricted and controlled through the review process.

## Key Concepts Learned

- Protected branches
- Branch protection rules
- Pull Requests
- Required reviews
- Feature branches
- Main branch
- Code review
- Controlled merging
- Production branch protection

## Why This Matters

The main branch can represent production-ready code.

Branch protection helps prevent accidental or unreviewed changes from being merged directly into an important branch and encourages a controlled development and review process.
