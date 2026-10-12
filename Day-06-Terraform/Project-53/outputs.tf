output "vpc_id" {
  description = "ID of the Multi-AZ VPC"
  value       = aws_vpc.main.id
}

output "availability_zones" {
  description = "Availability Zones used by this network"
  value = {
    public_a  = aws_subnet.this["public_a"].availability_zone
    public_b  = aws_subnet.this["public_b"].availability_zone
    private_a = aws_subnet.this["private_a"].availability_zone
    private_b = aws_subnet.this["private_b"].availability_zone
  }
}

output "subnet_ids" {
  description = "Public and private subnet IDs"
  value       = { for name, subnet in aws_subnet.this : name => subnet.id }
}

output "public_route_table_id" {
  value = aws_route_table.public.id
}

output "private_route_table_ids" {
  value = { for name, table in aws_route_table.private : name => table.id }
}
