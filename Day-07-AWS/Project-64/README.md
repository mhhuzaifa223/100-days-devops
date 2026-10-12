# Project 64: Three-Tier AWS Architecture

## Objective
Build a segmented AWS network for a web, application, and database architecture using Terraform.

## Network design
- VPC: 10.64.0.0/16
- Web subnets: 10.64.1.0/24 and 10.64.2.0/24
- Application subnets: 10.64.11.0/24 and 10.64.12.0/24
- Database subnets: 10.64.21.0/24 and 10.64.22.0/24
- Two Availability Zones
- Internet Gateway and public routing for web subnets
- Separate route tables for application and database subnets
- Web, application, and database security groups

## Security
- Web tier accepts HTTP on port 80.
- Application tier accepts port 8080 only from the web security group.
- Database tier accepts PostgreSQL on port 5432 only from the application security group.
- Application and database subnets have no direct internet route.

## Cost and scope
This initial version creates networking and security resources only. It does not create EC2 instances, an ALB, NAT Gateways, or RDS. Review the Terraform plan before applying.

## Commands
1. `terraform init`
2. `terraform fmt -recursive`
3. `terraform validate`
4. `terraform plan`
5. `terraform apply`
6. `terraform destroy`

## Cleanup
Run `terraform destroy` after verification. Never commit Terraform state, credentials, or private keys.
