# Project 54: Application Load Balancer and Auto Scaling Group

## Overview
This project uses Terraform to define an AWS web infrastructure with an Application Load Balancer (ALB) and an EC2 Auto Scaling Group (ASG). It demonstrates traffic distribution, health checks, automated instance replacement, and scalable infrastructure.

## Objectives
- Provision a custom AWS VPC across two Availability Zones.
- Create public subnets, an Internet Gateway, and public routing.
- Configure an Application Load Balancer to receive HTTP traffic.
- Create a target group with HTTP health checks.
- Define an EC2 Launch Template using Amazon Linux 2023.
- Configure an Auto Scaling Group with a minimum of 1, desired capacity of 1, and maximum of 2 instances.
- Restrict web-instance HTTP access to the ALB security group.
- Manage infrastructure as code with Terraform.

## Architecture
Internet -> Application Load Balancer -> Target Group -> EC2 instances managed by Auto Scaling

## Infrastructure
- AWS Region: us-east-1
- VPC CIDR: 10.54.0.0/16
- Public subnet CIDRs: 10.54.1.0/24 and 10.54.2.0/24
- Two Availability Zones
- Internet Gateway and public route table
- ALB security group allowing HTTP on port 80
- Web security group allowing HTTP only from the ALB security group
- Amazon Linux 2023 Launch Template
- Auto Scaling Group: minimum 1, desired 1, maximum 2
- Application Load Balancer with HTTP listener and target-group health checks

## Validation
Run Terraform formatting, initialization, validation, and planning before deployment. Review the plan before applying changes.

## Expected Outputs
- VPC ID
- Availability Zones
- ALB DNS name
- Auto Scaling Group name

After deployment, the ALB DNS name can be used to test the web application. The sample web page displays the responding EC2 instance hostname.

## Security
- Public HTTP traffic reaches the ALB on port 80.
- EC2 instances accept HTTP only from the ALB security group.
- This learning configuration uses HTTP, not HTTPS.
- Production deployments should use HTTPS/TLS, private application subnets, and least-privilege IAM permissions.

## Cost Considerations
The ALB, running EC2 instances, and public IPv4 addresses may incur ongoing AWS charges. Review current pricing and the Terraform plan before deployment. Do not deploy without checking the available budget.

## Cleanup
If deployed, inspect Terraform state and confirm resource ownership before destroying anything. Destroy only resources belonging to this project.

## Skills Demonstrated
- Terraform infrastructure as code
- AWS VPC and subnet networking
- Application Load Balancer configuration
- EC2 Launch Templates
- Auto Scaling Groups
- Security group design
- Health checks and traffic distribution
- Cost-aware infrastructure planning
