# Project 36 — Distroless / Minimal Production Container

## Objective

Build and run a Python application using a distroless container image.

The project demonstrates how minimal runtime images reduce unnecessary software and attack surface in production containers.

## Technologies

- Docker
- Python
- Distroless
- Debian
- Linux

## How It Works

The application uses:

    gcr.io/distroless/python3-debian12

The image contains the Python runtime and required application files without a traditional Linux shell or package manager.

Architecture:

    Distroless Runtime
          |
          +-- Python Runtime
          |
          +-- Application
          |
          +-- Required Libraries

## Project Structure

    Project-36/
    ├── app.py
    ├── Dockerfile
    └── README.md

## How to Run

Build the image:

    docker build -t project-36:1.0 .

Run the application:

    docker run --rm project-36:1.0

Expected output:

    Project 36 - Distroless Container
    Minimal production image is running

## Testing / Failure Scenario

An attempt was made to start a shell inside the distroless container:

    docker run --rm -it project-36:1.0 /bin/sh

The command failed because the distroless image does not contain `/bin/sh`.

Result:

    /usr/bin/python3.11: can't open file '/bin/sh': [Errno 2] No such file or directory

This demonstrates the minimal nature of the runtime image.

## Troubleshooting

### Cannot open a shell inside the container

This is expected behavior for a distroless image.

Distroless images intentionally omit common debugging utilities and shells.

Instead of modifying the running container, troubleshoot using:

    docker logs <container>

and external monitoring, health checks, metrics, or by rebuilding the image.

### Application does not start

Check the Dockerfile entrypoint and ensure the application file exists at the expected path.

## Key Concepts Learned

- Distroless images
- Minimal production containers
- Reduced attack surface
- Runtime-only container design
- Docker image security
- Container debugging limitations
- Application logging
- Production observability
- Security versus debugging tradeoffs

## Result

Successfully built and ran a Python application using a distroless production image.

An intentional shell-access test confirmed that the image does not contain a traditional shell, demonstrating its minimal runtime design.
