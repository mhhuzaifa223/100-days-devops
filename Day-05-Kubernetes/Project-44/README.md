# Project 44 — Kubernetes Horizontal Pod Autoscaling

## Objective

Deploy an Nginx application on Kubernetes and configure Horizontal Pod Autoscaling (HPA) to automatically increase or decrease the number of Pods based on CPU utilization.

The project demonstrates how Kubernetes reacts to changing application resource usage and maintains the desired workload capacity.

## Technologies

- Kubernetes
- Kind
- Nginx
- Kubernetes Deployments
- Horizontal Pod Autoscaler (HPA)
- Metrics Server
- kubectl

## How It Works

The application runs as a Kubernetes Deployment with an initial replica count of 2.

Each container has CPU resources configured:

- CPU request: 100m
- CPU limit: 200m

The HPA monitors CPU utilization through the Kubernetes Metrics API.

Configuration:

- Minimum replicas: 2
- Maximum replicas: 5
- CPU target: 50%

When CPU utilization increases above the target, Kubernetes increases the number of Pods.

When CPU utilization falls back down, Kubernetes gradually reduces the number of Pods.

## Project Structure

    Project-44/
    ├── k8s/
    │   ├── deployment.yaml
    │   └── hpa.yaml
    └── README.md

## Kubernetes Components

### Deployment

The Deployment manages the Nginx application Pods.

It starts with:

    replicas: 2

CPU resources are defined so the HPA can calculate CPU utilization.

### Metrics Server

Metrics Server provides resource usage information to Kubernetes.

Verify metrics with:

    kubectl top pods

    kubectl top nodes

For the local Kind environment, Metrics Server required:

    --kubelet-insecure-tls

This configuration is suitable for this local learning environment only. Production Kubernetes clusters should use proper kubelet certificate validation.

### Horizontal Pod Autoscaler

The HPA configuration uses:

    minReplicas: 2
    maxReplicas: 5
    averageUtilization: 50%

## How to Run

Apply the Deployment:

    kubectl apply -f k8s/deployment.yaml

Apply the HPA:

    kubectl apply -f k8s/hpa.yaml

Check the Deployment:

    kubectl get deployment project-44-app

Check the Pods:

    kubectl get pods -l app=project-44-app

Check the HPA:

    kubectl get hpa project-44-hpa

Check resource metrics:

    kubectl top pods -l app=project-44-app

## Testing

### Initial State

The application starts with:

    2 replicas

### Scale-Up Test

CPU load was introduced on the application Pods.

The HPA detected CPU utilization above the configured 50% target and increased the number of replicas.

Observed result:

    2 replicas → 4 replicas

This confirmed that HPA scaling was working.

### Scale-Down Test

After CPU usage returned to normal, the HPA gradually reduced the number of replicas.

Observed result:

    4 replicas → 2 replicas

This confirmed that the HPA could also scale the application down.

## Example Output

HPA after scaling:

    NAME             REFERENCE                   TARGETS       MINPODS   MAXPODS   REPLICAS
    project-44-hpa   Deployment/project-44-app   cpu: .../50%  2         5         4

After CPU usage returned to zero:

    project-44-hpa   Deployment/project-44-app   cpu: 0%/50%   2         5         2

## Troubleshooting

### HPA Shows `<unknown>`

Check Metrics Server:

    kubectl get pods -n kube-system | grep metrics-server

Check the Metrics API:

    kubectl top pods

If metrics are unavailable, inspect the Metrics Server logs:

    kubectl logs -n kube-system deployment/metrics-server

### HPA Does Not Scale

Verify that CPU requests are configured:

    kubectl get deployment project-44-app -o yaml

The HPA CPU utilization percentage is calculated relative to the configured CPU request.

### Metrics Server Certificate Error

In the local Kind environment, Metrics Server may fail to validate the Kind kubelet certificate.

The learning environment uses:

    --kubelet-insecure-tls

This should not be used as a production security solution.

## Key Concepts Learned

- Horizontal Pod Autoscaling
- Kubernetes Metrics Server
- CPU requests vs CPU limits
- CPU utilization-based scaling
- Minimum and maximum replica limits
- Automatic scale-up
- Automatic scale-down
- Kubernetes Metrics API
- HPA stabilization behavior
- Troubleshooting Metrics Server
- HPA resource requirements

## Result

Successfully implemented and tested Kubernetes Horizontal Pod Autoscaling.

The application automatically scaled from:

    2 → 4 replicas

under CPU pressure and then returned from:

    4 → 2 replicas

after CPU usage returned to normal.

Project 44 demonstrates automated workload scaling based on real Kubernetes resource metrics.
