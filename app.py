from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Flutter to interact with Flask

# Simulated database
database = []

# Home route
@app.route('/')
def home():
    return "Hello from Flask!"

# Route to save form data
@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json
    database.append(data)  # Save to "database"
    return jsonify({"message": "Data saved successfully!"})

# Route to calculate BMR
@app.route('/calculate-bmr', methods=['GET'])
def calculate_bmr():
    if database:
        user = database[-1]
        weight = float(user.get('weight', 0))
        height = float(user.get('height', 0))
        age = int(user.get('age', 0))
        bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Example formula
        return jsonify({"bmr": bmr})
    return jsonify({"error": "No data found!"})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
