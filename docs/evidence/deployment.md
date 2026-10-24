# Deployment Guide

## 1. Purpose

This document describes the development, testing, containerization, and infrastructure workflow for the AWS Infrastructure Platform project.

## 2. Prerequisites

The project uses the following tools:

- Python
- Docker Desktop
- Pulumi CLI
- AWS CLI
- Git
- GitHub Actions

## 3. Application Testing

The Flask application includes unit tests for its main endpoints.

Run the tests from the project root:

```bash
python -m unittest discover -s tests -v
```

The three application unit tests passed during local validation.

## 4. Docker Image

The application is packaged using Docker and a Python slim base image.

Build the image from the project root:

```bash
docker build -t aws-infrastructure-platform .
```

The Docker image build completed successfully during local validation. Docker Scout was also used to assess the image for known vulnerabilities.

## 5. Infrastructure as Code

Pulumi and Python are used to define the intended AWS infrastructure.

The infrastructure workflow includes:

1. Reviewing the infrastructure code.
2. Confirming AWS identity and permissions.
3. Inspecting proposed infrastructure changes with `pulumi preview`.
4. Reviewing resource configuration and expected costs.
5. Applying changes only after reviewing the proposed deployment.

The infrastructure code is maintained in the `infrastructure/` directory.

## 6. Continuous Integration

GitHub Actions automates application testing and Docker image building.

The workflow is defined in `.github/workflows/ci.yml`.

The CI workflow completed successfully, including the application tests and Docker image build.

## 7. Security and Cost Management

The project emphasizes secure configuration and cost awareness.

Practices include:

- Avoiding hardcoded AWS credentials.
- Reviewing IAM permissions and network access.
- Assessing Docker image vulnerabilities.
- Reviewing proposed infrastructure changes before deployment.
- Identifying temporary resources and checking for remaining charges during cleanup.

Pulumi can be used to manage the lifecycle of infrastructure defined by the project. AWS resource inventories and billing should be checked independently when verifying cleanup.

## 8. Deployment Architecture

The application is designed for container deployment using Amazon ECS and AWS Fargate, with Amazon ECR for image storage and Amazon CloudWatch for logging.

Pulumi provides the infrastructure-as-code definition for the intended AWS environment. The repository documents the architecture and workflow alongside the local testing and CI evidence.

## 9. Project Status

The Flask application, unit tests, Docker build, Pulumi infrastructure code, and GitHub Actions CI workflow are documented in this repository. The architecture, security considerations, and cost-management practices are covered in the supporting documentation.

This is a personal learning and portfolio project intended to demonstrate cloud engineering concepts and implementation practices.