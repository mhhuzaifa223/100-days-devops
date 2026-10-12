# Project 66 — Serverless Application

## Architecture
Client → API Gateway HTTP API → AWS Lambda → DynamoDB.

An S3 bucket is provisioned for private static frontend assets. CloudFront and public website access are intentionally not enabled in this initial version.

## API
- `GET /health` — health status
- `GET /` — list up to 25 stored messages
- `POST /` — create a message using JSON such as `{"message":"Hello serverless"}`

## Deploy
Run `terraform fmt -recursive`, `terraform init`, `terraform validate`, and `terraform plan`. Review the plan before applying.

## Cost and security
DynamoDB uses on-demand billing. API Gateway and Lambda usage are request-based, but logs and other usage may incur charges. The S3 bucket blocks public access. Destroy resources after testing.

## Cleanup
Run `terraform destroy` and verify resources are removed.
