from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Project 29 - GREEN Version"

@app.route("/health")
def health():
    return {"status": "healthy", "version": "green"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
