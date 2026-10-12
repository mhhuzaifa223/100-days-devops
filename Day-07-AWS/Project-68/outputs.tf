output "log_group_name" {
  value = aws_cloudwatch_log_group.application.name
}

output "archive_bucket_name" {
  value = aws_s3_bucket.archive.bucket
}

output "aws_region" {
  value = var.aws_region
}
