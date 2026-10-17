# Security Practices

## 1. Purpose

This document describes the security principles planned for the AWS Infrastructure Platform project. The goal is to reduce unnecessary access, protect credentials, and limit exposure of cloud resources.

## 2. Identity and Access Management

AWS IAM will be used to control access to AWS resources.

Planned practices include:

- Apply least-privilege permissions.
- Avoid using the AWS root account for routine development.
- Use separate identities for development and deployment where practical.
- Review permissions before deploying infrastructure.
- Prefer short-lived credentials over long-lived access keys when supported.

## 3. Network Security

The planned AWS network will use security groups and subnet configuration to limit access.

- Allow only the network traffic required by the application.
- Avoid exposing internal services directly to the public internet.
- Restrict administrative access.
- Review inbound and outbound rules before deployment.

## 4. Application and Container Security

The Flask application and Docker image will be reviewed for common security risks.

Planned practices include:

- Keep application dependencies updated.
- Avoid embedding secrets in the application or Docker image.
- Use a minimal base image where practical.
- Run automated tests before deployment.
- Expose only the required application port.

## 5. Secrets Management

Credentials and sensitive configuration must not be committed to GitHub.

- Do not store passwords or secret access keys in source code.
- Use appropriate environment configuration or AWS-managed secrets services when needed.
- Keep local configuration files containing secrets out of version control.
- Rotate credentials if they are exposed.

## 6. Logging and Monitoring

Amazon CloudWatch is planned for application logs and infrastructure monitoring. AWS audit logs will also be reviewed when investigating unexpected activity.

## 7. Security Validation

Before deployment, infrastructure changes and permissions will be reviewed. Security settings will be tested and documented rather than assumed to be effective.

## 8. Current Status

These are planned security practices. Each control will be marked as implemented only after it has been configured and verified.

This document will be updated as the project develops.