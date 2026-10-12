data "aws_ssm_parameter" "ami" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
}

resource "aws_vpc" "drift" {
  cidr_block           = "10.59.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name    = "project-59-drift-vpc"
    Project = "Project-59"
  }
}

resource "aws_subnet" "drift" {
  vpc_id                  = aws_vpc.drift.id
  cidr_block              = "10.59.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name    = "project-59-drift-subnet"
    Project = "Project-59"
  }
}

resource "aws_instance" "web" {
  ami                         = data.aws_ssm_parameter.ami.value
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.drift.id
  associate_public_ip_address = false

  tags = {
    Name        = "project-59-drift-demo"
    Environment = "dev"
    Owner       = "admin"
    Project     = "Project-59"
  }
}
