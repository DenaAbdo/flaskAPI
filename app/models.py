from app import db
import enum

class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"

# Add description in the frontend for each level so the user can know what to choose from them
class ActivityLevel(enum.Enum):
    sedentary = "Sedentary"
    lightly_active = "Lightly Active"
    moderately_active = "Moderately Active"
    very_active = "Very Active"
    super_active = "Super Active"

activity_multipliers = {
    ActivityLevel.sedentary: 1.2,
    ActivityLevel.lightly_active: 1.375,
    ActivityLevel.moderately_active: 1.55,
    ActivityLevel.very_active: 1.725,
    ActivityLevel.super_active: 1.9
}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6), nullable=False)
    activity_level = db.Column(db.String(20), nullable=False)    
def __init__(self, name, weight, height, age, gender, activity_level):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.activity_level = activity_level