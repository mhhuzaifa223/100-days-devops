variable "aws_region" {
  description = "AWS region for this lab"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project resource name prefix"
  type        = string
  default     = "project-56"
}

variable "vpc_cidr" {
  description = "VPC CIDR range"
  type        = string
  default     = "10.56.0.0/16"
}

variable "subnet_cidr" {
  description = "Public subnet CIDR range"
  type        = string
  default     = "10.56.1.0/24"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}
