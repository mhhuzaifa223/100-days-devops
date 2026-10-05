# Project 31 — Containerize a Real Web Application

## Objective
Containerize a Flask web application using Docker and run it inside a Docker container.

## Technologies
- Docker
- Python
- Flask
- Dockerfile
- Docker Image
- Docker Container

## How It Works
The Flask application runs on port 5000 inside the container.
Docker maps host port 8085 to container port 5000.

Application → Dockerfile → Docker Image → Docker Container → Host Port 8085

## Project Structure
Project-31/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

## Application
The Flask application provides two endpoints:
- `/` — Main application endpoint
- `/health` — Application health endpoint

## How to Run
cd ~/100-days-devops/Day-04-Docker/Project-31
docker build -t project-31:1.0 .
docker run -d --name project-31 -p 8085:5000 project-31:1.0
docker ps
curl http://localhost:8085
curl http://localhost:8085/health

## Example Output
Application:
Project 31 - Hello From Docker

Health:
{"status":"healthy"}

## Testing / Failure Scenario
The `/health` endpoint initially contained an incorrect Python dictionary syntax:

return {"status:" "healthy"}

This caused a 500 Internal Server Error.

The issue was fixed to:

return {"status": "healthy"}

The Docker image was rebuilt and the container recreated because the source code had already been copied into the image.

## Troubleshooting
Check containers:
docker ps

Check logs:
docker logs project-31

Check port mapping:
docker port project-31

Rebuild after source changes:
docker build -t project-31:1.0 .

Recreate the container:
docker rm -f project-31
docker run -d --name project-31 -p 8085:5000 project-31:1.0

## Key Concepts Learned
- Docker images vs containers
- Dockerfile
- Docker build
- Docker run
- Port mapping
- Container logs
- `.dockerignore`
- Flask inside Docker
- Rebuilding images after source changes
- Container troubleshooting

## Result
Successfully containerized the Flask web application and verified the application and health endpoints through Docker.
