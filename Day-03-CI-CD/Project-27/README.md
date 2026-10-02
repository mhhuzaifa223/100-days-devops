# Project 27 — CI/CD with SonarQube Quality Gates

## Objective

Learn how to integrate SonarQube into a CI/CD pipeline to automatically analyze source code and prevent poor-quality code from progressing toward deployment.

## Technologies

- Jenkins or GitHub Actions
- SonarQube
- Git
- Linux

## What I Practiced

- Static code analysis
- Detecting bugs and vulnerabilities
- Detecting code smells
- Integrating SonarQube with CI/CD
- Configuring quality gates
- Failing a pipeline when quality requirements are not met
- Using automated quality checks before deployment

## Pipeline Workflow

Code → Checkout → Build → SonarQube Analysis → Quality Gate → Tests → Deploy

## Quality Checks

SonarQube can analyze:

- Bugs
- Vulnerabilities
- Code smells
- Duplicated code
- Test coverage
- Maintainability
- Reliability

## Example Flow

1. Developer pushes code.
2. CI pipeline checks out the repository.
3. Application is built.
4. SonarQube analyzes the source code.
5. SonarQube evaluates the configured quality gate.
6. If the gate passes, the pipeline continues.
7. If the gate fails, the pipeline stops.

## Testing

Two pipeline scenarios should be tested:

### Passing Scenario

Submit code that satisfies the configured quality gate.

Expected result:

- SonarQube analysis succeeds.
- Quality gate passes.
- Pipeline continues.

### Failing Scenario

Introduce code-quality problems that violate the configured quality gate.

Expected result:

- SonarQube reports the problems.
- Quality gate fails.
- Pipeline stops before deployment.

## Key Concepts Learned

- SonarQube
- Static Application Security Testing
- Static code analysis
- Quality gate
- Code quality
- Code coverage
- Vulnerability detection
- Code smells
- CI/CD quality control

## Why This Matters

CI/CD should not only automate deployment.

Quality gates allow teams to automatically verify code quality before changes reach later environments or production.
