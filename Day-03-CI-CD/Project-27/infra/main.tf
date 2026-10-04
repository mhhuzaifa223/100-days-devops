terraform {
  required_version = ">= 1.0"
}

resource "aws_s3_bucket" "devsecops_demo" {
  bucket = "devsecops-project-27-demo"

  tags = {
    Project = "DevSecOps-Project-27"
  }
}
