import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for Next.js frontend

# Simulated database
ANALYTICS_DATA = [
    {"day": "Mon", "value": 120},
    {"day": "Tue", "value": 180},
    {"day": "Wed", "value": 150},
    {"day": "Thu", "value": 210},
    {"day": "Fri", "value": 250},
]

@app.route("/")
def index():
    return jsonify({"message": "Modern Analytics API is running v1.0"})

@app.route("/api/analytics")
def get_analytics():
    # BUG (Server-Side): Directly accessing 'range' without checking if it exists.
    # If the query parameter is missing, it will raise a KeyError (which Flask turns into 400).
    # Attendees should fix this to use request.args.get('range', 'all_time').
    range_type = request.args['range']
    
    return jsonify({
        "status": "success",
        "range": range_type,
        "data": ANALYTICS_DATA
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
