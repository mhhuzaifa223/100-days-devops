# Project 101: Argo CD Basic Deployment

## Objective
Deploy an NGINX application to Kubernetes using Argo CD and GitOps.

## Environment
- Kubernetes: Kind (`kind-devops-lab`)
- GitOps controller: Argo CD
- Application: NGINX
- Resources: Kubernetes Deployment and ClusterIP Service

## Architecture
GitHub repository → Argo CD → Kubernetes Deployment → 2 NGINX Pods

The Service provides a stable internal endpoint for Pods labelled `app: nginx-demo`.

## Manifests
- `manifests/deployment.yaml`: declares two NGINX replicas.
- `manifests/service.yaml`: exposes NGINX internally on port 80.

## Validation
The manifests passed `kubectl apply --dry-run=client`.
`kubectl diff` confirmed that the Deployment and Service do not yet exist in the cluster.

## Next steps
- Commit the manifests to Git.
- Create an Argo CD Application that references this repository path.
- Sync the Application and verify the Pods and Service.
- Test reconciliation by changing the desired replica count in Git.
