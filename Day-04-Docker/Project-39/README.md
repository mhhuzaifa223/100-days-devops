# Project 39 — Private Docker Registry

## Objective

Build and operate a private Docker registry locally, push Docker images to it, verify stored images, pull images back, and troubleshoot registry availability failures.

## Technologies

- Docker
- Docker Registry
- Docker CLI
- REST API
- Private Container Registry

## How It Works

The project uses the official Docker Registry image to run a private registry locally.

The workflow is:

    Docker Image
        ↓
    Tag for Registry
        ↓
    Push
        ↓
    Private Registry
        ↓
    Pull

The registry runs on:

    localhost:5000

## Project Structure

    Project-39/
    └── README.md

## Registry Setup

The registry was started with:

    docker run -d \
      --name project-39-registry \
      --restart unless-stopped \
      -p 5000:5000 \
      registry:2

The registry was verified with:

    docker ps --filter name=project-39-registry

## Tagging the Image

An existing Project 37 image was tagged for the private registry:

    docker tag project-37:1.0 localhost:5000/project-37:1.0

The image tag was verified with:

    docker images | grep project-37

## Push to Private Registry

The image was pushed using:

    docker push localhost:5000/project-37:1.0

The registry returned a successful image digest.

## Registry Verification

The registry catalog was checked using:

    curl http://localhost:5000/v2/_catalog

Result:

    {"repositories":["project-37"]}

The available tags were checked using:

    curl http://localhost:5000/v2/project-37/tags/list

Result:

    {"name":"project-37","tags":["1.0"]}

## Pull Test

The local registry tag was removed:

    docker rmi localhost:5000/project-37:1.0

The image was then pulled again from the private registry:

    docker pull localhost:5000/project-37:1.0

Docker successfully downloaded the image from the local registry.

## Failure Scenario

The registry container was intentionally stopped:

    docker stop project-39-registry

A pull was then attempted:

    docker pull localhost:5000/project-37:1.0

The operation failed with:

    connect: connection refused

This demonstrated that Docker could not reach the registry because the registry service was unavailable.

## Troubleshooting

The registry container was checked and then restarted:

    docker start project-39-registry

The image was pulled again:

    docker pull localhost:5000/project-37:1.0

The pull succeeded and Docker reported that the image was up to date.

## Key Concepts Learned

- Private Docker registries
- Docker image tagging
- Image push and pull
- Registry APIs
- Image digests
- Container networking
- Registry availability
- Connection refused errors
- Container service recovery
- Private image distribution

## Result

Successfully deployed and operated a private Docker registry, pushed and pulled Docker images, verified registry contents through its API, and recovered from an intentionally unavailable registry.

