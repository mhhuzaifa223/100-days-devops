# Project 29 — Kubernetes Deployment Pipeline

## Objective

Learn how a CI/CD pipeline can automatically build an application container, push it to a registry, deploy it to Kubernetes, verify the deployment, and support rollback.

## Technologies

- Git
- GitHub Actions or Jenkins
- Docker
- Kubernetes
- kubectl
- Helm
- Container Registry
- Linux

## What I Practiced

- Building Docker images in CI
- Tagging images with a version or commit SHA
- Pushing images to a container registry
- Deploying applications to Kubernetes
- Updating Kubernetes workloads
- Verifying deployment health
- Performing Kubernetes rollbacks

## Pipeline Workflow

Code
→ Checkout
→ Build
→ Test
→ Dockerize
→ Push Image
→ Deploy to Kubernetes
→ Verify
→ Rollback if Required

## Deployment Flow

1. Developer pushes code.
2. CI checks out the repository.
3. Application tests run.
4. Docker image is built.
5. Image receives a unique tag.
6. Image is pushed to a container registry.
7. Kubernetes deployment is updated.
8. Deployment status is checked.
9. Previous version can be restored if deployment fails.

## Commands Used

- git status
- git add
- git commit
- git push
- docker build
- docker tag
- docker push
- kubectl apply
- kubectl get pods
- kubectl get deployments
- kubectl rollout status
- kubectl rollout undo

## Testing

### Successful Deployment

Deploy a valid container image.

Expected result:

- Image is available in the registry.
- Kubernetes creates or updates the Pods.
- Pods become Ready.
- Deployment rollout completes successfully.

### Failed Deployment

Deploy an invalid image tag or intentionally broken application version.

Expected result:

- Kubernetes reports the deployment problem.
- Pods fail to become Ready.
- Rollout does not complete successfully.
- Previous working version can be restored.

## Key Concepts Learned

- CI/CD
- Docker image
- Container registry
- Kubernetes Deployment
- Kubernetes Pods
- Rolling update
- Readiness
- Deployment verification
- Rollback
- kubectl
- Helm

## Why This Matters

Modern applications are often deployed to Kubernetes through automated pipelines.

A Kubernetes deployment pipeline connects source code, container images, CI/CD automation, and cluster operations into one repeatable process.
