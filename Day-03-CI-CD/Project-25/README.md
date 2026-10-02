# Project 25 — Jenkins Shared Library

## Objective

Build a reusable Jenkins Shared Library and use it from a Jenkins Pipeline.

## Technologies

- Jenkins
- Jenkins Pipeline
- Groovy
- Git
- GitHub

## Architecture

GitHub Shared Library Repository
        |
        v
jenkins-shared-library
        |
        v
vars/helloPipeline.groovy
        |
        v
Jenkins Global Library: devops-lib
        |
        v
project-25-demo
        |
        v
helloPipeline('production')

## Shared Library Repository

The shared library is maintained in a separate GitHub repository.

Structure:

    jenkins-shared-library/
    └── vars/
        └── helloPipeline.groovy

## Shared Library Function

The reusable function is defined in vars/helloPipeline.groovy.

It accepts an environment parameter:

    helloPipeline('production')

The function prints:

    Hello from Jenkins Shared Library!
    Reusable CI/CD logic is working.
    Environment: production

## Jenkins Global Library Configuration

The library was configured in Jenkins using:

    Name: devops-lib
    Default version: main
    Retrieval method: Modern SCM
    SCM: Git
    Repository: jenkins-shared-library

The repository is public, so no Jenkins Git credentials were required.

## Jenkins Pipeline

The Jenkins pipeline imports the shared library:

    @Library('devops-lib') _

The shared function is then called with:

    helloPipeline('production')

## Successful Pipeline Output

The Jenkins Console Output showed:

    Hello from Jenkins Shared Library!
    Reusable CI/CD logic is working.
    Environment: production

Final result:

    Finished: SUCCESS

## Failure Scenario

During the initial setup, Jenkins could not find the configured main branch.

Error:

    Could not find main in remote references.

### Root Cause

The shared library repository did not initially have a remote main branch.

### Fix

The local branch was renamed to main:

    git branch -M main

Then it was pushed to GitHub:

    git push -u origin main

Jenkins was then able to load:

    devops-lib@main

and execute the shared library successfully.

## What This Project Demonstrates

- Jenkins Pipeline automation
- Jenkins Shared Libraries
- Reusable Groovy pipeline functions
- Global Trusted Pipeline Libraries
- GitHub-based Jenkins libraries
- Passing parameters to reusable functions
- Library version/branch management
- Jenkins SCM troubleshooting
- Separation of application pipelines and reusable CI/CD logic

## Result

Project 25 successfully demonstrates how common Jenkins automation logic can be centralized in a shared library and reused by Jenkins pipelines.

The shared library is maintained separately from the main 100-days-devops repository.
