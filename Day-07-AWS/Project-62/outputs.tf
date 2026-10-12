output "application_url" {
  value = "http://${aws_lb.main.dns_name}"
}

output "availability_zones" {
  value = aws_instance.web[*].availability_zone
}

output "instance_ids" {
  value = aws_instance.web[*].id
}
