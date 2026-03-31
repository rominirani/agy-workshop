from flask import Flask, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return None
    return a / b

@app.route('/calculate')
def calculate():
    # Intentionally simple for testing
    return jsonify({"result": add(10, 5)})

if __name__ == "__main__":
    app.run(debug=True)
