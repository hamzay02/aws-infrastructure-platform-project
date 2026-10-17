# Production-Style AWS Infrastructure & DevSecOps Platform

## Overview

This project is a hands-on cloud engineering project focused on building and managing AWS infrastructure using Infrastructure as Code (IaC), containerization, automated testing, and DevSecOps practices.

The goal is to develop a repeatable, secure, and cost-conscious deployment workflow while gaining practical experience with cloud infrastructure and automation.

## Technologies

- **Python** — application development and automation
- **Flask** — lightweight web application
- **Docker** — application containerization
- **Pulumi** — infrastructure as code using Python
- **AWS** — cloud infrastructure and deployment
- **GitHub Actions** — planned CI/CD automation
- **CloudWatch** — planned monitoring and logging

## Project Goals

- Build and test a Python web application.
- Package the application using Docker.
- Define AWS infrastructure using Pulumi and Python.
- Apply least-privilege access and secure networking practices.
- Automate testing and deployment using GitHub Actions.
- Monitor application health and infrastructure activity.
- Keep cloud costs under control and remove resources when they are no longer needed.

## Current Progress

- [x] Flask application created.
- [x] Application health, home, and version endpoints tested.
- [x] Three unit tests passing.
- [x] Dockerfile created.
- [x] Pulumi project initialized.
- [ ] AWS infrastructure implementation.
- [ ] Container deployment to Amazon ECS with AWS Fargate.
- [ ] GitHub Actions CI/CD pipeline.
- [ ] AWS monitoring and logging.
- [ ] Final security review and documentation.

## Planned Architecture

The intended workflow is:

1. Develop the Flask application in Python.
2. Run automated tests to validate application behavior.
3. Build a Docker image.
4. Use Pulumi to define and provision AWS infrastructure.
5. Deploy the container to Amazon ECS using AWS Fargate.
6. Use CloudWatch for logs and monitoring.
7. Use GitHub Actions to automate testing and deployment.

The AWS architecture will be implemented and verified as the project progresses.

## Project Structure

```text
aws-infrastructure-platform-project/
├── .github/
│   └── workflows/
├── app/
├── docs/
├── infrastructure/
├── scripts/
├── tests/
├── Dockerfile
├── README.md
└── requirements.txt
```

## Testing

The application includes unit tests for its main endpoints.

Tests are run locally using Python's unittest framework:

```bash
python -m unittest discover -s tests -v
```

The current application tests have passed locally.

## Security and Cost Management

Security and cost control are important project goals.

Planned practices include:

- Using least-privilege IAM permissions.
- Restricting network access to required ports and services.
- Avoiding hardcoded credentials and secrets.
- Monitoring AWS usage and billing.
- Reviewing resources before deployment.
- Destroying temporary infrastructure when it is no longer needed.

AWS deployments will be performed only after account security and access permissions have been verified.

## Learning Objectives

This project is designed to strengthen practical skills in cloud engineering, Linux and application environments, infrastructure automation, containerization, CI/CD, monitoring, and cloud security.

## Disclaimer

This is a personal learning and portfolio project. Features listed as planned are not considered implemented until they have been deployed or tested and verified.

