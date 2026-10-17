# AWS Cost Management

## 1. Purpose

This document describes how costs will be monitored and controlled while developing the AWS Infrastructure Platform project.

The goal is to gain practical cloud engineering experience while minimizing unnecessary spending.

## 2. Budget Monitoring

AWS billing tools will be used to review account charges and resource usage.

Planned practices include:

- Review AWS billing regularly.
- Configure AWS Budgets or billing alerts where available.
- Investigate unexpected charges promptly.
- Check which services and regions are generating costs.

Budget alerts help identify potential overspending, but they do not automatically stop resources or prevent all charges.

## 3. Resource Planning

Before creating AWS resources:

- Review the estimated cost where available.
- Identify resources that may incur ongoing charges.
- Avoid creating resources that are not required for the project.
- Use temporary resources only when needed.

## 4. Development and Testing

Development and testing will be performed locally whenever practical.

Docker and the Flask application can be tested locally before using AWS. Cloud resources will be created only when needed for the intended learning objectives.

## 5. Resource Cleanup

After cloud testing is complete:

1. Review the resources managed by Pulumi.
2. Confirm which resources belong to the project.
3. Check for dependencies and data that must be retained.
4. Review the proposed infrastructure changes.
5. Remove temporary resources safely.
6. Check AWS billing and resource inventories afterward.

Some services may retain billable resources or data after the main application is removed. Cleanup must therefore be verified rather than assumed complete.

## 6. Cost Awareness

Potential charges depend on the services, configuration, region, usage, data transfer, and storage.

The project will prioritize cost-conscious configurations and avoid leaving unnecessary resources running.

## 7. Current Status

Billing is being monitored, and no unexpected charges were found during the latest review. Automated budget alerts and the full AWS resource cleanup process will be verified as the project progresses.

This document will be updated as cost controls are configured and tested.