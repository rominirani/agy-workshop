def process_user_data(user_list):
    results = []
    for i in range(len(user_list)):
        user = user_list[i]
        name = user.get('name', 'N/A')
        age = user.get('age', 0)
        
        # Legacy string formatting
        msg = "User %s is %d years old." % (name, age)
        
        if age > 18:
            status = "Adult"
        else:
            status = "Minor"
            
        results.append({"name": name, "status": status, "message": msg})
    return results

data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 15},
    {'name': 'Charlie'}
]

processed = process_user_data(data)
for p in processed:
    print(p)
