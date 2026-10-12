# Project 65 — Private Application Using ALB + NAT

## Objective
Deploy a small AWS application whose EC2 instances remain in private subnets and are reachable from the internet only through a public Application Load Balancer (ALB).

## Architecture
- One VPC across two Availability Zones
- Two public subnets and two private application subnets
- Internet Gateway for public subnet routing
- One NAT Gateway and Elastic IP for private-instance outbound internet access
- Public ALB, HTTP listener, target group, and health checks
- Two Amazon Linux 2023 EC2 instances without public IP addresses
- Security group permits application HTTP traffic only from the ALB security group

## Deploy
Run `terraform init`, `terraform validate`, and `terraform plan`. Review the complete plan and costs before running `terraform apply`.

## Cost warning
The NAT Gateway and ALB incur ongoing hourly charges; NAT data processing, public IPv4, EC2, and storage may add charges. Destroy the lab immediately after testing.

## Cleanup
Run `terraform destroy` and verify that the ALB, NAT Gateway, Elastic IP, EC2 instances, and networking resources have been removed.
