# Project 62: Highly Available Web Application

## Objective
Deploy an HTTP application behind an AWS Application Load Balancer, with two EC2 web servers in separate Availability Zones.

## Architecture
Internet → Application Load Balancer → EC2 web servers in two Availability Zones.

## AWS services
- Amazon VPC, public subnets, and Internet Gateway
- Application Load Balancer and target group
- EC2 and security groups
- Terraform

## Security notes
- The ALB accepts HTTP on port 80.
- Web servers accept HTTP only from the ALB security group.
- This learning demo uses public subnets and public EC2 addresses; production systems should consider private application subnets and tighter egress controls.
- HTTP is not encrypted. HTTPS and a custom domain are outside this version.

## Cost and cleanup
The ALB and EC2 instances can incur charges while deployed. Destroy resources immediately after testing.

## Commands
```sh
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform destroy
}
