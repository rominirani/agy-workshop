from flask import Flask, jsonify
from typing import List, Dict, Any, Union

app = Flask(__name__)

def process_user_data(user_list: List[Dict[str, Any]]) -> List[Dict[str, Union[str, int]]]:
    """Processes raw user data into structured status reports.
    
    Args:
        user_list: A list of dictionaries containing 'name' and 'age'.
        
    Returns:
        List of processed records with modern f-string messaging and status.
    """
    results = []
    for user in user_list:
        name: str = user.get("name", "N/A")
        age: int = user.get("age", 0)
        
        # Modern f-string formatting
        msg: str = f"User {name} is {age} years old."
        status: str = "Adult" if age > 18 else "Minor"
            
        results.append({
            "name": name, 
            "status": status, 
            "message": msg
        })
    return results

@app.route("/users")
def get_users() -> Any:
    """API endpoint to retrieve processed user data."""
    sample_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 15},
        {"name": "Charlie"}
    ]
    processed = process_user_data(sample_data)
    return jsonify(processed)

if __name__ == "__main__":
    # Simulate legacy output for verification
    sample_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 15},
        {"name": "Charlie"}
    ]
    processed_results = process_user_data(sample_data)
    for p in processed_results:
        print(p)
    
    # app.run(debug=True) # Uncomment to run as Flask app
