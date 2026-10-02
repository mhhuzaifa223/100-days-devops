# Project 30 — Blue/Green Deployment Pipeline

## Objective

Learn how Blue/Green deployment can release a new application version while keeping the existing version available for traffic, allowing controlled testing and fast rollback.

## Technologies

- Git
- GitHub Actions or Jenkins
- Docker
- Kubernetes
- NGINX
- AWS ALB / Kubernetes Ingress
- Linux

## What I Practiced

- Running two application environments
- Deploying a new version separately from the active version
- Testing the new version before exposing it to users
- Switching traffic between environments
- Monitoring the new deployment
- Rolling back by switching traffic back to the previous version

## Deployment Model

Blue = Current production version

Green = New application version

Traffic initially goes to Blue.

After Green is deployed and verified, traffic is switched:

Blue → Green

If Green has a problem:

Green → Blue

## Pipeline Workflow

Code
→ Build
→ Test
→ Dockerize
→ Push Image
→ Deploy Green
→ Test Green
→ Switch Traffic
→ Monitor
→ Roll Back if Required

## Deployment Flow

1. Build the new application version.
2. Create the Docker image.
3. Push the image to a container registry.
4. Deploy the new version as Green.
5. Verify that Green is healthy.
6. Run application tests against Green.
7. Switch production traffic from Blue to Green.
8. Monitor the new version.
9. Switch traffic back to Blue if problems occur.

## Testing

### Successful Deployment

Green passes health checks and application tests.

Expected result:

- Green becomes healthy.
- Traffic is switched from Blue to Green.
- Users receive the new application version.

### Failed Deployment

Introduce a broken application version or failing health check.

Expected result:

- Green fails validation.
- Blue continues serving traffic.
- Production traffic is not switched to the broken version.

### Rollback

If problems are detected after switching traffic:

Green → Blue

Expected result:

- Traffic returns to the previous stable version.
- Recovery does not require rebuilding the application.

## Key Concepts Learned

- Blue/Green deployment
- Zero-downtime deployment
- Traffic switching
- Kubernetes Services
- Kubernetes Ingress
- Health checks
- Deployment validation
- Production monitoring
- Fast rollback
- Release strategies

## Why This Matters

Blue/Green deployment separates the new release from the currently active production version.

This allows the new version to be tested before receiving production traffic and provides a simple rollback mechanism when a deployment causes problems.
