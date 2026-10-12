# Project 59: Terraform Drift Detection and Recovery

## Goal
Detect and recover configuration drift when AWS resources are changed outside Terraform.

## Lab
- Provision a small EC2 instance using Terraform.
- Change a resource tag manually in the AWS Console.
- Run Terraform plan to detect the drift.
- Apply the configuration to restore the desired tag.
- Verify the corrected resource and destroy the lab.

## Key concepts
- Desired state versus actual infrastructure
- Terraform state and refresh
- Drift detection with terraform plan
- Recovery using terraform apply

## Safety
This lab creates a billable EC2 instance. Use only the designated Project-59 directory and destroy the instance after the exercise.
