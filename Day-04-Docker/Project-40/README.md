# Project 40 — Production Three-Tier Containerized App

## Objective

Build a production-style three-tier application using Docker Compose with Nginx, Flask, and PostgreSQL.

## Technologies

- Docker
- Docker Compose
- Nginx
- Python
- Flask
- PostgreSQL
- Docker Networks
- Docker Volumes
- Container Health Checks

## Architecture

    Client
       |
       v
    Nginx :8088
       |
       v
    Flask :5000
       |
       v
    PostgreSQL :5432

The Nginx container is the only service exposed to the host.

Flask is accessible only through the Docker frontend network.

PostgreSQL is accessible only through the Docker backend network.

## Project Structure

    Project-40/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── nginx.conf
    └── app/
        ├── app.py
        └── requirements.txt

## Networks

Two isolated Docker networks are used:

    frontend
    Nginx <-> Flask

    backend
    Flask <-> PostgreSQL

This prevents PostgreSQL from being directly exposed to the host.

## Database Persistence

PostgreSQL uses a named Docker volume:

    project-40-db-data

This keeps database data available even when the PostgreSQL container is recreated.

## Health Checks

Both Flask and PostgreSQL have Docker health checks.

Flask health endpoint:

    /health

PostgreSQL health check uses:

    pg_isready

Nginx waits for the Flask service to become healthy.

Flask waits for PostgreSQL to become healthy.

## Running the Application

Start all services:

    docker-compose up -d

Check service status:

    docker-compose ps

## Application Tests

Test through Nginx:

    curl http://localhost:8088/

Health check:

    curl http://localhost:8088/health

Database connectivity:

    curl http://localhost:8088/db

Successful database response:

    {"database":"connected"}

## Failure Scenario

The PostgreSQL service was intentionally stopped:

    docker-compose stop db

The database endpoint was then tested:

    curl http://localhost:8088/db

The application returned a database error because the PostgreSQL service was unavailable.

The error demonstrated Docker service-name based communication and the effect of a failed backend dependency.

## Recovery

PostgreSQL was restarted:

    docker-compose start db

The application was tested again:

    curl http://localhost:8088/db

The database connection successfully recovered.

## Key Concepts Learned

- Three-tier architecture
- Reverse proxy
- Nginx
- Docker Compose
- Docker service discovery
- Internal Docker networks
- Network isolation
- Database persistence
- Docker volumes
- Health checks
- Service dependencies
- Failure recovery
- Production container architecture

## Result

Successfully deployed a production-style three-tier application using Nginx, Flask, and PostgreSQL with isolated networks, persistent storage, health checks, and failure recovery.
