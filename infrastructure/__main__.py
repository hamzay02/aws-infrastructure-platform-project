

"""AWS Infrastructure Platform - Pulumi entry point."""

import json

import pulumi
import pulumi_aws as aws

project_name = "aws-infrastructure-platform"
environment = pulumi.get_stack()

# Existing VPC.
vpc = aws.ec2.Vpc(
    "portfolio-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_support=True,
    enable_dns_hostnames=True,
    tags={
        "Name": f"{project_name}-{environment}-vpc",
        "Environment": environment,
        "Project": project_name,
    },
)

# Internet Gateway for public subnet routing.
internet_gateway = aws.ec2.InternetGateway(
    "portfolio-igw",
    vpc_id=vpc.id,
    tags={"Name": f"{project_name}-{environment}-igw"},
)

# Public route table: send internet-bound traffic to the IGW.
public_route_table = aws.ec2.RouteTable(
    "public-route-table",
    vpc_id=vpc.id,
    routes=[
        {
            "cidr_block": "0.0.0.0/0",
            "gateway_id": internet_gateway.id,
        }
    ],
    tags={"Name": f"{project_name}-{environment}-public-rt"},
)

# Private route table: no internet route or NAT Gateway yet.
private_route_table = aws.ec2.RouteTable(
    "private-route-table",
    vpc_id=vpc.id,
    tags={"Name": f"{project_name}-{environment}-private-rt"},
)

# Two Availability Zones.
availability_zones = aws.get_availability_zones(
    state="available"
)

# Public subnet in Availability Zone 1.
public_subnet_1 = aws.ec2.Subnet(
    "public-subnet-1",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    availability_zone=availability_zones.names[0],
    map_public_ip_on_launch=True,
    tags={"Name": f"{project_name}-{environment}-public-1"},
)

# Public subnet in Availability Zone 2.
public_subnet_2 = aws.ec2.Subnet(
    "public-subnet-2",
    vpc_id=vpc.id,
    cidr_block="10.0.2.0/24",
    availability_zone=availability_zones.names[1],
    map_public_ip_on_launch=True,
    tags={"Name": f"{project_name}-{environment}-public-2"},
)

# Private subnet in Availability Zone 1.
private_subnet_1 = aws.ec2.Subnet(
    "private-subnet-1",
    vpc_id=vpc.id,
    cidr_block="10.0.11.0/24",
    availability_zone=availability_zones.names[0],
    tags={"Name": f"{project_name}-{environment}-private-1"},
)

# Private subnet in Availability Zone 2.
private_subnet_2 = aws.ec2.Subnet(
    "private-subnet-2",
    vpc_id=vpc.id,
    cidr_block="10.0.12.0/24",
    availability_zone=availability_zones.names[1],
    tags={"Name": f"{project_name}-{environment}-private-2"},
)

# Associate both public subnets with the public route table.
public_association_1 = aws.ec2.RouteTableAssociation(
    "public-association-1",
    subnet_id=public_subnet_1.id,
    route_table_id=public_route_table.id,
)

public_association_2 = aws.ec2.RouteTableAssociation(
    "public-association-2",
    subnet_id=public_subnet_2.id,
    route_table_id=public_route_table.id,
)

# Associate both private subnets with the private route table.
private_association_1 = aws.ec2.RouteTableAssociation(
    "private-association-1",
    subnet_id=private_subnet_1.id,
    route_table_id=private_route_table.id,
)

private_association_2 = aws.ec2.RouteTableAssociation(
    "private-association-2",
    subnet_id=private_subnet_2.id,
    route_table_id=private_route_table.id,
)


# Security group for the application.
app_security_group = aws.ec2.SecurityGroup(
    "app-security-group",
    vpc_id=vpc.id,
    description="Allow application traffic from within the VPC",
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 5000,
            "to_port": 5000,
            "cidr_blocks": ["10.0.0.0/16"],
            "description": "Flask application traffic from the VPC",
        }
    ],
    tags={
        "Name": f"{project_name}-{environment}-app-sg",
        "Project": project_name,
        "Environment": environment,
    },
)

# ECR repository for the Flask application's Docker image.
app_repository = aws.ecr.Repository(
    "app-repository",
    name=f"{project_name}-{environment}",
    image_tag_mutability="MUTABLE",
    image_scanning_configuration={
        "scan_on_push": True,
    },
    force_delete=True,
    tags={
        "Name": f"{project_name}-{environment}-ecr",
        "Project": project_name,
        "Environment": environment,
    },
)

# ECS cluster for running the application
app_cluster = aws.ecs.Cluster(
    "app-cluster",
    name=f"{project_name}-{environment}",
    settings=[
        {
            "name": "containerInsights",
            "value": "enabled",
        }
    ],
    tags={
        "Name": f"{project_name}-{environment}-ecs",
        "Project": project_name,
        "Environment": environment,
    },
)


# IAM role that ECS tasks use to pull images and publish logs.
task_execution_role = aws.iam.Role(
    "task-execution-role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "ecs-tasks.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }""",
    tags={
        "Name": f"{project_name}-{environment}-task-execution-role",
        "Project": project_name,
        "Environment": environment,
    },
)

# AWS-managed permissions for pulling from ECR and writing logs.
task_execution_policy = aws.iam.RolePolicyAttachment(
    "task-execution-policy",
    role=task_execution_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
)

# CloudWatch log group with 7-day retention.
app_log_group = aws.cloudwatch.LogGroup(
    "app-log-group",
    name=f"/ecs/{project_name}-{environment}",
    retention_in_days=7,
    tags={
        "Project": project_name,
        "Environment": environment,
    },
)

# Task definition: instructions for running the Flask container.
app_task_definition = aws.ecs.TaskDefinition(
    "app-task-definition",
    family=f"{project_name}-{environment}",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    execution_role_arn=task_execution_role.arn,
    container_definitions=pulumi.Output.all(
        app_repository.repository_url,
        app_log_group.name,
        aws.get_region().region,
    ).apply(lambda args: json.dumps([
        {
            "name": "flask-app",
            "image": f"{args[0]}:latest",
            "essential": True,
            "portMappings": [
                {
                    "containerPort": 5000,
                    "hostPort": 5000,
                    "protocol": "tcp",
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": args[1],
                    "awslogs-region": args[2],
                    "awslogs-stream-prefix": "ecs",
                },
            },
        }
    ])),
    tags={
        "Name": f"{project_name}-{environment}-task",
        "Project": project_name,
        "Environment": environment,
    },
)

pulumi.export("project_name", project_name)
pulumi.export("environment", environment)
pulumi.export("vpc_id", vpc.id)
pulumi.export("vpc_cidr", vpc.cidr_block)
pulumi.export("internet_gateway_id", internet_gateway.id)
pulumi.export("public_subnet_ids", [
    public_subnet_1.id,
    public_subnet_2.id,
])
pulumi.export("private_subnet_ids", [
    private_subnet_1.id,
    private_subnet_2.id,
])

pulumi.export("app_security_group_id", app_security_group.id)
pulumi.export("ecr_repository_url", app_repository.repository_url)
pulumi.export("ecs_cluster_name", app_cluster.name)
pulumi.export("ecs_cluster_arn", app_cluster.arn)
pulumi.export("ecs_task_definition_arn", app_task_definition.arn)
pulumi.export("ecs_log_group_name", app_log_group.name)
