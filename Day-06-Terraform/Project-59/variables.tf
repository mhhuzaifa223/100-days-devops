variable "aws_region" {
  description = "AWS region for the drift detection lab"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Desired EC2 instance type"
  type        = string
  default     = "t3.micro"
}
