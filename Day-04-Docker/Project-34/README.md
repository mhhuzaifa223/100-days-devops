# Project 34 — Docker Networking Lab

## Objective

Understand Docker container networking and demonstrate communication between containers using a custom Docker bridge network.

The project demonstrates Docker internal DNS, container-to-container communication, network isolation, and network recovery.

## Technologies

- Docker
- Docker Bridge Network
- Nginx
- Alpine Linux
- Docker DNS
- Linux

## How It Works

A custom Docker bridge network was created:

    project-34-network

Two containers were used:

    project-34-server
    project-34-client

The client communicated with the Nginx server using the container name:

    http://project-34-server

Docker's internal DNS resolved the container name to the server's container IP.

Architecture:

    Client Container
          |
          | HTTP
          v
    Docker Internal DNS
          |
          v
    project-34-server
          |
          v
        Nginx

## Project Structure

    Project-34/
    └── README.md

## How to Run

Create the network:

    docker network create project-34-network

Start the Nginx server:

    docker run -d --name project-34-server --network project-34-network nginx:alpine

Start a temporary client and connect to the server:

    docker run --rm --network project-34-network alpine:3.20 wget -qO- http://project-34-server

The client successfully retrieved the Nginx welcome page.

## Testing / Failure Scenario

The server was intentionally disconnected from the Docker network:

    docker network disconnect project-34-network project-34-server

The client then attempted to reach the server:

    docker run --rm --network project-34-network alpine:3.20 wget -qO- --timeout=3 http://project-34-server

The request failed with:

    wget: bad address 'project-34-server'

This demonstrated that Docker's internal DNS only resolves services/containers that are connected to the same network.

## Recovery

The server was reconnected:

    docker network connect project-34-network project-34-server

The client was tested again and successfully retrieved the Nginx welcome page.

## Troubleshooting

### Container name cannot be resolved

Check whether both containers are connected to the same network:

    docker network inspect project-34-network

If the server is missing from the network, reconnect it:

    docker network connect project-34-network project-34-server

### localhost vs container name

Inside a container:

    localhost

refers to that same container.

To communicate with another container on the same Docker network, use the other container's name.

Example:

    http://project-34-server

## Key Concepts Learned

- Docker bridge networks
- Custom Docker networks
- Container-to-container communication
- Docker internal DNS
- Container name resolution
- Network isolation
- Network disconnect/connect
- Difference between localhost and container names
- Troubleshooting Docker networking

## Result

Successfully demonstrated Docker container networking using a custom bridge network.

The client container communicated with the Nginx server using Docker's internal DNS, and an intentional network failure was created, diagnosed, and fixed.
