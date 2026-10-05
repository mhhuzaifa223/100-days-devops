# Project 29 — Blue/Green Deployment Pipeline

## Objective

Implement a Blue/Green deployment strategy using Kubernetes.

The project runs two application versions simultaneously and switches production traffic between them using a Kubernetes Service.

## Technologies

- Kubernetes
- Kind
- Docker
- kubectl
- Python
- Flask
- Jenkins

## Architecture

    Kubernetes Service
          |
          +---- BLUE deployment
          |
          +---- GREEN deployment

Only one version receives production traffic at a time.

## Blue Environment

Blue represents the current production version.

    BLUE
    Version 1
    2 replicas

The Service initially selects:

    app: project-29
    version: blue

## Green Environment

Green represents the new application version.

    GREEN
    Version 2
    2 replicas

Green is deployed and tested before receiving production traffic.

## Blue/Green Deployment Flow

    Blue running in production
            |
            v
    Deploy Green
            |
            v
    Test Green
            |
            v
    Switch Service selector
            |
            v
    Green receives production traffic

Blue remains available for rollback.

## Docker Images

Blue image:

    project-29-blue:latest

Green image:

    project-29-green:latest

Both images were loaded into the Kind Kubernetes node.

## Kubernetes Resources

### Blue Deployment

    k8s/blue-deployment.yaml

Runs two Blue replicas.

### Green Deployment

    k8s/green-deployment.yaml

Runs two Green replicas.

### Service

    k8s/service.yaml

The Service provides a stable endpoint and controls which version receives traffic.

## Traffic Switching

Initial selector:

    version: blue

Green cutover:

    kubectl patch service project-29 \
      -p '{"spec":{"selector":{"app":"project-29","version":"green"}}}'

Rollback:

    kubectl patch service project-29 \
      -p '{"spec":{"selector":{"app":"project-29","version":"blue"}}}'

No application pods need to be recreated during the traffic switch.

## Verification

Blue was verified with:

    Project 29 - BLUE Version

Green was verified with:

    Project 29 - GREEN Version

After switching the Service selector to Green, production traffic returned:

    Project 29 - GREEN Version

After rollback, production traffic returned:

    Project 29 - BLUE Version

## Rollback

Blue remains running while Green receives production traffic.

If Green has a problem, the Service selector can immediately be changed back to Blue.

This provides a fast rollback mechanism.

## Key Concepts Learned

- Blue/Green deployment
- Kubernetes Deployments
- Kubernetes Services
- Service selectors
- Traffic switching
- Zero-downtime deployment strategy
- Pre-production validation
- Fast rollback
- Multiple application versions
- Desired state

## Result

Project 29 successfully demonstrated:

- Blue deployment
- Green deployment
- Independent validation of Green
- Production traffic switching
- Blue/Green rollback

The application was switched from Blue to Green and successfully rolled back to Blue.

