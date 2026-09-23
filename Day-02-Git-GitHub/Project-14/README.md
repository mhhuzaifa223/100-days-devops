# Project 14 — Clean History with Git Rebase

## Objective

Learn how Git rebase can be used to keep commit history clean and linear before integrating changes into the main branch.

## Technologies

- Git
- GitHub
- Linux

## What I Practiced

- Creating a feature branch
- Making commits on the feature branch
- Updating the feature branch with changes from the main branch
- Using git rebase
- Resolving rebase conflicts when required
- Continuing a rebase
- Inspecting the resulting commit history
- Understanding the difference between rebase and merge

## Workflow

Main Branch → Feature Branch → New Main Changes → Rebase → Resolve Conflicts → Continue Rebase → Clean History

## Commands Used

- git switch
- git branch
- git add
- git commit
- git fetch
- git rebase
- git status
- git log
- git rebase --continue

## Testing

A feature branch was created and commits were added to it.

Changes from the main branch were introduced while the feature branch was still in development. The feature branch was then rebased onto the updated main branch.

The resulting history was inspected to verify that the feature commits were replayed on top of the latest main branch changes.

## Key Concepts Learned

- Git rebase
- Linear history
- Commit replay
- Feature branch synchronization
- Rebase conflicts
- git rebase --continue
- Difference between merge and rebase
- Rewriting local commit history

## Why This Matters

Rebase can produce a cleaner and more linear project history by replaying feature commits on top of the latest base branch.

Rebase should be used carefully because it rewrites commit history and should generally be avoided on shared commits that other developers are already depending on.
