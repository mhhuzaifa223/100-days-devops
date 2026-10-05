from flask import Flask

app = Flask(__name__)

VERSION = "2.0.0"

@app.route("/")
def home():
    return f"Project 30 - Production Application v{VERSION}"

@app.route("/health")
def health():
    return {"status": "healthy", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
