# Project 61 — Secure VPC Architecture

## Objective
Build a segmented AWS VPC with public and private subnets, an Internet Gateway, route tables, security groups, and a private-subnet network ACL.

## Architecture
- One VPC across two Availability Zones
- Two public subnets with routes to the Internet Gateway
- Two private subnets without a default internet route
- Separate public and private route tables
- Bastion and application security groups
- A custom network ACL associated with the private subnets

## Cost and safety
This foundation intentionally excludes NAT Gateways, EC2 instances, and RDS databases. No SSH access is exposed to the whole internet; the operator must provide their public IPv4 address with `/32`.

## Deployment
Initialize Terraform, review the plan, apply only after confirming the resources, verify them in the AWS Console, and destroy the lab when finished.

## Cleanup
Run `terraform destroy` from this directory after verifying the plan contains only Project 61 resources.
