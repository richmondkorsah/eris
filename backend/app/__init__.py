from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    print(f"App Context: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

    db.init_app(app)  # Register SQLAlchemy with Flask app
    migrate.init_app(app, db)  # Register Migrate with app

    with app.app_context():
        from app.models import UserData, EmergencyReport
        from app.routes import bp_ussd
        app.register_blueprint(bp_ussd)

    return app
