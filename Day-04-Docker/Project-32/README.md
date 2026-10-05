# Project 32 — Multi-Container Application with Docker Compose

## Objective

Build and run a multi-container application using Docker Compose.

The project demonstrates communication between:

- Flask web application
- PostgreSQL database
- Redis cache

The containers communicate through Docker Compose's internal network using service names.

## Technologies

- Docker
- Docker Compose
- Python
- Flask
- PostgreSQL
- Redis
- Linux

## How It Works

The Flask application runs in the `web` container.

The Flask container communicates with:

- PostgreSQL using the hostname `db`
- Redis using the hostname `redis`

Docker Compose automatically creates a network for the services and provides internal DNS resolution using service names.

Inside a container, `localhost` refers to that same container, not another service.

Architecture:

    Client
       |
       v
    Flask Web
       |
       +----> PostgreSQL
       |
       +----> Redis

## Project Structure

    Project-32/
    ├── app/
    │   ├── app.py
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── docker-compose.yml
    └── README.md

## Application

Available endpoints:

    /
    /health
    /db
    /cache

The `/db` endpoint verifies PostgreSQL connectivity.

The `/cache` endpoint verifies Redis connectivity.

## How to Run

Build and start all services:

    docker-compose up -d --build

Check running containers:

    docker-compose ps

Test the application:

    curl http://localhost:8086/
    curl http://localhost:8086/health
    curl http://localhost:8086/db
    curl http://localhost:8086/cache

Stop the application:

    docker-compose down

## Example Output

    Project 32 - Docker Compose Multi-Container App

    {"status":"healthy"}

    {"database":"connected"}

    {"redis":"project-32"}

## Testing / Failure Scenario

Redis was intentionally stopped:

    docker-compose stop redis

The `/cache` endpoint then returned a Redis connection/name-resolution error.

Redis was restored with:

    docker-compose start redis

The `/cache` endpoint returned successfully again.

This demonstrated how service availability affects communication between containers.

## Troubleshooting

### Docker Compose command not found

The system did not provide the `docker-compose-plugin` package, so the standalone Docker Compose package was installed and the legacy command was used:

    docker-compose

### Redis connection failure

The Flask application uses:

    redis:6379

rather than:

    localhost:6379`.

This is because Docker Compose service names provide internal DNS resolution between containers.

### PostgreSQL connection

The Flask application connects to:

    db:5432

because `db` is the PostgreSQL service name in Docker Compose.

## Key Concepts Learned

- Docker Compose
- Multi-container applications
- Docker Compose services
- Docker internal networking
- Service-name DNS resolution
- Container-to-container communication
- PostgreSQL containers
- Redis containers
- Environment variables
- Docker volumes
- `depends_on`
- Debugging container communication
- Difference between `localhost` and service names

## Result

Successfully built and deployed a multi-container application with Docker Compose.

All three services were running successfully:

- Flask
- PostgreSQL
- Redis

The project also included an intentional Redis failure and recovery test.
