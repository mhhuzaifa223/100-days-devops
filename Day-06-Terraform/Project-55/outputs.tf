output "vpc_id" {
  description = "Three-tier VPC ID"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "Public web-tier subnet IDs"
  value       = aws_subnet.public[*].id
}

output "application_subnet_ids" {
  description = "Private application-tier subnet IDs"
  value       = aws_subnet.app[*].id
}

output "database_subnet_ids" {
  description = "Private database-tier subnet IDs"
  value       = aws_subnet.db[*].id
}

output "security_group_ids" {
  description = "Security groups for the three tiers"
  value = {
    alb = aws_security_group.alb.id
    web = aws_security_group.web.id
    app = aws_security_group.app.id
    db  = aws_security_group.db.id
  }
}
