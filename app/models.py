from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    age = db.Column(db.Integer)
def __init__(self, name, weight, height, age):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age