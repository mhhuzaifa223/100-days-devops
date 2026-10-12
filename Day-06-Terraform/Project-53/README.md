# Project 53 — Multi-AZ Network Infrastructure

## Objective
Build a resilient AWS network across two Availability Zones using Terraform.

## Architecture
- One VPC: `10.53.0.0/16`
- Public subnet A: `10.53.1.0/24`
- Public subnet B: `10.53.2.0/24`
- Private subnet A: `10.53.11.0/24`
- Private subnet B: `10.53.12.0/24`
- Internet Gateway for public-subnet internet routing
- One public route table shared by both public subnets
- Separate private route tables associated with the private subnets
- No NAT Gateways, EC2 instances, or other application resources

## Routing and security
Public subnets have a default route to the Internet Gateway. Private subnets have no default internet route; they retain only the VPC's local route. No inbound security-group rules or compute resources are created by this project.

## Cost considerations
VPCs, subnets, route tables, and Internet Gateways generally have no hourly charge, but public IPv4 addresses and other added services can incur charges. NAT Gateways are intentionally omitted.

## Validation
Run `terraform fmt`, `terraform init`, `terraform validate`, and `terraform plan`. Review the plan before applying.

## Cleanup
If resources are provisioned, review the Terraform state and plan carefully before running `terraform destroy`. Do not destroy resources managed by another project or state.
