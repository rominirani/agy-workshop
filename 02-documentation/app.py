from flask import Flask, jsonify, request
import asyncio
from scheduler import s, g, w

app = Flask(__name__)

@app.route('/schedule', methods=['POST'])
async def schedule_task():
    # Intentionally messy and uncommented
    data = request.json
    delay = data.get('d', 0)
    
    async def some_work():
        await asyncio.sleep(1)
        print("WORK DONE")
        
    job_id = await s(some_work, delay)
    return jsonify({"id": job_id, "status": "PENDING"})

@app.route('/status/<job_id>')
def get_status(job_id):
    res = g(job_id)
    if not res:
        return jsonify({"error": "NOT_FOUND"}), 404
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
