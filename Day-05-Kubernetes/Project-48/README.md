# Project 48 — Zero-Downtime Rolling Deployment

## Objective

Deploy an application using a Kubernetes RollingUpdate strategy that maintains application availability during version upgrades and protects healthy Pods when a new version fails.

## Technologies

- Kubernetes
- Kind
- kubectl
- NGINX
- Kubernetes Deployments
- Kubernetes Services
- RollingUpdate
- Readiness Probes

## How It Works

The Deployment runs three NGINX replicas.

The rolling update strategy is configured with:

- `maxUnavailable: 0`
- `maxSurge: 1`

This means Kubernetes keeps all three existing replicas available while creating one additional Pod during an update.

A new Pod must become Ready before an old Pod is removed.

A readiness probe checks the NGINX HTTP endpoint before the Pod is considered Ready.

## Project Structure

    Project-48/
    ├── k8s/
    │   ├── deployment.yaml
    │   └── service.yaml
    └── README.md

## Application

Deployment:

    project-48-app

Service:

    project-48-service

Replicas:

    3

Initial image:

    nginx:1.25-alpine

Successful updated image:

    nginx:1.26-alpine

RollingUpdate configuration:

    maxUnavailable: 0
    maxSurge: 1

Readiness probe:

    HTTP GET /
    Port: 80

## How to Run

Apply the Deployment:

    kubectl apply -f k8s/deployment.yaml

Apply the Service:

    kubectl apply -f k8s/service.yaml

Check Pods:

    kubectl get pods -l app=project-48-app

Check the Service:

    kubectl get svc project-48-service

Check endpoints:

    kubectl get endpointslice -l kubernetes.io/service-name=project-48-service

Check rollout:

    kubectl rollout status deployment/project-48-app

## Rolling Update

The application was successfully updated from:

    nginx:1.25-alpine

to:

    nginx:1.26-alpine

The rollout completed successfully with all three replicas available.

The Service maintained three healthy endpoints throughout the deployment process.

## Testing / Failure Scenario

An intentional deployment failure was created using:

    kubectl set image deployment/project-48-app nginx=nginx:does-not-exist

The new Pod entered:

    ImagePullBackOff

The existing three Pods remained:

    1/1 Running

Because `maxUnavailable` was configured as `0`, Kubernetes did not remove the healthy Pods while the replacement Pod was unhealthy.

## Troubleshooting

The failed Pod was investigated using:

    kubectl get pods -l app=project-48-app

and:

    kubectl describe pod <failed-pod>

The Events section showed:

    Failed to pull image "nginx:does-not-exist"

and:

    docker.io/library/nginx:does-not-exist: not found

The root cause was an invalid container image tag.

## Recovery

The failed deployment was recovered using Kubernetes Deployment rollback:

    kubectl rollout history deployment/project-48-app

    kubectl rollout undo deployment/project-48-app

The rollout was then verified:

    kubectl rollout status deployment/project-48-app

Final state:

    READY: 3/3
    UP-TO-DATE: 3
    AVAILABLE: 3

Final image:

    nginx:1.26-alpine

## Key Concepts Learned

- Kubernetes RollingUpdate strategy
- `maxUnavailable`
- `maxSurge`
- Readiness probes
- Deployment rollout status
- ReplicaSets
- ImagePullBackOff
- ErrImagePull
- Kubernetes Events
- Service endpoints
- Zero-downtime deployment principles
- Deployment rollback
- Desired state reconciliation
- Troubleshooting failed Kubernetes releases

## Result

Successfully implemented and tested a Kubernetes zero-downtime rolling deployment.

The project demonstrated both a successful application upgrade and a failed deployment scenario where Kubernetes protected healthy application replicas and enabled recovery through Deployment rollback.
