output "api_base_url" {
  value = aws_apigatewayv2_api.api.api_endpoint
}

output "health_url" {
  value = "${aws_apigatewayv2_api.api.api_endpoint}/health"
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.messages.name
}

output "lambda_function_name" {
  value = aws_lambda_function.api.function_name
}

output "frontend_bucket_name" {
  value = aws_s3_bucket.frontend.bucket
}
