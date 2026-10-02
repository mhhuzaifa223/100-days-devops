# Project 26 — Jenkins Shared Library Project

## Objective

Learn how Jenkins Shared Libraries can be used to create reusable CI/CD pipeline code and avoid duplicating the same pipeline logic across multiple projects.

## Technologies

- Jenkins
- Groovy
- Git
- GitHub
- Linux

## What I Practiced

- Understanding Jenkins Shared Libraries
- Creating reusable pipeline functions
- Storing shared pipeline code in Git
- Using custom pipeline steps
- Calling shared functions from Jenkinsfiles
- Reusing the same CI/CD logic across multiple applications
- Versioning shared pipeline code

## Pipeline Workflow

Jenkinsfile → Load Shared Library → Call Reusable Functions → Execute Pipeline

## Shared Library Structure

- vars/ — reusable global pipeline functions
- src/ — reusable Groovy classes
- resources/ — supporting resources
- Jenkinsfile — consumes the shared library

## Example Workflow

1. Create a Git repository for the shared library.
2. Add reusable pipeline functions.
3. Configure Jenkins to load the shared library.
4. Reference the library from a Jenkinsfile.
5. Call reusable functions from the pipeline.
6. Run the pipeline.
7. Version the shared library using Git tags or branches.

## Commands Used

- git clone
- git status
- git add
- git commit
- git push
- git tag

## Testing

Multiple Jenkins pipelines can use the same shared library functions.

Changing the shared library allows common CI/CD logic to be maintained centrally instead of duplicating it in every Jenkinsfile.

## Key Concepts Learned

- Jenkins Shared Library
- Groovy
- Reusable pipeline code
- Custom pipeline steps
- Global variables
- Jenkinsfile
- Pipeline abstraction
- Library versioning
- Centralized CI/CD logic

## Why This Matters

Large organizations often have many CI/CD pipelines.

A shared library allows teams to standardize common pipeline logic, reduce duplication, and maintain CI/CD practices from a central version-controlled repository.
