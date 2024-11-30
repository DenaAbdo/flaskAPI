from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///KitchenSmartDB.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    # Register routes
    from app.routes import bp
    app.register_blueprint(bp)
    
    migrate = Migrate(app, db)

    # Create tables automatically (for development purposes)
    with app.app_context():
        db.create_all()  # Create all tables when the app starts

    return app
