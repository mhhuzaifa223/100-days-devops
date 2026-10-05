from flask import Flask
import os
import psycopg2
import redis

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "devops")
DB_USER = os.getenv("POSTGRES_USER", "devops")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devops123")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

@app.route("/")
def home():
    return "Project 32 - Docker Compose Multi-Container App"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/db")
def database():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "message": str(e)}, 500

@app.route("/cache")
def cache():
    try:
        client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
        client.set("project", "project-32")
        return {"redis": client.get("project")}
    except Exception as e:
        return {"redis": "error", "message": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
