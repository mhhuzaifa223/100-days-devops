# Project 27 — DevSecOps Security Scanning Pipeline

## Objective

Build a DevSecOps CI/CD pipeline that automatically checks application code, dependencies, infrastructure, and container images for security and quality issues before deployment.

## Technologies

- GitHub
- GitHub Actions
- Jenkins
- SonarQube
- pip-audit
- Checkov
- Trivy
- OWASP ZAP
- Docker
- Python
- Flask
- Terraform

## Project Structure

    Project-27/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── Jenkinsfile
    ├── sonar-project.properties
    └── infra/
        ├── main.tf
        └── README.md

## Application

The project contains a small Flask application with:

- `/` — application endpoint
- `/health` — health-check endpoint

Run locally:

    python3 app.py

The application listens on port 5000.

## Docker

Build the application image:

    docker build -t devsecops-project-27 .

Run the container:

    docker run --rm -p 8080:5000 devsecops-project-27

Verify:

    curl http://localhost:8080
    curl http://localhost:8080/health

## SAST — SonarQube

SonarQube performs Static Application Security Testing.

The pipeline analyzes the source code and sends the results to SonarQube.

Pipeline flow:

    Checkout
        ↓
    SonarQube Analysis
        ↓
    Quality Gate
        ↓
    Continue only if the gate passes

The Jenkins pipeline uses the SonarScanner configured in Jenkins.

The Quality Gate is configured as a deployment control. If the Quality Gate fails, the pipeline stops.

## SCA — Dependency Security

Software Composition Analysis checks third-party dependencies for known vulnerabilities.

The project uses pip-audit.

The application dependency was upgraded to:

    Flask==3.1.3

The audit was executed inside the same Python 3.12 environment used by the Docker image.

Result:

    No known vulnerabilities found

This prevents vulnerable dependencies from reaching later pipeline stages.

## IaC Security — Checkov

Terraform infrastructure is scanned using Checkov.

The initial Terraform configuration contained multiple security findings.

The configuration was hardened with:

- S3 public access blocking
- S3 versioning
- Server-side encryption
- Lifecycle configuration

Final Checkov result:

    11 passed
    5 failed

The remaining findings are additional AWS security best-practice recommendations such as:

- Access logging
- KMS encryption
- Cross-region replication
- Event notifications
- Multipart upload cleanup

## Container Security — Trivy

Trivy was selected for container image vulnerability scanning.

The Trivy Docker image was available and the scanner started successfully.

However, the vulnerability database could not be downloaded because of network/download problems.

The first Trivy scan therefore could not complete.

This limitation was documented instead of treating the scan as successful.

## DAST — OWASP ZAP

OWASP ZAP was selected for Dynamic Application Security Testing.

The intended flow is:

    Running application
          ↓
    OWASP ZAP
          ↓
    Security scan
          ↓
    Security report

The ZAP Docker image download failed with an unexpected EOF during image retrieval.

Therefore, the DAST scan was not reported as successful.

## Jenkins Pipeline

The Jenkins pipeline performs the security stages that were successfully integrated.

Main flow:

    Checkout
       ↓
    SAST — SonarQube
       ↓
    Quality Gate
       ↓
    SCA — Dependency Audit
       ↓
    Container Scan
       ↓
    IaC Scan
       ↓
    DAST
       ↓
    Deployment

Security tools are treated as pipeline gates rather than optional checks.

## Failure Testing

A security issue was intentionally introduced into the application.

Example:

    password = "SuperSecret123"

SonarQube detected the security issue.

The pipeline produced:

    Quality gate is 'ERROR'

Jenkins then stopped the pipeline:

    Pipeline aborted due to quality gate failure

After removing the security issue, the pipeline passed again.

## Key Concepts Learned

- DevSecOps
- Shift-left security
- SAST
- SCA
- Container security
- IaC security
- DAST
- Security gates
- Quality gates
- Jenkins credentials
- SonarQube integration
- Docker-based security tooling
- Terraform security scanning
- Dependency vulnerability management
- CI/CD security automation

## Troubleshooting

### SonarQube authentication failure

Verify:

- Jenkins credential
- SonarQube token
- SonarQube server configuration
- Jenkins SonarQube integration

### SonarQube connection failure

Verify that Jenkins and SonarQube are connected to the same Docker network.

Check:

    docker network inspect devops-network

Test:

    docker exec jenkins25 curl http://sonarqube:9000

### Trivy database failure

If Trivy cannot download its vulnerability database, the image scan cannot complete on the first run.

Do not report the scan as successful without a vulnerability database.

### ZAP image download failure

If Docker cannot retrieve the ZAP image and reports an unexpected EOF, verify Docker registry/network connectivity before retrying.

## DevSecOps Model

The project demonstrates security throughout the CI/CD lifecycle:

    Code
      ↓
    SAST
      ↓
    Dependencies
      ↓
    Container
      ↓
    Infrastructure
      ↓
    Running Application
      ↓
    DAST
      ↓
    Deployment

Instead of checking security only after deployment, security checks are integrated into the delivery pipeline.

## Result

Project 27 demonstrates a DevSecOps pipeline combining:

- Code quality and security analysis
- Dependency vulnerability scanning
- Infrastructure security scanning
- Container vulnerability scanning
- Dynamic application security testing
- Jenkins pipeline gates

Successfully integrated:

- SonarQube SAST
- SonarQube Quality Gate
- Dependency audit
- Checkov IaC scanning

Trivy and OWASP ZAP were investigated but blocked by external Docker/network download limitations.

## Repository

    https://github.com/mhhuzaifa223/100-days-devops

