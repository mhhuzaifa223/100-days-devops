variable "aws_region" {
  description = "AWS region for the backend lab"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Globally unique S3 bucket name; change this if already taken"
  type        = string
  default     = "huzaifa-terraform-state-project57-2026"
}

variable "dynamodb_table_name" {
  description = "DynamoDB table used for Terraform state locking"
  type        = string
  default     = "project-57-terraform-locks"
}
