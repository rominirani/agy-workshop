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
    
    # BUG (Security): SQL Injection Vulnerability
    # The user input is concatenated directly into the query string.
    # Try: admin' --
    query = f"SELECT username, secret_info FROM users WHERE username = '{username}'"
    
    try:
        cursor = db_conn.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        return f"Database Error: {str(e)}", 400

    # BUG (Security): Cross-Site Scripting (XSS) Vulnerability
    # The user input is rendered directly into the HTML without escaping.
    # Try: <script>alert('Hacked!')</script>
    template = """
    <html>
        <body>
            <h1>Search Results for: {{ username }}</h1>
            <p>We found {{ count }} user(s):</p>
            <ul>
                {% for user in results %}
                    <li>User: {{ user[0] }} | Data: {{ user[1] }}</li>
                {% endfor %}
            </ul>
            <a href="/">Back to Search</a>
        </body>
    </html>
    """
    
    # Using render_template_string for demonstration of "Bad" practice
    return render_template_string(template, username=username, results=results, count=len(results))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
