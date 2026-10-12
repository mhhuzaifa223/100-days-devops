variable "aws_region" {
  description = "AWS region for the Multi-AZ network"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project resource name prefix"
  type        = string
  default     = "project-53"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.53.0.0/16"
}
