variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Resource name prefix"
  type        = string
  default     = "project-54"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.54.0.0/16"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}
