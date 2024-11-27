from flask import Blueprint, request, jsonify
from app.models import User, db

bp = Blueprint('routes', __name__)
@bp.route('/')
def home():
    return "Hello from Flask!"

@bp.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json
    user = User(name=data['name'], weight=data['weight'], height=data['height'], age=data['age'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Data saved successfully!"})

@bp.route('/calculate-bmr', methods=['GET'])
def calculate_bmr():
    user = User.query.order_by(User.id.desc()).first()
    if user:
        bmr = 10 * user.weight + 6.25 * user.height - 5 * user.age + 5
        return jsonify({"bmr": bmr})
    return jsonify({"error": "No user data found!"})
