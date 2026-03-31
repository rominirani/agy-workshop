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
