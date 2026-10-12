# Project 69 — AWS Disaster Recovery Architecture

## Initial architecture

Primary AWS region (us-east-1)
  -> Private, encrypted, versioned S3 backup bucket

Recovery AWS region (us-west-2)
  -> Private, encrypted, versioned S3 recovery bucket

## Security

- S3 public access is blocked in both regions.
- Server-side encryption is enabled.
- Bucket versioning is enabled.
- No compute instances or databases are launched in this initial version.

## Limitations

The buckets are created independently. Cross-region replication,
automated backup scheduling, DNS failover, and application recovery
are not configured in this initial version.

## Cost and cleanup

S3 storage, requests, and any future cross-region data transfer may incur
charges. Terraform force_destroy is enabled for these dedicated lab buckets;
destroying this project can delete their objects and versions.

## Validation results

- Confirmed both S3 buckets exist in their intended regions.
- Confirmed versioning is enabled on both buckets.
- Uploaded a sample file to the primary bucket in us-east-1.
- Copied the file to the recovery bucket in us-west-2.
- Downloaded the recovery copy and confirmed its contents matched.

## Recovery test

The lab demonstrates a manual cross-region copy and recovery workflow.
Automatic S3 replication, Route 53 failover, scheduled backups, and
application/database recovery are not implemented in this version.
