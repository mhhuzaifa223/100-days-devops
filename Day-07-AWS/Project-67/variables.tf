variable "aws_region" {
  description = "AWS region for the S3 bucket"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project resource name prefix"
  type        = string
  default     = "project-67"
}
