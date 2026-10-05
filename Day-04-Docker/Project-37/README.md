# Project 37 — Container Health Check & Auto-Recovery

## Objective

Implement a Docker health check for a Flask application and demonstrate container recovery after a process failure.

The project demonstrates the difference between:

- Container running state
- Application health
- Docker health checks
- Docker restart policies

## Technologies

- Docker
- Python
- Flask
- Docker HEALTHCHECK
- Docker restart policy
- Linux

## How It Works

The Flask application exposes a `/health` endpoint.

Docker periodically executes a health check against this endpoint.

The container was started with:

    --restart=unless-stopped

Architecture:

    Docker Container
          |
          v
    Flask Application
          |
          v
    /health endpoint
          |
          v
    Docker HEALTHCHECK
          |
          v
    healthy / unhealthy

## Project Structure

    Project-37/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    └── README.md

## How to Run

Build the image:

    docker build -t project-37:1.0 .

Run the container:

    docker run -d --name project-37 --restart=unless-stopped -p 8087:5000 project-37:1.0

Check container health:

    docker ps

Inspect health details:

    docker inspect --format='{{json .State.Health}}' project-37

Expected status:

    Up ... (healthy)

## Health Check

The Dockerfile contains:

    HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
      CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

The health endpoint returns HTTP 200 when the application is healthy.

## Testing / Failure Scenario

An attempt was made to use `pkill` inside the container:

    docker exec project-37 pkill -f "python app.py"

This failed because the slim Python image does not contain the `pkill` utility.

The container was then intentionally killed using:

    docker kill project-37

The container entered:

    Exited (137)

The container was manually started again:

    docker start project-37

The container initially showed:

    Up ... (health: starting)

After the health checks completed, the status returned to:

    Up ... (healthy)

## Important Concept

A Docker HEALTHCHECK does not itself restart a container.

It reports whether the application is healthy or unhealthy.

Restart policies handle container/process termination.

This project demonstrated the difference between:

    HEALTHCHECK
    healthy / unhealthy

and:

    restart policy
    running / stopped

## Troubleshooting

### Container is unhealthy

Inspect the health check:

    docker inspect --format='{{json .State.Health}}' project-37

Check application logs:

    docker logs project-37

Test the endpoint:

    curl http://localhost:8087/health

### Container exits

Check the stopped container:

    docker ps -a --filter name=project-37

Inspect the exit code and logs:

    docker logs project-37

## Key Concepts Learned

- Docker HEALTHCHECK
- Application health endpoints
- Healthy versus running state
- Docker restart policies
- Container exit codes
- Docker logs
- Container troubleshooting
- Minimal images and missing debugging utilities
- Production health monitoring

## Result

Successfully implemented a Docker health check and tested container failure and recovery.

The application returned to a healthy state after the container was restarted.
