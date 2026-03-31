from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# In-memory storage for trips
trips = [
    {"destination": "Kyoto, Japan", "date": "2024-10-15", "note": "Walk through the Arashiyama Bamboo Grove at dawn."},
    {"destination": "Bali, Indonesia", "date": "2025-03-20", "note": "Sunrise yoga session overlooking the rice terraces."}
]

zen_quotes = [
    "Travel is the only thing you buy that makes you richer.",
    "The journey not the arrival matters.",
    "Not all those who wander are lost.",
    "Mindful travel is about the quality of the connection, not the quantity of destinations.",
    "Breathe in the new air, exhale the old worries."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        destination = request.form.get('destination')
        date = request.form.get('date')
        note = request.form.get('note')
        if destination and date:
            trips.append({"destination": destination, "date": date, "note": note})
        return redirect(url_for('index'))
    
    quote = random.choice(zen_quotes)
    return render_template('index.html', trips=trips, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
