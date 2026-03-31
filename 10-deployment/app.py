import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Ready for Deployment!",
        "version": "1.0.0",
        "env": os.getenv("FLASK_ENV", "production")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # In production, we typically use gunicorn, not app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
