# Project 56: Terraform Modules

## Goal
Build reusable Terraform child modules and compose them from a root module.

## Architecture
Root module -> VPC module -> VPC, internet gateway, public subnet and route table.
Root module -> EC2 module -> security group and one EC2 instance.

## Modules
- modules/vpc: reusable network infrastructure.
- modules/ec2: reusable EC2 instance and security group.

## Concepts
- Module inputs and outputs
- Passing outputs between modules
- Reusing infrastructure code
- Terraform dependency graph
- Resource naming and tagging

## Cost and security
The EC2 instance can incur charges while running. Apply only for the lab session and destroy it afterward. The security group has no inbound rules by default, so SSH is not exposed to the internet. Outbound traffic is allowed.

## Workflow
Format and validate the configuration, inspect the plan, apply, verify the resources in AWS, destroy, and confirm cleanup.
