# Deployment Guide

## 1. Purpose

This document describes the planned workflow for testing, containerizing, and deploying the AWS Infrastructure Platform application.

## 2. Prerequisites

The development environment uses the following tools:

- Python
- Docker Desktop
- Pulumi CLI
- AWS CLI
- Git
- Visual Studio Code

AWS deployment also requires a properly configured AWS identity with only the permissions needed for the deployment.

## 3. Local Application Testing

The Flask application can be tested locally using Python's unittest framework.

Run the following command from the project root:

```bash
python -m unittest discover -s tests -v
```

Review the test results before proceeding.

## 4. Docker Build

The Dockerfile defines how the application image is built.

The planned local build command is:

```bash
docker build -t aws-infrastructure-platform .
```

After building, the container can be tested locally once its runtime configuration is confirmed.

## 5. Infrastructure Deployment

Pulumi and Python will be used to define the AWS infrastructure.

The intended workflow is:

1. Review the infrastructure code.
2. Confirm the AWS identity and permissions.
3. Inspect the proposed changes with `pulumi preview`.
4. Review the planned resources and potential costs.
5. Deploy only after the changes and account status have been verified.

Do not run `pulumi up` until the AWS account is cleared for deployment and the infrastructure code is ready.

## 6. CI/CD Pipeline

GitHub Actions is planned to automate application tests and support deployment.

The workflow will be configured to use restricted AWS permissions and secure authentication. Deployment will require a review of the changes and expected costs.

## 7. Cleanup

When temporary AWS resources are no longer required:

1. Identify the resources created by the project.
2. Check for dependencies and retained data.
3. Review the resources that Pulumi proposes to remove.
4. Remove the resources safely.
5. Review AWS billing for any remaining charges.

Deleting infrastructure does not necessarily eliminate every possible cost, so billing and resource usage should still be checked.

## 8. Current Status

Local application tests have passed, the Dockerfile exists, and the Pulumi project has been initialized. The AWS deployment workflow has not yet been implemented and verified.

This guide will be updated as deployment steps are completed and tested.