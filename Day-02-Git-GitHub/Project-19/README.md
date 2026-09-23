# Project 19 — Git Disaster Recovery Project

## Objective

Learn how to recover Git work after accidental commits, deleted branches, unwanted changes, or other common repository mistakes.

## Technologies

- Git
- GitHub
- Linux

## What I Practiced

- Inspecting Git history
- Identifying previous commits
- Recovering previous versions of files
- Using Git reflog to locate previous repository states
- Recovering deleted branch references
- Understanding reset and revert
- Restoring work without losing useful history

## Recovery Workflow

Problem → Inspect History → Locate Correct Commit → Recover Changes → Verify Repository

## Commands Used

- git log
- git reflog
- git status
- git show
- git restore
- git reset
- git revert
- git branch

## Testing

A repository state was intentionally changed to simulate a common Git mistake.

Git history and the reflog were inspected to locate the previous valid state.

The required commit or changes were recovered and the repository was checked afterward to confirm that the expected files and history were restored.

## Key Concepts Learned

- Git disaster recovery
- Git reflog
- Commit history
- Deleted branches
- git reset
- git revert
- git restore
- Recovery from accidental changes
- Repository state recovery

## Why This Matters

Git stores references to previous repository states, making many accidental changes recoverable.

Understanding recovery commands is important because mistakes such as deleted branches, unwanted resets, or accidental changes can happen during normal development.
