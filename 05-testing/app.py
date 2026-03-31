from flask import Flask, jsonify, request
from finance_utils import convert_currency, calculate_tax, calculate_total

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    val = float(request.args.get('amt', 0))
    rate = float(request.args.get('rate', 1))
    res = convert_currency(val, rate)
    if res is None:
        return jsonify({"error": "INVALID_INPUT"}), 400
    return jsonify({"result": res})

@app.route('/tax', methods=['POST'])
def tax():
    data = request.json
    price = data.get('price', 0)
    rate = data.get('rate', 0)
    res = calculate_tax(price, rate)
    return jsonify({"tax": res})

if __name__ == "__main__":
    app.run(debug=True)
