output "vpc_id" {
  description = "Project VPC ID"
  value       = aws_vpc.main.id
}

output "availability_zones" {
  description = "Availability zones used"
  value       = data.aws_availability_zones.available.names
}

output "subnet_ids" {
  description = "Subnet IDs grouped by tier"
  value = {
    web = [aws_subnet.web_a.id, aws_subnet.web_b.id]
    app = [aws_subnet.app_a.id, aws_subnet.app_b.id]
    db  = [aws_subnet.db_a.id, aws_subnet.db_b.id]
  }
}

output "security_group_ids" {
  description = "Security groups for each tier"
  value = {
    web = aws_security_group.web.id
    app = aws_security_group.app.id
    db  = aws_security_group.database.id
  }
}
