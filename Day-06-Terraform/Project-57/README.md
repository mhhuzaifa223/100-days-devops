# Project 57: Terraform Remote State

## Goal
Create an S3 bucket for Terraform state with versioning, encryption, and public-access blocking, plus a DynamoDB table for state locking.

## Resources
- S3 state bucket
- S3 versioning
- S3 server-side encryption
- S3 public access block
- S3 bucket ownership controls
- DynamoDB lock table using pay-per-request billing

## Safety
This project provisions the backend infrastructure only. It does not configure a remote backend or migrate any existing Terraform state. Never commit state files or credentials to GitHub.

## Workflow
Format, initialize, validate, and review the plan. Apply only after confirming the bucket name is globally unique. Verify resources in AWS, then destroy the lab resources after confirming the bucket contains no important state objects.
