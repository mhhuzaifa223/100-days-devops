import json
import os
import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    method = event.get("httpMethod", "GET")
    path = event.get("path", "/")

    if method == "GET" and path.endswith("/health"):
        return response(200, {"status": "healthy", "service": "project-66"})

    if method == "GET":
        result = table.scan(Limit=25)
        return response(200, {"items": result.get("Items", [])})

    if method == "POST":
        try:
            body = json.loads(event.get("body") or "{}")
        except json.JSONDecodeError:
            return response(400, {"error": "Request body must be valid JSON"})

        message = body.get("message")
        if not isinstance(message, str) or not message.strip():
            return response(400, {"error": "Provide a non-empty message"})

        item = {
            "id": context.aws_request_id,
            "message": message.strip(),
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        table.put_item(Item=item)
        return response(201, item)

    return response(405, {"error": "Method not allowed"})

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
        },
        "body": json.dumps(body, default=str)
    }
