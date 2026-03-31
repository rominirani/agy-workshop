from flask import Flask, render_template, request
from legacy_script import process_user_data

app = Flask(__name__)

# Mock database
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 15}
]

@app.route('/')
def home():
    # Legacy way of building a response
    res = process_user_data(users)
    return render_template('index.html', results=res)

@app.route('/add_user', methods=['GET'])
def add():
    n = request.args.get('n')
    a = int(request.args.get('a', 0))
    users.append({'name': n, 'age': a})
    return "User " + n + " added successfully!" # Non-idiomatic Flask response

if __name__ == "__main__":
    app.run(debug=True)
