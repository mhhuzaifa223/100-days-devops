# Project 60: Production AWS Infrastructure with Terraform

## Objective
Design a secure, scalable, highly available AWS architecture using Terraform.

## Architecture
- VPC with public and private subnets across multiple Availability Zones
- Internet Gateway and carefully controlled routing
- Application Load Balancer for incoming application traffic
- EC2 Auto Scaling for application compute
- RDS Multi-AZ for database availability
- S3 for application assets and backups
- IAM and security groups for access control
- CloudWatch for monitoring and alarms

## Implementation strategy
1. Design and review the architecture.
2. Build reusable Terraform modules.
3. Validate the configuration and inspect the plan.
4. Estimate costs before deploying.
5. Deploy only approved, cost-controlled resources.
6. Verify resources and clean up after testing.

## Security and cost controls
- Do not expose application or database instances directly to the internet.
- Do not commit Terraform state, credentials, or private keys.
- Review every Terraform plan before applying.
- Do not deploy expensive persistent resources without an explicit cost review and approval.
