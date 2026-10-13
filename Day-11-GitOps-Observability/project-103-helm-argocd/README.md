# Project 103 — Helm + Argo CD Deployment

## Goal
Deploy NGINX to Kubernetes using a Helm chart managed by Argo CD.

## Tools
- Kind
- Kubernetes
- Helm
- Argo CD
- GitHub

## Verification
- Argo CD: Synced and Healthy
- NGINX pods: 3/3 Running
- Namespace: project-103

## Key learning
Helm packages Kubernetes manifests into a reusable chart. Argo CD reads the chart from Git and reconciles the desired application state with Kubernetes.
