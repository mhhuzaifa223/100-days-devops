# Project 46 — Helm-Based Application Deployment

## Objective

Deploy and manage a Kubernetes application using Helm.

This project demonstrates Helm chart creation, configurable deployments through `values.yaml`, application upgrades, release history, failure simulation, troubleshooting, and rollback to a known-good release.

## Technologies

- Kubernetes
- Kind
- Helm
- Nginx
- YAML
- kubectl

## How It Works

Helm manages Kubernetes applications using charts.

The deployment flow is:

values.yaml → Helm templates → Rendered Kubernetes manifests → Kubernetes resources

The Helm chart defines the Kubernetes resources, while `values.yaml` provides configurable values such as replica count and container image.

The project uses an Nginx application deployed through a Helm release named `project-46`.

## Project Structure

    Project-46/
    ├── project-46-chart/
    │   ├── Chart.yaml
    │   ├── values.yaml
    │   ├── templates/
    │   │   ├── deployment.yaml
    │   │   ├── service.yaml
    │   │   ├── serviceaccount.yaml
    │   │   ├── ingress.yaml
    │   │   ├── hpa.yaml
    │   │   ├── httproute.yaml
    │   │   ├── _helpers.tpl
    │   │   ├── NOTES.txt
    │   │   └── tests/
    │   │       └── test-connection.yaml
    │   └── .helmignore
    └── README.md

## Application

The application is an Nginx web server.

The Helm chart was configured with:

- Replica count: 2 initially
- Container image: nginx:alpine
- Service type: ClusterIP
- Service port: 80

The application was exposed locally using Kubernetes port-forwarding.

## How to Run

Create the chart:

    helm create project-46-chart

Render the Kubernetes manifests without deploying:

    helm template project-46 project-46-chart

Install the Helm release:

    helm install project-46 project-46-chart

Check the release:

    helm list

Check the pods:

    kubectl get pods -l app.kubernetes.io/instance=project-46

Check the Service:

    kubectl get svc -l app.kubernetes.io/instance=project-46

Access the application:

    kubectl port-forward svc/project-46-project-46-chart 8080:80

Then:

    curl http://localhost:8080

## Helm Upgrade

The deployment was upgraded from 2 replicas to 3 using Helm:

    helm upgrade project-46 project-46-chart --set replicaCount=3

Helm created a new release revision while preserving the release history.

## Failure Scenario

A broken container image was intentionally deployed:

    helm upgrade project-46 project-46-chart --set image.tag=does-not-exist

The Helm command completed successfully, but the newly created pod entered:

    ErrImagePull

This demonstrated an important operational concept:

Helm deployment success does not necessarily mean that the application is healthy.

Kubernetes still has to successfully create and run the requested containers.

## Troubleshooting

The failed pod was investigated with:

    kubectl get pods -l app.kubernetes.io/instance=project-46

Then:

    kubectl describe pod <failed-pod-name>

The Events section showed that Kubernetes could not pull the requested image.

The Helm release history was checked with:

    helm history project-46

The last known-good release was Revision 2.

## Rollback

The broken Revision 3 was recovered using:

    helm rollback project-46 2

Helm created Revision 4 as the new deployed revision.

The final release history showed:

    Revision 1 — Initial installation
    Revision 2 — Successful upgrade to 3 replicas
    Revision 3 — Broken image deployment
    Revision 4 — Rollback to Revision 2

The application returned to 3 healthy replicas.

## Key Concepts Learned

- Helm charts
- Helm releases
- Chart values
- Helm templates
- values.yaml
- Helm install
- Helm upgrade
- Helm release revisions
- Helm history
- Kubernetes Deployments
- Kubernetes Services
- ImagePullBackOff / ErrImagePull
- Kubernetes troubleshooting
- Helm rollback
- Known-good releases
- Application health versus deployment success
- Release-based recovery

## Result

Successfully deployed and managed an Nginx application using Helm.

The project demonstrated the complete lifecycle of a Helm-managed Kubernetes application:

Install → Upgrade → Break → Troubleshoot → Rollback → Recover

This provides practical experience with Helm-based deployment management and release recovery.
