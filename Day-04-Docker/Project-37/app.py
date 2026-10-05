from flask import Flask

app = Flask(__name__)

healthy = True

@app.route("/")
def home():
    return "Project 37 - Health Check Application"

@app.route("/health")
def health():
    if healthy:
        return "healthy", 200
    return "unhealthy", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
