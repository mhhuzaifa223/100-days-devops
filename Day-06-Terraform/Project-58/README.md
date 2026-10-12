# Project 58: Multi-Environment Terraform

## Goal
Use one Terraform configuration with separate Dev, QA, and Prod workspace state.

## Infrastructure
Each environment defines a VPC and one subnet. The environment variable and workspace are used to label resources.

## Environment inputs
- Dev: VPC 10.58.0.0/16, subnet 10.58.1.0/24
- QA: VPC 10.59.0.0/16, subnet 10.59.1.0/24
- Prod: VPC 10.60.0.0/16, subnet 10.60.1.0/24

## Safety
Workspaces separate Terraform state, but they do not provide complete security isolation. Review plans carefully and never apply to Prod without approval.

## Workflow
Select a workspace, use its environment variable file, validate and plan, then apply only when approved. Destroy test environments when finished.
