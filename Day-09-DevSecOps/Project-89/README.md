# Project 89: Kubernetes Admission Security

## Objective
Validate Kubernetes manifests against security policies before deployment.

## Tools
- Kubernetes YAML
- Open Policy Agent (OPA)
- Conftest
- Docker

## Security Rules
- Reject privileged containers.
- Reject container images using the mutable `latest` tag.

## Test Results
The intentionally insecure test manifest failed both rules:
- Images must not use the latest tag.
- Privileged containers are not allowed.

The replacement test manifest uses a versioned image tag and disables privileged mode.

## Key Learning
Policy-as-code helps detect insecure Kubernetes configuration before resources are deployed. This project validates YAML locally; it does not install or enforce policies on a live Kubernetes cluster.

## Safety Note
The manifests are test files only. No application was deployed to a Kubernetes cluster.
