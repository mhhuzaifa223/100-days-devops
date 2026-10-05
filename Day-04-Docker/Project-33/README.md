# Project 33 — Persistent Database with Docker Volumes

## Objective

Demonstrate how Docker volumes provide persistent storage for databases.

The project creates a PostgreSQL database, stores data inside it, removes the database container, recreates the container, and verifies that the data remains available.

## Technologies

- Docker
- Docker Compose
- PostgreSQL
- Docker Volumes
- Linux

## How It Works

PostgreSQL runs inside a Docker container.

The PostgreSQL data directory is mounted to a named Docker volume:

    project-33-data:/var/lib/postgresql/data

The container can be deleted and recreated without losing the database data because the data is stored in the Docker volume.

Architecture:

    PostgreSQL Container
           |
           v
    Docker Named Volume
           |
           v
    Persistent Database Data

## Project Structure

    Project-33/
    ├── docker-compose.yml
    └── README.md

## How to Run

Start PostgreSQL:

    docker-compose up -d

Check the container:

    docker-compose ps

Connect to PostgreSQL:

    docker-compose exec db psql -U devops -d devops

## Database Test

A users table was created:

    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name TEXT
    );

Test data was inserted:

    INSERT INTO users (name) VALUES ('Huzaifa');

The data was verified with:

    SELECT * FROM users;

Example result:

    id |  name
    ---+---------
    1  | Huzaifa

## Testing / Failure Scenario

The PostgreSQL container was intentionally removed using:

    docker-compose down

The Docker volume was then checked:

    docker volume ls | grep project-33

The volume remained available.

The PostgreSQL container was recreated:

    docker-compose up -d

The database was queried again:

    docker-compose exec db psql -U devops -d devops -c "SELECT * FROM users;"

The original Huzaifa record was still present.

This proves that the database data survived container deletion.

## Important Warning

Do not use:

    docker-compose down -v

during the persistence test.

The `-v` option removes the Docker volumes and would delete the persistent database storage.

## Troubleshooting

### Data disappears after deleting a container

Check whether the database directory is mounted to a Docker volume:

    docker inspect project-33-db

Look for the volume mounted at:

    /var/lib/postgresql/data

### Container exists but database is empty

Check the volume:

    docker volume ls

Then inspect the container mounts:

    docker inspect project-33-db

Make sure the expected named volume is attached.

## Key Concepts Learned

- Docker volumes
- Persistent storage
- Disposable containers
- PostgreSQL containers
- Docker Compose
- Database persistence
- Named volumes
- Container lifecycle
- Difference between containers and persistent data
- `docker-compose down`
- `docker-compose down -v`
- Database recovery after container recreation

## Result

Successfully demonstrated persistent PostgreSQL storage using a Docker named volume.

The PostgreSQL container was removed and recreated while the database data remained intact.
