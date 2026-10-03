# Project 26 — CI/CD with SonarQube Quality Gates

## Objective

Build a CI/CD quality-control pipeline using Jenkins and SonarQube.

The pipeline analyzes application source code, sends the results to SonarQube, waits for the Quality Gate result, and stops the pipeline when the defined quality/security conditions fail.

## Technologies

- Jenkins
- SonarQube
- Docker
- Git
- GitHub
- Python
- Jenkins Pipeline
- SonarScanner

## Project Structure

    Project-26/
    ├── app.py
    ├── sonar-project.properties
    └── README.md

## Application

The project contains a small Python application that calculates a total price.

    def calculate_total(price, quantity):
        return price * quantity

    def main():
        price = 10
        quantity = 5

        total = calculate_total(price, quantity)

        print(f"Total: {total}")

    if __name__ == "__main__":
        main()

## SonarQube Configuration

The project uses:

    sonar.projectKey=devops-project-26
    sonar.projectName=DevOps Project 26
    sonar.sources=.
    sonar.sourceEncoding=UTF-8

## Architecture

    Developer
        |
        | git push
        v
    GitHub
        |
        v
    Jenkins
        |
        | Checkout
        v
    Source Code
        |
        | SonarScanner
        v
    SonarQube
        |
        | Static Analysis
        v
    Quality Gate
        |
        +---- PASS ----> Pipeline continues
        |
        +---- FAIL ----> Pipeline stops

## Jenkins Pipeline

The Jenkins pipeline performs:

1. Checkout source code from GitHub.
2. Run SonarQube analysis.
3. Send analysis results to SonarQube.
4. Wait for the Quality Gate result.
5. Abort the pipeline when the Quality Gate fails.

The important Jenkins stages are:

    Checkout
        ↓
    SonarQube Analysis
        ↓
    Quality Gate
        ↓
    SUCCESS / FAILURE

## Jenkins Configuration

Jenkins was configured with:

- SonarQube Server: SonarQube
- SonarQube URL: http://sonarqube:9000
- SonarQube Scanner: SonarScanner
- Jenkins credential: sonarqube-token
- SonarQube webhook:
  http://jenkins25:8080/sonarqube-webhook/

Jenkins and SonarQube were connected through the Docker network:

    devops-network

## Local SonarQube

SonarQube was running as a Docker container:

    docker run -d \
      --name sonarqube \
      -p 9000:9000 \
      sonarqube:lts-community

Jenkins was also connected to the same Docker network so that it could communicate with SonarQube using:

    http://sonarqube:9000

## Important Concept: SonarQube vs Jenkins

Jenkins is responsible for automation.

SonarQube is responsible for code-quality and security analysis.

SonarScanner sends source-code information to SonarQube.

The Quality Gate determines whether the analyzed code satisfies the configured quality requirements.

In simple terms:

    Jenkins = Orchestrates
    SonarScanner = Sends analysis
    SonarQube = Analyzes
    Quality Gate = Decides pass/fail

## What Was Tested

### Successful Quality Gate

The clean application was analyzed successfully.

Expected result:

    ANALYSIS SUCCESSFUL
    Quality gate is 'OK'
    Finished: SUCCESS

This allows the CI/CD pipeline to continue.

### Failed Quality Gate

A security issue was intentionally introduced into the Python application.

Example:

    password = "SuperSecret123"

An unused variable was also introduced.

The pipeline detected the issue and returned:

    ANALYSIS SUCCESSFUL
    Quality gate is 'ERROR'
    Pipeline aborted due to quality gate failure
    Finished: FAILURE

This demonstrated that analysis can complete successfully while the pipeline itself fails because the Quality Gate rejected the code.

## Failure Scenario

The important distinction is:

    SonarQube Analysis SUCCESS
              ≠
    Quality Gate SUCCESS

The scanner can successfully upload the analysis while the Quality Gate can still fail.

This is an important CI/CD concept.

## Troubleshooting Performed

### Problem 1 — Jenkins could not use checkout scm

Error:

    checkout scm is only available when using a Pipeline script
    from SCM

Solution:

Use an explicit Git checkout:

    git branch: 'main',
        url: 'https://github.com/mhhuzaifa223/100-days-devops.git'

### Problem 2 — SonarScanner tool not found

Error:

    No tool named SonarScanner found

Solution:

Configure SonarQube Scanner under:

    Jenkins → Manage Jenkins → Tools

Scanner installation:

    SonarScanner

### Problem 3 — Jenkins could not communicate with SonarQube

The containers were initially on Docker's default network.

A dedicated network was created:

    docker network create devops-network

Both containers were connected to it:

    docker network connect devops-network jenkins25
    docker network connect devops-network sonarqube

Jenkins could then access:

    http://sonarqube:9000

### Problem 4 — Quality Gate returned HTTP 401

The SonarQube analysis itself worked, but Jenkins could not retrieve the Quality Gate result.

The Jenkins SonarQube server configuration was updated to use the correct SonarQube authentication credential.

After that:

    waitForQualityGate

successfully returned the Quality Gate result.

## Key Concepts Learned

- Jenkins CI/CD pipelines
- SonarQube
- SonarScanner
- Static code analysis
- Quality Gates
- Bugs
- Vulnerabilities
- Code smells
- Jenkins credentials
- Secrets management
- Docker networking
- Jenkins tool configuration
- SonarQube webhooks
- Quality Gate enforcement
- Pipeline failure handling
- CI/CD security gates

## Interview Explanation

A simple explanation:

    I integrated SonarQube into a Jenkins CI/CD pipeline.
    Jenkins checks out the source code and runs SonarScanner.
    SonarQube analyzes the code for quality and security issues.
    Jenkins then waits for the SonarQube Quality Gate.
    If the Quality Gate passes, the pipeline continues.
    If it fails, Jenkins aborts the pipeline and prevents bad code
    from progressing further.

## Production Relevance

In a production environment, a Quality Gate can be used as a control point before deployment.

Example:

    Developer Push
        ↓
    Build
        ↓
    Tests
        ↓
    SonarQube Analysis
        ↓
    Quality Gate
        ↓
    Security Scan
        ↓
    Deployment

This prevents code that violates defined quality or security requirements from automatically progressing through the delivery pipeline.

## Result

Project 26 successfully demonstrated:

- Jenkins + SonarQube integration
- Automated static analysis
- Quality Gate enforcement
- Successful pipeline execution
- Intentional Quality Gate failure
- Troubleshooting of Jenkins/SonarQube authentication
- Docker network communication
- CI/CD security and quality control
