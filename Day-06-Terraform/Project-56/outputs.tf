output "vpc_id" {
  description = "VPC created by the VPC module"
  value       = module.vpc.vpc_id
}

output "public_subnet_id" {
  description = "Public subnet created by the VPC module"
  value       = module.vpc.public_subnet_id
}

output "instance_id" {
  description = "EC2 instance created by the EC2 module"
  value       = module.ec2.instance_id
}

output "instance_private_ip" {
  description = "Private IP of the EC2 instance"
  value       = module.ec2.private_ip
}
