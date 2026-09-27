# Project 23 — Docker Build & Push Pipeline

## Objective

Build a Docker image from an application, test it locally, and automate Docker image building and publishing using GitHub Actions and Docker Hub.

The pipeline also creates an immutable image tag based on the Git commit SHA.

## Technologies

- Docker
- Dockerfile
- Git
- GitHub
- GitHub Actions
- Docker Hub
- Bash

## Project Structure

    Project-23/
    ├── app.sh
    ├── Dockerfile
    └── README.md

## Application

The application is a simple Bash script:

    #!/bin/bash

    echo "Docker CI/CD Pipeline"
    echo "Application is running inside a container"

## Dockerfile

The Dockerfile:

1. Uses Ubuntu 24.04 as the base image.
2. Creates `/app` as the working directory.
3. Copies `app.sh` into the image.
4. Makes the script executable.
5. Runs the application when the container starts.

## Build Docker Image Locally

From the Project-23 directory:

    docker build -t devops-project-23 .

## Run Container Locally

    docker run --rm devops-project-23

Expected output:

    Docker CI/CD Pipeline
    Application is running inside a container

## Docker Image vs Container

A Docker image is a packaged template containing the application and its required environment.

A container is a running instance created from that image.

The workflow is:

    Dockerfile
        ↓
    Docker Image
        ↓
    Docker Container
        ↓
    Application

## CI/CD Pipeline

The GitHub Actions workflow performs the following steps:

    Git push
        ↓
    Checkout repository
        ↓
    Set up Docker Buildx
        ↓
    Login to Docker Hub
        ↓
    Generate Git commit SHA tag
        ↓
    Build Docker image
        ↓
    Push versioned image
        ↓
    Push latest image
        ↓
    Docker Hub

## GitHub Secrets

The workflow uses GitHub repository secrets:

    DOCKERHUB_USERNAME
    DOCKERHUB_TOKEN

The Docker Hub token is not stored directly in the workflow.

## Docker Image Tags

The pipeline creates two tags:

    latest

and:

    <7-character Git commit SHA>

Example:

    devops-project-23:latest
    devops-project-23:77cf833

The Git SHA tag allows an image to be traced back to the exact source-code commit that created it.

## Failure Testing and Troubleshooting

### Failure 1 — Incorrect Docker run option

Incorrect:

    docker run -rm devops-project-23

Correct:

    docker run --rm devops-project-23

The `--rm` option automatically removes the container after it stops.

### Failure 2 — Incorrect Bash shebang

The application initially contained:

    #!/bin/hash

This caused the container to fail because `/bin/hash` does not exist.

Correct:

    #!/bin/bash

The shebang tells Linux which interpreter should execute the script.

### Failure 3 — Dockerfile not tracked by Git

The Dockerfile existed locally but was not committed to Git.

GitHub Actions therefore could not find it.

The problem was identified with:

    git status

The Dockerfile appeared as:

    Untracked files:
        Day-03-CI-CD/Project-23/Dockerfile

After adding and pushing the file, the GitHub Actions build succeeded.

### Failure 4 — Incorrect Docker build path

The CI pipeline initially used an incorrect build path.

The Docker build context must point to:

    Day-03-CI-CD/Project-23

This directory contains:

    Dockerfile
    app.sh

### Failure 5 — YAML indentation

GitHub Actions initially rejected the workflow because `run:` was incorrectly indented.

Correct structure:

    - name: Build Docker image
      run: docker build ...

YAML indentation determines the structure of the workflow.

## Troubleshooting Approach

When a Docker build works locally but fails in CI:

1. Verify that required files are committed and pushed.
2. Verify the Docker build context/path.
3. Verify that the Dockerfile exists in the CI workspace.
4. Check Dockerfile syntax and instructions.
5. Check GitHub Actions YAML syntax and indentation.
6. Review the exact CI error before changing configuration.

## Key Concepts Learned

- Dockerfile
- Docker image
- Docker container
- Docker build context
- `docker build`
- `docker run`
- `--rm`
- Docker Hub
- Docker Buildx
- GitHub Actions
- GitHub Secrets
- Docker image tagging
- Git commit SHA
- Immutable image versions
- YAML indentation
- CI/CD troubleshooting
- Git tracked vs untracked files

## Result

Project 23 successfully implements an automated Docker CI/CD pipeline.

A push to the `main` branch triggers GitHub Actions, which builds the Docker image and publishes both the `latest` tag and a Git commit SHA tag to Docker Hub.
