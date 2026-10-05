# Project 28 — Kubernetes Deployment Pipeline

## Objective

Deploy a containerized Flask application to Kubernetes using a Jenkins CI/CD pipeline.

## Technologies

- Jenkins
- Kubernetes
- Kind
- Docker
- Python
- Flask
- kubectl

## Architecture

    GitHub
       ↓
    Jenkins
       ↓
    Docker Image
       ↓
    Kubernetes Deployment
       ↓
    2 Flask Pods
       ↓
    Kubernetes Service

## Kubernetes Resources

### Deployment

The Deployment runs two replicas of the application.

    Deployment
       ├── Pod 1
       └── Pod 2

The Deployment controller maintains the desired replica count.

### Service

The application is exposed internally through a ClusterIP Service.

    Service :80
        ↓
    Pod :5000

## Local Kubernetes Environment

AWS EKS was previously configured in kubectl, but the old EKS API endpoint was no longer available.

For this project, a local Kind cluster was created:

    kind create cluster --name devops-lab

The cluster was verified with:

    kubectl get nodes

The control-plane node reported Ready.

## Docker Image

The application image was built locally:

    docker build -t devops-project-28:latest Day-03-CI-CD/Project-28

The image was loaded into the Kind node:

    kind load docker-image devops-project-28:latest --name devops-lab

## Image Pull Troubleshooting

The first deployment produced:

    ImagePullBackOff
    ErrImagePull

The image existed inside the Kind node, but Kubernetes attempted to pull the latest image.

The deployment was fixed with:

    imagePullPolicy: IfNotPresent

This allowed Kubernetes to use the locally loaded image.

## Verification

Successful deployment:

    kubectl get pods -l app=project-28

Result:

    2 pods Running

Deployment:

    kubectl get deployment project-28

Result:

    2/2 Available

Service:

    kubectl get service project-28

Result:

    ClusterIP :80

## Application Testing

The Service can be tested locally with:

    kubectl port-forward service/project-28 8082:80

Then:

    curl http://localhost:8082
    curl http://localhost:8082/health

## Self-Healing Test

Deleting a managed Pod causes the Deployment controller to create a replacement.

    kubectl delete pod -l app=project-28

This demonstrates Kubernetes desired-state reconciliation.

## Key Concepts Learned

- Kubernetes Deployment
- Kubernetes Pods
- Kubernetes Services
- ClusterIP
- Replica management
- Desired state
- Self-healing
- ImagePullBackOff
- imagePullPolicy
- Kind
- kubectl
- Container-to-Pod deployment

## Result

The Flask application was successfully deployed to a local Kubernetes cluster with two replicas.

The deployment was tested, the Service was verified, and Kubernetes self-healing behavior was demonstrated.

