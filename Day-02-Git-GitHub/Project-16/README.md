# Project 16 — Automated Semantic Versioning

## Objective

Learn how semantic versioning can be used to consistently identify software releases based on the type of changes introduced.

## Technologies

- Git
- GitHub
- Linux
- Bash

## What I Practiced

- Understanding semantic versioning
- Using MAJOR, MINOR, and PATCH version numbers
- Identifying the appropriate version increment
- Creating release tags based on semantic versions
- Checking existing version tags
- Automating version selection with a Bash script

## Semantic Versioning

Semantic versions follow this structure:

MAJOR.MINOR.PATCH

- MAJOR — breaking or incompatible changes
- MINOR — new backward-compatible functionality
- PATCH — backward-compatible bug fixes

## Commands Used

- git tag
- git tag -l
- git log
- git describe --tags
- git show
- git push --tags
- chmod +x

## Testing

Different types of changes were mapped to the appropriate semantic version increment.

A version tag was created using the resulting version number and checked against the Git commit history.

## Key Concepts Learned

- Semantic Versioning
- MAJOR version
- MINOR version
- PATCH version
- Release tags
- Version consistency
- Automated release versioning
- Backward compatibility

## Why This Matters

Consistent versioning makes software releases easier to understand and manage.

Semantic Versioning provides developers and users with a predictable way to understand whether a release contains breaking changes, new functionality, or bug fixes.
