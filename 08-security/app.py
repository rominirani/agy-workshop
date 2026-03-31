import sqlite3
from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

# Initialize a simple in-memory database
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, secret_info TEXT)")
    conn.execute("INSERT INTO users (username, secret_info) VALUES ('admin', 'SUPER_SECRET_PASSWORD_123')")
    conn.execute("INSERT INTO users (username, secret_info) VALUES ('guest', 'just_a_visitor')")
    return conn

db_conn = init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    username = request.args.get("username", "")
    
    # FIXED (Security): Parameterized Query to prevent SQL Injection
    query = "SELECT username, secret_info FROM users WHERE username = ?"
    
    try:
        # Pass (username,) as a tuple for parameterized search
        cursor = db_conn.execute(query, (username,))
        results = cursor.fetchall()
    except Exception as e:
        return f"Database Error: {str(e)}", 400

    # FIXED (Security): Use a dedicated HTML template file which automatically escapes inputs
    return render_template("results.html", username=username, results=results)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
