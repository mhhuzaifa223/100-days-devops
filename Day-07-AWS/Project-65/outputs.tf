output "application_url" {
  description = "Public URL for the application"
  value       = "http://${aws_lb.app.dns_name}"
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_instance_ids" {
  value = aws_instance.app[*].id
}

output "nat_gateway_id" {
  value = aws_nat_gateway.main.id
}

output "alb_dns_name" {
  value = aws_lb.app.dns_name
}
