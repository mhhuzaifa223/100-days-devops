output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "internet_gateway_id" {
  value = aws_internet_gateway.main.id
}

output "bastion_security_group_id" {
  value = aws_security_group.bastion.id
}

output "application_security_group_id" {
  value = aws_security_group.application.id
}

output "private_network_acl_id" {
  value = aws_network_acl.private.id
}
