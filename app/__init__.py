from flask import Flask
from app.config import Config
from app.database import db
from app.routes import bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 
    
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/api')

    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()

    return app
