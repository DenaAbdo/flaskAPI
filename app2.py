# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # To allow interaction with Flutter

# # Simulated in-memory database
# database = []

# # Endpoint to save form data
# @app.route('/submit-form', methods=['POST'])
# def submit_form():
#     data = request.json
#     database.append(data)  # Save to the simulated database
#     return jsonify({"message": "Data saved successfully!"})

# # Endpoint to calculate BMR
# @app.route('/calculate-bmr', methods=['GET'])
# def calculate_bmr():
#     # Example: Calculate BMR for the last entry
#     if database:
#         user = database[-1]
#         weight = float(user.get('weight', 0))
#         height = float(user.get('height', 0))
#         age = int(user.get('age', 0))
#         bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Example formula
#         return jsonify({"bmr": bmr})
#     return jsonify({"error": "No data found!"})

# if __name__ == '__main__':
#     app.run(debug=True)
