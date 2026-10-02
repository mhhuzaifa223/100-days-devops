# Project 25 — Multi-Environment CI/CD Pipeline

## Objective

Learn how CI/CD pipelines can promote the same application artifact through multiple environments such as Dev, QA, Staging, and Production.

## Technologies

- Git
- GitHub Actions
- Docker
- Kubernetes
- Linux

## What I Practiced

- Creating environment-specific deployment stages
- Separating development and production environments
- Promoting the same artifact between environments
- Adding approval gates for production
- Managing environment-specific configuration
- Designing rollback-ready deployments
- Understanding controlled software promotion

## Pipeline Workflow

Code → Build → Test → Package → Dev → QA → Staging → Approval → Production

## Commands Used

- git status
- git add
- git commit
- git push
- docker build
- docker tag
- kubectl apply
- kubectl get

## Testing

A CI/CD workflow was designed to deploy the application first to a development environment.

After validation, the same built artifact was promoted through QA and staging before reaching production.

Production deployment was protected by an approval step to prevent untested changes from being released automatically.

## Key Concepts Learned

- Multi-environment deployment
- Dev environment
- QA environment
- Staging environment
- Production environment
- Artifact promotion
- Environment isolation
- Approval gates
- Deployment rollback
- Configuration management

## Why This Matters

Production systems require controlled releases.

Promoting the same tested artifact across environments reduces deployment inconsistencies and provides a safer path from development to production.
