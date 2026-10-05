# Project 30 — Production CI/CD with Automated Rollback

## Objective

Build a production-style Kubernetes deployment with rolling updates, health checks, deployment verification, failure detection, and rollback.

## Technologies

- Kubernetes
- Kind
- Docker
- kubectl
- Python
- Flask
- Jenkins

## Architecture

    GitHub
       ↓
    CI/CD Pipeline
       ↓
    Docker Image
       ↓
    Kubernetes Deployment
       ↓
    Rolling Update
       ↓
    Health Checks
       ↓
    Production Service

If a deployment fails, Kubernetes can roll back to the previous working version.

## Application

The Flask application provides:

    /
    
and:

    /health

The health endpoint is used by Kubernetes readiness and liveness probes.

## Docker

The production image uses Python 3.12 and Flask.

Build:

    docker build -t project-30:1.0.0 Day-03-CI-CD/Project-30

Load into Kind:

    kind load docker-image project-30:1.0.0 --name devops-lab

## Kubernetes Deployment

The Deployment uses a RollingUpdate strategy.

Configuration:

    maxUnavailable: 0
    maxSurge: 1

This means Kubernetes does not intentionally make all existing replicas unavailable during an update.

## Health Checks

The application uses:

- Readiness probe
- Liveness probe

Readiness determines whether a Pod should receive traffic.

Liveness determines whether Kubernetes should consider the application unhealthy.

The probes use:

    /health

## Initial Production Version

The initial application version was:

    project-30:1.0.0

The deployment was verified with:

    kubectl rollout status deployment/project-30

The Pods reached Running and Ready status.

## Production Service

The application is exposed through a Kubernetes ClusterIP Service.

Test locally:

    kubectl port-forward service/project-30 8084:80

Then:

    curl http://localhost:8084
    curl http://localhost:8084/health

Expected application response:

    Project 30 - Production Application v1.0.0

## Failure Simulation

A broken version was intentionally created:

    project-30:2.0.0

The new version contained an invalid readiness probe configuration.

The application itself could start, but the Kubernetes health check could not succeed.

This simulated a production deployment failure.

## Failed Rollout

The Deployment was updated to version 2:

    project-30:2.0.0

The rollout was monitored with:

    kubectl rollout status deployment/project-30 --timeout=30s

The rollout could not successfully complete because the new Pods did not become Ready.

This demonstrated why health checks are important in production deployments.

## Rollback

The previous stable version was restored with:

    kubectl rollout undo deployment/project-30

Then the deployment was verified:

    kubectl rollout status deployment/project-30

The deployment returned to:

    project-30:1.0.0

## Deployment Flow

Successful deployment:

    Version 1
       ↓
    Production
       ↓
    Deploy Version 2
       ↓
    Health Checks
       ↓
    Ready
       ↓
    Production

Failed deployment:

    Version 1
       ↓
    Deploy Version 2
       ↓
    Health Check Failure
       ↓
    Rollout Failure
       ↓
    Rollback
       ↓
    Version 1
       ↓
    Healthy Production

## Key Concepts Learned

- Production CI/CD
- Kubernetes Deployments
- RollingUpdate
- Readiness probes
- Liveness probes
- Deployment health
- Rollout status
- Deployment history
- Kubernetes rollback
- Zero-downtime deployment strategy
- Failure recovery
- Desired state
- Production safety

## Troubleshooting

### Pods are not Ready

Check:

    kubectl get pods

Then:

    kubectl describe pod <pod-name>

Check:

- Container logs
- Readiness probe
- Liveness probe
- Container port
- Application endpoint

### Rollout is stuck

Check:

    kubectl rollout status deployment/project-30

Then:

    kubectl describe deployment project-30

Check the Pods and events for the reason.

### Roll back a failed deployment

Use:

    kubectl rollout undo deployment/project-30

Then verify:

    kubectl rollout status deployment/project-30

## Result

Project 30 successfully demonstrated a production-style Kubernetes deployment with:

- Rolling updates
- Health checks
- Deployment verification
- Failure simulation
- Failed rollout detection
- Automated rollback

The stable version was restored after the intentionally broken deployment failed its health checks.

