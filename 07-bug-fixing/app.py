from flask import Flask, request, jsonify

app = Flask(__name__)

# BUG 1: Shared Global State
# Items are added to this global list and NEVER cleared,
# so every new request sees items from all previous requests!
order_history = []

@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    items = data.get("items", [])
    for item in items:
        order_history.append(item)
    
    # BUG 2: Math Logic Error
    # Applying a 10% discount by subtracting 0.1 instead of multiplying by 0.9
    is_loyal = data.get("is_loyal", False)
    
    subtotal = 0
    for item in order_history:
        subtotal += item.get("price", 0)
    
    total = subtotal
    if is_loyal:
        # Logical typo: subtracting 0.1 instead of 10%
        total = subtotal - 0.1  # Should be: total = subtotal * 0.9
    
    # BUG 3: ZeroDivisionError
    # This will crash if order_history is empty (first request with no items)
    avg_price = total / len(order_history)
    
    return jsonify({
        "subtotal": subtotal,
        "total": round(total, 2),
        "average_item_price": round(avg_price, 2),
        "item_count": len(order_history),
        "items_in_calculation": order_history
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
