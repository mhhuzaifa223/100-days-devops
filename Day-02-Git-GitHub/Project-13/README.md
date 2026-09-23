# Project 13 — Merge Conflict Simulation & Resolution

## Objective

Learn how Git handles conflicting changes made by different developers and how to safely resolve merge conflicts.

## Technologies

- Git
- GitHub
- Linux

## What I Practiced

- Creating separate Git branches
- Making changes to the same file on different branches
- Creating a merge conflict intentionally
- Detecting the conflict
- Inspecting Git conflict markers
- Choosing the correct changes
- Resolving the conflict
- Staging the resolved file
- Completing the merge

## Workflow

Main Branch → Feature Branches → Conflicting Changes → Merge → Conflict → Resolve → Stage → Commit

## Commands Used

- git switch -c
- git switch
- git status
- git add
- git commit
- git merge
- git diff

## Testing

Two branches were created and changes were made to the same section of a file.

When the branches were merged, Git detected conflicting changes that could not be merged automatically.

The conflict was inspected, the correct content was selected, the conflict markers were removed, and the resolved file was staged and committed.

## Key Concepts Learned

- Merge conflicts
- Conflict markers
- HEAD
- Current branch changes
- Incoming branch changes
- Manual conflict resolution
- Merge process
- Conflict resolution workflow

## Why This Matters

Merge conflicts are common when multiple developers modify the same files.

Knowing how to safely resolve conflicts helps prevent accidental loss of changes and keeps collaborative Git workflows reliable.
