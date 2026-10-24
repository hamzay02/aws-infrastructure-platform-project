\# Architecture



\## Overview



This project demonstrates a containerized Python application and an Infrastructure as Code workflow using Pulumi and AWS.



The application is built with Flask, tested with Python's unittest framework, packaged as a Docker image, and checked through GitHub Actions.



\## Application Workflow



1\. Develop the Flask application in Python.

2\. Run unit tests for the home, health, and version endpoints.

3\. Build the Docker image.

4\. Use GitHub Actions to automate testing and image building.

5\. Define AWS infrastructure using Pulumi and Python.



\## Intended AWS Architecture



The infrastructure code defines AWS components intended to support a containerized application:



\- \*\*Amazon VPC:\*\* Network boundary for the application infrastructure.

\- \*\*Subnets and routing:\*\* Network placement and traffic routing.

\- \*\*Security groups:\*\* Network traffic controls.

\- \*\*IAM:\*\* Permissions for AWS resource access.

\- \*\*Amazon ECR:\*\* Container image storage.

\- \*\*Amazon ECS and AWS Fargate:\*\* Intended container execution environment.

\- \*\*Amazon CloudWatch:\*\* Intended application logging.



These components describe the intended design. They do not indicate that the application is currently running in AWS.



\## Deployment Status



The Flask application tests and Docker image build succeeded, and the GitHub Actions CI workflow passed.

Pulumi defines the AWS infrastructure for the intended container deployment architecture. The project also documents the application workflow, infrastructure design, and deployment process.


\## Infrastructure as Code



Pulumi and Python are used to define AWS resources so that infrastructure can be managed through code. The Pulumi stack was destroyed after the deployment attempt to reduce ongoing costs.



\## Local Project Structure



```text

aws-infrastructure-platform-project/

├── .github/

│   └── workflows/

├── app/

├── docs/

│   └── evidence/

├── infrastructure/

├── scripts/

├── tests/

├── Dockerfile

└── README.md

```



This tree summarizes the main local project folders and files.
