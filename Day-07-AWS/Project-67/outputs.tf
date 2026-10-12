output "website_url" {
  description = "HTTPS URL of the CloudFront website"
  value       = "https://${aws_cloudfront_distribution.website.domain_name}"
}

output "cloudfront_distribution_id" {
  value = aws_cloudfront_distribution.website.id
}

output "s3_bucket_name" {
  value = aws_s3_bucket.website.bucket
}
