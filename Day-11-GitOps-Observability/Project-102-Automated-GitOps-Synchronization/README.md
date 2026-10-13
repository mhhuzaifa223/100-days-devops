# Project 102 — Automated GitOps Synchronization

## Goal
Automatically apply Kubernetes changes committed to GitHub using Argo CD.

## Setup
- Kubernetes: Kind local cluster
- GitOps controller: Argo CD
- Application: nginx-demo
- Source manifests: Project 101

## Test
1. Enabled Argo CD automated sync with prune and self-heal.
2. Changed the Deployment replica count from 2 to 3 in Git.
3. Committed and pushed the change to GitHub.
4. Argo CD detected the change and applied it automatically.
5. Verified the rollout and three ready NGINX pods.

## Verification
- Argo CD status: Synced
- Health: Healthy
- Deployment rollout: Successful
- Ready replicas: 3/3

## Key learning
Git is the source of truth. Argo CD continuously compares the desired state in Git with the live Kubernetes state and synchronizes changes.
