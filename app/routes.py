from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Gender, activity_multipliers

bp = Blueprint('routes', __name__)
@bp.route('/')
def home():
    return "Hello from Flask!"

@bp.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json
    user = User(name=data['name'], weight=data['weight'], height=data['height'], age=data['age'], gender=data['gender'],activity_level=data['activity_level'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Data saved successfully!"})

@bp.route('/calculate-bmr', methods=['GET'])
def calculate_bmr():
    user = User.query.order_by(User.id.desc()).first()

    if user:
        if user.gender == Gender.FEMALE:  # For Female BMR calculation
            bmr = 447.593 + (9.247 * user.weight) + (3.098 * user.height) - (4.330 * user.age)
        elif user.gender == Gender.MALE:  # For Male BMR calculation
            bmr = 88.362 + (13.397 * user.weight) + (4.799 * user.height) - (5.677 * user.age)
        else:
            return jsonify({"error": "Invalid gender"})
        
        return jsonify({"bmr": bmr})
    else:
        return jsonify({"error": "No user data found!"})
@bp.route('/calculate-tdee', methods=['GET'])
def calculate_tdee(user):
    # Get the multiplier based on the user's activity level (enum value)
    multiplier = activity_multipliers.get(user.activity_level, 1.2)  # Default to sedentary if not found
    bmr = calculate_bmr(user)
    return bmr * multiplier
@bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(
        name=data['name'],
        weight=data['weight'],
        height=data['height'],
        age=data['age'],
        gender=data['gender'],
        activity_level=data['activity_level']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"})

# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=False)