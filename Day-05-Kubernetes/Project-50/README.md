# Project 50 — Production-Grade Kubernetes Application

## Objective

Deploy a production-style, three-tier application on Kubernetes with frontend routing, a Flask backend, PostgreSQL persistence, health checks, resource limits, and automated pod recovery.

## Technologies

- Kubernetes (Kind)
- Docker
- NGINX
- Python and Flask
- PostgreSQL 15
- ConfigMaps and Secrets
- Deployments and Services
- PersistentVolumeClaims
- NGINX Ingress Controller
- Prometheus and Grafana (cluster monitoring from Project 49)

## How It Works

1. Users access the frontend through an NGINX Service.
2. NGINX serves the web page and forwards `/api/` requests to the backend Service.
3. The Flask backend connects to PostgreSQL using Kubernetes configuration and secret references.
4. PostgreSQL stores its data on a PersistentVolumeClaim.
5. Kubernetes readiness and liveness probes check application health.
6. Deployments maintain the desired number of replicas and replace deleted or failed pods.
7. Resource requests and limits define CPU and memory requirements.

## Project Structure

    Project-50/
    ├── README.md
    ├── app/
    │   ├── Dockerfile
    │   ├── index.html
    │   └── nginx.conf
    └── k8s/
        └── app.yaml

## Application

The application contains:

- Frontend: NGINX serving the web interface
- Backend: Flask API using the backend image developed in Project 41
- Database: PostgreSQL 15
- Configuration: ConfigMap and Kubernetes Secret
- Storage: PersistentVolumeClaim for PostgreSQL data
- Routing: Kubernetes Services and NGINX Ingress

The application runs in the `project-50` namespace and uses the Ingress hostname `project50.local`.

## How to Run

Ensure the `devops-lab` Kind cluster and NGINX Ingress Controller are running.

Load the required local images into Kind if they are not already available:

    kind load docker-image project-50-frontend:1.0 project-41-backend:1.0 postgres:15 --name devops-lab

Apply the Kubernetes manifests:

    kubectl apply -f k8s/app.yaml

Check the deployment:

    kubectl get pods,services,pvc,ingress -n project-50

Forward the frontend Service to localhost:

    kubectl port-forward -n project-50 svc/project-50-frontend 8081:80

Keep the port-forward command running in one terminal. Test the application from another:

    curl -i http://localhost:8081/
    curl -i http://localhost:8081/api/health
    curl -i http://localhost:8081/api/db

## Example Output

Health endpoint:

    {"status":"healthy"}

Database endpoint:

    {"database":"connected"}

Exact responses depend on the running application and backend implementation.

## Testing / Failure Scenario

- Verified that the frontend, backend, and PostgreSQL pods reached the Running state.
- Verified that the PostgreSQL PVC was Bound.
- Tested the frontend and API endpoints through the frontend Service.
- Deleted a backend pod to test Kubernetes recovery.
- Checked that the Deployment restored its desired replicas and retested the API and database endpoints.

## Troubleshooting

Inspect pod status:

    kubectl get pods -n project-50

Inspect a failing pod:

    kubectl describe pod <pod-name> -n project-50

View backend logs:

    kubectl logs deployment/project-50-backend -n project-50

View database logs:

    kubectl logs deployment/project-50-database -n project-50

Check backend Service endpoints:

    kubectl get endpoints project-50-backend -n project-50

Check persistent storage:

    kubectl get pvc -n project-50

If curl returns no response, verify that the frontend port-forward is still running on port 8081. Check pod readiness, Service endpoints, and backend logs before changing the manifests.

## Key Concepts Learned

- Three-tier application architecture
- Kubernetes Deployments and Services
- Internal service discovery
- ConfigMaps and Secret references
- Persistent storage with PVCs
- Readiness and liveness probes
- CPU and memory requests and limits
- Ingress-based routing
- Pod replacement and self-healing
- API-to-database connectivity
- Practical Kubernetes troubleshooting

## Result

Deployed a production-style three-tier application in a local Kubernetes cluster, with persistent database storage, internal service communication, health probes, resource controls, and automated pod recovery.

This is a learning environment, not a hardened production deployment. Production use would require additional controls such as encrypted secret management, TLS, backups, access policies, and a validated CI/CD process.
