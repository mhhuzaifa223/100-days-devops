variable "aws_region" {
  description = "AWS region for Project 52"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name used to tag Project 52 resources"
  type        = string
  default     = "project-52"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.52.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  type        = string
  default     = "10.52.1.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR block for the private subnet"
  type        = string
  default     = "10.52.2.0/24"
}
