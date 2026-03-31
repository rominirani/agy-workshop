from flask import Flask, jsonify, request
from processor import process_calc

app = Flask(__name__)

# Intentionally messy and global-reliant logic in the route
@app.route('/calculate', methods=['POST'])
def calculate():
    payload = request.get_json()
    op = payload.get('type')
    v1 = payload.get('a')
    v2 = payload.get('b')
    # Using the legacy processor
    res = process_calc(op, v1, v2)
    if res is None:
        return jsonify({"error": "CALC_FAILED"}), 400
    return jsonify({"result": res})

if __name__ == "__main__":
    app.run(debug=True)
