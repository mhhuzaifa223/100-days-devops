# Project 55: Three-Tier AWS Infrastructure with Terraform

## Overview
Design a segmented AWS network for a three-tier application: web, application, and database. Terraform defines the network, subnet layout, route tables, and tier-specific security groups.

## Architecture
Internet -> Public Web Subnets -> Private Application Subnets -> Private Database Subnets

## Network Design
- Region: us-east-1
- VPC: 10.55.0.0/16
- Web subnets: 10.55.1.0/24 and 10.55.2.0/24
- Application subnets: 10.55.11.0/24 and 10.55.12.0/24
- Database subnets: 10.55.21.0/24 and 10.55.22.0/24
- Two Availability Zones
- Internet Gateway and public route table
- Separate private route tables for application and database subnets

## Security
- ALB security group accepts HTTP on port 80 from the internet.
- Web security group accepts HTTP only from the ALB security group.
- Application security group accepts TCP 8080 only from the web security group.
- Database security group accepts PostgreSQL TCP 5432 only from the application security group.
- Application and database subnets have no direct internet route.

## Cost-Conscious Scope
This project creates the Terraform configuration for the network and security foundation. It does not currently create an ALB, EC2 instances, NAT Gateways, or RDS. NAT Gateways and Multi-AZ RDS can generate significant charges, so add and deploy those components only after reviewing the budget and architecture.

## Validation
Run `terraform fmt`, `terraform init`, `terraform validate`, and `terraform plan`. Review the plan before any apply operation.

## Learning Outcomes
- Design a three-tier AWS network
- Separate public and private subnets
- Apply least-privilege security group rules
- Understand routing between tiers
- Use Terraform variables, resources, and outputs
- Review infrastructure changes before deployment

## Cleanup
No resources are created by `terraform plan`. If resources are deployed later, review Terraform state and ownership before destroying anything.
