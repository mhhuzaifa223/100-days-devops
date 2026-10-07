# Project 45 — Kubernetes Ingress-Based Application Routing

## Objective

Deploy two independent applications on Kubernetes and expose them through a single NGINX Ingress using path-based routing.

The project demonstrates how Kubernetes Ingress receives external HTTP requests and routes them to different backend Services.

## Technologies

- Kubernetes
- Kind
- NGINX
- NGINX Ingress Controller
- Kubernetes Deployments
- Kubernetes Services
- Kubernetes Ingress
- kubectl

## Architecture

    Client
       |
       v
    NGINX Ingress
       |
       +---- /app1 ----> project-45-app1 Service ----> App 1 Pods
       |
       +---- /app2 ----> project-45-app2 Service ----> App 2 Pods

Both applications use Nginx containers.

## Project Structure

    Project-45/
    ├── k8s/
    │   ├── app1.yaml
    │   ├── app2.yaml
    │   └── ingress.yaml
    └── README.md

## Applications

### App 1

Deployment:

    project-45-app1

Service:

    project-45-app1

Replicas:

    2

### App 2

Deployment:

    project-45-app2

Service:

    project-45-app2

Replicas:

    2

Both Services use ClusterIP because they are accessed internally through the Ingress Controller.

## Ingress Routing

The Ingress uses the NGINX Ingress Controller.

Routing rules:

    /app1 → project-45-app1:80

    /app2 → project-45-app2:80

The Ingress uses regular expressions and a rewrite rule so the application path prefix is removed before the request reaches the backend.

For example:

    /app1 → /

    /app2 → /

This is required because the default Nginx application serves its content from `/`.

## How to Run

Apply App 1:

    kubectl apply -f k8s/app1.yaml

Apply App 2:

    kubectl apply -f k8s/app2.yaml

Apply the Ingress:

    kubectl apply -f k8s/ingress.yaml

Verify Pods:

    kubectl get pods

Verify Services:

    kubectl get svc project-45-app1 project-45-app2

Verify Ingress:

    kubectl get ingress project-45-ingress

## Local Access

The Kind cluster does not expose the Ingress Controller directly on host port 80.

For local testing, use:

    kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80

Then test App 1:

    curl -H "Host: project45.local" http://localhost:8080/app1

Test App 2:

    curl -H "Host: project45.local" http://localhost:8080/app2

Both requests return the NGINX welcome page.

## Testing

### App 1

    curl -H "Host: project45.local" http://localhost:8080/app1

Result:

    NGINX Welcome Page

### App 2

    curl -H "Host: project45.local" http://localhost:8080/app2

Result:

    NGINX Welcome Page

## Failure Scenario

App 1 was intentionally scaled to zero:

    kubectl scale deployment project-45-app1 --replicas=0

The Service remained present, but it had no backend endpoints.

The Ingress request to `/app1` then failed because there was no available upstream Pod.

This demonstrated an important Kubernetes concept:

    Service exists ≠ Service has healthy endpoints

App 1 was restored:

    kubectl scale deployment project-45-app1 --replicas=2

After the Pods became Ready, the Service received endpoints again and routing recovered.

## Troubleshooting

### Ingress Returns 404

Check the Ingress rules:

    kubectl describe ingress project-45-ingress

Check that the requested Host header matches:

    project45.local

Also verify that the path rewrite configuration matches the application path.

### Ingress Returns 502

Check Service endpoints:

    kubectl get endpoints project-45-app1

For modern Kubernetes versions, EndpointSlice can also be checked:

    kubectl get endpointslice

If no endpoints exist, check the application Pods:

    kubectl get pods -l app=project-45-app1

### Service Has No Endpoints

Verify that the Service selector matches the Pod labels.

Service selector:

    app: project-45-app1

Pod label:

    app: project-45-app1

A mismatch prevents Kubernetes from associating Pods with the Service.

### Ingress Controller Issues

Check the controller:

    kubectl get pods -n ingress-nginx

Check controller logs:

    kubectl logs -n ingress-nginx deployment/ingress-nginx-controller

## Key Concepts Learned

- Kubernetes Ingress
- NGINX Ingress Controller
- Path-based routing
- IngressClass
- ClusterIP Services
- Service selectors
- Service endpoints
- EndpointSlice
- Ingress path rewriting
- Regular expression paths
- HTTP 404 troubleshooting
- HTTP 502 troubleshooting
- Kubernetes internal networking
- Failure recovery

## Result

Successfully implemented Kubernetes path-based Ingress routing.

A single Ingress entry point now routes:

    /app1 → Application 1

    /app2 → Application 2

The project also demonstrated failure detection and recovery when an application temporarily had zero available backend Pods.
