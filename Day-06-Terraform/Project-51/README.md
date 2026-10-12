# Project 51: Provision EC2 with Terraform

## Overview
Provision an Amazon EC2 instance and its supporting AWS network infrastructure using Terraform.

## Architecture
- AWS Region: us-east-1
- VPC CIDR: 10.51.0.0/16
- Public Subnet CIDR: 10.51.1.0/24
- Internet Gateway and public route table
- Security group restricting SSH to a configured IPv4 CIDR
- EC2 instance: Amazon Linux 2023, t3.micro
- Root volume: 8 GB gp3, encrypted
- Instance metadata: IMDSv2 required

## Resources
- VPC
- Public subnet
- Internet Gateway
- Public route table and subnet association
- Security group
- EC2 key pair
- EC2 instance

## Terraform Commands
```bash
terraform init
terraform fmt -check
terraform validate
terraform plan
terraform output
```

## Verification
- EC2 instance is running.
- EC2 system and instance status checks passed.
- AWS Systems Manager Session Manager access works.
- SSH from the local VM timed out; SSH connectivity remains unresolved.

## Security
- Never expose SSH to 0.0.0.0/0.
- Keep terraform.tfvars, private keys, and Terraform state out of Git.
- Review Terraform plans before applying changes.

## Cost and Cleanup
The EC2 instance and related resources may incur AWS charges. Check current costs before continuing. Do not destroy resources until you have reviewed the impact.

## Learning Outcomes
- Provision AWS infrastructure with Terraform.
- Understand VPCs, subnets, routes, internet gateways, and security groups.
- Inspect Terraform plans and verify deployed resources.
