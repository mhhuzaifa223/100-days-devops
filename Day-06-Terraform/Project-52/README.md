# Project 52 — Complete VPC with Terraform

## Objective
Build a custom AWS VPC with public and private subnets, an Internet Gateway, and separate route tables using Terraform.

## Architecture
- Region: us-east-1
- VPC: 10.52.0.0/16
- Public subnet: 10.52.1.0/24
- Private subnet: 10.52.2.0/24
- Internet Gateway attached to the VPC
- Public route table with a default route to the Internet Gateway
- Separate private route table without a default internet route
- DNS support and DNS hostnames enabled

## Security and Cost
No EC2 instances or NAT Gateway are created by this configuration. A NAT Gateway is intentionally excluded because it incurs ongoing charges.

## Validation
Run `terraform fmt`, `terraform init`, `terraform validate`, and `terraform plan`.

Review the plan before provisioning resources.
