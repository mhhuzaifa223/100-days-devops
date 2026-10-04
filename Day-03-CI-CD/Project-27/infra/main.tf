terraform {
  required_version = ">= 1.0"
}

resource "aws_s3_bucket" "devsecops_demo" {
  bucket = "devsecops-project-27-demo"

  tags = {
    Project = "DevSecOps-Project-27"
  }
}

resource "aws_s3_bucket_public_access_block" "devsecops_demo" {
  bucket = aws_s3_bucket.devsecops_demo.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "devsecops_demo" {
  bucket = aws_s3_bucket.devsecops_demo.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "devsecops_demo" {
  bucket = aws_s3_bucket.devsecops_demo.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "devsecops_demo" {
  bucket = aws_s3_bucket.devsecops_demo.id

  rule {
    id     = "cleanup"
    status = "Enabled"

    expiration {
      days = 365
    }
  }
}
