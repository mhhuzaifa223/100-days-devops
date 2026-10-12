# Project 68 — Centralized Logging Architecture

## Architecture

Application logs → Amazon CloudWatch Logs → Amazon S3 archive

## Resources

- CloudWatch Log Group with 7-day retention
- Private S3 archive bucket
- S3 public access block
- S3 server-side encryption
- S3 versioning
- IAM role and policy for CloudWatch Logs export permissions

## Learning objectives

- Centralize application logs
- Set retention policies
- Understand S3 log archiving
- Apply least-privilege access and private storage controls
- Manage logging infrastructure with Terraform

## Important

The initial version creates the logging foundation. Exporting logs from CloudWatch to S3 is a separate operation and must be configured and tested before the archive contains logs.

OpenSearch is excluded from the initial deployment to control costs.

## Validation results

- Created a CloudWatch log stream and ingested a test event.
- Retrieved the event successfully using the CloudWatch Logs API.
- Exported the log group to the private S3 archive.
- Confirmed that exported objects exist in S3, including a compressed `.gz` log file.
- Confirmed the export task completed successfully.

## Architecture and limitations

Application/test logs → CloudWatch Logs → on-demand S3 export.

The S3 export is manual and is not continuous or automatically scheduled.
OpenSearch and a real-time streaming pipeline are not included in this version.
The archive bucket uses private access controls, server-side encryption,
and versioning. The CloudWatch log group has a 7-day retention policy.
