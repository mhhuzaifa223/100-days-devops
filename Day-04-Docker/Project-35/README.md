# Project 35 — Multi-Stage Docker Build

## Objective

Build a Docker image using multiple stages so that build-time dependencies and tooling do not need to remain in the final production image.

## Technologies

- Docker
- Docker Multi-Stage Builds
- Python
- Linux

## How It Works

The Dockerfile contains two stages.

Builder stage:

    FROM python:3.12-slim AS builder

Dependencies are installed into a separate location.

Production stage:

    FROM python:3.12-slim

Only the required installed dependencies and application code are copied from the builder stage.

Architecture:

    Builder Stage
         |
         | install dependencies
         v
    /install
         |
         | COPY --from=builder
         v
    Production Image
         |
         v
    Python Application

## Project Structure

    Project-35/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── Dockerfile.single
    └── README.md

## How to Run

Build the multi-stage image:

    docker build -t project-35:1.0 .

Run the application:

    docker run --rm project-35:1.0

Expected output:

    Project 35 - Multi-Stage Docker Build
    Application running successfully

## Image Size Comparison

Multi-stage image:

    project-35:1.0
    131 MB

Single-stage comparison image:

    project-35-single:1.0
    139 MB

The multi-stage image was approximately 8 MB smaller in this example.

The size difference is small because this is a minimal Python application using a slim base image. The larger benefit of multi-stage builds appears when build tools, compilers, source code, and development dependencies are required.

## Testing / Failure Scenario

A single-stage Dockerfile was created for comparison.

Both images were built and their sizes were compared:

    docker images | grep project-35

The multi-stage image was smaller than the single-stage image.

## Troubleshooting

### Multi-stage COPY fails

Verify the builder stage name:

    AS builder

Then ensure the production stage uses:

    COPY --from=builder ...

### Application does not start

Run the image interactively or inspect the container logs:

    docker run --rm project-35:1.0

### Image is still large

Check the base image and installed dependencies.

Multi-stage builds reduce unnecessary build artifacts, but the final image still contains its runtime dependencies and base operating system.

## Key Concepts Learned

- Multi-stage Docker builds
- Builder stages
- Production stages
- `COPY --from`
- Runtime dependencies
- Build-time dependencies
- Image size optimization
- Production container optimization
- Minimal Docker images

## Result

Successfully created and tested a multi-stage Docker image and compared it against a single-stage build.

The multi-stage image was smaller and keeps the final runtime image focused on the application and its required dependencies.
