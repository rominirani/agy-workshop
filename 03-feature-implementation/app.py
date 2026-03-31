from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for simplicity
inventory = [
    {'id': 1, 'name': 'Laptop', 'quantity': 10, 'category': 'Electronics'},
    {'id': 2, 'name': 'Mouse', 'quantity': 2, 'category': 'Electronics'},
    {'id': 3, 'name': 'Desk Chair', 'quantity': 4, 'category': 'Furniture'},
    {'id': 4, 'name': 'Monitor', 'quantity': 3, 'category': 'Electronics'},
    {'id': 5, 'name': 'Keyboard', 'quantity': 8, 'category': 'Electronics'},
]

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/dashboard')
def dashboard():
    # Identify items with quantity < 5
    low_stock_items = [item for item in inventory if item['quantity'] < 5]
    total_items = len(inventory)
    low_stock_count = len(low_stock_items)
    return render_template('dashboard.html', 
                          low_stock_items=low_stock_items, 
                          total_items=total_items, 
                          low_stock_count=low_stock_count)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    category = request.form['category']
    new_item = {'id': len(inventory) + 1, 'name': name, 'quantity': quantity, 'category': category}
    inventory.append(new_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
