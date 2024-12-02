from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Gender, activity_multipliers, ActivityLevel

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return "Hello from Flask!"

@bp.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json
    user = User(name=data['name'], weight=data['weight'], height=data['height'], age=data['age'], gender=data['gender'], activity_level=data['activity_level'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Data saved successfully!"})

@bp.route('/calculate-bmr', methods=['GET'])
def calculate_bmr(user):
    if user.gender == Gender.FEMALE.value:  # For Female BMR calculation
        bmr = (10 * user.weight) + (6.25 * user.height) - (5 * user.age) - 161
    elif user.gender == Gender.MALE.value:  # For Male BMR calculation
        bmr = (10 * user.weight) + (6.25 * user.height) - (5 * user.age) + 5
    else:
        return jsonify({"error": "Invalid gender"})
    
    return bmr


@bp.route('/calculate-tdee', methods=['GET'])
def calculate_tdee():
    # Get the latest user data
    user_id = request.args.get('user_id')  # Get user_id from the query params
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    user = User.query.get(user_id)     
    if user:
        # Convert activity level string to enum
        try:
            activity_level_enum = ActivityLevel[user.activity_level.lower()]
        except KeyError:
            activity_level_enum = ActivityLevel.sedentary  # Default to sedentary if not found

        # Get the multiplier for the activity level
        multiplier = activity_multipliers.get(activity_level_enum, 1.2)
        
        # Calculate BMR
        bmr = calculate_bmr(user)  # Pass the user object and get BMR value

        # Calculate TDEE
        tdee = bmr * multiplier
        return jsonify({"tdee": tdee})
    else:
        return jsonify({"error": "No user data found!"})


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
