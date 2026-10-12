output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "availability_zones" {
  description = "Availability Zones used"
  value       = data.aws_availability_zones.available.names
}

output "alb_dns_name" {
  description = "Load balancer DNS name after deployment"
  value       = aws_lb.main.dns_name
}

output "autoscaling_group_name" {
  description = "Auto Scaling Group name"
  value       = aws_autoscaling_group.web.name
}
