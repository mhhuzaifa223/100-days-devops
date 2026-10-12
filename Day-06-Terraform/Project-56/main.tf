data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_ssm_parameter" "al2023" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
}

module "vpc" {
  source = "./modules/vpc"

  project_name      = var.project_name
  vpc_cidr          = var.vpc_cidr
  subnet_cidr       = var.subnet_cidr
  availability_zone = data.aws_availability_zones.available.names[0]
}

module "ec2" {
  source = "./modules/ec2"

  project_name  = var.project_name
  vpc_id        = module.vpc.vpc_id
  subnet_id     = module.vpc.public_subnet_id
  ami_id        = data.aws_ssm_parameter.al2023.value
  instance_type = var.instance_type
}
