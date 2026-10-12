output "application_url" {
  value = "http://${aws_lb.main.dns_name}"
}

output "autoscaling_group_name" {
  value = aws_autoscaling_group.web.name
}

output "min_desired_max_capacity" {
  value = {
    minimum = aws_autoscaling_group.web.min_size
    desired = aws_autoscaling_group.web.desired_capacity
    maximum = aws_autoscaling_group.web.max_size
  }
}
