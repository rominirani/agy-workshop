from flask import Flask, jsonify, render_template
from data_proc import generate_sales_data, find_top_sales_days

app = Flask(__name__)

# Pre-generate some data
SALES_DB = generate_sales_data(20000)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/report")
def get_report():
    # Calculate the top 5 sales days using the inefficient algorithm.
    # On a large dataset, this can take several seconds.
    # Attendees should optimize the logic in data_proc.py.
    top_5, time_taken = find_top_sales_days(SALES_DB, 5)
    
    return jsonify({
        "status": "success",
        "time_ms": int(time_taken * 1000),
        "results": top_5
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
