variable "aws_region" {
  description = "AWS region for Project 61"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project resource name prefix"
  type        = string
  default     = "project-61"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.61.0.0/16"
}

variable "my_ip_cidr" {
  description = "Public IPv4 CIDR allowed to SSH into the bastion"
  type        = string
}
