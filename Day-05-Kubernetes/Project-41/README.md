# Project 41 — Kubernetes Three-Tier Application

## Objective

Deploy and troubleshoot a three-tier application on Kubernetes using:

- Nginx frontend
- Flask backend
- PostgreSQL database
- Kubernetes Deployments
- Kubernetes Services
- StatefulSet
- PersistentVolumeClaim
- Configured Ingress
- Readiness probes
- Kind local Kubernetes cluster

The project demonstrates how traffic flows from an external user through Kubernetes Ingress and Services to application and database workloads.

## Technologies

- Kubernetes
- Kind
- Docker
- Nginx
- Python
- Flask
- PostgreSQL
- kubectl
- Kubernetes Ingress NGINX
- PersistentVolumeClaim

## How It Works

Application request flow:

    User
      |
      v
    NGINX Ingress
      |
      v
    Frontend Service
      |
      v
    Nginx Frontend Pods
      |
      | /api/*
      v
    Backend Service
      |
      v
    Flask Backend Pods
      |
      v
    Database Service
      |
      v
    PostgreSQL StatefulSet
      |
      v
    Persistent Storage

The frontend Nginx container serves the HTML application and proxies `/api/` requests to the Flask backend.

The Flask backend provides:

    /
    /health
    /db

The `/db` endpoint verifies connectivity to PostgreSQL.

## Project Structure

    Project-41/
    ├── backend/
    │   ├── app.py
    │   ├── requirements.txt
    │   └── Dockerfile
    │
    ├── frontend/
    │   ├── index.html
    │   ├── nginx.conf
    │   └── Dockerfile
    │
    └── k8s/
        ├── database.yaml
        ├── backend.yaml
        ├── frontend.yaml
        └── ingress.yaml

## Kubernetes Components

### Backend

- Deployment: `project-41-backend`
- Replicas: 2
- Container port: 5000
- Service: `project-41-backend`
- Service type: ClusterIP
- Readiness probe: `/health`

### Frontend

- Deployment: `project-41-frontend`
- Replicas: 2
- Container port: 80
- Service: `project-41-frontend`
- Service type: ClusterIP
- Readiness probe: `/`

### Database

- StatefulSet: `database`
- Image: PostgreSQL 15
- Replicas: 1
- Service: `database`
- PersistentVolumeClaim: `project-41-db-pvc`

The PVC was dynamically bound by the Kind cluster's default StorageClass.

### Ingress

- Ingress: `project-41-ingress`
- Ingress class: `nginx`
- Host: `project41.local`

Because the Kind cluster was created without host port mappings for ports 80/443, the Ingress was tested through:

    kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80

Requests were then sent using:

    curl -H "Host: project41.local" http://localhost:8080/

## Application

The frontend displays:

    Kubernetes Three-Tier Application

    Frontend: Nginx
    Backend: Flask
    Database: PostgreSQL

JavaScript requests:

    /api/health
    /api/db

These are proxied by Nginx to the Flask backend.

## How to Run

Start the Kind cluster:

    kind get clusters

Load the locally built images into Kind:

    kind load docker-image project-41-backend:1.0 --name devops-lab
    kind load docker-image project-41-frontend:1.0 --name devops-lab

Apply the Kubernetes resources:

    kubectl apply -f k8s/database.yaml
    kubectl apply -f k8s/backend.yaml
    kubectl apply -f k8s/frontend.yaml

Install or verify the NGINX Ingress Controller:

    kubectl get pods -n ingress-nginx

Apply the Ingress:

    kubectl apply -f k8s/ingress.yaml

Start the local Ingress port-forward:

    kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80

Test the application from another terminal:

    curl -H "Host: project41.local" http://localhost:8080/

    curl -H "Host: project41.local" http://localhost:8080/api/health

    curl -H "Host: project41.local" http://localhost:8080/api/db

## Example Output

Frontend:

    Kubernetes Three-Tier Application

Health endpoint:

    {"status":"healthy"}

Database endpoint:

    {"database":"connected"}

## Testing / Failure Scenario

The backend was intentionally scaled to zero replicas:

    kubectl scale deployment project-41-backend --replicas=0

Kubernetes then removed the backend endpoints:

    kubectl get endpoints project-41-backend

    ENDPOINTS   <none>

Direct connectivity from the frontend to the backend Service failed:

    wget: can't connect to remote host
    Connection refused

Testing through Nginx produced:

    HTTP/1.1 502 Bad Gateway

This demonstrated that the frontend remained available while the backend application was unavailable.

The backend was then restored:

    kubectl scale deployment project-41-backend --replicas=2

## Troubleshooting

### Apache occupied port 80

The initial request to `localhost:80` returned the Ubuntu Apache default page.

Port inspection showed:

    sudo ss -ltnp | grep ':80'

Apache was stopped:

    sudo systemctl stop apache2

### Kind did not expose port 80

The Kind node only exposed the Kubernetes API port.

Port inspection showed:

    docker port devops-lab-control-plane

Only port 6443 was mapped to the host.

The Ingress Service used NodePort ports internally, but they were not exposed directly to the VM.

A Kubernetes port-forward was therefore used:

    kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80

### Backend had no endpoints

After scaling the backend to zero:

    kubectl get pods -l app=project-41-backend

returned no backend pods.

The Service remained present, but:

    kubectl get endpoints project-41-backend

showed:

    ENDPOINTS   <none>

This demonstrated the difference between a Kubernetes Service existing and having healthy Pods behind it.

## Key Concepts Learned

- Kubernetes Deployments
- Replica management
- Kubernetes Services
- ClusterIP networking
- Service discovery
- Endpoint management
- StatefulSets
- PostgreSQL on Kubernetes
- PersistentVolumeClaims
- Dynamic storage provisioning
- Nginx reverse proxy
- Kubernetes Ingress
- Ingress controllers
- Kind networking
- Port forwarding
- Readiness probes
- Application health checks
- Failure simulation
- HTTP 502 troubleshooting
- End-to-end request tracing

## Result

Successfully deployed and tested a Kubernetes three-tier application locally using Kind.

The application was verified end-to-end through:

    Ingress
      ↓
    Frontend
      ↓
    Backend
      ↓
    PostgreSQL

The project also included intentional backend failure testing and troubleshooting of Kubernetes networking and external access.
