output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.lab.id
}

output "public_ip" {
  description = "Public IPv4 address of the EC2 instance"
  value       = aws_instance.lab.public_ip
}

output "ssh_command" {
  description = "Command to connect to the instance"
  value       = "ssh -i ~/.ssh/id_ed25519 ec2-user@${aws_instance.lab.public_ip}"
}
