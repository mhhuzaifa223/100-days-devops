variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "project-58"
}

variable "environment" {
  description = "Environment name selected by the Terraform workspace"
  type        = string
}

variable "vpc_cidr" {
  description = "Environment-specific VPC CIDR"
  type        = string
}

variable "subnet_cidr" {
  description = "Environment-specific subnet CIDR"
  type        = string
}
