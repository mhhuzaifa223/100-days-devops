# Project 11 — Git Repository & Commit Workflow

## Objective

Learn the fundamental Git workflow by creating a repository, tracking files, staging changes, creating commits, and inspecting Git history.

## Technologies

* Git
* Linux
* Bash

## Git Workflow

```text
Working Directory
       ↓
    git add
       ↓
Staging Area
       ↓
  git commit
       ↓
Git Repository
```

## What I Practiced

* Initializing a Git repository
* Tracking files
* Checking repository status
* Staging changes
* Creating commits
* Viewing commit history
* Inspecting changes with `git diff`

## Commands Used

```bash
git init
git status
git add
git commit
git log --oneline
git diff
```

## Testing

The application file was changed after the initial commit.

The change was inspected using:

```bash
git diff
```

The updated file was then staged and committed separately.

This created two commits:

```text
Add initial application file
Update application to version 2
```

## Key Concepts Learned

* Working directory
* Staging area
* Git repository
* Commits
* Commit hashes
* Git history
* `git diff`
* Meaningful commit messages
* Tracking file changes
