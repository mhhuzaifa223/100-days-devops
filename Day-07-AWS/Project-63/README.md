# Project 63: Auto Scaling Application Infrastructure

## Objective
Deploy a web application behind an Application Load Balancer with an EC2 Auto Scaling Group and CPU target-tracking policy.

## Architecture
Internet -> Application Load Balancer -> Auto Scaling Group -> EC2 web servers across two Availability Zones.

## AWS services
- VPC, public subnets, Internet Gateway and route table
- Application Load Balancer, listener and target group
- EC2 launch template and Auto Scaling Group
- CloudWatch metrics through the target-tracking scaling policy
- Terraform

## Scaling configuration
- Minimum instances: 2
- Desired instances: 2
- Maximum instances: 3
- Target average CPU utilization: 50%

## Security and limitations
The ALB accepts public HTTP traffic on port 80. Instances accept HTTP only from the ALB security group. This demo uses public subnets and does not configure HTTPS, a database, or NAT Gateways.

## Cost and cleanup
The ALB, EC2 instances, and related services can incur charges while deployed. Destroy resources immediately after testing.

## Commands
- terraform init
- terraform fmt
- terraform validate
- terraform plan
- terraform apply
- terraform destroy
