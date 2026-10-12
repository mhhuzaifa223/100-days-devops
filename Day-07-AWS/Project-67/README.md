# Project 67 — Static Website + CDN Architecture

## Architecture

Browser (HTTPS) → Amazon CloudFront → private Amazon S3 bucket

## What this project demonstrates

- Static website hosting with S3 object storage
- CloudFront content delivery and caching
- Origin Access Control (OAC) for private S3 access
- HTTPS delivery using the default CloudFront certificate
- Infrastructure as Code using Terraform

## Deployment

Initialize and validate Terraform, then inspect the plan before applying.

After deployment, retrieve the website URL using `terraform output website_url`.

## Security

S3 public access is blocked. CloudFront receives read-only access to objects through a bucket policy restricted to this distribution.

## Cost and cleanup

CloudFront distribution usage and S3 storage/requests may incur charges. Destroy the Terraform-managed resources when finished testing. The S3 bucket uses `force_destroy`, so objects in this dedicated project bucket will be deleted during Terraform destroy.
