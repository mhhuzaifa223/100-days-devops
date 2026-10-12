data "aws_caller_identity" "current" {}

resource "aws_cloudwatch_log_group" "application" {
  name              = "/devops/${var.project_name}/application"
  retention_in_days = var.log_retention_days

  tags = {
    Project = var.project_name
  }
}

resource "aws_s3_bucket" "archive" {
  bucket        = "${var.project_name}-${data.aws_caller_identity.current.account_id}-logs"
  force_destroy = true

  tags = {
    Project = var.project_name
    Purpose = "Log archive"
  }
}

resource "aws_s3_bucket_public_access_block" "archive" {
  bucket                  = aws_s3_bucket.archive.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "archive" {
  bucket = aws_s3_bucket.archive.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "archive" {
  bucket = aws_s3_bucket.archive.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_iam_role" "export" {
  name = "${var.project_name}-logs-export-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "logs.us-east-1.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "export" {
  name = "${var.project_name}-logs-export-policy"
  role = aws_iam_role.export.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetBucketAcl",
          "s3:PutObject"
        ]
        Resource = [
          aws_s3_bucket.archive.arn,
          "${aws_s3_bucket.archive.arn}/*"
        ]
      }
    ]
  })
}

resource "aws_s3_bucket_policy" "archive" {
  bucket = aws_s3_bucket.archive.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid    = "AllowCloudWatchLogsExport"
      Effect = "Allow"
      Principal = {
        Service = "logs.us-east-1.amazonaws.com"
      }
      Action = ["s3:GetBucketAcl", "s3:PutObject"]
      Resource = [
        aws_s3_bucket.archive.arn,
        "${aws_s3_bucket.archive.arn}/*"
      ]
      Condition = {
        StringEquals = {
          "aws:SourceAccount" = data.aws_caller_identity.current.account_id
        }
      }
    }]
  })

  depends_on = [aws_s3_bucket_public_access_block.archive]
}
