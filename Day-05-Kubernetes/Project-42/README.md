# Project 42 — ConfigMaps + Secrets Management

## Objective

Demonstrate how Kubernetes manages application configuration using ConfigMaps and Secrets, injects them into Pods as environment variables, and how to troubleshoot a Pod when a required Secret is missing.

## Technologies

- Kubernetes
- Kind
- ConfigMap
- Secret
- Pod
- kubectl
- BusyBox

## How It Works

The Pod imports configuration using `envFrom`.

ConfigMap provides non-sensitive configuration:

- DB_HOST
- DB_NAME
- APP_ENV

Secret provides sensitive configuration:

- DB_USER
- DB_PASSWORD

The application container receives these values as environment variables.

## Project Structure

    Project-42/
    ├── k8s/
    │   ├── configmap.yaml
    │   ├── secret.yaml
    │   └── test-pod.yaml
    └── README.md

## Configuration Management

The ConfigMap was created with:

    kubectl apply -f k8s/configmap.yaml

The Secret was created with:

    kubectl apply -f k8s/secret.yaml

The Pod imports both resources through:

    envFrom:
      - configMapRef:
          name: project-42-config
      - secretRef:
          name: project-42-secret

## Verification

The Pod successfully loaded all configuration values:

    DB_NAME=devops
    DB_PASSWORD=devops123
    APP_ENV=production
    DB_HOST=database
    DB_USER=devops

## Failure Scenario

The Secret was intentionally deleted:

    kubectl delete secret project-42-secret

The Pod was recreated and entered:

    CreateContainerConfigError

This happened because the Pod referenced a Secret that no longer existed.

## Troubleshooting

The problem was investigated with:

    kubectl describe pod project-42-test

The Events section identified the missing Secret dependency.

The Secret was restored with:

    kubectl apply -f k8s/secret.yaml

After recreating the Pod, it returned to Running state.

## Important Security Note

Kubernetes Secrets are not automatically encrypted simply because they are called Secrets.

Base64 encoding is not encryption.

This project uses a dummy password for learning purposes. Real production credentials should not be committed to Git repositories.

Applications should also avoid printing secret values to logs.

Production environments should use appropriate RBAC, encryption at rest, and dedicated secret-management solutions.

## Key Concepts Learned

- ConfigMap
- Kubernetes Secret
- envFrom
- Environment variable injection
- Pod configuration dependencies
- CreateContainerConfigError
- kubectl describe
- Kubernetes Events
- Troubleshooting missing resources
- Difference between encoding and encryption

## Result

Successfully demonstrated Kubernetes configuration management using ConfigMaps and Secrets, including failure simulation and production-style troubleshooting.
